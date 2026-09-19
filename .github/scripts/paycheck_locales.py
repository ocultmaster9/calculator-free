EXTRA = {}

EXTRA['pl'] = dict(
 country='PL', opts=[],
 title='Kalkulator wynagrodzenia netto 2026 — brutto na netto Polska',
 h1='Kalkulator wynagrodzenia netto Polska',
 desc='Oblicz pensję netto z brutto w Polsce: składki ZUS 13,71%, składka zdrowotna 9%, PIT 12% i 32%, kwota wolna 30 000 zł i koszty uzyskania 250 zł. Umowa o pracę, 2026.',
 name='Kalkulator wynagrodzenia netto Polska',
 ui=dict(gross='Wynagrodzenie brutto (PLN)', period='Okres', per_m='Miesięcznie', per_y='Rocznie'),
 labels=dict(gross='Wynagrodzenie brutto (miesięcznie)', zus='Składki ZUS (emerytalna, rentowa, chorobowa — 13,71%)',
   zdr='Składka zdrowotna (9%)', pit='Zaliczka na PIT (12% / 32%)', net='Wynagrodzenie netto (miesięcznie)',
   netYear='Netto rocznie', eff='Łączne obciążenie'),
 body='''<h2>Jak obliczyć wynagrodzenie netto w Polsce (2026)</h2>
<p>Z wynagrodzenia brutto pracownik płaci składki ZUS: emerytalną 9,76%, rentową 1,5% i chorobową 2,45%, razem 13,71%. Składki emerytalna i rentowa naliczane są do rocznego limitu 282 600 zł. Składka zdrowotna wynosi 9% podstawy, czyli brutto pomniejszonego o składki ZUS.</p>
<p>Podstawę PIT stanowi brutto minus składki ZUS minus koszty uzyskania przychodu (250 zł miesięcznie). Podatek to 12% do 120 000 zł rocznie i 32% od nadwyżki, pomniejszony o kwotę zmniejszającą podatek 3 600 zł rocznie (300 zł miesięcznie), co daje kwotę wolną 30 000 zł.</p>
<h3>Przykład</h3>
<p>Przy 8 000 zł brutto: ZUS 1 096,80 zł, składka zdrowotna 621,29 zł, podstawa PIT 6 653 zł, podatek 12% × 6 653 − 300 = 498 zł. Netto: około 5 784 zł.</p>
<p><em>Kalkulator zakłada umowę o pracę, jeden etat, koszty uzyskania 250 zł, brak ulg (np. dla młodych, na dzieci) i brak PPK. Wynik to średnia miesięczna z całego roku.</em></p>''',
 faq=[
  ('Ile wynoszą składki ZUS pracownika w 2026?','Pracownik płaci 9,76% na ubezpieczenie emerytalne, 1,5% na rentowe i 2,45% na chorobowe, razem 13,71%. Składki emerytalna i rentowa obowiązują do rocznego limitu 282 600 zł.'),
  ('Od czego liczy się składkę zdrowotną?','Składka zdrowotna to 9% podstawy, którą jest wynagrodzenie brutto pomniejszone o składki ZUS. Nie obniża ona podatku PIT.'),
  ('Ile wynosi kwota wolna od podatku?','Kwota wolna wynosi 30 000 zł rocznie. Wynika z kwoty zmniejszającej podatek 3 600 zł (12% z 30 000 zł), czyli 300 zł miesięcznie.'),
  ('Dlaczego mój przelew jest inny niż w kalkulatorze?','Na wypłatę wpływają m.in. ulgi, PPK, dodatkowe ubezpieczenia, koszty uzyskania 300 zł przy dojazdach oraz przekroczenie progów w trakcie roku.'),
 ],
 sources=[
  ('https://www.gazetaprawna.pl/praca/artykuly/10493630,az-282-600-zl-dopiero-taki-przychod-zwolni-ze-skladek-zus-w-2026-r.html','GazetaPrawna — limit składek ZUS 2026 (282 600 zł) i stawki'),
  ('https://www.podatki.gov.pl/podatki-firmowe/pit/stawki-i-limity','podatki.gov.pl — stawki i limity PIT'),
  ('https://policzmnie.pl/blog/skladki-zus-2026-pelny-przewodnik','policzmnie.pl — składki ZUS 2026, przykład 8 000 zł'),
 ],
 src_intro='Wzory i liczby użyte w kalkulatorze pochodzą z poniższych źródeł i dotyczą roku 2026.',
 src_note='Wyniki są szacunkami do planowania, nie poradą podatkową.',
 ad_lbl='Reklama', faq_h='Najczęstsze pytania', src_h='Źródła i metodologia',
)

EXTRA['de'] = dict(
 country='DE', opts=['childless'],
 title='Brutto-Netto-Rechner 2026 — Nettogehalt Deutschland (Steuerklasse I)',
 h1='Brutto-Netto-Rechner Deutschland',
 desc='Berechne dein Nettogehalt in Deutschland 2026: Lohnsteuer (Steuerklasse I), Solidaritätszuschlag sowie Beiträge zur Renten-, Kranken-, Pflege- und Arbeitslosenversicherung. Ohne Kirchensteuer.',
 name='Brutto-Netto-Rechner Deutschland',
 ui=dict(gross='Bruttogehalt (EUR)', period='Zeitraum', per_m='Monatlich', per_y='Jährlich',
   opt_childless='Keine Kinder (Pflegeversicherung +0,6 %)'),
 labels=dict(gross='Bruttogehalt pro Monat', rv='Rentenversicherung (9,3 %)', av='Arbeitslosenversicherung (1,3 %)',
   kv='Krankenversicherung (7,3 % + 1,45 % Zusatzbeitrag)', pv='Pflegeversicherung', lst='Lohnsteuer (Steuerklasse I)',
   soli='Solidaritätszuschlag', net='Nettogehalt pro Monat', netYear='Netto pro Jahr', eff='Abzüge gesamt'),
 body='''<h2>So berechnest du dein Nettogehalt in Deutschland (2026)</h2>
<p>Vom Brutto gehen die Arbeitnehmeranteile zur Sozialversicherung ab: Rentenversicherung 9,3 %, Arbeitslosenversicherung 1,3 %, Krankenversicherung 7,3 % plus die Hälfte des durchschnittlichen Zusatzbeitrags von 2,9 % (also 1,45 %) und Pflegeversicherung 1,8 % (2,4 % ohne Kinder). Die Beitragsbemessungsgrenze liegt 2026 bei 8.450 € im Monat für Renten- und Arbeitslosenversicherung und bei 5.812,50 € für Kranken- und Pflegeversicherung.</p>
<p>Die Lohnsteuer richtet sich nach dem Einkommensteuertarif 2026 (Grundfreibetrag 12.348 €). Der Rechner nutzt Steuerklasse I mit Arbeitnehmer-Pauschbetrag, Sonderausgaben-Pauschbetrag und Vorsorgepauschale. Der Solidaritätszuschlag fällt erst an, wenn die Einkommensteuer über 20.350 € im Jahr liegt.</p>
<h3>Beispiel</h3>
<p>Bei 4.000 € brutto ohne Kinder: Rentenversicherung 372 €, Arbeitslosenversicherung 52 €, Krankenversicherung 350 €, Pflegeversicherung 96 €, Lohnsteuer rund 525 €. Netto: etwa 2.606 €.</p>
<p><em>Nicht berücksichtigt sind Kirchensteuer, Steuerklassen II–VI, Freibeträge, abweichende Zusatzbeiträge der Krankenkasse, Kinderabschläge in der Pflegeversicherung und geldwerte Vorteile. Die Lohnabrechnung deines Arbeitgebers ist maßgeblich.</em></p>''',
 faq=[
  ('Welche Sozialabgaben zahlt der Arbeitnehmer 2026?','Rentenversicherung 9,3 %, Arbeitslosenversicherung 1,3 %, Krankenversicherung 8,75 % (7,3 % plus 1,45 % halber durchschnittlicher Zusatzbeitrag) und Pflegeversicherung 1,8 % bzw. 2,4 % für Kinderlose.'),
  ('Was ist die Beitragsbemessungsgrenze?','Über dieser Grenze werden keine weiteren Beiträge fällig. 2026 sind das 8.450 € pro Monat für Renten- und Arbeitslosenversicherung und 5.812,50 € pro Monat für Kranken- und Pflegeversicherung.'),
  ('Wann zahlt man den Solidaritätszuschlag?','Der Soli wird nur erhoben, wenn die Einkommensteuer 2026 bei Alleinstehenden über 20.350 € liegt. Darüber steigt er in einer Gleitzone bis maximal 5,5 % der Steuer.'),
  ('Warum weicht mein Netto von der Gehaltsabrechnung ab?','Kirchensteuer, individueller Zusatzbeitrag, Kinderanzahl, Steuerfreibeträge, Steuerklasse und Sachbezüge können das Netto verändern. Der Rechner ist eine Schätzung.'),
 ],
 sources=[
  ('https://www.lohn-info.de/sozialversicherungsbeitraege2026.html','lohn-info.de — Sozialversicherungsbeiträge und Beitragsbemessungsgrenzen 2026'),
  ('https://www.finanz-tools.de/einkommensteuer/berechnung-formeln/2026','finanz-tools.de — Einkommensteuer-Formeln 2026 (§ 32a EStG)'),
  ('https://www.tk.de/firmenkunden/fachthemen/fachthema-beitraege/solidaritaetszuschlag-2075802','Techniker Krankenkasse — Solidaritätszuschlag 2026, Freigrenze'),
 ],
 src_intro='Die Formeln und Zahlen dieses Rechners stammen aus den folgenden Quellen und gelten für das Jahr 2026.',
 src_note='Die Ergebnisse sind Schätzungen zur Planung und keine Steuerberatung.',
 ad_lbl='Werbung', faq_h='Häufige Fragen', src_h='Quellen und Methodik',
)

EXTRA['fr'] = dict(
 country='FR', opts=['cadre'], defgross=3000,
 title='Calculateur salaire brut en net 2026 — France (avant impôt)',
 h1='Calculateur salaire brut en net France',
 desc='Calculez votre salaire net avant impôt en France en 2026 : cotisations salariales de retraite (Agirc-Arrco), CSG et CRDS pour un salarié du secteur privé, cadre ou non cadre.',
 name='Calculateur salaire brut en net France',
 ui=dict(gross='Salaire brut (EUR)', period='Période', per_m='Mensuel', per_y='Annuel', opt_cadre='Statut cadre'),
 labels=dict(gross='Salaire brut mensuel', ret='Cotisations retraite (vieillesse, Agirc-Arrco, CEG, CET)',
   csg='CSG et CRDS (9,7 % sur 98,25 % du brut)', net='Salaire net mensuel avant impôt', netYear='Net annuel avant impôt', eff='Prélèvements totaux'),
 body='''<h2>Comment passer du brut au net en France (2026)</h2>
<p>Du salaire brut sont retirées les cotisations salariales : assurance vieillesse 6,90 % dans la limite du plafond mensuel de la Sécurité sociale (4 005 € en 2026) et 0,40 % sur la totalité du salaire, retraite complémentaire Agirc-Arrco 3,15 % et contribution d'équilibre général (CEG) 0,86 % sur la tranche 1, et contribution d'équilibre technique (CET) 0,14 %. S'y ajoutent la CSG (9,2 %) et la CRDS (0,5 %), calculées sur 98,25 % du brut.</p>
<p>Pour un cadre, l'Agirc-Arrco de 8,64 % et la CEG de 1,08 % s'appliquent aussi sur la tranche 2 (de 4 005 € à 32 040 €), avec l'APEC (0,024 %).</p>
<h3>Exemple</h3>
<p>Pour 3 000 € bruts par mois, non cadre : cotisations de retraite 343,50 €, CSG et CRDS 285,91 €. Net avant impôt : environ 2 370,59 €.</p>
<p><em>Le résultat est le net avant impôt sur le revenu. Le prélèvement à la source, la mutuelle, la prévoyance et les régimes locaux (Alsace-Moselle) ne sont pas inclus.</em></p>''',
 faq=[
  ('Quelle différence entre net avant impôt et net payé ?','Le net avant impôt est le salaire après cotisations salariales. Le net payé est ce montant diminué du prélèvement à la source, qui dépend de votre foyer fiscal.'),
  ('Pourquoi la CSG est-elle calculée sur 98,25 % du brut ?','La base de la CSG et de la CRDS est le salaire brut diminué d\'un abattement de 1,75 % pour frais professionnels, dans la limite de quatre plafonds de la Sécurité sociale.'),
  ('Quel est le plafond de la Sécurité sociale en 2026 ?','Il est de 4 005 € par mois. Il sert de limite à plusieurs cotisations, dont l\'assurance vieillesse plafonnée et la tranche 1 de la retraite complémentaire.'),
  ('Pourquoi mon bulletin de paie est-il différent ?','La mutuelle, la prévoyance, les avantages en nature, les régimes locaux et certains taux propres à votre convention collective modifient le net réel.'),
 ],
 sources=[('https://bulletin-paie.com/cotisations/taux/','bulletin-paie.com — taux de cotisations sociales 2026 et plafond de la Sécurité sociale')],
 src_intro='Les taux et plafonds utilisés proviennent de la source ci-dessous et valent pour 2026.',
 src_note='Les résultats sont des estimations de planification, pas un conseil fiscal.',
 ad_lbl='Publicité', faq_h='Questions fréquentes', src_h='Sources et méthodologie',
)

EXTRA['es'] = dict(
 country='ES', opts=[], defgross=30000, defper='12',
 title='Calculadora de sueldo neto 2026 — de bruto a neto en España',
 h1='Calculadora de sueldo neto España',
 desc='Calcula tu sueldo neto en España en 2026: cotización a la Seguridad Social (6,5 %) e IRPF con la escala general, para un trabajador soltero sin hijos con contrato indefinido.',
 name='Calculadora de sueldo neto España',
 ui=dict(gross='Salario bruto (EUR)', period='Periodo', per_m='Mensual', per_y='Anual'),
 labels=dict(gross='Salario bruto mensual', ss='Seguridad Social (6,5 %)', irpf='IRPF estimado', net='Sueldo neto mensual (12 mensualidades)',
   netYear='Neto anual', eff='Deducciones totales'),
 body='''<h2>Cómo pasar de bruto a neto en España (2026)</h2>
<p>El trabajador cotiza a la Seguridad Social un 6,5 % del salario: 4,70 % por contingencias comunes, 1,55 % por desempleo (contrato indefinido), 0,10 % por formación profesional y 0,15 % por el Mecanismo de Equidad Intergeneracional. La base máxima de cotización es de 5.101,20 € al mes.</p>
<p>Para el IRPF se parte del salario bruto menos la Seguridad Social y 2.000 € de otros gastos deducibles, con una reducción adicional para rendimientos del trabajo inferiores a 19.747,50 €. Sobre esa base se aplica la escala general (19 % hasta 12.450 €, 24 % hasta 20.200 €, 30 % hasta 35.200 €, 37 % hasta 60.000 €, 45 % hasta 300.000 € y 47 % por encima) y se resta la cuota correspondiente al mínimo personal de 5.550 €.</p>
<h3>Ejemplo</h3>
<p>Con 30.000 € brutos al año: Seguridad Social 1.950 €, IRPF 4.926 €, neto 23.124 € al año. Son unos 1.927 € al mes en 12 pagas o 1.652 € en 14 pagas.</p>
<p><em>El cálculo asume escala general sin diferencias autonómicas, soltero sin hijos ni otras circunstancias. La retención real de tu nómina puede variar.</em></p>''',
 faq=[
  ('¿Cuánto cotiza el trabajador a la Seguridad Social en 2026?','Un 6,5 % del salario: 4,70 % contingencias comunes, 1,55 % desempleo en contratos indefinidos, 0,10 % formación profesional y 0,15 % MEI, hasta la base máxima de 5.101,20 € mensuales.'),
  ('¿Qué es el mínimo personal y familiar?','Es la parte de la renta que no tributa por necesidades básicas. Para un contribuyente sin hijos son 5.550 € al año; se aplica restando de la cuota la que correspondería a esa cantidad.'),
  ('¿Por qué mi retención es distinta?','Las comunidades autónomas tienen escalas propias, y el número de hijos, la situación familiar, el tipo de contrato y otros gastos cambian la retención.'),
  ('¿Cuál es la diferencia entre 12 y 14 pagas?','El sueldo anual es el mismo. Con 14 pagas se reparte en 14 mensualidades, por lo que cada una es menor; el neto mensual mostrado corresponde a 12 pagas.'),
 ],
 sources=[
  ('https://www.uniondemutuas.es/wp-content/uploads/2026/04/Bases-y-tipos-de-cotizacion-2026-DO-115-ES_2026-01.pdf','Unión de Mutuas — bases y tipos de cotización 2026'),
  ('https://herramientasfiscales.com/calculadoras/calculadora-sueldo-neto/','herramientasfiscales.com — método de cálculo del IRPF y ejemplo de 30.000 €'),
 ],
 src_intro='Las cifras del calculador proceden de las fuentes siguientes y corresponden a 2026.',
 src_note='Los resultados son estimaciones para planificar, no asesoramiento fiscal.',
 ad_lbl='Publicidad', faq_h='Preguntas frecuentes', src_h='Fuentes y metodología',
)

