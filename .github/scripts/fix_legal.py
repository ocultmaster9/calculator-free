#!/usr/bin/env python3
"""The privacy policy was 60 words. AdSense requires publishers to disclose
third-party cookie use, name the ad technology, and tell visitors how to opt
out; the old text did none of that, and the About page claimed "no data
collection beyond standard analytics" while personalised ads were running.

Rewritten against what the site actually loads: GA4 G-Q7VYR4L8Z7, AdSense
ca-pub-5798786176755576, Google's Funding Choices consent tool, flagcdn.com
for the switcher flags, and a localStorage key ("cft") for the theme.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
UPDATED = "2026-09-18"

PRIVACY = """<p><strong>Last updated: %s</strong></p>

<p>This policy explains what happens to data when you use calculator-free.com.
It covers this website only, not any site we link to.</p>

<h2>What we do not collect</h2>
<p>Every calculator on this site runs entirely in your browser. The numbers you
type — your income, your weight, your loan, your dates — are never transmitted
to us and are never stored anywhere. We do not run user accounts, we do not ask
for your name or email to use a calculator, and we do not build profiles of
individual visitors.</p>

<h2>Cookies and similar technologies</h2>
<p>Three things on this site store or read data in your browser:</p>
<ul>
<li><strong>Google AdSense</strong> (publisher ID ca-pub-5798786176755576) serves
the advertising on this site. Google and its partners use cookies and similar
identifiers to serve and measure ads, and — where you have consented, or where
consent is not required — to personalise them based on your prior visits to this
and other websites.</li>
<li><strong>Google Analytics 4</strong> (property G-Q7VYR4L8Z7) records
aggregate traffic: which pages are viewed, roughly where visitors come from, and
which device type they use. IP addresses are anonymised by Google before
processing.</li>
<li><strong>A theme preference</strong> stored under the key
<code>cft</code> in your browser's local storage, so the site remembers whether
you chose light or dark mode. It never leaves your device and we cannot read
it.</li>
</ul>
<p>Google's use of advertising cookies is described in
<a href="https://policies.google.com/technologies/partner-sites" rel="nofollow noopener" target="_blank">How
Google uses information from sites or apps that use our services</a>. A full
list of the vendors Google may work with is at
<a href="https://business.safety.google/adscookies/" rel="nofollow noopener" target="_blank">business.safety.google/adscookies</a>.</p>

<h2>Consent, and how to change your mind</h2>
<p>Visitors in the European Economic Area, the United Kingdom and Switzerland
are shown a consent message powered by Google's Funding Choices before
personalised advertising cookies are set, as required by the GDPR and the
ePrivacy Directive. You can withdraw or change that consent at any time using
the privacy or consent link the message leaves on the page, or by clearing this
site's cookies in your browser.</p>
<p>Independently of that message, you can:</p>
<ul>
<li>turn off personalised advertising across Google's services at
<a href="https://myadcenter.google.com/" rel="nofollow noopener" target="_blank">My
Ad Center</a>;</li>
<li>opt out of third-party vendor cookies at
<a href="https://optout.aboutads.info/" rel="nofollow noopener" target="_blank">optout.aboutads.info</a>
or <a href="https://www.youronlinechoices.eu/" rel="nofollow noopener" target="_blank">youronlinechoices.eu</a>;</li>
<li>block Google Analytics with the
<a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow noopener" target="_blank">official
opt-out add-on</a>;</li>
<li>block or delete cookies in your browser settings. The calculators keep
working if you do.</li>
</ul>

<h2>Legal basis and retention</h2>
<p>Where the GDPR applies, advertising and analytics cookies are set on the
basis of your consent; the theme preference is set on the basis of our
legitimate interest in the site working as you left it. We hold no database of
visitors, so there is nothing for us to retain or delete. Data collected by
Google is retained under Google's own schedules, described in its
<a href="https://policies.google.com/privacy" rel="nofollow noopener" target="_blank">privacy
policy</a>.</p>

<h2>Your rights</h2>
<p>Under the GDPR you have the right to access, correct, erase, restrict and
port your personal data, and to object to processing. Under the CCPA/CPRA,
California residents have the right to know what is collected, to delete it, and
to opt out of its "sale" or "sharing" — the opt-out links above are the way to
exercise that here. Because we hold no personal data ourselves, a request about
advertising or analytics data should go to Google; we will help you direct it if
you <a href="https://calculator-free.com/contact/">contact us</a>.</p>

<h2>Other services this site loads</h2>
<p>Pages load fonts from Google Fonts and the small country flags in the
language switcher from flagcdn.com. Both receive your IP address as part of any
ordinary web request. The site is served through Cloudflare, which processes
requests to deliver pages and protect against abuse.</p>

