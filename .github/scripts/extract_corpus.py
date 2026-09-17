#!/usr/bin/env python3
"""Extract the translatable string corpus from the 25 EN pages that make up a
localized language set. Output: ~/i18n/corpus.json  {page: [strings]} plus a
flat unique list, so a new language is built from a real dictionary rather than
a find/replace over one page."""
import os, re, json, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
OUT = os.path.expanduser("~/i18n")
LANGNAMES = set()
for m in re.finditer(r'class="lang-drop"[^>]*>(.*?)</div>\s*</div>',
                     open("index.html", encoding="utf-8").read(), re.S):
    LANGNAMES |= set(x.strip() for x in re.findall(r'>\s*([^<>]+?)\s*</a>', m.group(0)))
SKIP = LANGNAMES | {"calculator-free.com", "English ▾", "+", "—", "%"}

PAGES = [""] + sorted(p for p in os.listdir("de") if os.path.isdir(os.path.join("de", p)))

def strings_of(path):
    t = open(path, encoding="utf-8").read()
    out = []
    for pat in (r"<title>([^<]+)</title>",
                r'<meta name="description" content="([^"]+)"'):
        out += [("meta", s) for s in re.findall(pat, t)]
    body = re.sub(r"(?s)<script type=\"application/ld\+json\">.*?</script>", "", t)
    body = re.sub(r"(?s)<script.*?</script>|<style.*?</style>|<!--.*?-->", "", body)
    for m in re.finditer(r">([^<>]+)<", body):
        s = re.sub(r"\s+", " ", m.group(1)).strip()
        if s and s not in SKIP and not re.fullmatch(r"[\d\s\W]+", s):
            out.append(("body", s))
    for m in re.finditer(r'<(?:label|option)[^>]*>([^<]+)<', t):
        s = m.group(1).strip()
        if s and s not in SKIP:
            out.append(("form", s))
    for m in re.finditer(r'placeholder="([^"]+)"|aria-label="([^"]+)"', t):
        s = (m.group(1) or m.group(2)).strip()
        if s and s not in SKIP:
            out.append(("attr", s))
    return out

corpus, seen, order = {}, set(), []
for pg in PAGES:
    p = os.path.join(pg, "index.html") if pg else "index.html"
    if not os.path.exists(p):
        continue
    ss = []
    for kind, s in strings_of(p):
        ss.append(s)
        if s not in seen:
            seen.add(s); order.append(s)
    corpus[pg or "/"] = ss

os.makedirs(OUT, exist_ok=True)
json.dump(corpus, open(os.path.join(OUT, "corpus_by_page.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
json.dump(order, open(os.path.join(OUT, "corpus.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("pages: %d   unique strings: %d   words: %d"
      % (len(corpus), len(order), sum(len(s.split()) for s in order)))
sizes = sorted(((len(set(v)), k) for k, v in corpus.items()), reverse=True)
for n, k in sizes[:6]:
    print("   %-32s %d unique" % (k, n))
