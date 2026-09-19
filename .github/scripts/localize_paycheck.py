#!/usr/bin/env python3
"""Rewrite <lang>/paycheck-calculator/index.html to use local payroll rules (paycheck-engine.js).
Usage: python3 .github/scripts/localize_paycheck.py ro   (idempotent; run from repo root)"""
import re, sys, json, pathlib

LOC = {}

LOC['ro'] = dict(
 country='RO',
 title='Calculator salariu net 2026 — brut în net România',
 h1='Calculator salariu net România',
 desc='Calculează salariul net din brut în România: CAS 25%, CASS 10%, impozit 10%, deducerea personală și scutirea de 200 lei pentru salariul minim. Valabil iulie–decembrie 2026.',
 name='Calculator salariu net România',
 ui=dict(gross='Salariu brut (RON)', period='Perioada', per_m='Lunar', per_y='Anual',
   opt_minbase='Salariul meu de bază este salariul minim brut (4.325 lei) — scutire 200 lei'),
 labels=dict(gross='Salariu brut lunar', cas='CAS (pensie, 25%)', cass='CASS (sănătate, 10%)', tax='Impozit pe venit (10%)',
   ded='Deducere personală aplicată (nu se scade din net)', net='Salariu net lunar', netYear='Net anual', eff='Rată totală de reținere'),
 body='''<h2>Cum se calculează salariul net în România (iulie–decembrie 2026)</h2>
<p>Din salariul brut se rețin CAS (pensie) 25% și CASS (sănătate) 10%. Impozitul pe venit de 10% se aplică la brut minus CAS, CASS și deducerea personală. Salariul minim brut este 4.325 lei din 1 iulie 2026.</p>
<p><strong>Deducerea personală de bază</strong> (fără persoane în întreținere, la funcția de bază) este 20% din salariul minim, adică 865 lei, pentru un brut de cel mult 4.325 lei. Peste acest nivel scade cu 0,5 puncte procentuale la fiecare 50 de lei și dispare la un brut de peste 6.325 lei.</p>
<p><strong>Scutirea de 200 lei:</strong> dacă salariul de bază din contract este salariul minim brut, iar brutul total nu depășește 4.600 lei, 200 lei pe lună nu se impozitează și nu intră în baza CAS/CASS. Bifează căsuța din calculator dacă ești în acest caz.</p>
<h3>Exemplu</h3>
<p>La un brut de 8.000 lei: CAS 2.000, CASS 800, deducere 0, impozit 10% × (8.000 − 2.800) = 520. Net: 4.680 lei.</p>
<p><em>Calculatorul nu include persoane în întreținere, deduceri suplimentare, tichete de masă, sporuri sau scutiri sectoriale. Rezultatele sunt estimări; fluturașul de salariu al angajatorului este cel valabil.</em></p>''',
 faq=[
  ('Cât este CAS și CASS în 2026?','CAS este 25% și CASS este 10% din salariul brut. Pentru angajații cu contract de muncă nu există plafon lunar la aceste contribuții.'),
  ('Ce este deducerea personală?','Este o sumă care se scade din baza de calcul a impozitului. Pentru un brut de cel mult salariul minim este 20% din salariul minim (865 lei din iulie 2026) și scade treptat până la zero la 2.000 lei peste salariul minim.'),
  ('Cum funcționează scutirea de 200 lei pentru salariul minim?','Din iulie 2026, dacă salariul de bază din contract este salariul minim brut și brutul total nu depășește 4.600 lei, 200 lei lunar sunt scutiți de impozit și de contribuții sociale (300 lei în ianuarie–iunie 2026).'),
  ('De ce diferă rezultatul de fluturașul meu?','Fluturașul poate include persoane în întreținere, tichete de masă, sporuri, alte deduceri sau un salariu parțial lucrat, pe care calculatorul nu le modelează.'),
 ],
 sources=[
  ('https://static.anaf.ro/static/3/Galati/20260123122801_suma%20neimpozabila%20in%202026.pdf','ANAF — suma minimă neimpozabilă în anul 2026'),
  ('https://mmuncii.gov.ro/salariul-de-baza-minim-brut-pe-tara-garantat-in-plata-se-majoreaza/','Ministerul Muncii — salariul minim brut 4.325 lei din 1 iulie 2026'),
  ('https://static.anaf.ro/static/10/Brasov/Brasov/contributii_296_nou.pdf','ANAF — contribuții sociale după Legea 296/2023'),
 ],
 src_intro='Formulele și cifrele folosite de acest calculator provin din sursele publicate de mai jos. Regulile sunt valabile pentru perioada iulie–decembrie 2026.',
 src_note='Rezultatele sunt estimări pentru planificare, nu consultanță fiscală.',
 ad_lbl='Publicitate', faq_h='Întrebări frecvente', src_h='Surse și metodologie',
)