<h2>Children</h2>
<p>This site is not directed at children under 13 (under 16 in parts of the
EEA), and we do not knowingly collect their data.</p>

<h2>Changes and contact</h2>
<p>If this policy changes, the date at the top changes with it. Questions about
privacy: <a href="https://calculator-free.com/contact/">contact us</a>.</p>""" % UPDATED

TERMS = """<p><strong>Last updated: %s</strong></p>

<p>By using calculator-free.com you accept the terms below. If you do not accept
them, please do not use the site.</p>

<h2>What this site is</h2>
<p>calculator-free.com provides free calculators for general information and
education. It is free to use, requires no account, and is funded by advertising.</p>

<h2>No professional advice</h2>
<p>Results are estimates produced by published, general-purpose formulas. They
are not financial, tax, legal, medical or nutritional advice, and they cannot
account for your individual circumstances.</p>
<ul>
<li>The finance calculators ignore fees, insurance, local taxes and rate changes,
and the pay calculator models United States federal income tax, Social Security
and Medicare only — no state or local tax, and nothing outside the US.</li>
<li>The health calculators (BMI, body fat, calories, ovulation, pregnancy,
sleep) use population-level formulas that do not diagnose anything. Speak to a
qualified clinician before acting on any of them, and never use them to make a
decision about medication, treatment or pregnancy.</li>
<li>The betting calculators work out the arithmetic of a stake. They are not
advice to gamble, do not predict outcomes, and are intended only for adults in
jurisdictions where betting is legal.</li>
</ul>
<p>Verify anything important independently before you rely on it.</p>

<h2>Accuracy and availability</h2>
<p>We work to keep the formulas correct and fix errors when we find them, but we
give no warranty that the site is accurate, complete, uninterrupted or fit for a
particular purpose. To the fullest extent permitted by law we are not liable for
any loss arising from your use of the site or reliance on its results.</p>

<h2>Acceptable use</h2>
<p>You may use the calculators freely, including at work. You may not scrape the
site at a volume that degrades it for others, present it as your own, or
interfere with the advertising that pays for it.</p>

<h2>Intellectual property</h2>
<p>The text, design and code of this site belong to calculator-free.com. The
underlying mathematical formulas are public knowledge and belong to no one.</p>

<h2>Third-party links and ads</h2>
<p>Advertising and outbound links lead to sites we do not control and are not
responsible for.</p>

<h2>Changes</h2>
<p>These terms may change; the date above shows when they last did. Questions:
<a href="https://calculator-free.com/contact/">contact us</a>.</p>""" % UPDATED

ABOUT = """<p>calculator-free.com provides free, instant online calculators for
everyday maths, finance, health and planning — in 45 languages. No registration,
no paywall, no app to install.</p>

<h2>How it works</h2>
<p>Every calculator runs entirely in your browser. The numbers you type never
leave your device and are never sent to a server, so you can put a real salary
or a real loan into these tools without wondering where it ends up.</p>

<h2>How it is paid for</h2>
<p>The site is free because it carries advertising, served by Google AdSense.
Those ads use cookies, and in Europe we ask for your consent before the
personalised ones are set. Aggregate traffic statistics are collected through
Google Analytics. What each of those does, and how to switch them off, is set
out in full in our <a href="https://calculator-free.com/privacy-policy/">privacy
policy</a>.</p>

<h2>How the formulas are chosen</h2>
<p>Each calculator uses a published, standard formula, and the page states which
one — the Hodgdon–Beckett equation for body fat, Mifflin–St Jeor for calories,
the standard amortisation formula for loans and mortgages, and so on. Where a
formula has a metric and an imperial form, we use the one that matches the units
the page asks for. If you find a result that looks wrong, please
<a href="https://calculator-free.com/contact/">tell us</a> — we would rather fix
it than defend it.</p>

<h2>What it is not</h2>
<p>These are estimating tools, not professional advice. The
<a href="https://calculator-free.com/terms-of-use/">terms of use</a> explain the
limits, particularly for the health and finance calculators.</p>"""

SEO_RE = re.compile(r'(<div class="seo-section">).*?(</div>)', re.S)

for path, body, label in (("privacy-policy/index.html", PRIVACY, "privacy policy"),
                          ("terms-of-use/index.html", TERMS, "terms of use"),
                          ("about/index.html", ABOUT, "about")):
    t = open(path, encoding="utf-8").read()
    if not SEO_RE.search(t):
        print("  !! no seo-section in", path); continue
    n = SEO_RE.sub(lambda m: m.group(1) + body + m.group(2), t, count=1)
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    if n != t:
        open(path, "w", encoding="utf-8", newline="").write(n)
    print("  %-14s rewritten (%d words)" % (label, words))
