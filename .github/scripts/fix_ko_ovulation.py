#!/usr/bin/env python3
"""ko/ovulation-calculator/index.html was truncated mid-JavaScript and has been
live in that state: no </script>, no article, no footer, and ovCalc() never
defined - so the Korean ovulation calculator did nothing at all when you typed
in it. The file stops at "...r.setDate(r.getDate()+n);return".

Restores the missing tail, matching the English page's structure exactly and
the Korean wording used by ko/pregnancy-calculator (its sibling page) for the
shared blocks.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
P = "ko/ovulation-calculator/index.html"
ENDS_WITH = "function addDays(d,n){var r=new Date(d);r.setDate(r.getDate()+n);return"

TAIL = """ r;}
function ovCalc(){
  var lmp=new Date(document.getElementById('ovlmp').value);
  var cyc=+document.getElementById('ovcyc').value||28;
  if(isNaN(lmp)){document.getElementById('ovResult').textContent='올바른 날짜를 입력하세요';return;}
  var ovDay=addDays(lmp,cyc-14);
  var fertStart=addDays(ovDay,-5);
  var fertEnd=addDays(ovDay,1);
  var nextPeriod=addDays(lmp,cyc);
  var today=new Date();today.setHours(0,0,0,0);
  var daysToOv=Math.round((ovDay-today)/86400000);
  var phase=daysToOv>0?'<strong>'+daysToOv+'일</strong> 후 배란 예정':daysToOv===0?'<strong>오늘이 배란일입니다!</strong>':Math.abs(daysToOv)+'일 전에 배란했습니다';
  document.getElementById('ovResult').innerHTML=
    '배란일: <strong>'+fmtDate(ovDay)+'</strong><br>'+
    '가임기: '+fmtDate(fertStart)+' – '+fmtDate(fertEnd)+'<br>'+
    '다음 생리 예정일: '+fmtDate(nextPeriod)+'<br>'+phase;
}
</script></div></div><div class="seo-section"><h2>배란일을 계산하는 방법</h2><p>배란은 보통 다음 생리가 시작되기 14일 <em>전</em>에 일어납니다. 지난 생리로부터 14일 뒤가 아닙니다. 28일 주기라면 배란은 14일째, 32일 주기라면 18일째(32 − 14 = 18)입니다. 정자는 생식관 안에서 최대 5일까지 생존할 수 있으므로, 가임기는 배란 5일 전부터 배란일까지입니다.</p>
<p><strong>이 계산기 사용법:</strong> 마지막 생리 시작일(LMP)과 평균 주기 길이를 입력하세요. 예상 배란일, 가임기, 다음 생리 예정일이 표시됩니다.</p>
<p>주기 길이는 21일에서 40일까지 사람마다 다르고, 스트레스·질병·여행·호르몬 변화에 따라 달마다 달라질 수 있습니다. 더 정확하게 배란을 파악하려면 달력 계산과 함께 기초체온(BBT) 기록, 그리고 배란 24~36시간 전 황체형성호르몬(LH) 급증을 감지하는 배란테스트기(OPK)를 병행하세요.</p>
<h2>배란 징후</h2>
<ul><li><strong>자궁경부 점액:</strong> 맑고 미끄러우며 날달걀 흰자 같은 상태 — 가장 뚜렷한 가임 신호</li><li><strong>기초체온:</strong> 배란 후 0.2~0.5°C 상승해 높은 상태를 유지</li><li><strong>LH 급증:</strong> 배란테스트기로 배란 24~36시간 전에 확인 가능</li><li><strong>배란통:</strong> 일부 여성에게 배란 시 한쪽 골반에 가벼운 통증</li></ul></div><div class="seo-section"><h2>자주 묻는 질문</h2><div class="faq-item"><div class="faq-q" onclick="faq(this)"><span>배란일은 어떻게 계산하나요?</span><span class="faq-arr">+</span></div><div class="faq-a">주기 길이에서 14를 빼면 생리 첫날부터 세어 며칠째가 배란일인지 알 수 있습니다. 28일 주기는 14일째, 30일 주기는 16일째, 35일 주기는 21일째입니다. 가임기는 배란 5일 전부터 배란일까지입니다.</div></div><div class="faq-item"><div class="faq-q" onclick="faq(this)"><span>가임기는 얼마나 지속되나요?</span><span class="faq-arr">+</span></div><div class="faq-a">가임기는 약 6일입니다. 배란 5일 전과 배란일 당일을 합한 기간입니다. 정자는 여성의 생식관 안에서 3~5일 생존하지만, 난자는 배출 후 12~24시간만 생존합니다.</div></div><div class="faq-item"><div class="faq-q" onclick="faq(this)"><span>가임기가 아닐 때도 임신할 수 있나요?</span><span class="faq-arr">+</span></div><div class="faq-a">가능성은 매우 낮지만 주기 길이가 달라지면 불가능하지는 않습니다. 어떤 달에 주기가 짧아지면 배란이 더 빨라져, 주기 초반의 관계로도 임신할 수 있습니다. 주기가 불규칙할수록 달력 계산의 신뢰도는 떨어집니다.</div></div><div class="faq-item"><div class="faq-q" onclick="faq(this)"><span>주기가 불규칙하면 어떻게 하나요?</span><span class="faq-arr">+</span></div><div class="faq-a">주기가 불규칙하면 달력 기반 배란 예측의 정확도가 낮아집니다. 배란테스트기(OPK)로 LH 급증을 확인하거나 기초체온을 매일 기록하세요. 여러 신호를 함께 보는 앱이 달력 계산만 쓰는 것보다 신뢰할 수 있습니다.</div></div></div><div class="seo-section"><h2>모든 계산기</h2><div class="related"><a href="https://calculator-free.com/ko/percentage-calculator/" class="rel-card"><div class="rel-icon">%</div><div class="rel-name">백분율 계산기</div></a><a href="https://calculator-free.com/ko/bmi-calculator/" class="rel-card"><div class="rel-icon">⚖️</div><div class="rel-name">BMI 계산기</div></a><a href="https://calculator-free.com/ko/mortgage-calculator/" class="rel-card"><div class="rel-icon">🏠</div><div class="rel-name">모기지 계산기</div></a></div></div><div class="ad-wrap"><span class="ad-lbl">광고</span>
<ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5798786176755576" data-ad-slot="6610588103" data-ad-format="auto" data-full-width-responsive="true"></ins>
<script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div></div><section style="max-width:860px;margin:2.5rem auto;padding:0 1.25rem;line-height:1.65"><h2>배란일 추정 방법</h2><p>배란은 보통 다음 생리가 시작되기 약 14일 전에 일어나며, 지난 생리로부터 14일 뒤가 아닙니다. 달력 기반 계산기는 평균 주기 길이에서 황체기(14일로 가정)를 빼서 배란일을 추정하고, 가임기는 배란 약 5일 전부터 배란일 당일까지로 봅니다.</p><h3>계산 예시</h3><p>7월 1일에 시작한 30일 주기라면 다음 생리는 7월 31일 예정, 배란은 7월 17일경으로 추정되며, 가임기는 대략 7월 12일부터 17일까지입니다.</p><h3>자주 묻는 질문</h3><p><strong>달력 추정은 얼마나 정확한가요?</strong> 대략적인 값일 뿐입니다. 주기 길이는 달라지고 배란 시점은 스트레스나 질병에 따라 앞뒤로 움직입니다. 배란테스트기와 기초체온 기록이 더 정확합니다.</p><p><strong>가임기 밖에서도 임신할 수 있나요?</strong> 정자는 최대 5일 생존하므로 배란 며칠 전의 관계로도 임신할 수 있습니다. 이 도구는 정보 제공용이며 피임 수단이나 의학적 조언이 아닙니다.</p></section><div class="seo-section" id="sources"><h2>출처 및 산출 방법</h2><p>이 계산기에 사용된 공식과 수치는 아래에 공개된 자료를 근거로 합니다. 해마다 바뀌는 수치는 어느 연도에 적용되는 값인지 페이지에 표시했습니다.</p><ul><li><a href="https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2017/05/methods-for-estimating-the-due-date" target="_blank" rel="noopener nofollow">ACOG — Methods for estimating the due date (Committee Opinion 700)</a></li></ul><p><em>이 도구는 일반적인 정보만 제공하며 의학적 조언이 아닙니다. 본인의 건강에 관한 문제는 의사 등 자격을 갖춘 의료 전문가와 상담하시기 바랍니다.</em></p></div><footer><div class="wrap">
<p>© 2026 calculator-free.com · <a href="https://calculator-free.com/ko/">모든 계산기</a> · <a href="https://calculator-free.com/about/">소개</a> · <a href="https://calculator-free.com/privacy-policy/">개인정보처리방침</a> · <a href="https://calculator-free.com/terms-of-use/">이용약관</a> · <a href="https://calculator-free.com/contact/">문의</a></p>
</div></footer></body></html>
"""

t = open(P, encoding="utf-8").read()
if "</html>" in t:
    print("already repaired, nothing to do")
else:
    assert t.rstrip("\n").endswith(ENDS_WITH), "unexpected truncation point"
    t = t.rstrip("\n") + TAIL
    open(P, "w", encoding="utf-8", newline="").write(t)
    print("ko/ovulation-calculator repaired: %d -> %d bytes, divs %d/%d, scripts %d/%d"
          % (31403, len(t), t.count("<div"), t.count("</div>"),
             t.count("<script"), t.count("</script>")))
