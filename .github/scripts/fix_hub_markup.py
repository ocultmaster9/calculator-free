#!/usr/bin/env python3
"""The four hub pages (finance / health / maths / date-time) left four <div>
elements open in every language - 180 pages. Browsers recover by closing them
at </body>, which quietly nests the ad block and the whole footer inside the
hero.

Close them where the homepage closes them: the hero ends after its intro
paragraph, and a fresh .wrap carries the tool grid and the article.
"""
import os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

# hero ends after the intro paragraph; a new .wrap opens for the rest
A1_OLD = '</p><div class="bento">'
A1_NEW = '</p></div></div></div></div><div class="wrap"><div class="bento">'
# ...and that .wrap closes before the one holding the ad
A2_OLD = '</div><div class="wrap"><div class="ad-wrap">'
A2_NEW = '</div></div><div class="wrap"><div class="ad-wrap">'

n = ok = bad = 0
for page in ("finance-calculators", "health-calculators", "math-calculators", "date-time-calculators"):
    for p in sorted(glob.glob("*/%s/index.html" % page)) + ["%s/index.html" % page]:
        t = open(p, encoding="utf-8").read()
        if t.count("<div") == t.count("</div>"):
            continue                      # already fixed
        if t.count(A1_OLD) != 1 or t.count(A2_OLD) != 1:
            print("  !! anchors not unique in", p); bad += 1; continue
        t = t.replace(A1_OLD, A1_NEW, 1).replace(A2_OLD, A2_NEW, 1)
        if t.count("<div") != t.count("</div>"):
            print("  !! still unbalanced, skipped:", p); bad += 1; continue
        open(p, "w", encoding="utf-8", newline="").write(t)
        n += 1; ok += 1
print("hub pages balanced: %d (%d refused)" % (n, bad))
