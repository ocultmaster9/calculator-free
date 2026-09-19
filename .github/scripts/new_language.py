#!/usr/bin/env python3
"""Build a full language directory for calculator-free.com from the English pages.

  python3 new_language.py ro

Reads ~/i18n/corpus.json (ordered EN strings), ~/i18n/<lang>.json (same order,
translated) and ~/i18n/<lang>_js.json (EN->translated for inline-JS literals).
Rebuilds the language switcher on EVERY page so the new language appears.
Never touches <ins class="adsbygoogle"> / push() pairs, GA4 or AdSense ids.
"""
import os, re, sys, json, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
I18N = os.path.expanduser("~/i18n")
BASE = "https://calculator-free.com"
FLAG = "https://flagcdn.com/20x15/%s.png"
IMG = ('<img src="' + FLAG + '" width="20" height="15" loading="lazy" alt="" '
       'style="vertical-align:-2px;margin-right:5px;border-radius:2px">')

# switcher order -> (flag cc, native name).  'en' is always first.
LANG_META = [
    ("en", "gb", "English"), ("ar", "sa", "العربية"), ("bg", "bg", "Български"), ("zh", "cn", "中文"),
    ("cs", "cz", "Čeština"), ("da", "dk", "Dansk"), ("de", "de", "Deutsch"),
    ("el", "gr", "Ελληνικά"), ("es", "es", "Español"), ("et", "ee", "Eesti"), ("fi", "fi", "Suomi"),
    ("fr", "fr", "Français"), ("ga", "ie", "Gaeilge"), ("hi", "in", "हिन्दी"), ("hr", "hr", "Hrvatski"), ("hu", "hu", "Magyar"),
    ("id", "id", "Indonesia"), ("it", "it", "Italiano"), ("ja", "jp", "日本語"),
    ("ko", "kr", "한국어"), ("lt", "lt", "Lietuvių"), ("lv", "lv", "Latviešu"), ("mt", "mt", "Malti"), ("nl", "nl", "Nederlands"), ("no", "no", "Norsk"),
    ("pl", "pl", "Polski"), ("pt", "br", "Português"), ("ro", "ro", "Română"),
    ("ru", "ru", "Русский"), ("sk", "sk", "Slovenčina"), ("sl", "si", "Slovenščina"), ("sv", "se", "Svenska"),
    ("tr", "tr", "Türkçe"), ("uk", "ua", "Українська"), ("vi", "vn", "Tiếng Việt"),
    ("af", "za", "Afrikaans"), ("fa", "ir", "فارسی"), ("he", "il", "עברית"), ("mk", "mk", "Македонски"),
    ("ms", "my", "Bahasa Melayu"), ("sq", "al", "Shqip"), ("sr", "rs", "Srpski"), ("sw", "ke", "Kiswahili"),
    ("th", "th", "ไทย"), ("tl", "ph", "Tagalog"),
]
RTL = {"ar", "he", "fa"}

DROP_RE = re.compile(r'(<div class="lang-drop" id="langDrop">).*?(</div>)\s*(</div>)', re.S)
BTN_RE = re.compile(r'<button class="lang-btn" onclick="toggleLang\(\)"[^>]*>.*?</button>', re.S)
SCRIPT_RE = re.compile(r'(?s)(<script(?![^>]*ld\+json)[^>]*>.*?</script>)')


def live_langs():
    """languages that actually have a directory on disk, plus en"""
    return ["en"] + [c for c, _, _ in LANG_META
                     if c != "en" and os.path.isdir(c)]


def page_keys():
    return [""] + sorted(p for p in os.listdir("de") if os.path.isdir(os.path.join("de", p)))


def url(lang, key):
    return BASE + "/" + ("" if lang == "en" else lang + "/") + ((key + "/") if key else "")


def switcher(lang, key, langs):
    items = []
    for c, cc, name in LANG_META:
        if c not in langs:
            continue
        cls = ' class="active"' if c == lang else ""
        items.append('<a href="%s"%s>%s %s</a>' % (url(c, key), cls, IMG % cc, name))
    meta = dict((c, (cc, n)) for c, cc, n in LANG_META)
    cc, name = meta[lang]
    btn = ('<button class="lang-btn" onclick="toggleLang()" aria-label="Language">'
           '%s<span class="lang-name">%s</span> ▾</button>'
           % (IMG % cc, name))
    return btn, "\n".join(items)


def set_switcher(html, lang, key, langs):
    btn, drop = switcher(lang, key, langs)
    html = BTN_RE.sub(lambda m: btn, html, count=1)
    html = DROP_RE.sub(lambda m: m.group(1) + drop + "\n" + m.group(2) + m.group(3),
                       html, count=1)
    return html


LDJSON_RE = re.compile(r'(?s)(<script type="application/ld\+json">.*?</script>)')
ATTRS = ("content", "placeholder", "aria-label", "alt")


def _sub_map(text, mapping):
    """single pass: longest key wins, replaced text is never rescanned"""
    if not mapping:
        return text
    pat = re.compile("|".join(re.escape(k) for k in
                              sorted(mapping, key=len, reverse=True)))
    return pat.sub(lambda m: mapping[m.group(0)], text)


