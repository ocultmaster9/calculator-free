#!/usr/bin/env python3
"""Two calculator bugs, in all 45 language copies of each page.

average-calculator
  * "10, 20, 30, " (a trailing comma or space - the way people actually type)
    produced an extra 0, so the mean of 10/20/30 came out as 15 and the count
    as 4. Empty tokens are now dropped before Number().
  * the <title> and meta description promised mode and range; neither was
    computed. Both are added, labelled with the words each page already uses.

compound-interest-calculator
  * a principal of 0 or an empty field printed "NaN% gain".
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

# ---------------------------------------------------------------- average ---
OLD_FILTER = ("var nums=raw.split(/[,\\s]+/).map(Number)"
              ".filter(n=>!isNaN(n)&&n!==undefined&&raw.trim()!=='');")
NEW_FILTER = ("var nums=raw.split(/[,;\\s]+/).filter(function(s){return s!=='';})"
              ".map(Number).filter(function(n){return isFinite(n);});")

MODE_BLOCK = """
  var freq={},best=0,modes=[];
  nums.forEach(function(v){freq[v]=(freq[v]||0)+1;if(freq[v]>best)best=freq[v];});
  Object.keys(freq).forEach(function(k){if(freq[k]===best)modes.push(+k);});
  modes.sort(function(a,b){return a-b;});
  var modeTxt=best<2?'\\u2014':modes.join(', ');
  var range=sorted[sorted.length-1]-sorted[0];"""

MINMAX_RE = re.compile(u"<br>([^:\uff1a'<]+)([:\uff1a]) '\\+sorted\\[0\\]\\+' \u00b7 ([^:\uff1a'<]+)[:\uff1a] '\\+sorted\\[sorted\\.length-1\\]\\+'<br>")
STD_TAIL = "+Math.round(std*1000)/1000;"

# the page's own word for "mode", read from its explainer list; three pages
# word that list differently, so those are given here.
MODE_FALLBACK = {"es": "Moda", "pt": "Moda", "zh": "众数"}
LI_RE = re.compile(u"<li><strong>([^<]{1,40}?)[:\uff1a]</strong>")


def fix_average():
    n = skipped = 0
    for p in sorted(glob.glob("*/average-calculator/index.html")) + ["average-calculator/index.html"]:
        lang = p.split("/")[0] if "/" in p and len(p.split("/")[0]) == 2 else "en"
        t = open(p, encoding="utf-8").read()
        o = t
        if OLD_FILTER in t:
            t = t.replace(OLD_FILTER, NEW_FILTER)

        if "modeTxt" not in t:
            mm = MINMAX_RE.search(t)
            lis = LI_RE.findall(t[t.find("seo-section"):])
            mode_label = MODE_FALLBACK.get(lang) or (lis[2] if len(lis) > 2 else None)
            if not mm or not mode_label:
                print("  !! no anchor for %s (%s)" % (p, "min/max" if not mm else "mode label"))
                skipped += 1
            else:
                mode_label = mode_label.strip()
                colon = mm.group(2)
                mn, mx = mm.group(1).strip(), mm.group(3).strip()
                t = t.replace("  var std=Math.sqrt(variance);",
                              "  var std=Math.sqrt(variance);" + MODE_BLOCK, 1)
                tail = ("+Math.round(std*1000)/1000+'<br>%s%s '+modeTxt+' · %s − %s%s '+range;"
                        % (mode_label, colon, mx, mn, colon))
                t = t.replace(STD_TAIL, tail, 1)
        if t != o:
            open(p, "w", encoding="utf-8", newline="").write(t)
            n += 1
    print("average-calculator fixed: %d files (%d skipped)" % (n, skipped))


# ------------------------------------------------------ compound interest ---
OLD_CI = "' ('+Math.round(gain/P*100)+'% gain)'"
CI_RE = re.compile(r"\+' \('\+Math\.round\(gain/P\*100\)\+'% ([^']*)\)';")


def fix_compound():
    n = 0
    for p in (sorted(glob.glob("*/compound-interest-calculator/index.html"))
              + ["compound-interest-calculator/index.html"]):
        t = open(p, encoding="utf-8").read()
        o = t
        m = CI_RE.search(t)
        if m:
            word = m.group(1)
            t = t[:m.start()] + ("+(P>0?' ('+Math.round(gain/P*100)+'%% %s)':'');" % word) + t[m.end():]
        if t != o:
            open(p, "w", encoding="utf-8", newline="").write(t)
            n += 1
    print("compound-interest fixed: %d files" % n)


if __name__ == "__main__":
    fix_average()
    fix_compound()
