#!/usr/bin/env python3
"""14 language homepages carried the *category* title ("All Calculators")
instead of the descriptive one every other language uses. The main keyword was
missing from the <title> on exactly the biggest markets - de, es, fr, it, pt,
ru, ja, ko, ar, hi, id, nl, pl, tr.

The H1 on those pages was already right, so the title is rebuilt from it.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
SUFFIX = " | calculator-free.com"

# "20 <tools>" in each language, written to read naturally, not word-for-word.
TOOLS = {
 "ar": "20 أداة",
 "de": "20 Tools",
 "es": "20 herramientas",
 "fr": "20 outils",
 "hi": "20 टूल",
 "id": "20 Alat",
 "it": "20 strumenti",
 "ja": "20のツール",
 "ko": "20가지 도구",
 "nl": "20 tools",
 "pl": "20 narzędzi",
 "pt": "20 ferramentas",
 "ru": "20 инструментов",
 "tr": "20 Araç",
}

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
OGT_RE = re.compile(r'(<meta property="og:title" content=")([^"]*)(">)')
TWT_RE = re.compile(r'(<meta name="twitter:title" content=")([^"]*)(">)')

n = 0
for lang, tools in sorted(TOOLS.items()):
    p = "%s/index.html" % lang
    if not os.path.exists(p):
        print("  !! missing", p); continue
    t = open(p, encoding="utf-8").read()
    h1 = re.sub(r"<[^>]+>", "", H1_RE.search(t).group(1)).strip()
    new_title = "%s — %s%s" % (h1, tools, SUFFIX)
    cur = re.sub(r"\s+", " ", TITLE_RE.search(t).group(1)).strip()
    if cur == new_title:
        continue
    esc = new_title.replace("&", "&amp;").replace('"', "&quot;")
    t = TITLE_RE.sub(lambda m: "<title>%s</title>" % new_title, t, count=1)
    t = OGT_RE.sub(lambda m: m.group(1) + esc + m.group(3), t, count=1)
    t = TWT_RE.sub(lambda m: m.group(1) + esc + m.group(3), t, count=1)
    open(p, "w", encoding="utf-8", newline="").write(t)
    print("  %s: %s  ->  %s" % (lang, cur, new_title))
    n += 1
print("homepage titles fixed: %d" % n)
