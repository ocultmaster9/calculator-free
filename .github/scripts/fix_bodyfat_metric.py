#!/usr/bin/env python3
"""CRITICAL: the body-fat calculator took cm inputs but used the US Navy
*imperial* (inch) constants, so every result was wrong.

  180cm / neck 38 / waist 90  ->  site said 26.4% "Obese", truth is 19.8%.

Swap in the metric form of the same Hodgdon-Beckett equation, and update the
formula printed in the SEO copy so the page documents what it actually runs.

  men:   495 / (1.0324   - 0.19077*log10(waist-neck)     + 0.15456*log10(height)) - 450
  women: 495 / (1.29579  - 0.35004*log10(waist+hip-neck) + 0.22100*log10(height)) - 450
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

JS_OLD_M = "bf=86.010*Math.log10(w-n)-70.041*Math.log10(h)+36.76;"
JS_NEW_M = "bf=495/(1.0324-0.19077*Math.log10(w-n)+0.15456*Math.log10(h))-450;"
JS_OLD_F = "bf=163.205*Math.log10(w+hip-n)-97.684*Math.log10(h)-78.387;"
JS_NEW_F = "bf=495/(1.29579-0.35004*Math.log10(w+hip-n)+0.22100*Math.log10(h))-450;"

# Prose: keep each language's own words for waist/neck/height, swap the maths.
# e.g. "86.010 × log₁₀(waist − neck) − 70.041 × log₁₀(height) + 36.76"
PROSE_M = re.compile(r"86\.010 × log₁₀\((?P<a>[^)]*)\) − 70\.041 × log₁₀\((?P<b>[^)]*)\) \+ 36\.76")
PROSE_F = re.compile(r"163\.205 × log₁₀\((?P<a>[^)]*)\) − 97\.684 × log₁₀\((?P<b>[^)]*)\) − 78\.387")

files = sorted(glob.glob("*/body-fat-calculator/index.html")) + ["body-fat-calculator/index.html"]
js_fixed = prose_fixed = 0
missed = []

for p in files:
    src = open(p, encoding="utf-8").read()
    out = src
    if JS_OLD_M in out and JS_OLD_F in out:
        out = out.replace(JS_OLD_M, JS_NEW_M).replace(JS_OLD_F, JS_NEW_F)
        js_fixed += 1
    else:
        missed.append(p)
    before = out
    out = PROSE_M.sub(lambda m: "495 ÷ (1.0324 − 0.19077 × log₁₀(%s) + 0.15456 × log₁₀(%s)) − 450"
                      % (m.group("a"), m.group("b")), out)
    out = PROSE_F.sub(lambda m: "495 ÷ (1.29579 − 0.35004 × log₁₀(%s) + 0.22100 × log₁₀(%s)) − 450"
                      % (m.group("a"), m.group("b")), out)
    if out != before:
        prose_fixed += 1
    if out != src:
        open(p, "w", encoding="utf-8", newline="").write(out)

print("body-fat metric formula: JS fixed in %d/%d files, prose fixed in %d"
      % (js_fixed, len(files), prose_fixed))
if missed:
    print("!! JS pattern not found in: %s" % ", ".join(missed))
