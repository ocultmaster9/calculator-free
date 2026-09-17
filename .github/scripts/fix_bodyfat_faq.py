#!/usr/bin/env python3
"""The first body-fat FAQ answer contained a raw '<' in HTML text ("(men <5%"),
which is invalid markup and truncated every downstream extraction - leaving the
tail of the sentence in English in 20 languages, and the whole answer English in
the JSON-LD. Rewrites the answer, in both places, with no raw '<'."""
import os, re, json, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
T = json.load(open(os.path.expanduser("~/i18n/bodyfat_faq.json"), encoding="utf-8"))
MARK = "<5%"
n = 0
for lang, new in T.items():
    p = "body-fat-calculator/index.html" if lang == "en" else \
        os.path.join(lang, "body-fat-calculator", "index.html")
    if not os.path.exists(p):
        print("  missing:", p); continue
    t = open(p, encoding="utf-8").read()
    # 1) the visible answer
    def faq(m):
        return m.group(1) + new + m.group(3) if MARK in m.group(2) else m.group(0)
    t2 = re.sub(r'(<div class="faq-a">)(.*?)(</div>)', faq, t, flags=re.S)
    # 2) the JSON-LD answer
    def ld(m):
        block = m.group(0)
        try:
            d = json.loads(m.group(1))
        except ValueError:
            return block
        if d.get("@type") != "FAQPage":
            return block
        hit = False
        for q in d.get("mainEntity", []):
            a = q.get("acceptedAnswer", {})
            if MARK in a.get("text", ""):
                a["text"] = new; hit = True
        if not hit:
            return block
        return '<script type="application/ld+json">%s</script>' % json.dumps(d, ensure_ascii=True)
    t2 = re.sub(r'<script type="application/ld\+json">(.*?)</script>', ld, t2, flags=re.S)
    if t2 != t:
        open(p, "w", encoding="utf-8", newline="").write(t2); n += 1
    if MARK in t2:
        print("  STILL PRESENT:", p)
print("body-fat FAQ rewritten in %d files" % n)