EXTRA['it'] = dict(
 country='IT', opts=[], defgross=30000, defper='12',
 title='Calcolo stipendio netto 2026 — da lordo a netto in Italia',
 h1='Calcolo stipendio netto Italia',
 desc='Calcola lo stipendio netto in Italia nel 2026 dalla RAL: contributi INPS 9,19%, IRPEF al 23%, 33% e 43% e detrazioni per lavoro dipendente. Stima senza addizionali locali.',
 name='Calcolo stipendio netto Italia',
 ui=dict(gross='RAL / stipendio lordo (EUR)', period='Periodo', per_m='Mensile', per_y='Annuale'),
 labels=dict(gross='Lordo mensile', inps='Contributi INPS (9,19%)', irpef='IRPEF netta (dopo le detrazioni)',
   bonus='Riduzione del cuneo fiscale (redditi bassi)', net='Netto mensile (su 12 mesi)', netYear='Netto annuo', eff='Trattenute totali'),
 body='''<h2>Come si passa dal lordo al netto in Italia (2026)</h2>
<p>Dal lordo si sottraggono i contributi INPS a carico del lavoratore (9,19%). Sul reddito imponibile che resta si applica l'IRPEF: 23% fino a 28.000 euro, 33% da 28.001 a 50.000 euro e 43% oltre.</p>
<p>Dall'imposta si sottraggono le detrazioni per lavoro dipendente: 1.955 euro fino a 15.000 euro, poi decrescenti fino a zero a 50.000 euro, con 65 euro in più tra 25.000 e 35.000 euro e un'ulteriore detrazione di 1.000 euro tra 20.000 e 32.000 euro (decrescente fino a 40.000 euro). Per redditi fino a 20.000 euro si aggiunge la riduzione del cuneo fiscale.</p>
<h3>Esempio</h3>
<p>Con una RAL di 30.000 euro: INPS 2.757 euro, IRPEF netta circa 3.222 euro, netto annuo circa 24.021 euro. Sono circa 2.002 euro al mese su 12 mensilità o 1.848 euro su 13.</p>
<p><em>Le addizionali regionali e comunali, il trattamento integrativo, i familiari a carico e il welfare aziendale non sono inclusi: le addizionali riducono il netto di alcune centinaia di euro l'anno. La busta paga è il riferimento ufficiale.</em></p>''',
 faq=[
  ('Quanto pago di contributi INPS come dipendente?','La quota a carico del lavoratore è il 9,19% della retribuzione lorda per la generalità dei dipendenti del settore privato.'),
  ('Come funzionano gli scaglioni IRPEF 2026?','L\'aliquota è progressiva per scaglioni: 23% fino a 28.000 euro, 33% tra 28.001 e 50.000 euro e 43% oltre. Ogni aliquota si applica solo alla parte di reddito compresa nello scaglione.'),
  ('Perché il mio netto è diverso da questo calcolo?','Contano le addizionali regionali e comunali, i familiari a carico, il numero di mensilità, eventuali benefit e il tipo di contratto.'),
  ('Cosa sono le detrazioni per lavoro dipendente?','Sono importi che riducono direttamente l\'IRPEF dovuta e dipendono dal reddito: sono più alti per i redditi bassi e si azzerano oltre 50.000 euro.'),
 ],
 sources=[
  ('https://www.informazionefiscale.it/IRPEF-scaglioni-aliquote-calcolo','informazionefiscale.it — scaglioni IRPEF 2026 e detrazioni'),
  ('https://stipendionettocalcolatore.it/ral-30000-netto-2026/','stipendionettocalcolatore.it — esempio RAL 30.000 (INPS 9,19%)'),
 ],
 src_intro='Le aliquote e le formule usate provengono dalle fonti seguenti e valgono per il 2026.',
 src_note='I risultati sono stime a scopo di pianificazione, non consulenza fiscale.',
 ad_lbl='Pubblicità', faq_h='Domande frequenti', src_h='Fonti e metodologia',
)

EXTRA['nl'] = dict(
 country='NL', opts=['holiday'], optdef=['holiday'], defgross=4000,
 title='Bruto-netto berekenen 2026 — nettoloon Nederland',
 h1='Bruto-netto calculator Nederland',
 desc='Bereken je nettoloon in Nederland in 2026: loonheffing volgens de schijven van box 1, met algemene heffingskorting en arbeidskorting. Voor werknemers onder de AOW-leeftijd.',
 name='Bruto-netto calculator Nederland',
 ui=dict(gross='Brutoloon (EUR)', period='Periode', per_m='Per maand', per_y='Per jaar', opt_holiday='Inclusief 8% vakantiegeld (bovenop het brutoloon)'),
 labels=dict(gross='Brutoloon per maand', tax='Loonheffing (na heffingskortingen)', net='Nettoloon per maand (gemiddeld)',
   netYear='Netto per jaar', eff='Totale inhouding'),
 body='''<h2>Zo bereken je je nettoloon in Nederland (2026)</h2>
<p>In 2026 geldt voor werknemers onder de AOW-leeftijd in box 1 een tarief van 35,75% tot € 38.883, 37,56% tot € 78.426 en 49,50% daarboven. In het eerste tarief zitten de premies volksverzekeringen al.</p>
<p>Daarop komen de heffingskortingen. De algemene heffingskorting is maximaal € 3.115 en wordt vanaf € 29.736 afgebouwd met 6,398% van het meerdere tot nul bij € 78.426. De arbeidskorting stijgt tot € 5.685 bij een arbeidsinkomen van € 45.592 en daalt daarna met 6,51% tot nul bij € 132.920.</p>
<h3>Voorbeeld</h3>
<p>Bij € 4.000 bruto per maand met 8% vakantiegeld (€ 51.840 per jaar): loonheffing € 11.788 na € 1.701 algemene heffingskorting en € 5.278 arbeidskorting. Netto ongeveer € 3.338 per maand.</p>
<p><em>Pensioenpremie, de 30%-regeling, reiskosten en andere inhoudingen zijn niet meegenomen. Je loonstrook is leidend.</em></p>''',
 faq=[
  ('Welke belastingschijven gelden in 2026?','Tot € 38.883 geldt 35,75%, van € 38.883 tot € 78.426 geldt 37,56% en daarboven 49,50% (onder de AOW-leeftijd).'),
  ('Wat is de algemene heffingskorting?','Een korting op de te betalen belasting van maximaal € 3.115 in 2026. Boven een inkomen van € 29.736 wordt de korting lager en vanaf € 78.426 is ze nul.'),
  ('Wat is de arbeidskorting?','Een korting voor mensen die werken. In 2026 loopt ze op tot € 5.685 bij een arbeidsinkomen van € 45.592 en daalt daarna tot nul bij € 132.920.'),
  ('Waarom wijkt mijn netto van deze berekening af?','Pensioenpremie, de 30%-regeling, onbetaald verlof, bijtelling of afwijkende cao-afspraken veranderen het netto. Ook is vakantiegeld hier op 8% gezet.'),
 ],
 sources=[
  ('https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/voorlopige-aanslag-tarieven-en-heffingskortingen','Belastingdienst — tarieven en heffingskortingen 2026'),
  ('https://belastinghelden.nl/bruto-netto/salaris/4000','belastinghelden.nl — voorbeeld € 4.000 bruto per maand'),
 ],
 src_intro='De tarieven en kortingen komen uit de onderstaande bronnen en gelden voor 2026.',
 src_note='De uitkomsten zijn schattingen voor planning, geen belastingadvies.',
 ad_lbl='Advertentie', faq_h='Veelgestelde vragen', src_h='Bronnen en methode',
)

EXTRA['bg'] = dict(
 country='BG', opts=[], defgross=2000,
 title='Калкулатор на заплата 2026 — от бруто към нето в България',
 h1='Калкулатор на заплата България',
 desc='Изчислете нетната си заплата в България за 2026 г.: осигуровки 13,78% (максимален осигурителен доход 2 300 евро) и данък общ доход 10%.',
 name='Калкулатор на заплата България',
 ui=dict(gross='Брутна заплата (EUR)', period='Период', per_m='Месечно', per_y='Годишно'),
 labels=dict(gross='Брутна заплата на месец', ins='Осигуровки за сметка на служителя (13,78%)', tax='Данък общ доход (10%)',
   net='Нетна заплата на месец', netYear='Нетно на година', eff='Общо удръжки'),
 body='''<h2>Как се изчислява нетната заплата в България (2026)</h2>
<p>От брутната заплата се удържат осигуровки за сметка на служителя в размер на 13,78%: пенсионно осигуряване (включително универсален пенсионен фонд), фонд „Общо заболяване и майчинство“, безработица и здравно осигуряване. Осигурява се доход до максималния осигурителен доход от 2 300 евро на месец, в сила от 1 август 2026 г.</p>
<p>Данъкът общ доход е 10% върху заплатата след удържаните осигуровки.</p>
<h3>Пример</h3>
<p>При брутна заплата от 2 000 евро: осигуровки 275,60 евро, данък 172,44 евро. Нетна заплата: 1 551,96 евро.</p>
<p><em>Калкулаторът приема, че сте осигурен и в универсален пенсионен фонд, и не включва данъчни облекчения (например за деца или за хора с увреждания).</em></p>''',
 faq=[
  ('Колко са осигуровките за сметка на служителя през 2026 г.?','Общо 13,78% от осигурителния доход: пенсия 6,58%, универсален пенсионен фонд 2,2%, безработица 0,4%, общо заболяване и майчинство 1,4% и здравно осигуряване 3,2%.'),
  ('Кой е максималният осигурителен доход?','2 300 евро на месец от 1 август 2026 г. Върху доход над този размер осигуровки не се дължат.'),
  ('Какъв е данъкът върху заплатата?','Плосък данък общ доход от 10%, който се изчислява върху брутната заплата след удържаните осигуровки.'),
 ],
 sources=[
  ('https://smetni.bg/en/calculators/financial/salary/','Сметни — калкулатор бруто-нето 2026, ставки и пример'),
  ('https://www.noi.bg/dohod01082026/','НОИ — осигурителни доходи от 1 август 2026 г.'),
 ],
 src_intro='Ставките и праговете на калкулатора са от посочените източници и важат за 2026 г.',
 src_note='Резултатите са приблизителни, за планиране, и не представляват данъчна консултация.',
 ad_lbl='Реклама', faq_h='Често задавани въпроси', src_h='Източници и методика',
)

EXTRA['cs'] = dict(
 country='CZ', opts=[], defgross=40000,
 title='Kalkulačka čisté mzdy 2026 — z hrubé mzdy na čistou',
 h1='Kalkulačka čisté mzdy Česko',
 desc='Vypočítejte čistou mzdu v Česku pro rok 2026: sociální pojištění 7,1 %, zdravotní pojištění 4,5 %, daň z příjmu 15 % a 23 % a sleva na poplatníka 2 570 Kč měsíčně.',
 name='Kalkulačka čisté mzdy Česko',
 ui=dict(gross='Hrubá mzda (CZK)', period='Období', per_m='Měsíčně', per_y='Ročně'),
 labels=dict(gross='Hrubá mzda měsíčně', soc='Sociální pojištění (7,1 %)', zdr='Zdravotní pojištění (4,5 %)',
   tax='Záloha na daň z příjmu (po slevě na poplatníka)', net='Čistá mzda měsíčně', netYear='Čistá mzda ročně', eff='Celkové srážky'),
 body='''<h2>Jak se počítá čistá mzda v Česku (2026)</h2>
<p>Zaměstnanec platí ze mzdy sociální pojištění 7,1 % (do ročního stropu 2 350 416 Kč) a zdravotní pojištění 4,5 % bez stropu. Záloha na daň z příjmu činí 15 % z hrubé mzdy, z části měsíční mzdy nad 146 901 Kč pak 23 %.</p>
<p>Od vypočtené daně se odečítá sleva na poplatníka 2 570 Kč měsíčně (30 840 Kč ročně).</p>
<h3>Příklad</h3>
<p>Při hrubé mzdě 40 000 Kč: sociální pojištění 2 840 Kč, zdravotní pojištění 1 800 Kč, daň po slevě 3 430 Kč. Čistá mzda: 31 930 Kč.</p>
<p><em>Výpočet nezahrnuje slevy na děti, na studenta ani další slevy a odpočty. Rozhodující je výplatní páska od zaměstnavatele.</em></p>''',
 faq=[
  ('Kolik odvádí zaměstnanec na pojištění?','Sociální pojištění 7,1 % a zdravotní pojištění 4,5 % z hrubé mzdy, dohromady 11,6 %. Sociální pojištění se platí do ročního stropu 2 350 416 Kč.'),
  ('Co je sleva na poplatníka?','Základní sleva, která snižuje daň o 2 570 Kč měsíčně, tedy o 30 840 Kč za rok. Uplatňuje se po podpisu prohlášení u zaměstnavatele.'),
  ('Kdy se platí vyšší sazba daně 23 %?','Z části mzdy nad 146 901 Kč měsíčně. Nižší část mzdy se stále zdaňuje 15 %.'),
 ],
 sources=[('https://mzdy.cz/odvody/odvody-ze-mzdy','mzdy.cz — odvody ze mzdy 2026, sazby, sleva na poplatníka a příklad 40 000 Kč')],
 src_intro='Sazby a limity použité v kalkulačce pocházejí z uvedeného zdroje a platí pro rok 2026.',
 src_note='Výsledky jsou orientační odhady pro plánování, nikoli daňové poradenství.',
 ad_lbl='Reklama', faq_h='Časté otázky', src_h='Zdroje a metodika',
)

EXTRA['hu'] = dict(
 country='HU', opts=[], defgross=600000,
 title='Bruttó-nettó bérkalkulátor 2026 — nettó fizetés Magyarország',
 h1='Bruttó-nettó bérkalkulátor',
 desc='Számítsd ki a nettó fizetésed Magyarországon 2026-ban: 15% szja és 18,5% társadalombiztosítási járulék, kedvezmények nélkül.',
 name='Bruttó-nettó bérkalkulátor Magyarország',
 ui=dict(gross='Bruttó bér (HUF)', period='Időszak', per_m='Havi', per_y='Éves'),
 labels=dict(gross='Havi bruttó bér', szja='Személyi jövedelemadó (15%)', tb='Társadalombiztosítási járulék (18,5%)',
   net='Havi nettó bér', netYear='Éves nettó', eff='Összes levonás'),
 body='''<h2>Így számítható a nettó fizetés Magyarországon (2026)</h2>
<p>A bruttó bérből a munkavállaló 15% személyi jövedelemadót (szja) és 18,5% társadalombiztosítási járulékot fizet. Ez utóbbi 10% nyugdíjjárulékból, 4% egészségbiztosítási járulékból, 3% pénzbeli egészségbiztosítási járulékból és 1,5% munkaerőpiaci járulékból áll.</p>
<h3>Példa</h3>
<p>600 000 forint bruttó bérnél: szja 90 000 Ft, társadalombiztosítási járulék 111 000 Ft. Nettó bér: 399 000 Ft, a bruttó 66,5%-a.</p>
<p><em>A számítás nem tartalmazza a családi adókedvezményt, a 25 év alattiak szja-mentességét, a friss házasok kedvezményét és más adókedvezményeket. A munkáltató bérszámfejtése a mérvadó.</em></p>''',
 faq=[
  ('Mennyi a munkavállalói járulék 2026-ban?','A bruttó bér 18,5%-a: 10% nyugdíj, 4% egészségbiztosítás, 3% pénzbeli egészségbiztosítás és 1,5% munkaerőpiaci járulék.'),
  ('Mennyi a személyi jövedelemadó?','Egységesen 15% a bruttó bér után, kedvezmények nélkül.'),
  ('Miért más a nettó bérem a bérpapíromon?','A családi kedvezmény, a 25 év alattiak szja-mentessége, a friss házasok kedvezménye és a cafeteria-elemek módosítják a nettó összeget.'),
 ],
 sources=[('https://www.allaskisokos.hu/kalkulator/brutto-netto','allaskisokos.hu — bruttó-nettó kalkulátor 2026, járulékok és 600 000 Ft példa')],
 src_intro='A kalkulátor adatai az alábbi forrásból származnak és a 2026-os évre érvényesek.',
 src_note='Az eredmények tervezési célú becslések, nem adótanácsadás.',
 ad_lbl='Hirdetés', faq_h='Gyakori kérdések', src_h='Források és módszertan',
)

EXTRA['sk'] = dict(
 country='SK', opts=[], defgross=1620,
 title='Kalkulačka čistej mzdy 2026 — z hrubej mzdy na čistú',
 h1='Kalkulačka čistej mzdy Slovensko',
 desc='Vypočítajte čistú mzdu na Slovensku pre rok 2026: odvody zamestnanca 14,4 %, daň z príjmu 19 % až 35 % a nezdaniteľná časť základu dane 497,23 € mesačne.',
 name='Kalkulačka čistej mzdy Slovensko',
 ui=dict(gross='Hrubá mzda (EUR)', period='Obdobie', per_m='Mesačne', per_y='Ročne'),
 labels=dict(gross='Hrubá mzda mesačne', soc='Sociálne poistenie (9,4 %)', zdr='Zdravotné poistenie (5 %)',
   tax='Preddavok na daň z príjmu', net='Čistá mzda mesačne', netYear='Čistá mzda ročne', eff='Celkové zrážky'),
 body='''<h2>Ako sa počíta čistá mzda na Slovensku (2026)</h2>
<p>Zamestnanec platí sociálne poistenie 9,4 % (nemocenské, starobné, invalidné a poistenie v nezamestnanosti) a od roku 2026 zdravotné poistenie 5 %. Základ dane tvorí hrubá mzda znížená o odvody a o nezdaniteľnú časť základu dane 497,23 € mesačne.</p>
<p>Sadzby dane z príjmu v roku 2026: 19 % do ročného základu 43 983,32 €, 25 % do 60 349,21 €, 30 % do 75 010,32 € a 35 % nad touto hranicou.</p>
<h3>Príklad</h3>
<p>Pri hrubej mzde 1 620 €: sociálne poistenie 152,28 €, zdravotné poistenie 81,00 €, preddavok na daň 169,00 €. Čistá mzda: 1 217,72 €.</p>
<p><em>Výpočet predpokladá podpísané vyhlásenie na uplatnenie nezdaniteľnej časti a nezahŕňa daňový bonus na deti, maximálne vymeriavacie základy ani krátenie nezdaniteľnej časti pri vysokých príjmoch.</em></p>''',
 faq=[
  ('Koľko odvodov platí zamestnanec v roku 2026?','Spolu 14,4 % z hrubej mzdy: 9,4 % sociálne poistenie a 5 % zdravotné poistenie.'),
  ('Aké sú sadzby dane z príjmu v roku 2026?','Progresívne štyri sadzby: 19 %, 25 %, 30 % a 35 %. Prvá hranica je 43 983,32 € ročného základu dane.'),
  ('Čo je nezdaniteľná časť základu dane?','Suma, ktorá znižuje základ dane. V tomto výpočte je 497,23 € mesačne pri podpísanom vyhlásení u zamestnávateľa.'),
 ],
 sources=[
  ('https://jaspis.sk/aktuality/konsolidacny-balik-2026-zmeny-dane-odvody-priklady','Jaspis — konsolidačný balík 2026, sadzby dane a odvody'),
  ('https://bezkecov.sk/vypocet-cistej-mzdy/','bezkecov.sk — výpočet čistej mzdy 2026, príklad 1 620 €'),
 ],
 src_intro='Sadzby a sumy použité v kalkulačke pochádzajú z uvedených zdrojov a platia pre rok 2026.',
 src_note='Výsledky sú orientačné odhady na plánovanie, nie daňové poradenstvo.',
 ad_lbl='Reklama', faq_h='Časté otázky', src_h='Zdroje a metodika',
)

