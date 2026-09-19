#!/usr/bin/env python3
"""Every money calculator printed US dollars in en-US number format, in all 45
languages: a German saw "Hauspreis ($)" and "$1,769.79".

Adds a currency selector to the eight money calculators. It defaults to the
currency of the page's language, remembers the visitor's choice in
localStorage, and formats through Intl.NumberFormat with the page's own locale,
so /ro/ shows "1.769,79 RON" and /ja/ shows "￥1,769" (no decimals, as yen
should be).

Idempotent - guarded by the CF_CUR_MARK marker.
"""
import os, re, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
MARK = "/*cf-cur-v1*/"

DEFAULT = {
 "af":"ZAR","ar":"AED","bg":"BGN","cs":"CZK","da":"DKK","de":"EUR","el":"EUR","en":"USD",
 "es":"EUR","et":"EUR","fa":"USD","fi":"EUR","fr":"EUR","ga":"EUR","he":"ILS","hi":"INR",
 "hr":"EUR","hu":"HUF","id":"IDR","it":"EUR","ja":"JPY","ko":"KRW","lt":"EUR","lv":"EUR",
 "mk":"MKD","ms":"MYR","mt":"EUR","nl":"EUR","no":"NOK","pl":"PLN","pt":"BRL","ro":"RON",
 "ru":"RUB","sk":"EUR","sl":"EUR","sq":"ALL","sr":"RSD","sv":"SEK","sw":"KES","th":"THB",
 "tl":"PHP","tr":"TRY","uk":"UAH","vi":"VND","zh":"CNY",
}
# code -> symbol shown in the dropdown. Codes are international, so the list
# needs no translation.
CURRENCIES = [
 ("USD","$"),("EUR","€"),("GBP","£"),("CHF","CHF"),("CAD","C$"),("AUD","A$"),
 ("JPY","¥"),("CNY","¥"),("INR","₹"),("KRW","₩"),("BRL","R$"),
 ("MXN","MX$"),("ZAR","R"),("TRY","₺"),("RUB","₽"),("UAH","₴"),
 ("PLN","zł"),("CZK","Kč"),("HUF","Ft"),("RON","lei"),("BGN","лв"),
 ("HRK","kn"),("RSD","din"),("MKD","ден"),("ALL","L"),
 ("SEK","kr"),("NOK","kr"),("DKK","kr"),("ILS","₪"),("AED","د.إ"),
 ("SAR","ر.س"),("EGP","E£"),("NGN","₦"),("KES","KSh"),
 ("IDR","Rp"),("MYR","RM"),("THB","฿"),("PHP","₱"),("VND","₫"),("SGD","S$"),
]

# page dir -> the page's own recalculate function
PAGES = {
 "mortgage-calculator":"mort", "loan-calculator":"loan", "savings-calculator":"sav",
 "compound-interest-calculator":"ci", "retirement-calculator":"ret",
 "paycheck-calculator":"pcCalc", "tip-calculator":"tip", "fuel-cost-calculator":"fuel",
}

OLD_FMT_2DP = ("function fmt$(n){return'$'+n.toLocaleString('en-US',"
               "{minimumFractionDigits:2,maximumFractionDigits:2});}")
OLD_FMT_0DP = "function fmt$(n){return'$'+Math.round(n).toLocaleString();}"

RUNTIME = """%s
var CFDEF='%%s';
function cfCur(){try{var v=localStorage.getItem('cfcur');if(v)return v;}catch(e){}return CFDEF;}
function cfFmt(n,dec){
  var loc=document.documentElement.lang||'en',c=cfCur(),o={style:'currency',currency:c};
  if(dec!=null){o.minimumFractionDigits=dec;o.maximumFractionDigits=dec;}
  try{return new Intl.NumberFormat(loc,o).format(n);}
  catch(e){return c+'\\u00a0'+(dec!=null?n.toFixed(dec):Math.round(n));}
}
function cfCurLabels(){var c=cfCur();
  Array.prototype.forEach.call(document.querySelectorAll('.cf-cur'),function(s){s.textContent=c;});
  var sel=document.getElementById('cfCurSel');if(sel)sel.value=c;}
function cfSetCur(v){try{localStorage.setItem('cfcur',v);}catch(e){}cfCurLabels();%%s();}
""" % MARK

SELECT = ('<select id="cfCurSel" aria-label="Currency" onchange="cfSetCur(this.value)" '
          'style="width:auto;margin-inline-start:auto;padding:5px 8px;font-size:.78rem;'
          'border-radius:8px">%s</select>')
OPTIONS = "".join('<option value="%s">%s %s</option>' % (c, s, c) for c, s in CURRENCIES)

LABEL_RE = re.compile(r'(<label[^>]*>[^<]*?) \(\$\)(</label>)')
HEAD_RE = re.compile(r'(<div class="calc-head">.*?)(</div>)', re.S)


def lang_of(p):
    parts = p.split("/")
    return parts[0] if len(parts) > 2 else "en"


def main():
    done = skipped = 0
    only = tuple(sys.argv[1:])
    for page, fn in sorted(PAGES.items()):
        for p in sorted(glob.glob("*/%s/index.html" % page)) + ["%s/index.html" % page]:
            if only and not p.startswith(only):
                continue
            t = open(p, encoding="utf-8").read()
            if MARK in t:
                continue
            o = t
            lang = lang_of(p)
            cur = DEFAULT.get(lang, "USD")

            # 1. labels: " ($)" -> " (<span class="cf-cur"></span>)"
            t = LABEL_RE.sub(lambda m: m.group(1) + ' (<span class="cf-cur"></span>)' + m.group(2), t)

            # 2. formatter
            if OLD_FMT_2DP in t:
                t = t.replace(OLD_FMT_2DP, "function fmt$(n){return cfFmt(n);}")
            elif OLD_FMT_0DP in t:
                t = t.replace(OLD_FMT_0DP, "function fmt$(n){return cfFmt(n,0);}")
            elif page == "fuel-cost-calculator":
                t = t.replace("'$'+cost.toFixed(2)", "cfFmt(cost)")
                t = t.replace("'$'+(cost/dist).toFixed(3)", "cfFmt(cost/dist,3)")
            else:
                print("  !! no formatter anchor in", p); skipped += 1; continue

            # 3. runtime, in front of the page's own calc script
            anchor = "\nfunction %s()" % fn
            if anchor not in t:
                print("  !! no %s() in %s" % (fn, p)); skipped += 1; continue
            t = t.replace(anchor, "\n" + (RUNTIME % (cur, fn)) + anchor, 1)

            # 4. selector in the card header + init
            t = HEAD_RE.sub(lambda m: m.group(1) + (SELECT % OPTIONS) + m.group(2), t, count=1)
            t = t.replace("\n%s();\n" % fn, "\ncfCurLabels();\n%s();\n" % fn, 1)

            open(p, "w", encoding="utf-8", newline="").write(t)
            done += 1
    print("currency selector added: %d pages (%d skipped)" % (done, skipped))


if __name__ == "__main__":
    main()
