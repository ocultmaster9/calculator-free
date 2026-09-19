#!/usr/bin/env python3
"""Interim fix: mark every translated paycheck-calculator page as US-only (title, H1, description).
Idempotent. Run from repo root. Pass already-localized language codes as args to skip them."""
import re, sys, pathlib

US = {'af':'VSA','ar':'الولايات المتحدة','bg':'САЩ','zh':'美国','cs':'USA','da':'USA','de':'USA','el':'ΗΠΑ',
'es':'EE. UU.','et':'USA','fa':'آمریکا','fi':'USA','fr':'États-Unis','ga':'SAM','he':'ארה״ב','hi':'अमेरिका',
'hr':'SAD','hu':'USA','id':'AS','it':'USA','ja':'米国','ko':'미국','lt':'JAV','lv':'ASV','mk':'САД','ms':'AS',
'mt':'Stati Uniti','nl':'VS','no':'USA','pl':'USA','pt':'EUA','ro':'SUA','ru':'США','sk':'USA','sl':'ZDA',
'sq':'SHBA','sr':'SAD','sv':'USA','sw':'Marekani','th':'สหรัฐฯ','tl':'US','tr':'ABD','uk':'США','vi':'Mỹ'}
SKIP = set(sys.argv[1:])
root = pathlib.Path('.')
changed = 0
for lang, us in US.items():
    if lang in SKIP: continue
    p = root/lang/'paycheck-calculator'/'index.html'
    s = p.read_text(encoding='utf-8')
    if 'data-cf-us="1"' in s: continue
    title = re.search(r'<title>([^<]*)</title>', s).group(1)
    new_title = re.sub(r' (2026|۲۰۲۶) — ', lambda m: f' {m.group(1)} ({us}) — ', title, count=1)
    assert new_title != title, lang
    d = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
    h = re.search(r'<h1([^>]*)>([^<]*)</h1>', s)
    s = s.replace(title, new_title).replace(d, f'({us}) {d}')
    s = s.replace(h.group(0), f'<h1{h.group(1)} data-cf-us="1">{h.group(2)} ({us})</h1>', 1)
    p.write_text(s, encoding='utf-8', newline='')
    changed += 1
print('changed', changed)