EXTRA['et'] = dict(
 country='EE', opts=['pillar'], optdef=['pillar'], defgross=2000,
 title='Palgakalkulaator 2026 — bruto- ja netopalk Eestis',
 h1='Palgakalkulaator Eesti',
 desc='Arvuta netopalk Eestis 2026. aastal: tulumaks 22%, maksuvaba tulu 700 eurot kuus, töötuskindlustus 1,6% ja kogumispension 2%.',
 name='Palgakalkulaator Eesti',
 ui=dict(gross='Brutopalk (EUR)', period='Periood', per_m='Kuus', per_y='Aastas', opt_pillar='Kogumispensioni (II samba) makse 2%'),
 labels=dict(gross='Brutopalk kuus', un='Töötuskindlustusmakse (1,6%)', pen='Kogumispension (2%)', tax='Tulumaks (22%)',
   net='Netopalk kuus', netYear='Netopalk aastas', eff='Kogu kinnipidamine'),
 body='''<h2>Kuidas arvutada netopalka Eestis (2026)</h2>
<p>Brutopalgast peetakse kinni töötuskindlustusmakse 1,6% ja kogumispensioni makse 2% (kui oled II sambaga liitunud). Tulumaks 22% arvutatakse summalt, millest on maha arvatud need maksed ja maksuvaba tulu 700 eurot kuus.</p>
<h3>Näide</h3>
<p>2000-eurose brutopalga korral: töötuskindlustus 32 eurot, kogumispension 40 eurot, tulumaks 270,16 eurot. Netopalk: 1657,84 eurot.</p>
<p><em>Arvestamata on lapsed, III samba sissemaksed, eluasemelaenu intressid ja muud maksuvabastused. Tööandja palgaarvestus on määrav.</em></p>''',
 faq=[
  ('Kui suur on tulumaks Eestis 2026?','22% summalt, millest on maha arvatud töötuskindlustus, kogumispension ja maksuvaba tulu.'),
  ('Kui suur on maksuvaba tulu?','700 eurot kuus, kui töötaja on selle tööandjale avaldusega kasutamiseks esitanud.'),
  ('Kas kogumispensioni makse on kohustuslik?','Kogumispension on II sambaga liitunutele. Standardmakse on 2% brutopalgast, soovi korral saab valida ka 4% või 6%.'),
 ],
 sources=[('https://minukalkulaator.ee/en/palgakalkulaator','minukalkulaator.ee — palgakalkulaator 2026, maksumäärad ja näide')],
 src_intro='Kalkulaatori määrad pärinevad allolevast allikast ja kehtivad 2026. aastal.',
 src_note='Tulemused on hinnangulised ja mõeldud planeerimiseks, mitte maksunõustamiseks.',
 ad_lbl='Reklaam', faq_h='Korduma kippuvad küsimused', src_h='Allikad ja metoodika',
)

EXTRA['lv'] = dict(
 country='LV', opts=[], defgross=1500,
 title='Algas kalkulators 2026 — no bruto uz neto Latvijā',
 h1='Algas kalkulators Latvija',
 desc='Aprēķiniet neto algu Latvijā 2026. gadā: VSAOI 10,5%, iedzīvotāju ienākuma nodoklis 25,5% un neapliekamais minimums 550 eiro mēnesī.',
 name='Algas kalkulators Latvija',
 ui=dict(gross='Bruto alga (EUR)', period='Periods', per_m='Mēnesī', per_y='Gadā'),
 labels=dict(gross='Bruto alga mēnesī', vs='Valsts sociālās apdrošināšanas iemaksas (10,5%)', tax='Iedzīvotāju ienākuma nodoklis (25,5% / 33%)',
   net='Neto alga mēnesī', netYear='Neto gadā', eff='Kopējie atvilkumi'),
 body='''<h2>Kā aprēķina neto algu Latvijā (2026)</h2>
<p>No bruto algas tiek ieturētas darba ņēmēja valsts sociālās apdrošināšanas obligātās iemaksas (VSAOI) 10,5% apmērā līdz 8 775 eiro mēnesī. Iedzīvotāju ienākuma nodokli (IIN) 25,5% aprēķina no algas pēc VSAOI un neapliekamā minimuma 550 eiro mēnesī. Ienākumam virs 8 775 eiro mēnesī piemēro 33%.</p>
<h3>Piemērs</h3>
<p>Ja bruto alga ir 1 500 eiro: VSAOI 157,50 eiro, IIN 202,09 eiro. Neto alga: 1 140,41 eiro.</p>
<p><em>Neapliekamo minimumu piemēro tikai pie viena darba devēja, kur iesniegta nodokļu grāmatiņa. Atvieglojumi par apgādājamiem nav iekļauti. Darba devēja algas aprēķins ir noteicošais.</em></p>''',
 faq=[
  ('Cik liels ir neapliekamais minimums 2026. gadā?','550 eiro mēnesī jeb 6 600 eiro gadā, ko piemēro vienā darba vietā ar iesniegtu nodokļu grāmatiņu.'),
  ('Cik procentu VSAOI ietur no algas?','Darba ņēmēja daļa ir 10,5% no bruto algas.'),
  ('Kāda ir IIN likme?','25,5% ienākumam līdz 8 775 eiro mēnesī un 33% ienākuma daļai virs šīs robežas.'),
 ],
 sources=[
  ('https://www.vid.gov.lv/lv/neapliekamais-minimums','Valsts ieņēmumu dienests — neapliekamais minimums'),
  ('https://pats.lv/algas-kalkulators','pats.lv — algas kalkulators 2026, IIN un VSAOI likmes'),
 ],
 src_intro='Kalkulatora likmes un summas ņemtas no norādītajiem avotiem un attiecas uz 2026. gadu.',
 src_note='Rezultāti ir aptuveni aprēķini plānošanai, nevis nodokļu konsultācija.',
 ad_lbl='Reklāma', faq_h='Biežāk uzdotie jautājumi', src_h='Avoti un metodika',
)

EXTRA['lt'] = dict(
 country='LT', opts=[], defgross=2000,
 title='Atlyginimo skaičiuoklė 2026 — nuo bruto iki neto Lietuvoje',
 h1='Atlyginimo skaičiuoklė Lietuva',
 desc='Apskaičiuokite atlyginimą „į rankas“ Lietuvoje 2026 m.: Sodros įmokos 19,5%, GPM 20% ir NPD pagal 2026 m. formulę.',
 name='Atlyginimo skaičiuoklė Lietuva',
 ui=dict(gross='Atlyginimas „ant popieriaus“ (EUR)', period='Laikotarpis', per_m='Per mėnesį', per_y='Per metus'),
 labels=dict(gross='Atlyginimas prieš mokesčius per mėnesį', vsd='Valstybinis socialinis draudimas (12,52%)', psd='Privalomasis sveikatos draudimas (6,98%)',
   tax='Gyventojų pajamų mokestis (GPM)', net='Atlyginimas „į rankas“ per mėnesį', netYear='Grynasis per metus', eff='Bendros išskaitos'),
 body='''<h2>Kaip skaičiuojamas grynasis atlyginimas Lietuvoje (2026)</h2>
<p>Iš bruto atlyginimo išskaičiuojamos Sodros įmokos: valstybinis socialinis draudimas (VSD) 12,52% ir privalomasis sveikatos draudimas (PSD) 6,98%. GPM taikomas 20% tarifas atlyginimui, sumažintam neapmokestinamuoju pajamų dydžiu (NPD).</p>
<p>2026 m. NPD = 747 − 0,49 × (bruto − 1 153) eurų, kai bruto viršija minimalią mėnesio algą (1 153 €); jei bruto nedidesnis, NPD yra 747 €. Metinės pajamos virš 82 962 € apmokestinamos 25%, o virš 138 270 € – 32%.</p>
<h3>Pavyzdys</h3>
<p>Kai bruto yra 2 000 €: VSD 250,40 €, PSD 139,60 €, NPD 331,97 €, GPM 333,61 €. Grynasis atlyginimas: 1 276,39 €.</p>
<p><em>NPD taikomas tik pagrindinėje darbovietėje pateikus prašymą. Neįtraukti papildomas NPD dėl vaikų ar negalios ir VSD įmokų viršutinė riba.</em></p>''',
 faq=[
  ('Kiek Sodros įmokų sumoka darbuotojas?','Iš viso 19,5% atlyginimo: 12,52% VSD ir 6,98% PSD.'),
  ('Kaip skaičiuojamas NPD 2026 m.?','Kai bruto ne didesnis nei 1 153 €, NPD yra 747 €. Didesnio atlyginimo atveju NPD = 747 − 0,49 × (bruto − 1 153).'),
  ('Koks GPM tarifas?','20% iki 82 962 € metinių pajamų, 25% nuo 82 962 € iki 138 270 € ir 32% viršijant šią sumą.'),
 ],
 sources=[
  ('https://grynai.lt/npd-skaiciuokle/','grynai.lt — NPD 2026 m. formulė'),
  ('https://atlyginimoskaiciuokle.com/','atlyginimoskaiciuokle.com — Sodros įmokų tarifai 2026 m.'),
  ('https://www.countrytaxcalc.com/tax-calculator/lithuania/','countrytaxcalc.com — GPM pakopos 2026 m.'),
 ],
 src_intro='Skaičiuoklėje naudojami tarifai ir formulės paimti iš šių šaltinių ir galioja 2026 m.',
 src_note='Rezultatai yra apytiksliai planavimo skaičiavimai, o ne mokesčių konsultacija.',
 ad_lbl='Reklama', faq_h='Dažniausiai užduodami klausimai', src_h='Šaltiniai ir metodika',
)

EXTRA['hr'] = dict(
 country='HR', opts=[], defgross=2000,
 title='Kalkulator neto plaće 2026 — bruto u neto Hrvatska',
 h1='Kalkulator neto plaće Hrvatska',
 desc='Izračunajte neto plaću u Hrvatskoj za 2026.: doprinosi za mirovinsko 20%, osobni odbitak 600 eura i porez na dohodak po stopama Grada Zagreba (23% i 33%).',
 name='Kalkulator neto plaće Hrvatska',
 ui=dict(gross='Bruto plaća (EUR)', period='Razdoblje', per_m='Mjesečno', per_y='Godišnje'),
 labels=dict(gross='Bruto plaća mjesečno', mio='Mirovinski doprinosi (MIO I 15% + MIO II 5%)', tax='Porez na dohodak (Zagreb 23% / 33%)',
   net='Neto plaća mjesečno', netYear='Neto godišnje', eff='Ukupni odbici'),
 body='''<h2>Kako se računa neto plaća u Hrvatskoj (2026)</h2>
<p>Iz bruto plaće radnik plaća doprinose za mirovinsko osiguranje: 15% u I. stup i 5% u II. stup, ukupno 20%. Od dohotka (bruto minus doprinosi) oduzima se osnovni osobni odbitak od 600 eura mjesečno, a na ostatak se plaća porez na dohodak.</p>
<p>Kalkulator koristi stope Grada Zagreba: 23% do 5 000 eura mjesečne porezne osnovice i 33% iznad toga. Ostali gradovi i općine imaju drukčije stope, pa se neto plaća izvan Zagreba može razlikovati.</p>
<h3>Primjer</h3>
<p>Uz bruto plaću od 2 000 eura: doprinosi 400 eura, porez 230 eura. Neto plaća: 1 370 eura.</p>
<p><em>Nisu uključeni odbici za djecu i uzdržavane članove ni gornja granica osnovice za doprinose. Obračun poslodavca je mjerodavan.</em></p>''',
 faq=[
  ('Koliko iznose doprinosi iz plaće?','20% bruto plaće za mirovinsko osiguranje: 15% za I. stup (MIO I) i 5% za II. stup (MIO II). Doprinos za zdravstveno plaća poslodavac povrh bruto plaće.'),
  ('Koliki je osobni odbitak u 2026.?','Osnovni osobni odbitak iznosi 600 eura mjesečno, uz dodatne iznose za djecu i uzdržavane članove.'),
  ('Zašto se porez razlikuje po gradovima?','Gradovi i općine sami određuju stope poreza na dohodak, a od 2025. prirez je uključen u te stope. Ovaj kalkulator koristi stope Grada Zagreba.'),
 ],
 sources=[
  ('https://mojkalkulator.com.hr/neto-placa','MojKalkulator — neto plaća 2026, doprinosi i osobni odbitak'),
  ('https://www.fiskai.hr/vodic/obracun-place/','FiskAI — obračun plaće 2026, redoslijed izračuna'),
 ],
 src_intro='Stope i iznosi u kalkulatoru potječu iz navedenih izvora i vrijede za 2026.',
 src_note='Rezultati su procjene za planiranje, a ne porezno savjetovanje.',
 ad_lbl='Oglas', faq_h='Česta pitanja', src_h='Izvori i metodologija',
)

EXTRA['da'] = dict(
 country='DK', opts=[], defgross=40000,
 title='Lønberegner 2026 — udbetalt løn efter skat i Danmark',
 h1='Lønberegner Danmark',
 desc='Beregn din løn efter skat i Danmark i 2026: AM-bidrag 8 %, bundskat 12,01 %, kommuneskat, mellemskat og topskat samt personfradrag og beskæftigelsesfradrag.',
 name='Lønberegner Danmark',
 ui=dict(gross='Bruttoløn (DKK)', period='Periode', per_m='Pr. måned', per_y='Pr. år'),
 labels=dict(gross='Bruttoløn pr. måned', am='Arbejdsmarkedsbidrag (8 %)', state='Statsskat (bundskat, mellem- og topskat)',
   komm='Kommuneskat (ca. 25,05 %)', net='Udbetalt løn pr. måned', netYear='Udbetalt pr. år', eff='Samlet træk'),
 body='''<h2>Sådan beregnes lønnen efter skat i Danmark (2026)</h2>
<p>Fra bruttolønnen betales først arbejdsmarkedsbidrag (AM-bidrag) på 8 %. Af den personlige indkomst betales bundskat på 12,01 % efter personfradrag på 54.100 kr. Kommuneskatten er i gennemsnit ca. 25,05 % og beregnes af indkomsten efter personfradrag og beskæftigelsesfradrag (12,75 %, højst 63.300 kr.).</p>
<p>Mellemskat på 7,5 % gælder for personlig indkomst mellem 641.200 og 777.900 kr. Over 777.900 kr. kommer topskat oveni med yderligere 7,5 %, og over 2.592.700 kr. yderligere 5 %.</p>
<h3>Eksempel</h3>
<p>Ved en bruttoløn på 40.000 kr. om måneden: AM-bidrag 3.200 kr., statsskat 3.878 kr. og kommuneskat 6.914 kr. Udbetalt: ca. 26.008 kr.</p>
<p><em>Kirkeskat, pension, ATP og øvrige fradrag er ikke medregnet, og kommuneskatten varierer mellem kommuner. Lønsedlen fra din arbejdsgiver er afgørende.</em></p>''',
 faq=[
  ('Hvad er AM-bidrag?','Arbejdsmarkedsbidraget er 8 % af bruttolønnen og trækkes, før der beregnes anden skat.'),
  ('Hvornår betaler man mellemskat og topskat?','Mellemskat på 7,5 % gælder for personlig indkomst mellem 641.200 og 777.900 kr. Topskat på yderligere 7,5 % gælder over 777.900 kr. i 2026.'),
  ('Hvor stort er personfradraget?','54.100 kr. om året i 2026. Det er den del af indkomsten, der ikke beskattes med bund- og kommuneskat.'),
 ],
 sources=[
  ('https://www.exploringdenmark.com/danish-tax-rates-2026/','Exploring Denmark — danske skattesatser 2026'),
  ('https://andreasregnskab.dk/news/danish-tax-reform-2026-net-salary/','Andreas Regnskab — skattereformen 2026 og beskæftigelsesfradrag'),
 ],
 src_intro='Satserne og beløbene i beregneren stammer fra kilderne nedenfor og gælder for 2026.',
 src_note='Resultaterne er vejledende skøn til planlægning og ikke skatterådgivning.',
 ad_lbl='Reklame', faq_h='Ofte stillede spørgsmål', src_h='Kilder og metode',
)

