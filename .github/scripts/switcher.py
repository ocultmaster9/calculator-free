#!/usr/bin/env python3
"""Rebuild the language switcher on every page.

A language links to its OWN copy of the current page when that copy exists, and
to that language's homepage when it does not. Linking every language at every
page unconditionally produces 404s on the English-only pages (bet-calculator,
blog, about, legal), which is what a previous run of new_language.py did.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
BASE = "https://calculator-free.com"
FLAG = "https://flagcdn.com/20x15/%s.png"
IMG = ('<img src="' + FLAG + '" width="20" height="15" loading="lazy" alt="" '
       'style="vertical-align:-2px;margin-right:5px;border-radius:2px">')
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
META = dict((c, (cc, n)) for c, cc, n in LANG_META)
SKIP = {".git", "_stage", "node_modules", ".wrangler", ".github", "cdn-cgi"}
DROP_RE = re.compile(r'(<div class="lang-drop" id="langDrop">).*?(</div>)\s*(</div>)', re.S)
BTN_RE = re.compile(r'<button class="lang-btn" onclick="toggleLang\(\)"[^>]*>.*?</button>', re.S)


def url(lang, key):
    return BASE + "/" + ("" if lang == "en" else lang + "/") + ((key + "/") if key else "")


def scan():
    pages = {}
    for dp, dn, fn in os.walk("."):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in fn:
            if f != "index.html":
                continue
            rel = os.path.relpath(dp, ".").replace(os.sep, "/")
            rel = "" if rel == "." else rel
            parts = rel.split("/") if rel else []
            if parts and parts[0] in META and parts[0] != "en":
                lang, key = parts[0], "/".join(parts[1:])
            else:
                lang, key = "en", rel
            pages[os.path.join(dp, f)[2:]] = (lang, key)
    return pages


def main():
    pages = scan()
    have = set(pages.values())                      # (lang, key) pairs that exist
    langs = [c for c, _, _ in LANG_META if c == "en" or os.path.isdir(c)]
    changed = fallbacks = 0
    only = tuple(sys.argv[1:])
    for p, (lang, key) in sorted(pages.items()):
        if only and not p.startswith(only):
            continue
        items = []
        for c in langs:
            cc, name = META[c]
            target = key if (c, key) in have else ""
            if target != key:
                fallbacks += 1
            cls = ' class="active"' if c == lang else ""
            items.append('<a href="%s"%s>%s %s</a>' % (url(c, target), cls, IMG % cc, name))
        cc, name = META[lang]
        btn = ('<button class="lang-btn" onclick="toggleLang()" aria-label="Language">'
           '%s<span class="lang-name">%s</span> ▾</button>'
               % (IMG % cc, name))
        h = open(p, encoding="utf-8").read()
        n = BTN_RE.sub(lambda m: btn, h, count=1)
        n = DROP_RE.sub(lambda m: m.group(1) + "\n".join(items) + "\n" + m.group(2) + m.group(3),
                        n, count=1)
        if n != h:
            open(p, "w", encoding="utf-8", newline="").write(n)
            changed += 1
    print("switcher rebuilt: %d pages changed, %d links fall back to a language homepage"
          % (changed, fallbacks))


if __name__ == "__main__":
    main()
