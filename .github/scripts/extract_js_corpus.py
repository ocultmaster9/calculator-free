#!/usr/bin/env python3
"""Extract user-visible string literals from the calculators' inline JS.
These never appear in the HTML corpus but are what the user sees as a result."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
PAGES = [""] + sorted(p for p in os.listdir("de") if os.path.isdir(os.path.join("de", p)))
DROP = re.compile(r"^(?:[a-z][\w-]*|#[\w-]+|\.[\w-]+|[\w-]+\s*[:=]|,new Date|;|%)")
def js_blocks(t):
    return [m.group(1) for m in
            re.finditer(r'(?s)<script(?![^>]*ld\+json)[^>]*>(.*?)</script>', t)]
order, seen = [], set()
for pg in PAGES:
    p = os.path.join(pg, "index.html") if pg else "index.html"
    if not os.path.exists(p):
        continue
    t = open(p, encoding="utf-8").read()
    for b in js_blocks(t):
        for s in re.findall(r"'([^'\\\n]*)'", b):
            if not re.search(r"[A-Za-z]{3}", s):      # needs real words
                continue
            if s.startswith(",new Date") or "gtag" in s:
                continue
            if re.fullmatch(r"[\w.#\[\]=:\-\s]*", s) and not re.search(r"[A-Z]", s):
                continue                               # css selector / id
            if s in seen:
                continue
            seen.add(s); order.append(s)
json.dump(order, open(os.path.expanduser("~/i18n/js_corpus.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("js strings:", len(order))
for i, s in enumerate(order):
    print("%d\t%r" % (i, s))