EXTRA['no'] = dict(
 country='NO', opts=[], defgross=50000,
 title='Lønnskalkulator 2026 — lønn etter skatt i Norge',
 h1='Lønnskalkulator Norge',
 desc='Beregn lønn etter skatt i Norge for 2026: trygdeavgift 7,6 %, skatt på alminnelig inntekt 22 %, trinnskatt, minstefradrag og personfradrag.',
 name='Lønnskalkulator Norge',
 ui=dict(gross='Bruttolønn (NOK)', period='Periode', per_m='Per måned', per_y='Per år'),
 labels=dict(gross='Bruttolønn per måned', alm='Skatt på alminnelig inntekt (22 %)', trinn='Trinnskatt', trygd='Trygdeavgift (7,6 %)',
   net='Lønn etter skatt per måned', netYear='Lønn etter skatt per år', eff='Samlet trekk'),
 body='''<h2>Slik beregnes lønn etter skatt i Norge (2026)</h2>
<p>Trygdeavgiften på lønn er 7,6 %. Skatten på alminnelig inntekt er 22 % av lønnen etter minstefradrag (46 %, høyst 95 700 kr) og personfradrag (114 540 kr).</p>
<p>I tillegg kommer trinnskatt på brutto inntekt: 1,7 % over 226 100 kr, 4,0 % over 318 300 kr, 13,7 % over 725 050 kr, 16,8 % over 980 100 kr og 17,8 % over 1 467 200 kr.</p>
<h3>Eksempel</h3>
<p>Ved 50 000 kr i bruttolønn per måned (600 000 kr i året): skatt på alminnelig inntekt 7 146 kr, trinnskatt 1 070 kr og trygdeavgift 3 800 kr per måned. Lønn etter skatt: ca. 37 985 kr.</p>
<p><em>Feriepenger, pensjon, fagforeningskontingent, andre fradrag og lavere satser i Finnmark og Nord-Troms er ikke med. Skattekortet og lønnsslippen er avgjørende.</em></p>''',
 faq=[
  ('Hva er trygdeavgiften i 2026?','7,6 % av lønnen. Avgiften gjelder når inntekten overstiger 99 650 kr.'),
  ('Hva er minstefradraget?','Et standardfradrag på lønnsinntekt: 46 % av inntekten, høyst 95 700 kr i 2026.'),
  ('Hvordan fungerer trinnskatten?','Trinnskatten beregnes av brutto inntekt i fem trinn med stigende satser fra 1,7 % til 17,8 %. Hver sats gjelder bare den delen av inntekten som ligger i trinnet.'),
 ],
 sources=[('https://www.regjeringen.no/no/tema/okonomi-og-budsjett/skatter-og-avgifter/skatte-og-avgiftssatser/skattesatser-2026/id3121978/','Regjeringen — skattesatser 2026')],
 src_intro='Satsene og beløpene i kalkulatoren er hentet fra kilden nedenfor og gjelder for 2026.',
 src_note='Resultatene er veiledende anslag til planlegging, ikke skatterådgivning.',
 ad_lbl='Annonse', faq_h='Ofte stilte spørsmål', src_h='Kilder og metode',
)

EXTRA['ga'] = dict(
 country='IE', opts=[], defgross=3333.33,
 title='Áireamhán Pá 2026 — Pá Glan in Éirinn',
 h1='Áireamhán Pá Glan Éire',
 desc='Ríomh do phá glan in Éirinn i 2026: cáin ioncaim 20% agus 40%, an Muirear Comhchoiteann Sóisialta (USC) agus PRSI, le creidmheasanna cánach.',
 name='Áireamhán Pá Glan Éire',
 ui=dict(gross='Pá comhlán (EUR)', period='Tréimhse', per_m='Sa mhí', per_y='Sa bhliain'),
 labels=dict(gross='Pá comhlán in aghaidh na míosa', tax='Cáin ioncaim (PAYE) tar éis creidmheasanna', usc='USC', prsi='PRSI',
   net='Pá glan in aghaidh na míosa', netYear='Pá glan in aghaidh na bliana', eff='Iomlán na mbaintí'),
 body='''<h2>Conas pá glan a ríomh in Éirinn (2026)</h2>
<p>In 2026 íocann duine singil cáin ioncaim ar an ráta caighdeánach 20% ar ioncam suas le €44,000 agus 40% ar an gcuid eile. Laghdaíonn creidmheas pearsanta €2,000 agus creidmheas fostaí PAYE €2,000 an cháin.</p>
<p>Cuirtear USC i bhfeidhm ar bhandaí: 0.5% ar na chéad €12,012, 2% suas le €28,700, 3% suas le €70,044 agus 8% os a chionn sin. Íocann fostaithe PRSI Aicme A ag 4.2% agus ardaíonn sé go 4.35% ó Dheireadh Fómhair 2026; úsáideann an t-áireamhán meánráta 4.2375% don bhliain.</p>
<h3>Sampla</h3>
<p>Ar phá comhlán €40,000 sa bhliain: cáin ioncaim €4,000, USC €732.80, PRSI €1,695. Pá glan: thart ar €2,798 sa mhí.</p>
<p><em>Níl creidmheasanna eile, pinsean ná baill teaghlaigh san áireamh. Is é do bhileog pá an fhoinse cheart.</em></p>''',
 faq=[
  ('Cad iad na rátaí cánach ioncaim in 2026?','20% ar ioncam suas le €44,000 do dhuine singil agus 40% ar an gcuid eile.'),
  ('Cad iad na creidmheasanna cánach?','Faigheann duine singil creidmheas pearsanta €2,000 agus creidmheas fostaí PAYE €2,000 in 2026.'),
  ('Cad é PRSI?','Ranníocaíocht árachais shóisialaigh is ea PRSI. Íocann fostaithe 4.2% in 2026, ag ardú go 4.35% ó Dheireadh Fómhair.'),
 ],
 sources=[('https://kpmg.com/ie/en/insights/tax/budget-2026/tables.html','KPMG Ireland — Budget 2026, rátaí cánach, USC agus PRSI')],
 src_intro='Tá na rátaí agus na méideanna san áireamhán seo tógtha ón bhfoinse thíos agus baineann siad le 2026.',
 src_note='Meastacháin le haghaidh pleanála iad na torthaí, ní comhairle cánach.',
 ad_lbl='Fógra', faq_h='Ceisteanna coitianta', src_h='Foinsí agus modheolaíocht',
)

EXTRA['mt'] = dict(
 country='MT', opts=[], defgross=2500,
 title='Kalkulatur tal-Paga 2026 — Paga Netta f\'Malta',
 h1='Kalkulatur tal-Paga Malta',
 desc='Ikkalkula l-paga netta tiegħek f\'Malta għall-2026: taxxa fuq id-dħul għal persuna waħda (0%, 15%, 25%, 35%) u kontribuzzjoni tas-sigurtà soċjali ta\' 10%.',
 name='Kalkulatur tal-Paga Malta',
 ui=dict(gross='Paga grossa (EUR)', period='Perjodu', per_m='Fix-xahar', per_y='Fis-sena'),
 labels=dict(gross='Paga grossa fix-xahar', tax='Taxxa fuq id-dħul', ssc='Sigurtà soċjali (10%, massimu €55.93 fil-ġimgħa)',
   net='Paga netta fix-xahar', netYear='Paga netta fis-sena', eff='Total tat-tnaqqis'),
 body='''<h2>Kif tiġi kkalkulata l-paga netta f\'Malta (2026)</h2>
<p>Fl-2026 persuna waħda tħallas taxxa fuq id-dħul skont l-iskala: 0% sa €12,000, 15% bejn €12,001 u €16,000, 25% bejn €16,001 u €60,000, u 35% fuq dan.</p>
<p>Il-kontribuzzjoni tas-sigurtà soċjali tal-impjegat hija 10% tal-paga, b\'massimu ta\' €55.93 fil-ġimgħa għal dawk imwielda wara l-1962.</p>
<h3>Eżempju</h3>
<p>B\'paga grossa ta\' €30,000 fis-sena: taxxa €4,100 u sigurtà soċjali €2,908.36. Paga netta: €22,991.64 fis-sena, jew madwar €1,916 fix-xahar.</p>
<p><em>Ir-riżultat ma jinkludix l-allowance tal-għoli tal-ħajja (COLA), bonusijiet, tnaqqis għal tfal jew skali oħra ta\' taxxa. Il-payslip tal-impjegatur huwa d-dokument uffiċjali.</em></p>''',
 faq=[
  ('X\'inhuma r-rati tat-taxxa għal persuna waħda?','0% sa €12,000, 15% sa €16,000, 25% sa €60,000 u 35% fuq dan.'),
  ('Kemm hija l-kontribuzzjoni tas-sigurtà soċjali?','10% tal-paga, b\'massimu ta\' €55.93 fil-ġimgħa għal dawk imwielda wara l-1962.'),
  ('Għaliex il-payslip tiegħi huwa differenti?','COLA, bonusijiet, skali tat-taxxa differenti (miżżewġin jew ġenituri) u tnaqqis oħra jistgħu jbiddlu n-net.'),
 ],
 sources=[('https://maltacalculator.com/blog/how-to-calculate-net-salary-malta-2026','maltacalculator.com — kif tikkalkula l-paga netta f\'Malta 2026')],
 src_intro='Ir-rati u l-ammonti tal-kalkulatur ġejjin mis-sors hawn taħt u japplikaw għall-2026.',
 src_note='Ir-riżultati huma stimi għall-ippjanar, mhux parir dwar it-taxxa.',
 ad_lbl='Reklam', faq_h='Mistoqsijiet frekwenti', src_h='Sorsi u metodoloġija',
)

EXTRA['tr'] = dict(
 country='TR', opts=[], defgross=60000,
 title='Brütten Nete Maaş Hesaplama 2026 — Türkiye',
 h1='Brütten Nete Maaş Hesaplama Türkiye',
 desc='2026 için Türkiye\'de net maaşınızı hesaplayın: SGK işçi payı %14, işsizlik sigortası %1, gelir vergisi dilimleri, damga vergisi ve asgari ücret istisnası.',
 name='Net Maaş Hesaplayıcı Türkiye',
 ui=dict(gross='Brüt maaş (TRY)', period='Dönem', per_m='Aylık', per_y='Yıllık'),
 labels=dict(gross='Aylık brüt maaş', sgk='SGK işçi payı (%14)', iss='İşsizlik sigortası (%1)',
   tax='Gelir vergisi (asgari ücret istisnası sonrası)', damga='Damga vergisi (binde 7,59)', net='Aylık net maaş (yıllık ortalama)',
   netYear='Yıllık net maaş', eff='Toplam kesinti'),
 body='''<h2>Türkiye\'de brütten nete maaş nasıl hesaplanır (2026)</h2>
<p>Brüt maaştan işçi payı olarak %14 SGK primi ve %1 işsizlik sigortası primi kesilir. Prim kesintisi için aylık üst sınır 297.270 TL\'dir. Kalan tutar gelir vergisi matrahını oluşturur.</p>
<p>2026 gelir vergisi dilimleri: 190.000 TL\'ye kadar %15, 540.000 TL\'ye kadar %20, 1.500.000 TL\'ye kadar %27, 4.000.000 TL\'ye kadar %35 ve üzeri %40. Damga vergisi binde 7,59\'dur. Brüt asgari ücrete (33.030 TL) karşılık gelen kısım gelir vergisi ve damga vergisinden istisnadır.</p>
<h3>Örnek</h3>
<p>60.000 TL brüt maaşta: SGK 8.400 TL, işsizlik 600 TL, gelir vergisi yaklaşık 5.005 TL, damga vergisi yaklaşık 205 TL. Net maaş: yaklaşık 45.790 TL.</p>
<p><em>Gelir vergisi matrahı yıl içinde kümülatif hesaplandığından aylık net maaş değişebilir; bu hesap yıllık ortalamadır. Yemek, ikramiye ve bireysel emeklilik kesintileri dahil değildir.</em></p>''',
 faq=[
  ('SGK işçi payı yüzde kaç?','%14 SGK ve %1 işsizlik sigortası, toplam %15. Prime esas kazanç aylık 297.270 TL ile sınırlıdır.'),
  ('2026 gelir vergisi dilimleri nelerdir?','%15 (190.000 TL\'ye kadar), %20 (540.000 TL\'ye kadar), %27 (1.500.000 TL\'ye kadar), %35 (4.000.000 TL\'ye kadar) ve %40.'),
  ('Asgari ücret istisnası nedir?','Brüt asgari ücret olan 33.030 TL\'ye karşılık gelen tutar gelir vergisi ve damga vergisinden istisna tutulur.'),
 ],
 sources=[
  ('https://musavirlerkulubu.com.tr/makale/2026-asgari-ucret-ve-yasal-kesintiler-tablosu-net-brut-ve-maliyet','Müşavirler Kulübü — 2026 asgari ücret ve yasal kesintiler'),
  ('https://kolayik.com/blog/2026-gelir-vergisi-dilimleri-guncel-tablo','Kolay İK — 2026 gelir vergisi dilimleri'),
 ],
 src_intro='Hesaplayıcıdaki oranlar ve tutarlar aşağıdaki kaynaklardan alınmıştır ve 2026 yılı içindir.',
 src_note='Sonuçlar planlama amaçlı tahminlerdir, vergi danışmanlığı değildir.',
 ad_lbl='Reklam', faq_h='Sık sorulan sorular', src_h='Kaynaklar ve yöntem',
)

EXTRA['ru'] = dict(
 country='RU', opts=[], defgross=100000,
 title='Калькулятор зарплаты 2026 — зарплата на руки в России',
 h1='Калькулятор зарплаты Россия',
 desc='Рассчитайте зарплату на руки в России на 2026 год: НДФЛ по прогрессивной шкале 13%, 15%, 18%, 20% и 22%. Страховые взносы платит работодатель.',
 name='Калькулятор зарплаты Россия',
 ui=dict(gross='Зарплата до налогов (RUB)', period='Период', per_m='В месяц', per_y='В год'),
 labels=dict(gross='Начисленная зарплата в месяц', ndfl='НДФЛ (прогрессивная шкала 13–22%)', net='Зарплата на руки в месяц',
   netYear='На руки в год', eff='Общая доля удержаний'),
 body='''<h2>Как рассчитывается зарплата на руки в России (2026)</h2>
<p>В России действует прогрессивная шкала НДФЛ: 13% с годового дохода до 2,4 млн рублей, 15% с части дохода от 2,4 до 5 млн, 18% от 5 до 20 млн, 20% от 20 до 50 млн и 22% с суммы свыше 50 млн рублей.</p>
<p>Страховые взносы на пенсионное, медицинское и социальное страхование платит работодатель сверх зарплаты, из зарплаты работника они не удерживаются.</p>
<h3>Пример</h3>
<p>При зарплате 100 000 рублей в месяц: НДФЛ 13 000 рублей. На руки: 87 000 рублей.</p>
<p><em>Расчёт не учитывает налоговые вычеты (стандартные, на детей, социальные, имущественные) и удержания по решению работника или суда.</em></p>''',
 faq=[
  ('Какие ставки НДФЛ действуют в 2026 году?','13% до 2,4 млн рублей годового дохода, 15% от 2,4 до 5 млн, 18% от 5 до 20 млн, 20% от 20 до 50 млн и 22% свыше 50 млн.'),
  ('Платит ли работник страховые взносы?','Нет. Страховые взносы за наёмного работника платит работодатель, они не уменьшают зарплату на руки.'),
  ('Почему сумма на руки отличается от расчётного листка?','На неё влияют налоговые вычеты, премии, алименты, удержания по исполнительным листам и особые режимы работодателя.'),
 ],
 sources=[('https://www.consultant.ru/document/cons_doc_LAW_495571/','КонсультантПлюс — прогрессивная шкала НДФЛ с 2025 года')],
 src_intro='Ставки и пороги калькулятора приведены по источнику ниже и относятся к 2026 году.',
 src_note='Результаты являются оценкой для планирования и не заменяют налоговую консультацию.',
 ad_lbl='Реклама', faq_h='Частые вопросы', src_h='Источники и методика',
)

EXTRA['uk'] = dict(
 country='UA', opts=[], defgross=30000,
 title='Калькулятор зарплати 2026 — зарплата на руки в Україні',
 h1='Калькулятор зарплати Україна',
 desc='Розрахуйте зарплату на руки в Україні на 2026 рік: ПДФО 18% та військовий збір 5%. Єдиний соціальний внесок сплачує роботодавець.',
 name='Калькулятор зарплати Україна',
 ui=dict(gross='Нарахована зарплата (UAH)', period='Період', per_m='На місяць', per_y='На рік'),
 labels=dict(gross='Нарахована зарплата на місяць', pdfo='ПДФО (18%)', vz='Військовий збір (5%)', net='Зарплата на руки за місяць',
   netYear='На руки за рік', eff='Загальна частка утримань'),
 body='''<h2>Як розраховується зарплата на руки в Україні (2026)</h2>
<p>З нарахованої зарплати роботодавець утримує податок на доходи фізичних осіб (ПДФО) 18% і військовий збір 5%. Єдиний соціальний внесок (ЄСВ) у розмірі 22% сплачує роботодавець понад зарплату, з неї він не утримується.</p>
<h3>Приклад</h3>
<p>Нарахована зарплата 30 000 грн: ПДФО 5 400 грн, військовий збір 1 500 грн. На руки: 23 100 грн.</p>
<p><em>Калькулятор не враховує податкові пільги та інші утримання. Розрахунковий листок роботодавця є остаточним.</em></p>''',
 faq=[
  ('Які податки утримують із зарплати в 2026 році?','ПДФО 18% та військовий збір 5% від нарахованої зарплати, разом 23%.'),
  ('Хто сплачує ЄСВ?','Єдиний соціальний внесок 22% сплачує роботодавець за свій рахунок, він не зменшує зарплату на руки.'),
  ('Чому сума на руки відрізняється від розрахункового листка?','На неї впливають податкові пільги, аліменти, утримання за виконавчими документами та інші виплати.'),
 ],
 sources=[('https://smartfin.ua/blog/podatky-iz-zarplaty-pratsivnyka-u-2026-rotsi','SMARTFIN — податки із зарплати 2026, приклад розрахунку')],
 src_intro='Ставки калькулятора наведено за джерелом нижче й стосуються 2026 року.',
 src_note='Результати є орієнтовною оцінкою для планування, а не податковою консультацією.',
 ad_lbl='Реклама', faq_h='Поширені запитання', src_h='Джерела та методологія',
)

