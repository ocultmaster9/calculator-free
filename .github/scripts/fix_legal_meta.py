#!/usr/bin/env python3
"""The four non-calculator pages had placeholder meta descriptions ("Privacy
Policy") and About repeated the brand twice in its title. Give them real ones,
and keep og:/twitter: in step."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

PAGES = {
 "privacy-policy": (
   "Privacy Policy | calculator-free.com",
   "How calculator-free.com handles data: calculations never leave your browser. "
   "What Google AdSense and Analytics cookies do, and how to opt out."),
 "terms-of-use": (
   "Terms of Use | calculator-free.com",
   "Terms for using calculator-free.com. The calculators give general estimates, "
   "not financial, medical or legal advice."),
 "about": (
   "About calculator-free.com",
   "Free calculators for maths, finance, health and planning in 45 languages. "
   "Everything runs in your browser — your numbers never reach a server."),
 "contact": (
   "Contact | calculator-free.com",
   "Report a wrong result, suggest a calculator or ask about privacy — "
   "how to reach calculator-free.com."),
}

CONTACT_BODY = """<p>calculator-free.com is a small, independently run site. Email is the only
channel, and a real person reads it.</p>
<p>Email us at <a href="/cdn-cgi/l/email-protection#7f101c0a130b121e0c0b1a0d463f18121e1613511c1012"><span class="__cf_email__" data-cfemail="e58a86908991888496918097dca58288848c89cb868a88">[email&#160;protected]</span></a></p>
<h2>What we are glad to hear about</h2>
<ul>
<li><strong>A result that looks wrong.</strong> Tell us the calculator, the
numbers you entered and what you expected. Formula errors get priority over
everything else.</li>
<li><strong>A translation that reads badly.</strong> These pages are published in
45 languages and native speakers catch things we cannot.</li>
<li><strong>A calculator you wish existed.</strong></li>
<li><strong>Privacy questions</strong> — see the
<a href="https://calculator-free.com/privacy-policy/">privacy policy</a> first;
it covers cookies, advertising and how to opt out.</li>
</ul>
<p>We usually reply within a few days. We do not accept guest posts, link
exchanges or paid placements, and those emails are not answered.</p>"""

T_RE = re.compile(r"<title>.*?</title>", re.S)
SEO_RE = re.compile(r'(<div class="seo-section">).*?(</div>)', re.S)

def setmeta(t, pat, val):
    return re.sub(pat, lambda m: m.group(1) + val.replace("&", "&amp;").replace('"', "&quot;") + m.group(2), t, count=1)

for slug, (title, desc) in PAGES.items():
    p = slug + "/index.html"
    t = open(p, encoding="utf-8").read()
    o = t
    t = T_RE.sub("<title>%s</title>" % title, t, count=1)
    t = setmeta(t, r'(<meta name="description" content=")[^"]*(">)', desc)
    t = setmeta(t, r'(<meta property="og:title" content=")[^"]*(">)', title)
    t = setmeta(t, r'(<meta property="og:description" content=")[^"]*(">)', desc)
    t = setmeta(t, r'(<meta name="twitter:title" content=")[^"]*(">)', title)
    t = setmeta(t, r'(<meta name="twitter:description" content=")[^"]*(">)', desc)
    if slug == "contact" and SEO_RE.search(t):
        t = SEO_RE.sub(lambda m: m.group(1) + CONTACT_BODY + m.group(2), t, count=1)
    if t != o:
        open(p, "w", encoding="utf-8", newline="").write(t)
        print("  %s updated" % slug)
