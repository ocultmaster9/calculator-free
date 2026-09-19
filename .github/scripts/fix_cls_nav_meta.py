#!/usr/bin/env python3
"""Three site-wide repairs, one pass per file.

1. CLS was 0.317 (Google's "poor" threshold is 0.25) because ad slots had no
   reserved height: every filled ad pushed the page down after load. Reserve it.
2. On a 375px phone the header ran to 436px - the theme button sat off-screen
   and every page scrolled sideways. Shrink the header and drop the redundant
   "All Calculators" link (the logo already links home) below 620px.
3. The repo already ships og-image.png, favicon.svg and manifest.json but no
   page referenced them: no social card, no declared icon, no manifest.

Idempotent - guarded by the CF_CSS_MARK / CF_META_MARK markers.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
BASE = "https://calculator-free.com"
SKIP = {".git", "_stage", "node_modules", ".wrangler", ".github", "cdn-cgi"}

CF_CSS_MARK = "/*cf-fix-v1*/"
CF_META_MARK = "<!--cf-meta-v1-->"

CSS = CF_CSS_MARK + """
html{overflow-x:clip}
.ad-wrap ins.adsbygoogle{min-height:280px}
.ad-wrap:has(ins.adsbygoogle[data-ad-status="unfilled"]) ins.adsbygoogle{min-height:0}
.nav-inner{min-width:0}
.logo{min-width:0;overflow:hidden;text-overflow:ellipsis}
.nav-right{flex:0 0 auto}
@media(max-width:620px){
.ad-wrap ins.adsbygoogle{min-height:300px}
.nav-link{display:none}
.nav-right{gap:6px}
.logo{font-size:.85rem}
.lang-btn{padding:6px 8px}
.theme-btn{padding:6px 8px}
.lang-name{display:none}
.lang-drop{max-height:70vh;overflow-y:auto}
}
"""

OG_LOCALE = {
 "af":"af_ZA","ar":"ar_AR","bg":"bg_BG","cs":"cs_CZ","da":"da_DK","de":"de_DE","el":"el_GR",
 "en":"en_US","es":"es_ES","et":"et_EE","fa":"fa_IR","fi":"fi_FI","fr":"fr_FR","ga":"ga_IE",
 "he":"he_IL","hi":"hi_IN","hr":"hr_HR","hu":"hu_HU","id":"id_ID","it":"it_IT","ja":"ja_JP",
 "ko":"ko_KR","lt":"lt_LT","lv":"lv_LV","mk":"mk_MK","ms":"ms_MY","mt":"mt_MT","nl":"nl_NL",
 "no":"nb_NO","pl":"pl_PL","pt":"pt_BR","ro":"ro_RO","ru":"ru_RU","sk":"sk_SK","sl":"sl_SI",
 "sq":"sq_AL","sr":"sr_RS","sv":"sv_SE","sw":"sw_KE","th":"th_TH","tl":"tl_PH","tr":"tr_TR",
 "uk":"uk_UA","vi":"vi_VN","zh":"zh_CN",
}

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
DESC_RE = re.compile(r'<meta name="description" content="([^"]*)"')


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def pages(roots=None):
    out = []
    for root in (roots or ["."]):
     for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in fn:
            if f.endswith(".html"):
                out.append(os.path.relpath(os.path.join(dp, f), "."))
    return sorted(set(out))


def lang_of(path):
    parts = path.split("/")
    return parts[0] if len(parts) > 1 and len(parts[0]) == 2 and parts[0] in OG_LOCALE else "en"


def main():
    css_n = meta_n = 0
    for p in pages(sys.argv[1:] or None):
        src = open(p, encoding="utf-8").read()
        out = src

        if CF_CSS_MARK not in out and "</style>" in out:
            out = out.replace("</style>", CSS + "</style>", 1)
            css_n += 1

        if CF_META_MARK not in out and "</head>" in out:
            t = TITLE_RE.search(out)
            d = DESC_RE.search(out)
            title = re.sub(r"\s+", " ", t.group(1)).strip() if t else "calculator-free.com"
            desc = d.group(1) if d else ""
            loc = OG_LOCALE.get(lang_of(p), "en_US")
            block = (CF_META_MARK + "\n"
                     '<meta property="og:site_name" content="calculator-free.com">\n'
                     '<meta property="og:locale" content="%s">\n'
                     '<meta property="og:image" content="%s/og-image.png">\n'
                     '<meta property="og:image:width" content="1200">\n'
                     '<meta property="og:image:height" content="630">\n'
                     '<meta property="og:image:alt" content="calculator-free.com">\n'
                     '<meta name="twitter:card" content="summary_large_image">\n'
                     '<meta name="twitter:title" content="%s">\n'
                     '<meta name="twitter:description" content="%s">\n'
                     '<meta name="twitter:image" content="%s/og-image.png">\n'
                     '<link rel="icon" href="/favicon.ico" sizes="32x32">\n'
                     '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
                     '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
                     '<link rel="manifest" href="/manifest.json">\n'
                     % (loc, BASE, esc(title), esc(desc), BASE))
            out = out.replace("</head>", block + "</head>", 1)
            meta_n += 1

        if out != src:
            open(p, "w", encoding="utf-8", newline="").write(out)
    print("css patched: %d   head meta patched: %d" % (css_n, meta_n))


if __name__ == "__main__":
    main()