EXTRA['sr'] = dict(
 country='RS', opts=[], defgross=100000,
 title='Kalkulator plate 2026 — neto plata nakon poreza u Srbiji',
 h1='Kalkulator plate Srbija',
 desc='Izračunajte neto platu u Srbiji za 2026: doprinosi zaposlenog 19,9%, porez na zaradu 10% i neoporezivi iznos od 34.221 dinar.',
 name='Kalkulator plate Srbija',
 ui=dict(gross='Bruto zarada (RSD)', period='Period', per_m='Mesečno', per_y='Godišnje'),
 labels=dict(gross='Bruto zarada mesečno', dop='Doprinosi zaposlenog (19,9%)', tax='Porez na zarade (10%)', net='Neto zarada mesečno',
   netYear='Neto godišnje', eff='Ukupna izdvajanja'),
 body='''<h2>Kako se računa neto plata u Srbiji (2026)</h2>
<p>Iz bruto zarade zaposleni plaća doprinose od 19,9%: penzijsko i invalidsko osiguranje (PIO) 14%, zdravstveno osiguranje 5,15% i osiguranje za slučaj nezaposlenosti 0,75%. Osnovica za doprinose je ograničena na iznos od 51.297 do 732.820 dinara mesečno.</p>
<p>Porez na zarade iznosi 10% i obračunava se na zaradu umanjenu za neoporezivi iznos od 34.221 dinar.</p>
<h3>Primer</h3>
<p>Za bruto zaradu od 100.000 dinara: doprinosi 19.900 dinara, porez 6.577,90 dinara. Neto zarada: 73.522,10 dinara.</p>
<p><em>Obračun ne uključuje olakšice za mlade ili druge posebne slučajeve, kao ni topli obrok i regres. Platni listić poslodavca je merodavan.</em></p>''',
 faq=[
  ('Koliki su doprinosi zaposlenog u 2026?','Ukupno 19,9% bruto zarade: PIO 14%, zdravstveno 5,15% i nezaposlenost 0,75%.'),
  ('Koliki je neoporezivi iznos u 2026?','34.221 dinar mesečno. Porez od 10% obračunava se samo na zaradu iznad tog iznosa.'),
  ('Zašto se moj neto razlikuje od obračuna?','Na neto utiču olakšice, prekovremeni rad, naknade i posebni režimi poslodavca.'),
 ],
 sources=[('https://feruvi.rs/blog/bruto-neto-plata','Feruvi — bruto u neto plata 2026, obračun i primer')],
 src_intro='Stope i iznosi u kalkulatoru potiču iz navedenog izvora i važe za 2026.',
 src_note='Rezultati su procene za planiranje, a ne poreski saveti.',
 ad_lbl='Reklama', faq_h='Česta pitanja', src_h='Izvori i metodologija',
)

EXTRA['el'] = dict(
 country='GR', opts=[], defgross=2000,
 title='Αριθμομηχανή Μισθού 2026 — Καθαρός μισθός στην Ελλάδα',
 h1='Αριθμομηχανή καθαρού μισθού Ελλάδα',
 desc='Υπολογίστε τον καθαρό μισθό σας στην Ελλάδα για το 2026: εισφορές e-EFKA 13,37%, φορολογική κλίμακα 9%–44% και έκπτωση φόρου 777 €. Με 14 μισθούς.',
 name='Αριθμομηχανή καθαρού μισθού Ελλάδα',
 ui=dict(gross='Μεικτός μισθός (EUR)', period='Περίοδος', per_m='Μηνιαίως (ανά μισθό)', per_y='Ετησίως'),
 labels=dict(gross='Μεικτός μισθός ανά μήνα (14 μισθοί)', efka='Εισφορές e-EFKA (13,37%)', tax='Φόρος εισοδήματος μετά την έκπτωση φόρου',
   net='Καθαρός μισθός ανά μήνα (14 μισθοί)', netYear='Καθαρό ετήσιο εισόδημα (14 μισθοί)', eff='Συνολικές κρατήσεις'),
 body='''<h2>Πώς υπολογίζεται ο καθαρός μισθός στην Ελλάδα (2026)</h2>
<p>Η αριθμομηχανή θεωρεί 14 μισθούς τον χρόνο. Ο εργαζόμενος πληρώνει εισφορές e-EFKA 13,37% μέχρι το μηνιαίο όριο των 7.761,94 €.</p>
<p>Ο φόρος υπολογίζεται στο ετήσιο εισόδημα μετά τις εισφορές με κλίμακα: 9% έως 10.000 €, 20% έως 20.000 €, 26% έως 30.000 €, 34% έως 40.000 €, 39% έως 60.000 € και 44% πάνω από 60.000 €. Η έκπτωση φόρου είναι 777 € για εργαζόμενο χωρίς παιδιά και μειώνεται κατά 20 € για κάθε 1.000 € εισοδήματος πάνω από 12.000 €.</p>
<h3>Παράδειγμα</h3>
<p>Με μεικτό μισθό 2.000 € ανά μήνα (28.000 € τον χρόνο): εισφορές 267,40 €, φόρος 248,20 € ανά μήνα. Καθαρός μισθός: περίπου 1.484 €.</p>
<p><em>Δεν περιλαμβάνονται τα ειδικά φορολογικά μέτρα για νέους έως 30 ετών, τα παιδιά και άλλες εκπτώσεις. Το εκκαθαριστικό του εργοδότη είναι το επίσημο.</em></p>''',
 faq=[
  ('Πόσες είναι οι εισφορές του εργαζομένου το 2026;','13,37% επί των αποδοχών, μέχρι το μηνιαίο όριο 7.761,94 €.'),
  ('Ποιοι είναι οι φορολογικοί συντελεστές;','Η κλίμακα είναι 9%, 20%, 26%, 34%, 39% και 44%, με όρια στις 10.000 €, 20.000 €, 30.000 €, 40.000 € και 60.000 €.'),
  ('Τι είναι η έκπτωση φόρου;','Ποσό που αφαιρείται από τον φόρο. Είναι 777 € χωρίς παιδιά και μειώνεται κατά 20 € ανά 1.000 € εισοδήματος πάνω από 12.000 €.'),
 ],
 sources=[('https://joberos.com/en/ypologismos-misthou','Joberos — υπολογισμός μισθού 2026 (νόμος 5246/2025)')],
 src_intro='Οι συντελεστές και τα ποσά της αριθμομηχανής προέρχονται από την παρακάτω πηγή και ισχύουν για το 2026.',
 src_note='Τα αποτελέσματα είναι εκτιμήσεις για προγραμματισμό, όχι φορολογική συμβουλή.',
 ad_lbl='Διαφήμιση', faq_h='Συχνές ερωτήσεις', src_h='Πηγές και μεθοδολογία',
)

EXTRA['pt'] = dict(
 country='BR', opts=[], defgross=5800,
 title='Calculadora de Salário Líquido 2026 — CLT no Brasil',
 h1='Calculadora de salário líquido Brasil',
 desc='Calcule o salário líquido no Brasil em 2026: INSS progressivo (teto R$ 8.475,55), IRRF com desconto simplificado e a isenção até R$ 5.000 de renda mensal.',
 name='Calculadora de salário líquido Brasil',
 ui=dict(gross='Salário bruto (BRL)', period='Período', per_m='Mensal', per_y='Anual'),
 labels=dict(gross='Salário bruto mensal', inss='INSS (progressivo)', irrf='IRRF (imposto de renda retido)', net='Salário líquido mensal', netYear='Líquido anual (12 meses)', eff='Total de descontos'),
 body='''<h2>Como calcular o salário líquido no Brasil (2026)</h2>
<p>Do salário bruto desconta-se primeiro o INSS, de forma progressiva: 7,5% até R$ 1.621,00, 9% até R$ 2.902,84, 12% até R$ 4.354,27 e 14% até o teto de R$ 8.475,55. A contribuição máxima é de R$ 988,09 por mês.</p>
<p>Sobre o valor após o INSS, ou sobre o desconto simplificado de R$ 607,20 quando for mais vantajoso, aplica-se a tabela do IRRF (0%, 7,5%, 15%, 22,5% e 27,5%). Em 2026, quem recebe até R$ 5.000 por mês não paga IRRF, e entre R$ 5.000,01 e R$ 7.350 há um redutor que diminui gradualmente o imposto.</p>
<h3>Exemplo</h3>
<p>Com salário bruto de R$ 5.800: INSS de R$ 613,51 e IRRF de R$ 311,17. Líquido: R$ 4.875,32.</p>
<p><em>O cálculo não considera dependentes, FGTS (pago pelo empregador), vale-transporte, plano de saúde, pensão alimentícia nem outras deduções. O holerite da empresa é o documento válido.</em></p>''',
 faq=[
  ('Quanto é o desconto do INSS em 2026?','É progressivo: 7,5%, 9%, 12% e 14% por faixa, até o teto de R$ 8.475,55, o que dá no máximo R$ 988,09 por mês.'),
  ('Quem está isento de Imposto de Renda em 2026?','Quem recebe até R$ 5.000 por mês fica isento na fonte. Entre R$ 5.000,01 e R$ 7.350 há redução parcial do imposto.'),
  ('O FGTS é descontado do meu salário?','Não. O depósito de 8% no FGTS é feito pelo empregador e não reduz o salário líquido.'),
 ],
 sources=[
  ('https://www.deel.com/pt/blog/nova-tabela-irrf-como-calcular/','Deel — nova tabela do IRRF e como calcular'),
  ('https://www.contabilizei.com.br/contabilidade-online/tabela-inss/','Contabilizei — tabela do INSS'),
  ('https://calcularclt.com.br/tabelas/irrf-2026','CalcularCLT — tabela do IRRF 2026'),
 ],
 src_intro='As alíquotas e os valores desta calculadora vêm das fontes abaixo e valem para 2026.',
 src_note='Os resultados são estimativas para planejamento, não aconselhamento tributário.',
 ad_lbl='Publicidade', faq_h='Perguntas frequentes', src_h='Fontes e metodologia',
)

EXTRA['ja'] = dict(
 country='JP', opts=[], defgross=400000,
 title='手取り計算 2026 — 日本の給与の額面から手取りへ',
 h1='手取り計算(日本)',
 desc='2026年の日本の手取りを計算:健康保険、厚生年金、雇用保険、所得税(復興特別所得税2.1%)、住民税10%を反映。東京・協会けんぽ、40歳未満、扶養なしの目安。',
 name='手取り計算(日本)',
 ui=dict(gross='月額の額面給与(JPY)', period='期間', per_m='月額', per_y='年額'),
 labels=dict(gross='月額の額面給与', health='健康保険(子ども・子育て支援金を含む)', pension='厚生年金(9.15%)', emp='雇用保険(0.5%)', tax='所得税(復興特別所得税を含む)', res='住民税(10%+均等割)', net='月額の手取り', netYear='年間の手取り', eff='控除の合計割合'),
 body='''<h2>日本の手取りの計算方法(2026年)</h2>
<p>額面給与から、健康保険(東京・協会けんぽで本人負担約5.04%、子ども・子育て支援金を含む)、厚生年金9.15%(標準報酬月額の上限65万円)、雇用保険0.5%が引かれます。</p>
<p>所得税は、給与所得控除、社会保険料控除、基礎控除(合計所得に応じて104万円など)を差し引いた課税所得に5%〜45%の税率を適用し、復興特別所得税2.1%を加えます。住民税は所得割10%と均等割5,000円です。</p>
<h3>計算例</h3>
<p>年収500万円(月額約41.7万円、賞与なしの年換算)の場合、年間の手取りは約394万円です。</p>
<p><em>賞与、扶養家族、40歳以上の介護保険、地域ごとの保険料率の違い、住民税の前年課税は含まれていません。給与明細が正式な金額です。</em></p>''',
 faq=[
  ('手取りは額面のどれくらいですか?','おおむね75〜85%です。年収が上がるほど所得税・住民税の割合が高くなります。'),
  ('社会保険料の内訳は?','健康保険(東京・協会けんぽで約5.04%)、厚生年金9.15%、雇用保険0.5%です。厚生年金の標準報酬月額の上限は65万円です。'),
  ('住民税はいつ引かれますか?','前年の所得に基づいて翌年6月から12か月で引かれるのが一般的です。この計算機は年間の目安を月割りで示しています。'),
 ],
 sources=[
  ('https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm','国税庁 — 所得税の税率(タックスアンサー No.2260)'),
  ('https://www.tkc.jp/consolidate/webcolumn/column202605_1_col01/','TKC — 給与所得控除と基礎控除の見直し'),
  ('https://tedori-calc.com/tedori-keisan-hyo/','手取り計算表 — 2026年の計算例'),
 ],
 src_intro='この計算機の税率と金額は下記の資料に基づき、2026年に対応しています。',
 src_note='結果は計画のための目安であり、税務上の助言ではありません。',
 ad_lbl='広告', faq_h='よくある質問', src_h='出典と計算方法',
)

EXTRA['ko'] = dict(
 country='KR', opts=[], defgross=2500000,
 title='실수령액 계산기 2026 — 한국 월급 세후 계산',
 h1='실수령액 계산기 한국',
 desc='2026년 한국 월급 실수령액을 계산하세요: 국민연금 4.75%, 건강보험 3.595%, 장기요양, 고용보험 0.9%, 근로소득세와 지방소득세. 연말정산 기준 추정치입니다.',
 name='실수령액 계산기 한국',
 ui=dict(gross='월 급여(세전, KRW)', period='기간', per_m='월', per_y='연'),
 labels=dict(gross='월 급여(세전)', nps='국민연금(4.75%)', health='건강보험(3.595%)', ltc='장기요양보험', ei='고용보험(0.9%)', tax='근로소득세', local='지방소득세(10%)', net='월 실수령액', netYear='연 실수령액', eff='총 공제 비율'),
 body='''<h2>한국 월급 실수령액 계산 방법 (2026)</h2>
<p>세전 월급에서 국민연금 4.75%(기준소득월액 상한 659만 원), 건강보험 3.595%, 장기요양보험(건강보험료의 13.14%), 고용보험 0.9%가 공제됩니다.</p>
<p>근로소득세는 근로소득공제, 기본공제 150만 원, 4대보험료 공제를 뺀 과세표준에 6%~45% 누진세율을 적용하고 근로소득세액공제와 표준세액공제 13만 원을 뺍니다. 지방소득세는 소득세의 10%입니다.</p>
<h3>예시</h3>
<p>월 급여 250만 원: 국민연금 118,750원, 건강보험 89,875원, 장기요양 11,810원, 고용보험 22,500원, 소득세 약 30,987원, 지방소득세 약 3,099원. 실수령액은 약 2,222,979원입니다.</p>
<p><em>이 계산기는 연말정산 후 확정세액 기준이며, 매월 원천징수되는 간이세액표 금액과는 다를 수 있습니다. 부양가족 공제, 비과세 수당, 각종 세액공제는 포함되지 않습니다.</em></p>''',
 faq=[
  ('국민연금 보험료율은 얼마인가요?','2026년 총 9.5%이며 근로자 부담은 4.75%입니다. 상한 기준소득월액은 2026년 7월부터 659만 원입니다.'),
  ('건강보험료율과 장기요양보험은?','건강보험료율은 7.19%로 근로자 부담 3.595%이고, 장기요양보험료는 건강보험료의 13.14%입니다.'),
  ('왜 급여명세서와 금액이 다른가요?','매월 원천징수는 간이세액표를 사용하고 연말정산에서 정산되므로, 이 계산기의 연간 확정 기준과 차이가 날 수 있습니다.'),
 ],
 sources=[
  ('https://calculkorea.com/salary-table','CalculKorea — 연봉 실수령액 표'),
  ('https://moneyroan.com/national-pension-upper-limit-2026/','MoneyRoan — 2026 국민연금 상한액'),
  ('https://www.khanews.com/news/articleView.html?idxno=238627','경향신문 — 2026년 건강보험료율과 장기요양보험료율'),
 ],
 src_intro='이 계산기의 요율과 금액은 아래 자료를 기준으로 하며 2026년에 해당합니다.',
 src_note='결과는 계획용 추정치이며 세무 상담이 아닙니다.',
 ad_lbl='광고', faq_h='자주 묻는 질문', src_h='출처 및 계산 방법',
)

EXTRA['zh'] = dict(
 country='CN', opts=[], defgross=20000,
 title='税后工资计算器 2026 — 中国个税与五险一金',
 h1='税后工资计算器(中国)',
 desc='计算2026年中国税后工资:养老保险8%、医疗保险2%、失业保险0.5%、公积金7%(以上海为例)和个人所得税3%至45%累进税率,起征点每月5000元。',
 name='税后工资计算器(中国)',
 ui=dict(gross='税前月薪(CNY)', period='周期', per_m='每月', per_y='每年'),
 labels=dict(gross='税前月薪', si='社会保险(养老8%+医疗2%+失业0.5%)', hf='住房公积金(7%)', tax='个人所得税', net='税后月薪', netYear='税后年收入', eff='扣除合计占比'),
 body='''<h2>中国税后工资如何计算(2026年)</h2>
<p>员工个人缴纳养老保险8%、医疗保险2%、失业保险0.5%,合计10.5%。本计算器采用上海2026年7月起的缴费基数(下限7546元、上限37731元),住房公积金按7%计算(基数2740至37731元)。</p>
<p>个人所得税按年累计:应纳税所得额为年收入减去社保、公积金和每年6万元(每月5000元)基本减除费用,再适用3%至45%的七级超额累进税率。</p>
<h3>示例</h3>
<p>税前月薪20000元:社保2100元,公积金1400元,个税940元。税后月薪15560元。</p>
<p><em>不含专项附加扣除(子女教育、住房贷款利息、租房等)、年终奖及企业年金。其他城市的缴费基数和公积金比例不同,请以工资条为准。</em></p>''',
 faq=[
  ('个税起征点是多少?','每年6万元,即每月5000元的基本减除费用。'),
  ('员工要缴纳哪些社保?','养老保险8%、医疗保险2%、失业保险0.5%,合计10.5%,另有住房公积金。'),
  ('为什么与实际工资条不同?','城市不同缴费基数和公积金比例不同,专项附加扣除和年终奖计税方式也会改变结果。'),
 ],
 sources=[
  ('https://taxsummaries.pwc.com/peoples-republic-of-china/individual/taxes-on-personal-income','PwC — 中国个人所得税税率和扣除'),
  ('https://rsj.sh.gov.cn/tgsgg_17341/20260818/t0035_1443203.html','上海市人社局 — 2026年7月起社保缴费基数'),
  ('https://sh.bendibao.com/zffw/2026818/308501.shtm','上海本地宝 — 2026年公积金缴存基数'),
 ],
 src_intro='本计算器使用的税率和金额来自以下资料,适用于2026年。',
 src_note='结果仅为规划用的估算,不构成税务建议。',
 ad_lbl='广告', faq_h='常见问题', src_h='资料来源与方法',
)

