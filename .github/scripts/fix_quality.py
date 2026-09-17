#!/usr/bin/env python3
"""One-off quality fixes for calculator-free.com localized pages.

1. BMI result categories left in English inside the JS (18 languages).
2. Footer /bet-calculator/ link mislabelled with the "All calculators"
   translation (70 pages).
3. Category hub pages carry the AdSense loader but zero manual ad units.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
LANGS = ["ar","zh","da","nl","fr","de","hi","id","it","ja","ko","no",
         "pl","pt","ru","es","sv","tr","vi"]

# under / over / obese, taken from the terms each page already prints in its body.
BMI = {
 "ar":("نقص وزن","زيادة وزن","سمنة"),
 "zh":("体重过轻","超重","肥胖"),
 "da":("Undervægt","Overvægt","Svær overvægt"),
 "nl":("Ondergewicht","Overgewicht","Obesitas"),
 "fr":("Insuffisance pondérale","Surpoids","Obésité"),
 "de":("Untergewicht","Übergewicht","Adipositas"),
 "hi":("कम वज़न","अधिक वज़न","मोटापा"),
 "id":("Kurus","Kelebihan berat badan","Obesitas"),
 "it":("Sottopeso","Sovrappeso","Obesità"),
 "ja":("低体重","過体重","肥満"),
 "ko":("저체중","과체중","비만"),
 "no":("Undervekt","Overvekt","Fedme"),
 "pl":("Niedowaga","Nadwaga","Otyłość"),
 "pt":("Baixo peso","Sobrepeso","Obesidade"),
 "ru":("Дефицит массы тела","Избыточный вес","Ожирение"),
 "es":("Bajo peso","Sobrepeso","Obesidad"),
 "sv":("Undervikt","Övervikt","Fetma"),
 "tr":("Zayıf","Fazla kilolu","Obezite"),
}
BET = {
 "ar":"حاسبات المراهنات","zh":"投注计算器","da":"Væddemålsberegnere",
 "nl":"Wedcalculators","fr":"Calculateurs de paris","de":"Wettrechner",
 "hi":"बेटिंग कैलकुलेटर","id":"Kalkulator Taruhan","it":"Calcolatori di scommesse",
 "ja":"ベッティング計算機","ko":"베팅 계산기","no":"Oddskalkulatorer",
 "pl":"Kalkulatory zakładów","pt":"Calculadoras de apostas","ru":"Калькуляторы ставок",
 "es":"Calculadoras de apuestas","sv":"Oddskalkylatorer","tr":"Bahis Hesaplayıcıları",
 "vi":"Máy tính cá cược",
}
AD_LBL = {
 "en":"Advertisement","ar":"إعلان","zh":"广告","da":"Annonce","nl":"Advertentie",
 "fr":"Publicité","de":"Werbung","hi":"विज्ञापन","id":"Iklan","it":"Pubblicità",
 "ja":"広告","ko":"광고","no":"Annonse","pl":"Reklama","pt":"Publicidade",
 "ru":"Реклама","es":"Publicidad","sv":"Annons","tr":"Reklam","vi":"Quảng cáo",
}
SLOT = '6610588103'
CLIENT = 'ca-pub-5798786176755576'

def ad_block(lang):
    return ('<div class="wrap"><div class="ad-wrap"><span class="ad-lbl">%s</span>\n'
            '<ins class="adsbygoogle" style="display:block" data-ad-client="%s" '
            'data-ad-slot="%s" data-ad-format="auto" data-full-width-responsive="true"></ins>\n'
            '<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div></div>'
            % (AD_LBL[lang], CLIENT, SLOT))

def lang_of(p):
    h = p.split("/")[0]
    return h if h in LANGS else "en"

def pages():
    for dp, dn, fn in os.walk("."):
        dn[:] = [d for d in dn if d not in {".git","_stage","node_modules",".wrangler",".github","cdn-cgi","th"}]
        for f in fn:
            if f == "index.html":
                yield os.path.join(dp, f)[2:]

n_bmi = n_bet = n_ad = 0
for p in pages():
    lang = lang_of(p)
    t = open(p, encoding="utf-8").read()
    o = t

    # 1 — BMI categories
    if p.endswith("bmi-calculator/index.html") and lang in BMI:
        under, over, obese = BMI[lang]
        m = re.search(r"var cat=b<18\.5\?'([^']*)':b<25\?'([^']*)':b<30\?'([^']*)':'([^']*)';", t)
        if m:
            normal = m.group(2)
            t = t.replace(m.group(0),
                "var cat=b<18.5?'%s':b<25?'%s':b<30?'%s':'%s';" % (under, normal, over, obese))
            mc = re.search(r"var colors=\{[^}]*\};", t)
            if mc:
                t = t.replace(mc.group(0),
                    "var colors={'%s':'#3b82f6','%s':'#10b981','%s':'#f59e0b','%s':'#ef4444'};"
                    % (under, normal, over, obese))
        if t != o:
            n_bmi += 1

    # 2 — footer bet-calculator label
    if lang in BET:
        b = t
        t = re.sub(r'(<a href="https://calculator-free\.com/bet-calculator/">)[^<]*(</a>)',
                   lambda m: m.group(1) + BET[lang] + m.group(2), t)
        if t != b:
            n_bet += 1

    # 3 — hub pages with no manual ad units
    if re.search(r'-calculators/index\.html$', p) and '<ins class="adsbygoogle"' not in t:
        if 'ad-wrap{' in t and '</nav>' in t and '<footer>' in t:
            t = t.replace('</nav>', '</nav>' + ad_block(lang), 1)
            t = t.replace('<footer>', ad_block(lang) + '<footer>', 1)
            n_ad += 1

    if t != o:
        open(p, "w", encoding="utf-8", newline="").write(t)

print("bmi js fixed: %d   footer labels fixed: %d   hub ad units added: %d" % (n_bmi, n_bet, n_ad))