STR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def _ld_value(m, dmap, long_map):
    """Replace one JSON string literal inside a JSON-LD block.

    Matching is done on the DECODED value, because JSON-LD escapes non-ASCII
    (an en dash is \\u2013 there but literal in the HTML body), so raw substring
    matching against the HTML corpus silently misses those strings.
    """
    try:
        val = json.loads('"' + m.group(1) + '"')
    except ValueError:
        return m.group(0)
    if val in dmap:
        new = dmap[val]
    else:
        new = _sub_map(val, long_map)
        if new == val:
            return m.group(0)
    return json.dumps(new, ensure_ascii=True)


def translate(html, pairs, js_pairs):
    """pairs: [(en, translated)] from the HTML corpus; js_pairs: same for inline JS.

    HTML text is matched as WHOLE text nodes and whole attribute values, never as
    loose substrings - otherwise a short entry ("To") corrupts a longer
    translation that already contains it ("Toate" -> "Laate").
    JSON-LD, which has no text nodes, uses substring replacement restricted to
    strings long enough to be unambiguous.
    """
    dmap = dict(pairs)
    jmap = dict(js_pairs)
    long_map = dict((e, t) for e, t in pairs if len(e) >= 25)
    esc_map = {}
    for e, t in long_map.items():
        ee = e.replace("\\", "\\\\").replace('"', '\\"')
        if ee != e:
            esc_map[ee] = t.replace("\\", "\\\\").replace('"', '\\"')

    def node(m):
        raw = m.group(1)
        key = re.sub(r"\s+", " ", raw).strip()
        if key in dmap:
            lead = raw[:len(raw) - len(raw.lstrip())]
            tail = raw[len(raw.rstrip()):]
            return ">" + lead + dmap[key] + tail + "<"
        return m.group(0)

    def attr(m):
        name, val = m.group(1), m.group(2)
        key = re.sub(r"\s+", " ", val).strip()
        return '%s="%s"' % (name, dmap[key]) if key in dmap else m.group(0)

    out = []
    for part in SCRIPT_RE.split(html):
        if part.startswith("<script") and "ld+json" not in part[:60]:
            out.append(_sub_map(part, jmap))
            continue
        chunks = []
        for sub in LDJSON_RE.split(part):
            if sub.startswith('<script type="application/ld+json">'):
                sub = STR_RE.sub(lambda m: _ld_value(m, dmap, long_map), sub)
            else:
                sub = re.sub(r">([^<>]+)<", node, sub)
                sub = re.sub(r'\b(%s)="([^"]*)"' % "|".join(ATTRS), attr, sub)
            chunks.append(sub)
        out.append("".join(chunks))
    return "".join(out)


def localize_links(html, lang, keys):
    """point internal links at the language copy where one exists"""
    for k in sorted(keys, key=len, reverse=True):
        if k == "":
            continue
        html = html.replace('"%s/%s/"' % (BASE, k), '"%s/%s/%s/"' % (BASE, lang, k))
    html = html.replace('"%s/"' % BASE, '"%s/%s/"' % (BASE, lang))
    return html


def main(lang):
    corpus = json.load(open(os.path.join(I18N, "corpus.json"), encoding="utf-8"))
    tr = json.load(open(os.path.join(I18N, "%s.json" % lang), encoding="utf-8"))
    if len(tr) != len(corpus):
        sys.exit("dictionary has %d entries, corpus has %d" % (len(tr), len(corpus)))
    js = json.load(open(os.path.join(I18N, "%s_js.json" % lang), encoding="utf-8"))

    pairs = sorted(((e, t) for e, t in zip(corpus, tr) if e != t),
                   key=lambda p: len(p[0]), reverse=True)
    js_pairs = sorted(js.items(), key=lambda p: len(p[0]), reverse=True)
    keys = page_keys()

    made = 0
    for key in keys:
        src = os.path.join(key, "index.html") if key else "index.html"
        if not os.path.exists(src):
            continue
        dst_dir = os.path.join(lang, key) if key else lang
        os.makedirs(dst_dir, exist_ok=True)
        html = open(src, encoding="utf-8").read()
        html = translate(html, pairs, js_pairs)
        html = localize_links(html, lang, keys)
        tag = '<html lang="%s"%s>' % (lang, ' dir="rtl"' if lang in RTL else "")
        html = re.sub(r"<html[^>]*>", tag, html, count=1)
        html = re.sub(r'(<link rel="canonical" href=")[^"]*(">)',
                      lambda m: m.group(1) + url(lang, key) + m.group(2), html, count=1)
        html = re.sub(r'(<meta property="og:url" content=")[^"]*(">)',
                      lambda m: m.group(1) + url(lang, key) + m.group(2), html, count=1)
        html = re.sub(r'("url": ")%s[^"]*(")' % re.escape(BASE),
                      lambda m: m.group(1) + url(lang, key) + m.group(2), html)
        open(os.path.join(dst_dir, "index.html"), "w", encoding="utf-8", newline="").write(html)
        made += 1
    print("  %s: %d pages written" % (lang, made))

    # The switcher is rebuilt by switcher.py, which links a language to its own
    # copy of the page when one exists and to that language's homepage when it
    # does not. Doing it here unconditionally shipped 640 dead links once.
    import subprocess
    subprocess.check_call([sys.executable,
                           os.path.join(os.path.dirname(os.path.abspath(__file__)), "switcher.py")])


if __name__ == "__main__":
    main(sys.argv[1])