EXTRA['hi'] = dict(
 country='IN', opts=[], defgross=1500000, defper='12',
 title='सैलरी कैलकुलेटर 2026 — भारत में इन-हैंड सैलरी',
 h1='भारत सैलरी कैलकुलेटर (इन-हैंड)',
 desc='भारत में 2026-27 की इन-हैंड सैलरी निकालें: नई कर व्यवस्था के स्लैब, ₹75,000 स्टैंडर्ड डिडक्शन, ₹12 लाख तक रिबेट, 4% सेस और कर्मचारी PF।',
 name='भारत सैलरी कैलकुलेटर',
 ui=dict(gross='सकल वेतन (INR)', period='अवधि', per_m='मासिक', per_y='वार्षिक'),
 labels=dict(gross='मासिक सकल वेतन', tax='आयकर (सेस सहित)', pf='कर्मचारी PF (12%)', net='मासिक इन-हैंड वेतन', netYear='वार्षिक इन-हैंड वेतन', eff='कुल कटौती'),
 body='''<h2>भारत में इन-हैंड सैलरी कैसे निकलती है (वित्त वर्ष 2026-27)</h2>
<p>नई कर व्यवस्था में वेतनभोगी को ₹75,000 की स्टैंडर्ड डिडक्शन मिलती है। स्लैब: ₹4 लाख तक शून्य, ₹4–8 लाख पर 5%, ₹8–12 लाख पर 10%, ₹12–16 लाख पर 15%, ₹16–20 लाख पर 20%, ₹20–24 लाख पर 25% और ₹24 लाख से ऊपर 30%।</p>
<p>कर योग्य आय ₹12 लाख तक होने पर धारा 87A की छूट से कर शून्य रहता है, और उससे थोड़ा ऊपर मार्जिनल रिलीफ मिलता है। कर पर 4% हेल्थ एंड एजुकेशन सेस लगता है। कैलकुलेटर मूल वेतन को सकल का 50% मानकर PF 12% लेता है, जिसकी सीमा ₹15,000 मूल वेतन (₹1,800 प्रति माह) है।</p>
<h3>उदाहरण</h3>
<p>₹15,00,000 वार्षिक सकल वेतन: कर योग्य आय ₹14,25,000, कर ₹93,750 + सेस ₹3,750 = ₹97,500। PF ₹21,600 के बाद इन-हैंड लगभग ₹13,80,900 प्रति वर्ष।</p>
<p><em>सरचार्ज, प्रोफेशनल टैक्स, बोनस, HRA और अन्य कटौतियाँ शामिल नहीं हैं। वेतन पर्ची ही अंतिम है।</em></p>''',
 faq=[
  ('₹12 लाख तक कर क्यों नहीं लगता?','नई व्यवस्था में ₹12 लाख तक की कर योग्य आय पर धारा 87A की छूट मिलती है। ₹75,000 स्टैंडर्ड डिडक्शन के साथ ₹12.75 लाख तक का वेतन कर-मुक्त रहता है।'),
  ('स्टैंडर्ड डिडक्शन कितना है?','नई कर व्यवस्था में वेतनभोगियों के लिए ₹75,000।'),
  ('PF कितना कटता है?','मूल वेतन का 12%। सामान्य मामले में मूल वेतन ₹15,000 प्रति माह की सीमा तक, यानी अधिकतम ₹1,800 प्रति माह।'),
 ],
 sources=[
  ('https://cleartax.in/s/income-tax-slabs','ClearTax — आयकर स्लैब'),
  ('https://incometaxreturnindia.com/new-tax-regime-2026-27-income-tax-act-2025/','Income Tax Return India — नई कर व्यवस्था 2026-27'),
  ('https://cleartax.in/s/salary-calculator','ClearTax — सैलरी कैलकुलेटर'),
 ],
 src_intro='इस कैलकुलेटर की दरें और राशियाँ नीचे दिए स्रोतों से ली गई हैं और वित्त वर्ष 2026-27 पर लागू होती हैं।',
 src_note='परिणाम योजना के लिए अनुमान हैं, कर सलाह नहीं।',
 ad_lbl='विज्ञापन', faq_h='अक्सर पूछे जाने वाले प्रश्न', src_h='स्रोत और पद्धति',
)

EXTRA['id'] = dict(
 country='ID', opts=[], defgross=15000000,
 title='Kalkulator Gaji Bersih 2026 — PPh 21 dan BPJS Indonesia',
 h1='Kalkulator gaji bersih Indonesia',
 desc='Hitung gaji bersih di Indonesia 2026: PPh 21 (PTKP TK/0, tarif 5%–35%), biaya jabatan, JHT 2%, JP 1% dan BPJS Kesehatan 1%.',
 name='Kalkulator gaji bersih Indonesia',
 ui=dict(gross='Gaji bruto (IDR)', period='Periode', per_m='Per bulan', per_y='Per tahun'),
 labels=dict(gross='Gaji bruto per bulan', pph='PPh 21 (rata-rata bulanan)', jht='BPJS JHT (2%)', jp='BPJS Jaminan Pensiun (1%)', kes='BPJS Kesehatan (1%)', net='Gaji bersih per bulan', netYear='Gaji bersih per tahun', eff='Total potongan'),
 body='''<h2>Cara menghitung gaji bersih di Indonesia (2026)</h2>
<p>Dari gaji bruto dipotong iuran karyawan: JHT 2%, Jaminan Pensiun 1% (batas upah Rp 11.086.300) dan BPJS Kesehatan 1% (batas upah Rp 12.000.000).</p>
<p>PPh 21 dihitung dengan metode tahunan untuk karyawan tetap TK/0: penghasilan bruto setahun dikurangi biaya jabatan 5% (maksimal Rp 500.000 per bulan), iuran JHT dan JP, serta PTKP Rp 54.000.000. Sisanya (PKP) dikenai tarif 5% sampai Rp 60 juta, 15% sampai Rp 250 juta, 25% sampai Rp 500 juta, 30% sampai Rp 5 miliar dan 35% di atasnya. Hasilnya dibagi 12 sebagai rata-rata bulanan.</p>
<h3>Contoh</h3>
<p>Gaji bruto Rp 15.000.000 per bulan: PPh 21 sekitar Rp 938.363, JHT Rp 300.000, JP Rp 110.863, BPJS Kesehatan Rp 120.000. Gaji bersih sekitar Rp 13.530.775.</p>
<p><em>Tarif efektif bulanan (TER) dan pemotongan Desember dapat mengubah nominal tiap bulan, tetapi total setahun sama. Tunjangan, bonus, premi JKK/JKM dan status kawin/tanggungan tidak dihitung.</em></p>''',
 faq=[
  ('Berapa PTKP untuk TK/0 tahun 2026?','Rp 54.000.000 per tahun untuk wajib pajak lajang tanpa tanggungan.'),
  ('Apa itu biaya jabatan?','Pengurang 5% dari penghasilan bruto, maksimal Rp 500.000 per bulan (Rp 6.000.000 per tahun).'),
  ('Mengapa potongan PPh 21 tiap bulan berbeda dari hasil ini?','Pemotongan Januari–November memakai tarif efektif rata-rata (TER) dan Desember menyesuaikan sehingga total setahun sesuai perhitungan tahunan. Kalkulator ini menampilkan rata-ratanya.'),
 ],
 sources=[
  ('https://kalkulin.id/pajak-gaji/kalkulator-gaji-bersih','Kalkulin — kalkulator gaji bersih'),
  ('https://www.krishandsoftware.com/blog/2046/perhitungan-pph-21-desember/','Krishand — perhitungan PPh 21 Desember'),
  ('https://jateng.antaranews.com/berita/625410/bpjs-ketenagakerjaan-sosialisasikan-batasan-upah-jaminan-pensiun','ANTARA — batas upah Jaminan Pensiun'),
 ],
 src_intro='Tarif dan angka kalkulator ini berasal dari sumber di bawah dan berlaku untuk 2026.',
 src_note='Hasil hanyalah estimasi untuk perencanaan, bukan nasihat pajak.',
 ad_lbl='Iklan', faq_h='Pertanyaan yang sering diajukan', src_h='Sumber dan metodologi',
)

EXTRA['vi'] = dict(
 country='VN', opts=[], defgross=20000000,
 title='Tính lương Gross sang Net 2026 — Việt Nam',
 h1='Tính lương Gross sang Net Việt Nam',
 desc='Tính lương Net từ Gross tại Việt Nam năm 2026: bảo hiểm 10,5%, giảm trừ gia cảnh bản thân 15,5 triệu đồng và biểu thuế thu nhập cá nhân lũy tiến 5 bậc.',
 name='Tính lương Gross sang Net Việt Nam',
 ui=dict(gross='Lương Gross (VND)', period='Kỳ', per_m='Hàng tháng', per_y='Hàng năm'),
 labels=dict(gross='Lương Gross hàng tháng', si='BHXH + BHYT (9,5%)', ui='Bảo hiểm thất nghiệp (1%)', tax='Thuế thu nhập cá nhân', net='Lương Net hàng tháng', netYear='Lương Net hàng năm', eff='Tổng khoản khấu trừ'),
 body='''<h2>Cách tính lương Net tại Việt Nam (2026)</h2>
<p>Người lao động đóng bảo hiểm xã hội 8% và bảo hiểm y tế 1,5% trên mức lương tối đa 46,8 triệu đồng, cùng bảo hiểm thất nghiệp 1% trên mức tối đa 106,2 triệu đồng.</p>
<p>Thu nhập tính thuế bằng lương Gross trừ bảo hiểm và giảm trừ gia cảnh bản thân 15,5 triệu đồng mỗi tháng. Biểu thuế lũy tiến từng phần gồm 5 bậc: 5% đến 10 triệu, 10% đến 30 triệu, 20% đến 60 triệu, 30% đến 100 triệu và 35% trên 100 triệu đồng.</p>
<h3>Ví dụ</h3>
<p>Lương Gross 20.000.000 đồng, không người phụ thuộc: bảo hiểm 2.100.000 đồng, thuế TNCN 120.000 đồng. Lương Net: 17.780.000 đồng.</p>
<p><em>Chưa tính giảm trừ người phụ thuộc (6,2 triệu đồng mỗi người), phụ cấp miễn thuế, thưởng hay các khoản khác. Cách áp dụng biểu thuế mới cho cả năm 2026 dựa trên các nguồn dưới đây; hãy đối chiếu bảng lương của công ty.</em></p>''',
 faq=[
  ('Mức giảm trừ gia cảnh năm 2026 là bao nhiêu?','15,5 triệu đồng mỗi tháng cho bản thân và 6,2 triệu đồng mỗi tháng cho mỗi người phụ thuộc.'),
  ('Người lao động đóng bảo hiểm bao nhiêu phần trăm?','10,5% gồm BHXH 8%, BHYT 1,5% và BHTN 1%, tính trên mức lương tối đa theo quy định.'),
  ('Biểu thuế thu nhập cá nhân gồm mấy bậc?','5 bậc: 5%, 10%, 20%, 30% và 35%, với các ngưỡng 10, 30, 60 và 100 triệu đồng mỗi tháng.'),
 ],
 sources=[
  ('https://www.ey.com/en_vn/technical/tax/tax-and-law-updates/new-personal-income-tax-law-109-2025-qh25','EY Việt Nam — Luật thuế TNCN mới 109/2025/QH15'),
  ('https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/100277/bieu-thue-tncn-luy-tien-2026-bieu-thue-5-bac','Thư viện Pháp luật — biểu thuế TNCN lũy tiến 2026'),
  ('https://www.bakermckenzie.com/en/insight/publications/2026/03/vietnam-change-to-the-regional-minimum-wage-in-2026','Baker McKenzie — lương tối thiểu vùng 2026'),
 ],
 src_intro='Thuế suất và số liệu của công cụ này lấy từ các nguồn dưới đây và áp dụng cho năm 2026.',
 src_note='Kết quả chỉ là ước tính để lập kế hoạch, không phải tư vấn thuế.',
 ad_lbl='Quảng cáo', faq_h='Câu hỏi thường gặp', src_h='Nguồn và phương pháp',
)

EXTRA['th'] = dict(
 country='TH', opts=[], defgross=30000,
 title='เครื่องคิดเงินเดือนสุทธิ 2026 — ภาษีและประกันสังคมไทย',
 h1='เครื่องคิดเงินเดือนสุทธิ ประเทศไทย',
 desc='คำนวณเงินเดือนสุทธิในไทยปี 2026: ประกันสังคม 5% (เพดาน 17,500 บาท) ภาษีเงินได้บุคคลธรรมดาอัตราก้าวหน้า 0–35% หักค่าใช้จ่าย 50% และลดหย่อนส่วนตัว 60,000 บาท',
 name='เครื่องคิดเงินเดือนสุทธิ ประเทศไทย',
 ui=dict(gross='เงินเดือนก่อนหัก (THB)', period='ช่วงเวลา', per_m='ต่อเดือน', per_y='ต่อปี'),
 labels=dict(gross='เงินเดือนก่อนหักต่อเดือน', ss='ประกันสังคม (5%, สูงสุด 875 บาท)', tax='ภาษีเงินได้บุคคลธรรมดา', net='เงินเดือนสุทธิต่อเดือน', netYear='เงินได้สุทธิต่อปี', eff='รวมรายการหัก'),
 body='''<h2>วิธีคำนวณเงินเดือนสุทธิในประเทศไทย (2026)</h2>
<p>ลูกจ้างจ่ายเงินสมทบประกันสังคม 5% ของค่าจ้าง โดยตั้งแต่ปี 2026 ฐานค่าจ้างสูงสุดคือ 17,500 บาทต่อเดือน จึงจ่ายสูงสุด 875 บาทต่อเดือน</p>
<p>ภาษีคำนวณจากเงินได้ทั้งปี หักค่าใช้จ่าย 50% (ไม่เกิน 100,000 บาท) ค่าลดหย่อนส่วนตัว 60,000 บาท และเงินสมทบประกันสังคมที่หักลดหย่อนได้ไม่เกิน 9,000 บาท แล้วใช้อัตราก้าวหน้า: 0% ถึง 150,000 บาท, 5% ถึง 300,000, 10% ถึง 500,000, 15% ถึง 750,000, 20% ถึง 1,000,000, 25% ถึง 2,000,000, 30% ถึง 5,000,000 และ 35% ส่วนที่เกิน</p>
<h3>ตัวอย่าง</h3>
<p>เงินเดือน 30,000 บาท: ประกันสังคม 875 บาท ภาษีประมาณ 171 บาทต่อเดือน เงินเดือนสุทธิประมาณ 28,954 บาท</p>
<p><em>ไม่รวมโบนัส ค่าลดหย่อนอื่น (คู่สมรส บุตร กองทุนต่าง ๆ) หรือเงินได้อื่น สลิปเงินเดือนของนายจ้างเป็นตัวเลขที่ถูกต้อง</em></p>''',
 faq=[
  ('ประกันสังคมหักเท่าไรในปี 2026?','5% ของค่าจ้าง ฐานสูงสุด 17,500 บาท จึงสูงสุด 875 บาทต่อเดือน'),
  ('อัตราภาษีเงินได้บุคคลธรรมดาคือเท่าไร?','อัตราก้าวหน้า 0% ถึง 35% โดยเงินได้สุทธิ 150,000 บาทแรกได้รับยกเว้น'),
  ('ค่าใช้จ่ายและค่าลดหย่อนพื้นฐานคือเท่าไร?','หักค่าใช้จ่าย 50% ของเงินได้ไม่เกิน 100,000 บาท และลดหย่อนส่วนตัว 60,000 บาท'),
 ],
 sources=[
  ('https://www.hlbthai.com/thailand-social-security-contribution-changes-for-2026/','HLB Thailand — การเปลี่ยนแปลงเงินสมทบประกันสังคม 2026'),
  ('https://www.rd.go.th/60061.html','กรมสรรพากร — ค่าลดหย่อนและการหักเงินสมทบประกันสังคม'),
  ('https://www.expattaxthailand.com/thailand-expat-tax-rates-allowances-and-deductions/','Expat Tax Thailand — อัตราภาษีและค่าลดหย่อน'),
 ],
 src_intro='อัตราและตัวเลขในเครื่องมือนี้มาจากแหล่งข้อมูลด้านล่างและใช้กับปี 2026',
 src_note='ผลลัพธ์เป็นค่าประมาณเพื่อการวางแผน ไม่ใช่คำปรึกษาด้านภาษี',
 ad_lbl='โฆษณา', faq_h='คำถามที่พบบ่อย', src_h='แหล่งที่มาและวิธีคำนวณ',
)

