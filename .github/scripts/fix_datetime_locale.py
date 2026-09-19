#!/usr/bin/env python3
"""Dates and clock times were formatted 'en-US' on all 45 languages: a Romanian
reading the ovulation calculator got "March 14, 2026", and the sleep calculator
printed "10:45 PM" to countries that use a 24-hour clock.

Format with the page's own language instead - one line each, and the browser
does the rest.
"""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
LOC = "(document.documentElement.lang||'en')"

SUBS = [
 # ovulation + pregnancy: long date
 ("d.toLocaleDateString('en-US',{month:'long',day:'numeric',year:'numeric'})",
  "d.toLocaleDateString(%s,{month:'long',day:'numeric',year:'numeric'})" % LOC),
 # date-calculator: weekday + long date
 ("toLocaleDateString('en-US',{weekday:'long',year:'numeric',month:'long',day:'numeric'})",
  "toLocaleDateString(%s,{weekday:'long',year:'numeric',month:'long',day:'numeric'})" % LOC),
]

OLD_TIME = ("function fmtTime(mins){var h=Math.floor(((mins%1440)+1440)%1440/60),"
            "m=((mins%1440)+1440)%1440%60;var ampm=h>=12?'PM':'AM';h=h%12||12;"
            "return h+':'+(m<10?'0':'')+m+' '+ampm;}")
NEW_TIME = ("function fmtTime(mins){var t=((mins%1440)+1440)%1440,h=Math.floor(t/60),m=t%60;"
            "try{return new Date(2000,0,1,h,m).toLocaleTimeString(" + LOC +
            ",{hour:'numeric',minute:'2-digit'});}"
            "catch(e){return (h<10?'0':'')+h+':'+(m<10?'0':'')+m;}}")

targets = []
for page in ("ovulation-calculator", "pregnancy-calculator", "date-calculator", "sleep-calculator"):
    targets += sorted(glob.glob("*/%s/index.html" % page)) + ["%s/index.html" % page]

n = 0
misses = {}
for p in targets:
    t = open(p, encoding="utf-8").read()
    o = t
    for old, new in SUBS:
        t = t.replace(old, new)
    t = t.replace(OLD_TIME, NEW_TIME)
    if t != o:
        open(p, "w", encoding="utf-8", newline="").write(t)
        n += 1
    elif "en-US" in o or "'PM':'AM'" in o:
        misses[p] = True
print("date/time locale fixed: %d files" % n)
if misses:
    print("  !! still carrying en-US / AM-PM: %s" % ", ".join(sorted(misses))[:400])
