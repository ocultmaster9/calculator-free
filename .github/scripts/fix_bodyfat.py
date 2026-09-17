#!/usr/bin/env python3
"""Body-fat result categories left in English inside the JS (18 languages).
Terms taken from the category list each page already prints in its body."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

# athletic, fitness, average, obese  (essential-fat term is already translated)
T = {
 "ar":("الرياضيون","اللياقة","المتوسط","سمنة"),
 "zh":("运动员","健身水平","平均值","肥胖"),
 "da":("Atleter","Veltrænet","Gennemsnit","Svær overvægt"),
 "nl":("Sporters","Fit","Gemiddelde","Obesitas"),
 "fr":("Athlètes","En forme","Moyenne","Obésité"),
 "de":("Sportler","Fit","Durchschnitt","Adipös"),
 "hi":("खिलाड़ी","फ़िटनेस","औसत","मोटा"),
 "id":("Atlet","Bugar","Rata-rata","Obesitas"),
 "it":("Atleti","In forma","Media","Obeso"),
 "ja":("アスリート","フィットネス","平均","肥満"),
 "ko":("운동선수","체력 수준","평균","비만"),
 "no":("Idrettsutøvere","Veltrent","Gjennomsnitt","Fedme"),
 "pl":("Sportowcy","Wysportowanie","Średnia","Otyłość"),
 "pt":("Atletas","Condicionamento físico","Média","Obesidade"),
 "ru":("Спортсмены","Спортивная форма","Среднее","Ожирение"),
 "es":("Atletas","En forma","Promedio","Obesidad"),
 "sv":("Idrottare","Vältränad","Genomsnitt","Fetma"),
 "tr":("Sporcular","Fit","Ortalama","Obez"),
}
PAT = re.compile(r"cat=bf<(\d+)\?'([^']*)':bf<(\d+)\?'([^']*)':bf<(\d+)\?'([^']*)':bf<(\d+)\?'([^']*)':'([^']*)';")
n = 0
for lang, (ath, fit, avg, obe) in T.items():
    p = "%s/body-fat-calculator/index.html" % lang
    t = open(p, encoding="utf-8").read(); o = t
    def rep(m):
        return ("cat=bf<%s?'%s':bf<%s?'%s':bf<%s?'%s':bf<%s?'%s':'%s';"
                % (m.group(1), m.group(2), m.group(3), ath, m.group(5), fit, m.group(7), avg, obe))
    t = PAT.sub(rep, t)
    if t != o:
        open(p, "w", encoding="utf-8", newline="").write(t); n += 1
print("body-fat js fixed in %d languages" % n)