EXTRA['tl'] = dict(
 country='PH', opts=[], defgross=30000,
 title='Kalkulator ng Take-Home Pay 2026 — Sweldo sa Pilipinas',
 h1='Kalkulator ng take-home pay Pilipinas',
 desc='Kalkulahin ang take-home pay sa Pilipinas para sa 2026: SSS 5%, PhilHealth 2.5%, Pag-IBIG at income tax ayon sa TRAIN law (0% hanggang 35%).',
 name='Kalkulator ng take-home pay Pilipinas',
 ui=dict(gross='Gross na sahod (PHP)', period='Panahon', per_m='Buwanan', per_y='Taunan'),
 labels=dict(gross='Gross na sahod kada buwan', sss='SSS (5%)', ph='PhilHealth (2.5%)', pi='Pag-IBIG (2%, hanggang ₱200)', tax='Income tax (withholding)', net='Take-home pay kada buwan', netYear='Take-home pay kada taon', eff='Kabuuang bawas'),
 body='''<h2>Paano kinakalkula ang take-home pay sa Pilipinas (2026)</h2>
<p>Bahagi ng empleyado: SSS na 5% ng Monthly Salary Credit (₱5,000 hanggang ₱35,000), PhilHealth na 2.5% ng buwanang sahod (sahod na ₱10,000 hanggang ₱100,000), at Pag-IBIG na 2% na may pinakamataas na ₱200.</p>
<p>Ang income tax ay kinakalkula sa taunang taxable income matapos ibawas ang mga kontribusyon: 0% hanggang ₱250,000, 15% hanggang ₱400,000, 20% hanggang ₱800,000, 25% hanggang ₱2,000,000, 30% hanggang ₱8,000,000 at 35% sa itaas nito. Ang 13th month pay at iba pang benepisyo ay exempted hanggang ₱90,000 kada taon.</p>
<h3>Halimbawa</h3>
<p>Gross na ₱30,000 kada buwan: SSS ₱1,500, PhilHealth ₱750, Pag-IBIG ₱200, income tax ₱1,007.50. Take-home pay: ₱26,542.50.</p>
<p><em>Hindi kasama ang overtime, bonus, allowance at ibang bawas. Ang payslip ng employer ang opisyal.</em></p>''',
 faq=[
  ('Magkano ang SSS contribution ng empleyado?','5% ng Monthly Salary Credit, mula ₱5,000 hanggang ₱35,000, kaya hanggang ₱1,750 kada buwan.'),
  ('Magkano ang PhilHealth?','5% ng buwanang sahod na hinahati ng employer at empleyado, kaya 2.5% ang bahagi ng empleyado, sa sahod na ₱10,000 hanggang ₱100,000.'),
  ('Sino ang hindi nagbabayad ng income tax?','Ang taunang taxable income na hanggang ₱250,000 ay walang tax sa ilalim ng TRAIN law.'),
 ],
 sources=[
  ('https://incometaxcalculator.ph/','Income Tax Calculator PH — TRAIN tax table'),
  ('https://phsalarycalculator.com/','PH Salary Calculator — halimbawa ng kalkulasyon'),
  ('https://www.forvismazars.com/ph/en/insights/hr-payroll-alerts/pag-ibig-circular-460','Forvis Mazars — Pag-IBIG Circular 460'),
 ],
 src_intro='Ang mga rate at halaga sa kalkulator na ito ay mula sa mga sanggunian sa ibaba at para sa 2026.',
 src_note='Ang mga resulta ay pagtataya para sa pagpaplano, hindi payong pang-buwis.',
 ad_lbl='Patalastas', faq_h='Mga madalas itanong', src_h='Mga sanggunian at pamamaraan',
)

EXTRA['ms'] = dict(
 country='MY', opts=['skbbk'], defgross=5000,
 title='Kalkulator Gaji Bersih 2026 — EPF, PERKESO dan PCB Malaysia',
 h1='Kalkulator gaji bersih Malaysia',
 desc='Kira gaji bersih di Malaysia untuk 2026: KWSP 11%, PERKESO 0.5%, SIP 0.2% dan cukai pendapatan (PCB) mengikut kadar berperingkat, dengan pelepasan cukai individu.',
 name='Kalkulator gaji bersih Malaysia',
 ui=dict(gross='Gaji kasar (MYR)', period='Tempoh', per_m='Bulanan', per_y='Tahunan', opt_skbbk='Sertakan caruman SKBBK / Lindung 24 Jam (0.75%, pilihan)'),
 labels=dict(gross='Gaji kasar sebulan', epf='KWSP / EPF (11%)', socso='PERKESO / SOCSO (0.5%)', eis='SIP / EIS (0.2%)', skbbk='SKBBK (0.75%)', pcb='Cukai pendapatan (PCB)', net='Gaji bersih sebulan', netYear='Gaji bersih setahun', eff='Jumlah potongan'),
 body='''<h2>Cara mengira gaji bersih di Malaysia (2026)</h2>
<p>Pekerja warganegara di bawah 60 tahun mencarum KWSP 11%, PERKESO 0.5% dan SIP 0.2%. Caruman PERKESO dan SIP dikira berdasarkan jadual upah bertingkat RM100 dengan had upah RM6,000.</p>
<p>Cukai pendapatan (PCB) dikira secara tahunan: pendapatan bercukai ialah gaji setahun tolak pelepasan individu RM9,000, KWSP (sehingga RM4,000) dan PERKESO/SIP (sehingga RM350). Kadar berperingkat bermula 0% sehingga RM5,000 dan meningkat kepada 30% melebihi RM2 juta. Rebat RM400 diberi jika pendapatan bercukai tidak melebihi RM35,000.</p>
<h3>Contoh</h3>
<p>Gaji kasar RM5,000: KWSP RM550, PERKESO RM24.75, SIP RM9.90, PCB RM108.25. Gaji bersih: RM4,307.10.</p>
<p><em>Caruman SKBBK adalah pilihan bagi pekerja tempatan sejak 8 Julai 2026. Pelepasan lain (pasangan, anak, insurans) dan bonus tidak dikira. Slip gaji majikan ialah dokumen rasmi.</em></p>''',
 faq=[
  ('Berapakah kadar KWSP pekerja?','11% daripada gaji bagi pekerja warganegara; majikan mencarum 12% atau 13% bergantung pada gaji.'),
  ('Apakah pelepasan cukai asas?','RM9,000 untuk individu, KWSP sehingga RM4,000 dan PERKESO/SIP sehingga RM350 setahun.'),
  ('Adakah SKBBK wajib?','Bagi pekerja tempatan ia menjadi sukarela mulai 8 Julai 2026. Anda boleh menandakan pilihan di atas untuk melihat kesannya.'),
 ],
 sources=[
  ('https://www.pwc.com/my/en/publications/mtb/personal-income-tax.html','PwC Malaysia — cukai pendapatan individu'),
  ('https://www.ajobthing.com/resources/blog/epf-socso-eis-contribution-2026-latest-rates-rules-employer-guide-malaysia','AJobThing — kadar EPF, SOCSO dan EIS 2026'),
  ('https://recruitgo.com/malaysia/salary-calculator/','RecruitGo — contoh pengiraan gaji'),
 ],
 src_intro='Kadar dan jumlah dalam kalkulator ini datang daripada sumber di bawah dan terpakai untuk 2026.',
 src_note='Keputusan hanyalah anggaran untuk perancangan, bukan nasihat cukai. Jadual PERKESO dan SIP dianggarkan daripada kadar dan jalur upah.',
 ad_lbl='Iklan', faq_h='Soalan lazim', src_h='Sumber dan kaedah',
)

EXTRA['af'] = dict(
 country='ZA', opts=[], defgross=20000,
 title='Salarisberekenaar 2026 — Netto salaris in Suid-Afrika',
 h1='Salarisberekenaar Suid-Afrika',
 desc='Bereken jou netto salaris in Suid-Afrika vir 2026/27: PAYE-skale (18% tot 45%), primêre korting van R17 820 en UIF van 1%.',
 name='Salarisberekenaar Suid-Afrika',
 ui=dict(gross='Bruto salaris (ZAR)', period='Tydperk', per_m='Per maand', per_y='Per jaar'),
 labels=dict(gross='Bruto salaris per maand', paye='PAYE (inkomstebelasting)', uif='UIF (1%)', net='Netto salaris per maand', netYear='Netto salaris per jaar', eff='Totale aftrekkings'),
 body='''<h2>Hoe netto salaris in Suid-Afrika bereken word (2026/27)</h2>
<p>Vir die belastingjaar 1 Maart 2026 tot 28 Februarie 2027 is die skale: 18% tot R245 100, 26% tot R383 100, 31% tot R530 200, 36% tot R695 800, 39% tot R887 000, 41% tot R1 878 600 en 45% daarbo. Die primêre korting van R17 820 word van die belasting afgetrek, sodat niks betaal word onder R99 000 per jaar nie.</p>
<p>UIF is 1% van jou salaris, met ’n maandelikse plafon van R17 712, dus hoogstens R177,12 per maand.</p>
<h3>Voorbeeld</h3>
<p>Bruto salaris van R20 000 per maand: PAYE R2 115 en UIF R177,12. Netto salaris: R17 707,88.</p>
<p><em>Mediese krediete, aftreefondsbydraes, ouderdomskortings en ander aftrekkings is nie ingesluit nie. Jou salarisstrokie is die geldige dokument.</em></p>''',
 faq=[
  ('Wat is die belastingdrempel in 2026/27?','R99 000 per jaar vir persone onder 65, weens die primêre korting van R17 820.'),
  ('Hoeveel is UIF?','1% van jou salaris tot ’n maandelikse plafon van R17 712, dus maksimum R177,12 per maand.'),
  ('Waarom verskil my salarisstrokie?','Mediese fondskrediete, pensioenbydraes, bonusse en ouderdomskortings verander die uitkoms.'),
 ],
 sources=[
  ('https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/','SARS — Begroting 2026 gereelde vrae'),
  ('https://www.sars.gov.za/types-of-tax/unemployment-insurance-fund/','SARS — Werkloosheidsversekeringsfonds (UIF)'),
  ('https://www.govchain.co.za/blog/how-to-calculate-paye-in-south-africa','GovChain — hoe om PAYE te bereken'),
 ],
 src_intro='Die skale en bedrae in hierdie berekenaar kom uit die bronne hieronder en geld vir 2026/27.',
 src_note='Resultate is skattings vir beplanning en nie belastingadvies nie.',
 ad_lbl='Advertensie', faq_h='Gereelde vrae', src_h='Bronne en metode',
)

EXTRA['sw'] = dict(
 country='KE', opts=[], defgross=100000,
 title='Kikokotoo cha Mshahara 2026 — Mshahara Halisi Kenya',
 h1='Kikokotoo cha mshahara halisi Kenya',
 desc='Kokotoa mshahara halisi nchini Kenya kwa 2026: PAYE (10% hadi 35%), NSSF, SHIF 2.75%, Ushuru wa Nyumba za Gharama Nafuu 1.5% na msamaha wa kibinafsi wa KES 2,400.',
 name='Kikokotoo cha mshahara halisi Kenya',
 ui=dict(gross='Mshahara ghafi (KES)', period='Kipindi', per_m='Kwa mwezi', per_y='Kwa mwaka'),
 labels=dict(gross='Mshahara ghafi kwa mwezi', nssf='NSSF (6%)', shif='SHIF (2.75%)', ahl='Ushuru wa Nyumba (1.5%)', paye='PAYE (baada ya msamaha wa KES 2,400)', net='Mshahara halisi kwa mwezi', netYear='Mshahara halisi kwa mwaka', eff='Jumla ya makato'),
 body='''<h2>Jinsi mshahara halisi unavyokokotolewa Kenya (2026)</h2>
<p>Mfanyakazi huchangia NSSF kwa 6% ya mshahara (Kiwango cha Chini KES 9,000 na Kiwango cha Juu KES 108,000), SHIF kwa 2.75% ya mshahara ghafi (kima cha chini KES 300) na Ushuru wa Nyumba za Gharama Nafuu kwa 1.5%.</p>
<p>Michango hii inaondolewa kabla ya kukokotoa PAYE. Viwango vya kila mwezi: 10% kwa KES 24,000 za kwanza, 25% hadi KES 32,333, 30% hadi KES 500,000, 32.5% hadi KES 800,000 na 35% juu ya hapo. Msamaha wa kibinafsi wa KES 2,400 hupunguza kodi.</p>
<h3>Mfano</h3>
<p>Mshahara ghafi wa KES 100,000: NSSF 6,000, SHIF 2,750, Ushuru wa Nyumba 1,500 na PAYE 19,308.35. Mshahara halisi: KES 70,441.65.</p>
<p><em>Bima, posho, bonasi na michango ya hiari haijajumuishwa. Hati ya mshahara ya mwajiri ndiyo rasmi.</em></p>''',
 faq=[
  ('SHIF ni asilimia ngapi?','2.75% ya mshahara ghafi, kwa kima cha chini cha KES 300 kwa mwezi.'),
  ('NSSF ni kiasi gani mwaka 2026?','6% ya mshahara hadi kikomo cha juu cha KES 108,000, kwa hiyo hadi KES 6,480 kwa mwezi.'),
  ('Michango inaondolewa kabla ya kodi?','Ndiyo, SHIF, Ushuru wa Nyumba na NSSF hupunguza mapato yanayotozwa PAYE, kulingana na taarifa ya KRA na vyanzo vya malipo.'),
 ],
 sources=[
  ('https://www.kra.go.ke/news-center/public-notices/2157-amendments-to-paye-computation-pursuant-to-the-tax-laws-amendment-act,-2024','KRA — mabadiliko ya ukokotoaji wa PAYE'),
  ('https://www.payspace.com/blog/kenya-nssf-rates-update-2026','PaySpace — viwango vya NSSF 2026'),
  ('https://www.payecalculator.co.ke/blog/take-home-pay-on-a-kes-100000-salary-in-kenya','PAYE Calculator Kenya — mshahara wa KES 100,000'),
 ],
 src_intro='Viwango na kiasi katika kikokotoo hiki vinatoka kwenye vyanzo vilivyo hapa chini na vinatumika kwa 2026.',
 src_note='Matokeo ni makadirio ya kupanga, si ushauri wa kodi.',
 ad_lbl='Tangazo', faq_h='Maswali yanayoulizwa mara nyingi', src_h='Vyanzo na mbinu',
)

EXTRA['sv'] = dict(
 country='SE', opts=[], defgross=38800,
 title='Nettolönekalkylator 2026 — lön efter skatt i Sverige',
 h1='Lön efter skatt Sverige',
 desc='Räkna ut lön efter skatt i Sverige 2026: kommunalskatt (snitt 32,38 %), grundavdrag, jobbskatteavdrag och statlig skatt 20 % över 643 000 kr.',
 name='Lön efter skatt Sverige',
 ui=dict(gross='Bruttolön (SEK)', period='Period', per_m='Per månad', per_y='Per år'),
 labels=dict(gross='Bruttolön per månad', kom='Kommunal- och regionskatt (snitt 32,38 %)', stat='Statlig inkomstskatt (20 %)', jsa='Jobbskatteavdrag (minskar skatten)', net='Nettolön per månad', netYear='Nettolön per år', eff='Total skatt'),
 body='''<h2>Så räknas lönen efter skatt i Sverige (2026)</h2>
<p>Skatten beräknas på årsinkomsten efter grundavdrag. Kommunal- och regionskatten är i genomsnitt 32,38 %. Statlig inkomstskatt på 20 % tillkommer på beskattningsbar inkomst över 643 000 kr. Kyrkoavgift och begravningsavgift ingår inte.</p>
<p>Jobbskatteavdraget minskar skatten för dem som arbetar och beräknas utifrån prisbasbeloppet 59 200 kr. Allmän pensionsavgift på 7 % kvittas mot en skattereduktion och påverkar därför inte nettolönen.</p>
<h3>Exempel</h3>
<p>Med 38 800 kr i månadslön: kommunalskatt ca 12 091 kr och jobbskatteavdrag ca 4 278 kr per månad. Nettolön: ca 30 987 kr.</p>
<p><em>Din kommuns skattesats avgör det verkliga resultatet. Skattetabellen som arbetsgivaren använder kan ge något annorlunda belopp.</em></p>''',
 faq=[
  ('När betalar man statlig skatt 2026?','20 % statlig inkomstskatt betalas på den del av den beskattningsbara inkomsten som överstiger 643 000 kr per år.'),
  ('Vad är jobbskatteavdraget?','En skattereduktion för förvärvsinkomst som minskar skatten på arbete. Den beräknas med prisbasbeloppet, som är 59 200 kr 2026.'),
  ('Varför skiljer sig min lönespecifikation?','Kommunalskatten varierar mellan kommuner, och kyrkoavgift, förmåner och tabellen som arbetsgivaren använder påverkar beloppet.'),
 ],
 sources=[
  ('https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html','Skatteverket — belopp och procent 2026'),
  ('https://www.ekonomifakta.se/sakomraden/skatt/din-skatt-ar-2026_1246309.html','Ekonomifakta — din skatt 2026'),
 ],
 src_intro='Satserna och beloppen i kalkylatorn kommer från källorna nedan och gäller 2026.',
 src_note='Resultaten är uppskattningar för planering och inte skatterådgivning.',
 ad_lbl='Annons', faq_h='Vanliga frågor', src_h='Källor och metod',
)

EXTRA['fi'] = dict(
 country='FI', opts=[], defgross=3500,
 title='Nettopalkkalaskuri 2026 — palkka verojen jälkeen Suomessa',
 h1='Nettopalkkalaskuri Suomi',
 desc='Laske nettopalkka Suomessa vuonna 2026: valtion tuloveroasteikko, kunnallisvero, sairaanhoitomaksu, TyEL 7,30 %, työttömyysvakuutus, Yle-vero ja työtulovähennys.',
 name='Nettopalkkalaskuri Suomi',
 ui=dict(gross='Bruttopalkka (EUR)', period='Jakso', per_m='Kuukaudessa', per_y='Vuodessa'),
 labels=dict(gross='Bruttopalkka kuukaudessa', soc='TyEL, työttömyys- ja päivärahamaksu', tax='Tulovero (valtio, kunta, sairaanhoito) työtulovähennyksen jälkeen', yle='Yle-vero', net='Nettopalkka kuukaudessa', netYear='Nettopalkka vuodessa', eff='Vähennykset yhteensä'),
 body='''<h2>Näin nettopalkka lasketaan Suomessa (2026)</h2>
<p>Palkansaaja maksaa TyEL-maksun 7,30 %, työttömyysvakuutusmaksun 0,89 % ja päivärahamaksun 0,88 %. Verotettavasta ansiotulosta vähennetään tulonhankkimisvähennys 750 euroa.</p>
<p>Valtion tulovero noudattaa asteikkoa 12,64 % (22 000 euroon asti), 19 %, 30,25 %, 33,25 % ja 37,5 % yli 52 100 euron. Kunnallisvero on keskimäärin 7,57 % ja sairaanhoitomaksu 1,10 %. Lisäksi peritään Yle-vero enintään 160 euroa. Työtulovähennys (enintään 3 430 euroa) pienentää veroa. Kirkollisveroa ei ole mukana.</p>
<h3>Esimerkki</h3>
<p>Kuukausipalkka 3 500 euroa: sosiaalimaksut 317,45 euroa, tulovero 510,33 euroa ja Yle-vero 13,33 euroa. Nettopalkka: 2 658,88 euroa.</p>
<p><em>Kotikuntasi veroprosentti ja mahdollinen kirkollisvero muuttavat tulosta. Lomarahat, edut ja muut vähennykset eivät ole mukana. Palkkalaskelma on ratkaiseva.</em></p>''',
 faq=[
  ('Kuinka suuri TyEL-maksu on vuonna 2026?','Palkansaajan TyEL-maksu on 7,30 % palkasta iästä riippumatta.'),
  ('Mikä on työtulovähennys?','Verovähennys, joka pienentää ansiotulon veroa. Se on enintään 3 430 euroa ja pienenee suuremmilla tuloilla.'),
  ('Miksi palkkalaskelmani poikkeaa?','Kunnan veroprosentti, kirkollisvero, verokortti ja lomarahat vaikuttavat lopputulokseen.'),
 ],
 sources=[
  ('https://www.veronmaksajat.fi/tutkimus-ja-tilastot/tuloverot/palkansaajan-veroprosentit/palkansaajan-tuloverolaskuri-2026/','Veronmaksajat — palkansaajan tuloverolaskuri 2026'),
  ('https://www.veronmaksajat.fi/neuvot/henkiloverotus/tyo-elake-ja-etuudet/ansiotulojen-verot-ja-maksut/valtion-tulovero/','Veronmaksajat — valtion tulovero'),
  ('https://www.elo.fi/fi-fi/tyonantaja/tyel-vakuuttaminen/tyel-maksu/sosiaalivakuutusmaksut-2026','Elo — sosiaalivakuutusmaksut 2026'),
 ],
 src_intro='Laskurin prosentit ja summat perustuvat alla oleviin lähteisiin ja koskevat vuotta 2026.',
 src_note='Tulokset ovat suunnittelua varten tehtyjä arvioita, eivät veroneuvontaa.',
 ad_lbl='Mainos', faq_h='Usein kysytyt kysymykset', src_h='Lähteet ja menetelmä',
)