sys.path.insert(0,str(pathlib.Path(__file__).parent))
from paycheck_locales import EXTRA
LOC.update(EXTRA)

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def build(lang):
    L = LOC[lang]
    p = pathlib.Path(lang)/'paycheck-calculator'/'index.html'
    s = p.read_text(encoding='utf-8')
    # head strings
    old_title = re.search(r'<title>([^<]*)</title>', s).group(1)
    old_desc = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
    s = s.replace(old_title, esc(L['title'])).replace(old_desc, esc(L['desc']))
    # JSON-LD
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in L['faq']]}
    app_ld = {"@context":"https://schema.org","@type":"WebApplication","name":L['name'],
        "url":f"https://calculator-free.com/{lang}/paycheck-calculator/","description":L['desc'],
        "applicationCategory":"UtilitiesApplication","operatingSystem":"Any","inLanguage":lang,
        "offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}}
    lds = re.findall(r'<script type="application/ld\+json">.*?</script>', s, re.S)
    assert len(lds) >= 2, lds
    s = s.replace(lds[0], '<script type="application/ld+json">'+json.dumps(app_ld,ensure_ascii=False)+'</script>', 1)
    s = s.replace(lds[1], '<script type="application/ld+json">'+json.dumps(faq_ld,ensure_ascii=False)+'</script>', 1)
    # hero
    s = re.sub(r'<h1[^>]*>[^<]*</h1><p>[^<]*</p>', f'<h1>{esc(L["h1"])}</h1><p>{esc(L["desc"])}</p>', s, count=1)
    # body
    a = s.index('<div class="wrap"><div class="calc-card">')
    b = s.index('<footer>')
    region = s[a:b]
    ad = re.findall(r'<div class="wrap"><div class="ad-wrap">.*?</div></div>', region, re.S)
    ad = ad[-1] if ad else ''
    u = L['ui']
    faq_html = ''.join(f'<div class="faq-item"><div class="faq-q" onclick="faq(this)"><span>{esc(q)}</span><span class="faq-arr">+</span></div><div class="faq-a">{esc(a_)}</div></div>' for q,a_ in L['faq'])
    src_html = ''.join(f'<li><a href="{h}" target="_blank" rel="noopener nofollow">{esc(t)}</a></li>' for h,t in L['sources'])
    dg = L.get('defgross', 6000)
    sel_y = ' selected' if L.get('defper') == '12' else ''
    sel_m = '' if sel_y else ' selected'
    chk = lambda o: ' checked' if o in L.get('optdef', []) else ''
    opts = ''.join(f'<label style="display:flex;gap:8px;align-items:flex-start;font-size:.85rem;margin-top:8px;text-transform:none;letter-spacing:0;font-weight:500"><input type="checkbox" id="pcopt_{o}"{chk(o)}><span>{esc(u["opt_"+o])}</span></label>' for o in L.get('opts',['minbase']))
    new = (
      '<div class="wrap"><div class="calc-card"><div class="calc-head"><span class="calc-icon">💵</span>'
      f'<span class="calc-title">{esc(L["name"])}</span></div><div class="calc-body">\n'
      '<div class="row2">\n'
      f'  <div class="field"><label for="pcgross">{esc(u["gross"])}</label><input type="number" id="pcgross" value="{dg}" min="0"></div>\n'
      f'  <div class="field"><label for="pcperiod">{esc(u["period"])}</label><select id="pcperiod"><option value="1"{sel_m}>{esc(u["per_m"])}</option><option value="12"{sel_y}>{esc(u["per_y"])}</option></select></div>\n'
      '</div>\n'+opts+'\n<div class="result" id="pcResult"></div>\n'
      '<script src="/paycheck-engine.js"></script>\n'
      f'<script>CFPay.init({{country:"{L["country"]}",labels:{json.dumps(L["labels"],ensure_ascii=False)}}});</script>\n'
      '</div></div>'
      f'<div class="seo-section">{L["body"]}</div>'
      f'<div class="seo-section"><h2>{esc(L["faq_h"])}</h2>{faq_html}</div>'
      f'{ad}</div>'
      f'<div class="seo-section" id="sources"><h2>{esc(L["src_h"])}</h2><p>{esc(L["src_intro"])}</p><ul>{src_html}</ul><p><em>{esc(L["src_note"])}</em></p></div>'
    )
    s = s[:a] + new + s[b:]
    p.write_text(s, encoding='utf-8', newline='')
    print('ok', lang)

for l in sys.argv[1:]: build(l)
