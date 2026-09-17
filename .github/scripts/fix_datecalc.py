#!/usr/bin/env python3
"""date-calculator: the whole main SEO body and the FAQPage schema were left in
English in all 19 languages. Replaces them with real translations and reports
any string it could not place, so nothing stays English silently."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
I18N = os.path.expanduser("~/i18n")
EN = {
"h2a":"How to Calculate Days Between Two Dates",
"p1":"The simplest way to find days between dates is to convert both dates to a day count from a fixed reference point, then subtract. Our calculator does this automatically for any pair of dates.",
"p2":"Common uses for date calculations: counting days until a deadline or event, calculating someone's age in days, determining contract durations, figuring out when a payment is due, and calculating how many shopping days until a holiday.",
"p3":"Adding months is trickier than adding days because months have different lengths. Adding 1 month to January 31 is ambiguous — some systems use February 28, others use the last day of the target month. Our calculator uses the standard approach of adjusting to the last valid day of the month.",
"h2b":"Useful Date Facts",
"l1":"A regular year has 365 days; a leap year has 366 days",
"l2":"Leap years occur every 4 years, except centuries not divisible by 400 (2000 was a leap year; 1900 was not)",
"l3":"There are 52 weeks + 1 day in a regular year; 52 weeks + 2 days in a leap year",
"l4":"The average month length is 30.44 days (365.25 ÷ 12)",
"q1":"How many days are there between two dates?",
"a1":"Subtract the earlier date from the later date. Our calculator shows the result in days, weeks, months, and years simultaneously. Example: from January 1 to December 31 of the same year = 364 days.",
"q2":"How do I add 90 days to a date?",
"a2":'Enter your start date and type 90 in the "Add/Subtract Days" tab. Our calculator accounts for different month lengths and leap years automatically.',
"q3":"How many working/business days between two dates?",
"a3":"Business day calculation requires knowing local holidays. Our calculator shows calendar days. To convert: subtract weekends (2 days per week) and estimate roughly 10–12 public holidays per year for the US.",
"q4":"What is a Julian date?",
"a4":"A Julian date is a continuous count of days since noon on January 1, 4713 BC, used in astronomy. It is not the same as the Julian calendar. For everyday date arithmetic, standard calendar math is what you need.",
}

T = {}
for fn in ("date1.json", "date2.json", "date3.json"):
    T.update(json.load(open(os.path.join(I18N, fn), encoding="utf-8")))

def esc(s):
    """same escaping the page uses inside its JSON-LD string literals"""
    return s.replace("\\", "\\\\").replace('"', '\\"')

fail = 0
for lang, tr in sorted(T.items()):
    p = os.path.join(ROOT, lang, "date-calculator", "index.html")
    t = open(p, encoding="utf-8").read()
    missed = []
    for k, en in EN.items():
        new = tr[k]
        hit = False
        if en in t:
            t = t.replace(en, new); hit = True
        if esc(en) in t:
            t = t.replace(esc(en), esc(new)); hit = True
        if not hit:
            missed.append(k)
    open(p, "w", encoding="utf-8", newline="").write(t)
    if missed:
        fail = 1
        print("  %s: NOT REPLACED -> %s" % (lang, ",".join(missed)))
    else:
        print("  %s ok" % lang)
sys.exit(fail)