EXTRA['sl'] = dict(
 country='SI', opts=[], defgross=2000,
 title='Kalkulator neto plače 2026 — bruto v neto Slovenija',
 h1='Kalkulator neto plače Slovenija',
 desc='Izračunajte neto plačo v Sloveniji za 2026: prispevki delojemalca 23,1 % (z dolgotrajno oskrbo), splošna olajšava in dohodninska lestvica 16 % do 50 %.',
 name='Kalkulator neto plače Slovenija',
 ui=dict(gross='Bruto plača (EUR)', period='Obdobje', per_m='Mesečno', per_y='Letno'),
 labels=dict(gross='Bruto plača na mesec', soc='Prispevki delojemalca (23,1 %)', tax='Akontacija dohodnine', net='Neto plača na mesec', netYear='Neto letno', eff='Skupni odtegljaji'),
 body='''<h2>Kako se izračuna neto plača v Sloveniji (2026)</h2>
<p>Iz bruto plače delojemalec plača prispevke v višini 22,10 % (pokojninsko 15,50 %, zdravstveno 6,36 %, brezposelnost 0,14 %, starševsko varstvo 0,10 %) ter od 1. julija 2025 še 1 % za dolgotrajno oskrbo, skupaj 23,10 %.</p>
<p>Davčna osnova je bruto plača brez prispevkov in splošne olajšave 462,66 EUR na mesec. Dohodnina se obračuna po lestvici: 16 % do 810,12 EUR, 26 % do 2.382,70 EUR, 33 % do 4.765,41 EUR, 39 % do 6.862,19 EUR in 50 % nad tem (mesečni zneski).</p>
<h3>Primer</h3>
<p>Bruto plača 2.000 EUR: prispevki 462,00 EUR, dohodnina 198,58 EUR. Neto plača: 1.339,42 EUR.</p>
<p><em>Regres, prehrana, prevoz, otroci in druge olajšave niso vključeni, zato se lahko rezultat razlikuje od obračuna delodajalca.</em></p>''',
 faq=[
  ('Kolikšni so prispevki delojemalca v letu 2026?','22,10 % in 1 % za dolgotrajno oskrbo, skupaj 23,10 % bruto plače.'),
  ('Kolikšna je splošna olajšava?','5.551,93 EUR na leto ali 462,66 EUR na mesec.'),
  ('Zakaj se moja neto plača razlikuje?','Na neto vplivajo dodatne olajšave (otroci, vzdrževani družinski člani), dodatki in dejanski davčni status.'),
 ],
 sources=[
  ('https://www.zvezarfr.si/pripomocki/uporabni-podatki/a-lestvica-za-odmero-dohodnine','Zveza RFR — lestvica za odmero dohodnine'),
  ('https://www.minimax.si/sl-si/od-1-julija-2025-obvezno-placevanje-prispevka-za-dolgotrajno-oskrbo','Minimax — prispevek za dolgotrajno oskrbo'),
  ('https://kalkulo.eu/sl/izracun-place/','Kalkulo — izračun plače'),
 ],
 src_intro='Stopnje in zneski v kalkulatorju izvirajo iz spodnjih virov in veljajo za leto 2026.',
 src_note='Rezultati so ocene za načrtovanje in ne davčno svetovanje.',
 ad_lbl='Oglas', faq_h='Pogosta vprašanja', src_h='Viri in metodologija',
)

EXTRA['he'] = dict(
 country='IL', opts=[], defgross=20000,
 title='מחשבון שכר נטו 2026 — ברוטו לנטו בישראל',
 h1='מחשבון שכר נטו בישראל',
 desc='חשבו את שכר הנטו בישראל לשנת 2026: מדרגות מס הכנסה 10%–50%, נקודות זיכוי, ביטוח לאומי ומס בריאות לפי המדרגות המעודכנות.',
 name='מחשבון שכר נטו בישראל',
 ui=dict(gross='שכר ברוטו (ILS)', period='תקופה', per_m='חודשי', per_y='שנתי'),
 labels=dict(gross='שכר ברוטו חודשי', tax='מס הכנסה (אחרי נקודות זיכוי)', ni='ביטוח לאומי', health='מס בריאות', net='שכר נטו חודשי', netYear='שכר נטו שנתי', eff='סך הניכויים'),
 body='''<h2>איך מחשבים שכר נטו בישראל (2026)</h2>
<p>מס ההכנסה חודשי לפי מדרגות: 10% עד 7,010 ₪, 14% עד 10,060 ₪, 20% עד 19,000 ₪, 31% עד 25,100 ₪, 35% עד 46,690 ₪, 47% עד 60,130 ₪ ו־50% מעל. מהמס מופחתים נקודות זיכוי: המחשבון מניח 2.25 נקודות (תושב) בשווי 242 ₪ לנקודה.</p>
<p>ביטוח לאומי: 1.04% עד 7,703 ₪ ו־7% עד תקרה של 51,910 ₪. מס בריאות: 3.23% עד 7,703 ₪ ו־5.17% עד התקרה.</p>
<h3>דוגמה</h3>
<p>שכר ברוטו 20,000 ₪: מס הכנסה 2,681.50 ₪, ביטוח לאומי 940.90 ₪, מס בריאות 884.56 ₪. שכר נטו: 15,493.04 ₪.</p>
<p><em>ללא הפרשות לפנסיה וקרן השתלמות, נקודות זיכוי נוספות (ילדים, אשה) והטבות אחרות. תלוש השכר של המעסיק הוא המסמך המחייב.</em></p>''',
 faq=[
  ('מהי נקודת זיכוי?','סכום קבוע שמופחת מהמס. ערך נקודה הוא 242 ₪ לחודש, ותושב גבר מקבל 2.25 נקודות.'),
  ('מהם שיעורי הביטוח הלאומי ומס הבריאות?','ביטוח לאומי 1.04% ומס בריאות 3.23% עד 7,703 ₪, ואחרי כן 7% ו־5.17% עד תקרה של 51,910 ₪.'),
  ('למה התלוש שלי שונה?','הפרשות לפנסיה, נקודות זיכוי נוספות והטבות שווי משנים את התוצאה.'),
 ],
 sources=[
  ('https://www.malam-payroll.com/national-insurance-updates-for-2026/','Malam Payroll — עדכוני ביטוח לאומי 2026'),
  ('https://www.bizportal.co.il/guides/news/article/20038711','ביזפורטל — מדרגות מס הכנסה 2026'),
  ('https://mysachar.co.il/articles/en/tax-brackets.html','מי שכר — מדרגות מס'),
 ],
 src_intro='השיעורים והסכומים במחשבון לקוחים מהמקורות שלהלן ותקפים לשנת 2026.',
 src_note='התוצאות הן הערכה לתכנון בלבד ואינן ייעוץ מס.',
 ad_lbl='פרסומת', faq_h='שאלות נפוצות', src_h='מקורות ושיטה',
)

EXTRA['mk'] = dict(
 country='MK', opts=[], defgross=60000,
 title='Калкулатор на плата 2026 — бруто во нето Македонија',
 h1='Калкулатор на плата Македонија',
 desc='Пресметајте ја нето платата во Македонија за 2026: придонеси од 28%, личен одбиток од 10.932 денари и данок на личен доход од 10%.',
 name='Калкулатор на плата Македонија',
 ui=dict(gross='Бруто плата (MKD)', period='Период', per_m='Месечно', per_y='Годишно'),
 labels=dict(gross='Бруто плата месечно', si='Придонеси (28%)', tax='Данок на личен доход (10%)', net='Нето плата месечно', netYear='Нето годишно', eff='Вкупни одбитоци'),
 body='''<h2>Како се пресметува нето плата во Македонија (2026)</h2>
<p>Од бруто платата работникот плаќа придонеси од вкупно 28%: пензиско и инвалидско осигурување 18,8%, здравствено 7,5%, за невработеност 1,2% и дополнително здравствено 0,5%. Основицата за придонесите е ограничена меѓу 34.570 и 1.106.256 денари.</p>
<p>Данокот на личен доход е 10% и се пресметува на платата по одбивање на придонесите и личниот одбиток од 10.932 денари месечно.</p>
<h3>Пример</h3>
<p>Бруто плата од 60.000 денари: придонеси 16.800 денари, данок 3.226,80 денари. Нето плата: 39.973,20 денари.</p>
<p><em>Пресметката не вклучува додатоци, надомести и посебни олеснувања. Платниот список од работодавецот е меродавен.</em></p>''',
 faq=[
  ('Колку изнесуваат придонесите во 2026?','Вкупно 28% од бруто платата, со основица ограничена од 34.570 до 1.106.256 денари.'),
  ('Колкав е личниот одбиток?','10.932 денари месечно во 2026.'),
  ('Која е стапката на данок на личен доход?','Рамна стапка од 10%.'),
 ],
 sources=[
  ('http://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1187','УЈП — соопштение за основица и просечна плата'),
  ('https://www.podatok.mk/kalkulator-za-plata/','Podatok.mk — калкулатор за плата'),
  ('https://www.facturino.mk/en/alati/plata-kalkulator','Facturino — калкулатор за плата'),
 ],
 src_intro='Стапките и износите во калкулаторот се преземени од изворите подолу и важат за 2026.',
 src_note='Резултатите се проценки за планирање, а не даночен совет.',
 ad_lbl='Реклама', faq_h='Често поставувани прашања', src_h='Извори и методологија',
)

EXTRA['sq'] = dict(
 country='AL', opts=[], defgross=80000,
 title='Llogaritësi i pagës neto 2026 — bruto në neto Shqipëri',
 h1='Llogaritësi i pagës neto Shqipëri',
 desc='Llogarit pagën neto në Shqipëri për 2026: sigurime shoqërore 9,5%, shëndetësore 1,7% dhe tatim mbi të ardhurat nga punësimi me shkallë 0%, 13% dhe 23%.',
 name='Llogaritësi i pagës neto Shqipëri',
 ui=dict(gross='Paga bruto (ALL)', period='Periudha', per_m='Mujore', per_y='Vjetore'),
 labels=dict(gross='Paga bruto mujore', ss='Sigurime shoqërore (9,5%)', health='Sigurime shëndetësore (1,7%)', tax='Tatim mbi të ardhurat nga punësimi', net='Paga neto mujore', netYear='Neto vjetore', eff='Totali i zbritjeve'),
 body='''<h2>Si llogaritet paga neto në Shqipëri (2026)</h2>
<p>Punonjësi paguan sigurime shoqërore 9,5% (paga maksimale e kontributit është 186.416 lekë në muaj) dhe sigurime shëndetësore 1,7% pa tavan.</p>
<p>Tatimi mbi të ardhurat nga punësimi llogaritet mbi pagën bruto: 0 deri në 50.000 lekë; 13% e diferencës mbi 35.000 lekë për pagat 50.001–60.000; 13% e diferencës mbi 30.000 lekë për pagat 60.001–200.000; dhe 22.100 lekë plus 23% e diferencës mbi 200.000 lekë për pagat më të larta.</p>
<h3>Shembull</h3>
<p>Paga bruto 80.000 lekë: sigurime shoqërore 7.600, shëndetësore 1.360, tatim 6.500. Paga neto: 64.540 lekë.</p>
<p><em>Shkallët kanë kërcime mes kufijve. Nuk përfshihen shtesa, përfitime dhe zbritje të tjera. Fleta e pagës e punëdhënësit është dokumenti i vlefshëm.</em></p>''',
 faq=[
  ('Sa janë sigurimet e punonjësit në 2026?','9,5% sigurime shoqërore deri në pagën 186.416 lekë dhe 1,7% sigurime shëndetësore pa tavan.'),
  ('Kur nis tatimi mbi pagën?','Paga bruto deri në 50.000 lekë në muaj nuk tatohet. Mbi këtë kufi zbatohen shkallët 13% dhe 23%.'),
  ('Pse ndryshon fleta ime e pagës?','Shtesat, bonuset, përfitimet dhe rregullat për paga nën minimumin e kontributit mund ta ndryshojnë rezultatin.'),
 ],
 sources=[
  ('https://taxsummaries.pwc.com/albania/individual/taxes-on-personal-income','PwC — tatimi mbi të ardhurat personale në Shqipëri'),
  ('https://kalkulator.al/kalkulator-pages','Kalkulator.al — kalkulatori i pagës'),
  ('https://sherbimekontabiliteti.al/guida/paga-bruto-neto/','Shërbime Kontabiliteti — paga bruto dhe neto'),
 ],
 src_intro='Normat dhe shumat në këtë llogaritës vijnë nga burimet më poshtë dhe vlejnë për vitin 2026.',
 src_note='Rezultatet janë vlerësime për planifikim, jo këshillë tatimore.',
 ad_lbl='Reklamë', faq_h='Pyetje të shpeshta', src_h='Burimet dhe metodologjia',
)

EXTRA['ar'] = dict(
 country='EG', opts=[], defgross=20000,
 title='حاسبة صافي الراتب 2026 — الضرائب والتأمينات في مصر',
 h1='حاسبة صافي الراتب في مصر',
 desc='احسب صافي راتبك في مصر لعام 2026: التأمينات الاجتماعية 11%، ضريبة كسب العمل بالشرائح من 0% إلى 27.5%، الإعفاء الشخصي 20 ألف جنيه ورسم صندوق الشهداء.',
 name='حاسبة صافي الراتب في مصر',
 ui=dict(gross='الراتب الإجمالي (EGP)', period='الفترة', per_m='شهرياً', per_y='سنوياً'),
 labels=dict(gross='الراتب الإجمالي الشهري', si='التأمينات الاجتماعية (11%)', tax='ضريبة كسب العمل', mf='صندوق الشهداء (0.05%)', net='صافي الراتب الشهري', netYear='صافي الدخل السنوي', eff='إجمالي الاستقطاعات'),
 body='''<h2>كيف يُحسب صافي الراتب في مصر (2026)</h2>
<p>يدفع الموظف 11% من الأجر التأميني للتأمينات الاجتماعية، بحد أدنى 2,700 وحد أقصى 16,700 جنيه شهرياً اعتباراً من يناير 2026، أي بحد أقصى 1,837 جنيهاً.</p>
<p>تُحسب ضريبة كسب العمل على الدخل السنوي بعد خصم التأمينات والإعفاء الشخصي 20,000 جنيه: 0% حتى 40,000، 10% حتى 55,000، 15% حتى 70,000، 20% حتى 200,000، 22.5% حتى 400,000، 25% حتى 1,200,000 و27.5% فوق ذلك. ويُخصم كذلك 0.05% من الراتب لصندوق الشهداء.</p>
<h3>مثال</h3>
<p>راتب إجمالي 20,000 جنيه: التأمينات 1,837، الضريبة 2,445.10، صندوق الشهداء 10. صافي الراتب: 15,707.90 جنيه.</p>
<p><em>لا تشمل الحاسبة الحوافز والبدلات وضرائب الدمغة والخصومات الأخرى، كما تفترض أن الأجر التأميني يساوي الراتب الإجمالي. كشف الراتب لدى جهة العمل هو المرجع.</em></p>''',
 faq=[
  ('كم نسبة التأمينات على الموظف؟','11% من الأجر التأميني، بحد أدنى 2,700 وحد أقصى 16,700 جنيه شهرياً في 2026.'),
  ('كم الإعفاء الشخصي؟','20,000 جنيه سنوياً، ثم تُطبق الشرائح الضريبية ابتداءً من 0% حتى 40,000 جنيه.'),
  ('لماذا يختلف كشف راتبي؟','الأجر التأميني قد يختلف عن الإجمالي، كما تؤثر الحوافز والبدلات وأي ضرائب أو رسوم إضافية على النتيجة.'),
 ],
 sources=[
  ('https://www.nosi.gov.eg/ar/News/Pages/2025-11-30.aspx','الهيئة القومية للتأمين الاجتماعي — حدود الأجر التأميني 2026'),
  ('https://www.tawzef.com/en/blogs/egypt-salary-calculator-2026-faq','Tawzef — حاسبة الرواتب في مصر 2026'),
  ('https://taxsummaries.pwc.com/egypt/individual/taxes-on-personal-income','PwC — ضرائب الدخل الشخصي في مصر'),
 ],
 src_intro='النسب والمبالغ في هذه الحاسبة مأخوذة من المصادر أدناه وتسري على عام 2026.',
 src_note='النتائج تقديرات للتخطيط وليست استشارة ضريبية.',
 ad_lbl='إعلان', faq_h='الأسئلة الشائعة', src_h='المصادر والمنهجية',
)
