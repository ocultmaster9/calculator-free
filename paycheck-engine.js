/* calculator-free.com paycheck engine — per-country payroll rules (monthly gross -> net).
   Each country: {cur, opts:[ids], calc(monthlyGross, opts) -> {rows:[[key,amount,sign]], net}}.
   sign: -1 deducted from gross, 0 informational. Rules year noted per country. */
(function(){
var C={};
/* RO — Jul–Dec 2026. Sources: ANAF (non-taxable amount 2026), MMuncii HG salariul minim 2026, Legea 296/2023. */
C.RO={cur:'RON',opts:['minbase'],calc:function(g,o){
  var MIN=4325,ex=(o.minbase&&g>=MIN&&g<=4600)?200:0,base=g-ex;
  var cas=Math.round(base*.25),cass=Math.round(base*.10),ded=0;
  if(g<=MIN)ded=.20*MIN;else if(g<=MIN+2000)ded=(.20-.005*Math.ceil((g-MIN)/50))*MIN;
  ded=Math.round(ded);
  var tax=Math.round(Math.max(0,base-cas-cass-ded)*.10);
  return {rows:[['cas',cas,-1],['cass',cass,-1],['ded',ded,0],['tax',tax,-1]],net:g-cas-cass-tax};
}};

/* PL — 2026. Sources: zus.pl (składki 2026), podatki.gov.pl (skala podatkowa), GazetaPrawna (limit 282 600 zł). Umowa o pracę, KUP 250 zł/mies. */
C.PL={cur:'PLN',dec:2,opts:[],calc:function(g,o){
  var A=g*12,em=Math.min(A,282600)*.0976,re=Math.min(A,282600)*.015,ch=A*.0245,soc=em+re+ch;
  var health=(A-soc)*.09,base=Math.max(0,Math.round(A-soc-3000));
  var tax=Math.max(0,Math.round(.12*Math.min(base,120000)+.32*Math.max(0,base-120000)-3600));
  return {rows:[['zus',soc/12,-1],['zdr',health/12,-1],['pit',tax/12,-1]],net:(A-soc-health-tax)/12};
}};
/* DE — 2026, Steuerklasse I, ohne Kirchensteuer. §32a EStG 2026; SV-Sätze/BBG 2026; Soli-Freigrenze 20.350 €. */
C.DE=(function(){
  function est(x){x=Math.floor(x);if(x<=12348)return 0;var y,z;
    if(x<=17799){y=(x-12348)/1e4;return Math.floor((914.51*y+1400)*y);}
    if(x<=69878){z=(x-17799)/1e4;return Math.floor((173.10*z+2397)*z+1034.87);}
    if(x<=277825)return Math.floor(.42*x-11135.63);
    return Math.floor(.45*x-19470.38);}
  return {cur:'EUR',dec:2,opts:['childless'],calc:function(g,o){
    var A=g*12,rvb=Math.min(A,101400),kvb=Math.min(A,69750),pvr=.018+(o.childless?.006:0);
    var rv=rvb*.093,av=rvb*.013,kv=kvb*.0875,pv=kvb*pvr;
    var vp=rv+kvb*.0845+pv,zve=A-1230-36-vp,lst=est(zve),soli=0;
    if(lst>20350)soli=Math.min(.055*lst,.119*(lst-20350));
    return {rows:[['rv',rv/12,-1],['av',av/12,-1],['kv',kv/12,-1],['pv',pv/12,-1],['lst',lst/12,-1],['soli',soli/12,-1]],
      net:(A-rv-av-kv-pv-lst-soli)/12};
  }};
})();

/* FR — 2026, net avant impôt sur le revenu, salarié du privé (bulletin-paie.com: PMSS 4 005 €). */
C.FR={cur:'EUR',dec:2,opts:['cadre'],calc:function(g,o){
  var PM=4005,T1=Math.min(g,PM),T2=Math.max(0,Math.min(g,8*PM)-PM);
  var ret=.069*T1+.004*g+.0315*T1+.0086*T1+.0014*Math.min(g,8*PM);
  if(o.cadre)ret+=.0864*T2+.0108*T2+.00024*Math.min(g,4*PM);
  var base=.9825*Math.min(g,4*PM)+Math.max(0,g-4*PM),csg=.097*base;
  return {rows:[['ret',ret,-1],['csg',csg,-1]],net:g-ret-csg};
}};
/* ES — 2026, régimen general, escala general IRPF (estatal+autonómica por defecto), soltero sin hijos. */
C.ES=(function(){
  var B=[[12450,.19],[20200,.24],[35200,.30],[60000,.37],[300000,.45],[Infinity,.47]];
  function sc(x){var t=0,p=0;B.forEach(function(b){t+=Math.max(0,Math.min(x,b[0])-p)*b[1];p=b[0];});return t;}
  return {cur:'EUR',dec:2,opts:[],calc:function(g,o){
    var A=g*12,ss=Math.min(g,5101.20)*12*.065,rn=Math.max(0,A-ss-2000),red=0;
    if(rn<=14852)red=7302;else if(rn<=17673.52)red=7302-1.75*(rn-14852);else if(rn<=19747.5)red=2364.34-1.14*(rn-17673.52);
    var base=Math.max(0,rn-red),irpf=Math.max(0,sc(base)-sc(5550));
    return {rows:[['ss',ss/12,-1],['irpf',irpf/12,-1]],net:(A-ss-irpf)/12};
  }};
})();
/* IT — 2026, dipendente privato, IRPEF 23/33/43, INPS 9,19%; senza addizionali regionali/comunali. */
C.IT={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var A=g*12,inps=A*.0919,R=A-inps;
  var lorda=.23*Math.min(R,28000)+.33*Math.max(0,Math.min(R,50000)-28000)+.43*Math.max(0,R-50000),d=0;
  if(R<=15000)d=1955;else if(R<=28000)d=1910+1190*(28000-R)/13000;else if(R<=50000)d=1910*(50000-R)/22000;
  if(R>25000&&R<=35000)d+=65;
  if(R>20000&&R<=32000)d+=1000;else if(R>32000&&R<=40000)d+=1000*(40000-R)/8000;
  var irpef=Math.max(0,lorda-d),bonus=A<=8500?.071*A:A<=15000?.053*A:A<=20000?.048*A:0;
  if(R>20000)bonus=0;
  return {rows:[['inps',inps/12,-1],['irpef',irpef/12,-1],['bonus',bonus/12,1]],net:(A-inps-irpef+bonus)/12};
}};
/* NL — 2026, loonheffing incl. volksverzekeringen, onder AOW-leeftijd, algemene heffingskorting + arbeidskorting (Belastingdienst). */
C.NL={cur:'EUR',dec:2,opts:['holiday'],calc:function(g,o){
  var A=g*12*(o.holiday?1.08:1);
  var t=.3575*Math.min(A,38883)+.3756*Math.max(0,Math.min(A,78426)-38883)+.495*Math.max(0,A-78426);
  var ahk=A<=29736?3115:A<=78426?3115-.06398*(A-29736):0;
  var ak=A<=11965?.08324*A:A<=25845?996+.31009*(A-11965):A<=45592?5300+.0195*(A-25845):A<=132920?5685-.0651*(A-45592):0;
  var tax=Math.max(0,t-Math.max(0,ahk)-Math.max(0,ak));
  return {rows:[['tax',tax/12,-1]],net:(A-tax)/12};
}};

/* BG — 2026, 13,78% осигуровки (макс. осигурителен доход 2 300 € от 1.8.2026, НОИ), 10% данък. */
C.BG={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var ins=Math.min(g,2300)*.1378,tax=Math.max(0,g-ins)*.10;
  return {rows:[['ins',ins,-1],['tax',tax,-1]],net:g-ins-tax};
}};
/* CZ — 2026, sociální 7,1 % (strop 2 350 416 Kč/rok), zdravotní 4,5 %, daň 15 %/23 % nad 146 901 Kč/měs., sleva na poplatníka 2 570 Kč/měs. */
C.CZ={cur:'CZK',opts:[],calc:function(g,o){
  var soc=Math.min(g,2350416/12)*.071,zdr=g*.045,t=.15*Math.min(g,146901)+.23*Math.max(0,g-146901);
  var tax=Math.max(0,t-2570);
  return {rows:[['soc',soc,-1],['zdr',zdr,-1],['tax',tax,-1]],net:g-soc-zdr-tax};
}};
/* HU — 2026, SZJA 15 %, társadalombiztosítási járulék 18,5 %, kedvezmények nélkül. */
C.HU={cur:'HUF',opts:[],calc:function(g,o){
  var szja=g*.15,tb=g*.185;
  return {rows:[['szja',szja,-1],['tb',tb,-1]],net:g-szja-tb};
}};
/* SK — 2026, odvody 9,4 % + 5 % zdravotné, daň 19/25/30/35 %, nezdaniteľná časť 497,23 €/mes. */
C.SK={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var soc=g*.094,zdr=g*.05,b=Math.max(0,g-soc-zdr-497.23),B=[[3665.28,.19],[5029.10,.25],[6250.86,.30],[Infinity,.35]],t=0,p=0;
  B.forEach(function(x){t+=Math.max(0,Math.min(b,x[0])-p)*x[1];p=x[0];});
  return {rows:[['soc',soc,-1],['zdr',zdr,-1],['tax',t,-1]],net:g-soc-zdr-t};
}};
/* EE — 2026, tulumaks 22 %, maksuvaba tulu 700 €/kuus, töötuskindlustus 1,6 %, kogumispension 2 %. */
C.EE={cur:'EUR',dec:2,opts:['pillar'],calc:function(g,o){
  var un=g*.016,pen=o.pillar?g*.02:0,tax=Math.max(0,g-un-pen-700)*.22;
  return {rows:[['un',un,-1],['pen',pen,-1],['tax',tax,-1]],net:g-un-pen-tax};
}};
/* LV — 2026, VSAOI 10,5 % (līdz 8 775 €/mēn.), IIN 25,5 % / 33 % virs 8 775 €, neapliekamais minimums 550 €. */
C.LV={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var vs=Math.min(g,8775)*.105,b=Math.max(0,g-vs-550),tax=.255*Math.min(b,8775)+.33*Math.max(0,b-8775);
  return {rows:[['vs',vs,-1],['tax',tax,-1]],net:g-vs-tax};
}};
/* LT — 2026, Sodra 12,52 % + 6,98 %, GPM 20 % (25 %/32 % nuo 82 962 €/138 270 € per metus), NPD = 747 − 0,49 × (bruto − 1 153). */
C.LT={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var vsd=g*.1252,psd=g*.0698,npd=g<=1153?747:Math.max(0,747-.49*(g-1153)),b=Math.max(0,g-npd),A=b*12;
  var t=(.20*Math.min(A,82962)+.25*Math.max(0,Math.min(A,138270)-82962)+.32*Math.max(0,A-138270))/12;
  return {rows:[['vsd',vsd,-1],['psd',psd,-1],['tax',t,-1]],net:g-vsd-psd-t};
}};
/* HR — 2026, MIO I 15 % + MIO II 5 %, osobni odbitak 600 €, porez 23 % / 33 % (iznad 5 000 €/mj., Zagreb). */
C.HR={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var mio=g*.20,b=Math.max(0,g-mio-600),tax=.23*Math.min(b,5000)+.33*Math.max(0,b-5000);
  return {rows:[['mio',mio,-1],['tax',tax,-1]],net:g-mio-tax};
}};

function brk(x,B){var t=0,p=0;B.forEach(function(b){t+=Math.max(0,Math.min(x,b[0])-p)*b[1];p=b[0];});return t;}
/* DK — 2026: AM-bidrag 8 %, bundskat 12,01 %, kommuneskat Ø 25,05 %, mellem-/topskat, personfradrag 54.100 kr, beskæftigelsesfradrag 12,75 % (maks 63.300). Uden kirkeskat. */
C.DK={cur:'DKK',opts:[],calc:function(g,o){
  var A=g*12,am=.08*A,pi=A-am,besk=Math.min(.1275*pi,63300);
  var bund=.1201*Math.max(0,pi-54100),komm=.2505*Math.max(0,pi-besk-54100);
  var st=bund+.075*Math.max(0,Math.min(pi,777900)-641200)+.15*Math.max(0,pi-777900)+.05*Math.max(0,pi-2592700);
  return {rows:[['am',am/12,-1],['state',st/12,-1],['komm',komm/12,-1]],net:(A-am-st-komm)/12};
}};
/* NO — 2026: trygdeavgift 7,6 %, alminnelig inntekt 22 %, trinnskatt, minstefradrag 46 % (maks 95.700), personfradrag 114.540. */
C.NO={cur:'NOK',opts:[],calc:function(g,o){
  var A=g*12,mf=Math.min(.46*A,95700),alm=.22*Math.max(0,A-mf-114540);
  var tr;
  tr=.017*Math.max(0,Math.min(A,318300)-226100)+.04*Math.max(0,Math.min(A,725050)-318300)+.137*Math.max(0,Math.min(A,980100)-725050)+.168*Math.max(0,Math.min(A,1467200)-980100)+.178*Math.max(0,A-1467200);
  var trygd=A>99650?Math.min(.076*A,.25*(A-99650)):0;
  return {rows:[['alm',alm/12,-1],['trinn',tr/12,-1],['trygd',trygd/12,-1]],net:(A-alm-tr-trygd)/12};
}};
/* IE — 2026: 20 %/40 % (standard rate band €44,000), credits €2.000 + €2.000, USC, PRSI 4.2 % (4.35 % from October 2026, blended). */
C.IE={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var A=g*12,t=Math.max(0,.2*Math.min(A,44000)+.4*Math.max(0,A-44000)-4000);
  var usc=A<=13000?0:.005*Math.min(A,12012)+.02*Math.max(0,Math.min(A,28700)-12012)+.03*Math.max(0,Math.min(A,70044)-28700)+.08*Math.max(0,A-70044);
  var prsi=A*.042375;
  return {rows:[['tax',t/12,-1],['usc',usc/12,-1],['prsi',prsi/12,-1]],net:(A-t-usc-prsi)/12};
}};
/* MT — 2026, single computation, SSC 10 % (max €55,93/week). */
C.MT={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var A=g*12,t=brk(A,[[12000,0],[16000,.15],[60000,.25],[Infinity,.35]]),ssc=Math.min(.1*A/52,55.93)*52;
  return {rows:[['tax',t/12,-1],['ssc',ssc/12,-1]],net:(A-t-ssc)/12};
}};
/* TR — 2026: SGK 14 % + işsizlik 1 % (tavan 297.270 TL/ay), gelir vergisi dilimleri, damga vergisi ‰7,59, asgari ücret istisnası (33.030 TL). */
C.TR=(function(){
  var B=[[190000,.15],[540000,.20],[1500000,.27],[4000000,.35],[Infinity,.40]],MIN=33030;
  return {cur:'TRY',opts:[],calc:function(g,o){
    var b=Math.min(g,297270),sgk=.14*b,iss=.01*b,A=12*(g-sgk-iss);
    var tax=Math.max(0,brk(A,B)-brk(12*MIN*.85,B)),damga=Math.max(0,g-MIN)*.00759;
    if(g<=MIN)tax=0;
    return {rows:[['sgk',sgk,-1],['iss',iss,-1],['tax',tax/12,-1],['damga',damga,-1]],net:g-sgk-iss-tax/12-damga};
  }};
})();
/* RU — 2026: НДФЛ 13/15/18/20/22 % (2,4 / 5 / 20 / 50 млн руб. в год). */
C.RU={cur:'RUB',opts:[],calc:function(g,o){
  var A=g*12,t=brk(A,[[2400000,.13],[5000000,.15],[20000000,.18],[50000000,.20],[Infinity,.22]]);
  return {rows:[['ndfl',t/12,-1]],net:g-t/12};
}};
/* UA — 2026: ПДФО 18 % + військовий збір 5 %; ЄСВ сплачує роботодавець. */
C.UA={cur:'UAH',opts:[],calc:function(g,o){
  var p=g*.18,v=g*.05;return {rows:[['pdfo',p,-1],['vz',v,-1]],net:g-p-v};
}};
/* RS — 2026: PIO 14 % + zdravstveno 5,15 % + nezaposlenost 0,75 %, porez 10 % iznad 34.221 RSD (osnovica doprinosa 51.297–732.820 RSD). */
C.RS={cur:'RSD',opts:[],calc:function(g,o){
  var c=Math.min(Math.max(g,51297),732820)*.199,tax=Math.max(0,g-34221)*.10;
  return {rows:[['dop',c,-1],['tax',tax,-1]],net:g-c-tax};
}};
/* GR — 2026: 14 μισθοί, e-EFKA 13,37 % (μέχρι 7.761,94 €/μήνα), κλίμακα 9/20/26/34/39/44 %, μείωση φόρου 777 € (−20 € ανά 1.000 € άνω των 12.000 €). Χωρίς παιδιά, ηλικία άνω των 30. */
C.GR={cur:'EUR',dec:2,pay:14,opts:[],calc:function(g,o){
  var A=14*g,ef=.1337*Math.min(g,7761.94)*14,Z=A-ef;
  var t=brk(Z,[[10000,.09],[20000,.20],[30000,.26],[40000,.34],[60000,.39],[Infinity,.44]]);
  var cr=Math.max(0,777-20*Math.max(0,(Z-12000)/1000)),tax=Math.max(0,t-cr);
  return {rows:[['efka',ef/14,-1],['tax',tax/14,-1]],net:(A-ef-tax)/14};
}};
/* BR — 2026: INSS progressivo (teto 8.475,55), IRRF Lei 15.191/2025 (tabela + desconto simplificado 607,20) e redutor Lei 15.270/2025 (isenção até 5.000, redução até 7.350). Sem dependentes. */
C.BR={cur:'BRL',dec:2,opts:[],calc:function(g,o){
  var r=function(x){return Math.round(x*100)/100;};
  var inss=r(brk(Math.min(g,8475.55),[[1621,.075],[2902.84,.09],[4354.27,.12],[8475.55,.14]]));
  var b=g-Math.max(inss,607.20),t=0;
  if(b>4664.68)t=b*.275-908.73;else if(b>3751.05)t=b*.225-675.49;else if(b>2826.65)t=b*.15-394.16;else if(b>2428.80)t=b*.075-182.16;
  t=r(Math.max(0,t));
  var red=g<=5000?t:(g<=7350?Math.min(t,Math.max(0,978.62-.133145*g)):0);
  var irrf=r(Math.max(0,t-red));
  return {rows:[['inss',inss,-1],['irrf',irrf,-1]],net:g-inss-irrf};
}};
/* JP — 2026: modelo anual (Tóquio, Kyokai Kenpo, <40 anos, solteiro): seguro-saúde 4,925 % + apoio à infância 0,115 %, pensão 9,15 % (teto 650 mil), emprego 0,5 %, imposto nacional (+2,1 %) e imposto residente 10 % + 5.000. Sem bônus. */
C.JP={cur:'JPY',opts:[],calc:function(g,o){
  var S=12*g,G=[88,98,104,110,118,126,134,142,150,160,170,180,190,200,220,240,260,280,300,320,340,360,380,410,440,470,500,530,560,590,620,650,680,710,750,790,830,870,910,950,990,1030,1070,1110,1150,1210,1270,1330,1390],sr=G[0]*1000;
  for(var i=0;i<G.length;i++){var lo=i?(G[i-1]+G[i])/2:0,hi=i<G.length-1?(G[i]+G[i+1])/2:1e9;if(g>=lo*1000&&g<hi*1000){sr=G[i]*1000;break;}}
  var hl=.05040*sr*12,pn=.0915*Math.min(sr,650000)*12,em=.005*S,si=hl+pn+em;
  var ed=S<=2200000?740000:S<=3600000?.3*S+80000:S<=6600000?.2*S+440000:S<=8500000?.1*S+1100000:1950000,inc=Math.max(0,S-ed);
  var bd=inc<=4890000?1040000:inc<=6550000?670000:inc<=23500000?620000:inc<=24000000?480000:inc<=24500000?320000:inc<=25000000?160000:0;
  var ti=Math.max(0,inc-si-bd),it=brk(ti,[[1949000,.05],[3299000,.10],[6949000,.20],[8999000,.23],[17999000,.33],[39999000,.40],[Infinity,.45]])*1.021;
  var rt=Math.max(0,inc-si-430000)*.10+5000;
  return {rows:[['health',hl/12,-1],['pension',pn/12,-1],['emp',em/12,-1],['tax',it/12,-1],['res',rt/12,-1]],net:g-(si+it+rt)/12};
}};
/* KR — 2026: 4대보험 (국민연금 4,75 %, 상한 6.590.000; 건강 3,595 %; 장기요양 13,14 %; 고용 0,9 %), 근로소득공제, 기본공제 150만, 세액공제, 지방소득세 10 %. 연말정산 기준. */
C.KR={cur:'KRW',opts:[],calc:function(g,o){
  var S=12*g,nps=.0475*Math.min(Math.max(g,410000),6590000),hi=.03595*g,ltc=hi*.1314,ei=.009*g,ins=(nps+hi+ltc+ei)*12;
  var ed=S<=5e6?.7*S:S<=15e6?3.5e6+.4*(S-5e6):S<=45e6?7.5e6+.15*(S-15e6):S<=100e6?12e6+.05*(S-45e6):14.75e6+.02*(S-100e6);ed=Math.min(ed,2e7);
  var base=Math.max(0,S-ed-1.5e6-ins),tx=brk(base,[[14e6,.06],[50e6,.15],[88e6,.24],[150e6,.35],[300e6,.38],[500e6,.40],[1e9,.42],[Infinity,.45]]);
  var cr=tx<=1.3e6?.55*tx:715000+.3*(tx-1.3e6),lim=S<=33e6?74e4:S<=70e6?Math.max(74e4-.008*(S-33e6),66e4):S<=120e6?Math.max(66e4-.5*(S-70e6),5e5):Math.max(5e5-.5*(S-120e6),2e5);
  tx=Math.max(0,tx-Math.min(cr,lim)-130000);
  return {rows:[['nps',nps,-1],['health',hi,-1],['ltc',ltc,-1],['ei',ei,-1],['tax',tx/12,-1],['local',tx/120,-1]],net:g-nps-hi-ltc-ei-tx/12-tx/120};
}};
/* CN — 2026 (Xangai): seguro social 10,5 % (base 7.546–37.731), fundo de habitação 7 % (base 2.740–37.731), deducao 5.000/mês, IIT 3–45 %. */
C.CN={cur:'CNY',opts:[],calc:function(g,o){
  var b=Math.min(Math.max(g,7546),37731),si=.105*b,hf=Math.round(.07*Math.min(Math.max(g,2740),37731));
  var t=brk(Math.max(0,12*(g-si-hf-5000)),[[36000,.03],[144000,.10],[300000,.20],[420000,.25],[660000,.30],[960000,.35],[Infinity,.45]])/12;
  return {rows:[['si',si,-1],['hf',hf,-1],['tax',t,-1]],net:g-si-hf-t};
}};
/* IN — FY2026-27, novo regime: dedução padrão 75.000, rebate 87A até 12 lakh (com alívio marginal), cess 4 %, PF 12 % do básico (50 % do bruto, teto 15.000). Sem sobretaxa nem professional tax. */
C.IN={cur:'INR',opts:[],calc:function(g,o){
  var A=12*g,T=Math.max(0,A-75000),t=brk(T,[[400000,0],[800000,.05],[1200000,.10],[1600000,.15],[2000000,.20],[2400000,.25],[Infinity,.30]]);
  if(T<=1200000)t=0;else t=Math.min(t,T-1200000);t*=1.04;
  var pf=.12*Math.min(.5*g,15000);
  return {rows:[['tax',t/12,-1],['pf',pf,-1]],net:g-t/12-pf};
}};
/* ID — 2026: PPh 21 pegawai tetap TK/0 (metode tahunan): PTKP 54 juta, biaya jabatan 5 % (maks 500 rb/bln), JHT 2 %, JP 1 % (maks 11.086.300), BPJS Kesehatan 1 % (maks 12 juta). */
C.ID={cur:'IDR',opts:[],calc:function(g,o){
  var A=12*g,jht=.02*g,jp=.01*Math.min(g,11086300),kes=.01*Math.min(g,12e6),bj=Math.min(.05*A,6e6);
  var pkp=Math.max(0,Math.floor((A-bj-12*(jht+jp)-54e6)/1000)*1000),t=brk(pkp,[[60e6,.05],[250e6,.15],[500e6,.25],[5e9,.30],[Infinity,.35]]);
  return {rows:[['pph',t/12,-1],['jht',jht,-1],['jp',jp,-1],['kes',kes,-1]],net:g-t/12-jht-jp-kes};
}};
/* VN — 2026: bảo hiểm 10,5 % (XH+YT 9,5 % trần 46,8 tr; TN 1 % trần 106,2 tr), giảm trừ bản thân 15,5 tr, biểu thuế 5 bậc (5/10/20/30/35 %). */
C.VN={cur:'VND',opts:[],calc:function(g,o){
  var s1=.095*Math.min(g,46.8e6),s2=.01*Math.min(g,106.2e6),tx=Math.max(0,g-s1-s2-15.5e6),t=brk(tx,[[10e6,.05],[30e6,.10],[60e6,.20],[100e6,.30],[Infinity,.35]]);
  return {rows:[['si',s1,-1],['ui',s2,-1],['tax',t,-1]],net:g-s1-s2-t};
}};
/* TH — 2026: ประกันสังคม 5 % (เพดาน 17,500 บาท), หักค่าใช้จ่าย 50 % (สูงสุด 100,000), ลดหย่อนส่วนตัว 60,000, หักประกันสังคมไม่เกิน 9,000, อัตราก้าวหน้า 0–35 %. */
C.TH={cur:'THB',opts:[],calc:function(g,o){
  var A=12*g,ss=.05*Math.min(g,17500),tx=Math.max(0,A-Math.min(.5*A,1e5)-6e4-Math.min(12*ss,9000)),t=brk(tx,[[150000,0],[300000,.05],[500000,.10],[750000,.15],[1e6,.20],[2e6,.25],[5e6,.30],[Infinity,.35]])/12;
  return {rows:[['ss',ss,-1],['tax',t,-1]],net:g-ss-t};
}};
/* PH — 2026: SSS 5 % (MSC 5.000–35.000), PhilHealth 2,5 % (10.000–100.000), Pag-IBIG 2 % (maks 200), TRAIN 2023+ (0/15/20/25/30/35 %). */
C.PH={cur:'PHP',dec:2,opts:[],calc:function(g,o){
  var sss=.05*Math.min(Math.max(Math.round(g/500)*500,5000),35000),ph=.025*Math.min(Math.max(g,1e4),1e5),pi=Math.min(.02*g,200);
  var t=brk(Math.max(0,12*(g-sss-ph-pi)),[[250000,0],[400000,.15],[800000,.20],[2e6,.25],[8e6,.30],[Infinity,.35]])/12;
  return {rows:[['sss',sss,-1],['ph',ph,-1],['pi',pi,-1],['tax',t,-1]],net:g-sss-ph-pi-t};
}};
/* MY — YA2026: EPF 11 %, SOCSO 0,5 % + EIS 0,2 % (tavan RM6.000, jalur RM100), SKBBK 0,75 % (pilihan), PCB kaedah tahunan, pelepasan 9.000 + EPF (maks 4.000) + SOCSO/EIS (maks 350), rebat RM400. */
C.MY={cur:'MYR',dec:2,opts:['skbbk'],calc:function(g,o){
  var epf=Math.ceil(.11*g),b=Math.min(g,6000),mid=b>0?Math.ceil(b/100)*100-50:0,so=Math.round(.005*mid*20)/20,ei=.002*mid,sk=o.skbbk?Math.min(.0075*b,45):0;
  var c=Math.max(0,12*g-9000-Math.min(12*epf,4000)-Math.min(12*(so+ei),350)),t=brk(c,[[5000,0],[20000,.01],[35000,.03],[50000,.06],[70000,.11],[100000,.19],[400000,.25],[600000,.26],[2e6,.28],[Infinity,.30]]);
  if(c<=35000)t=Math.max(0,t-400);t/=12;
  return {rows:[['epf',epf,-1],['socso',so,-1],['eis',ei,-1],['skbbk',sk,-1],['pcb',t,-1]],net:g-epf-so-ei-sk-t};
}};
/* ZA — 2026/27: PAYE (7 escalões, rebate primário 17.820), UIF 1 % (teto R17.712). Sem crédito médico. */
C.ZA={cur:'ZAR',dec:2,opts:[],calc:function(g,o){
  var t=Math.max(0,brk(12*g,[[245100,.18],[383100,.26],[530200,.31],[695800,.36],[887000,.39],[1878600,.41],[Infinity,.45]])-17820)/12,u=.01*Math.min(g,17712);
  return {rows:[['paye',t,-1],['uif',u,-1]],net:g-t-u};
}};
/* KE — 2026: NSSF 6 % (LEL 9.000, UEL 108.000), SHIF 2,75 % (mín. 300), Housing Levy 1,5 %, PAYE 10–35 %, relief 2.400. */
C.KE={cur:'KES',dec:2,opts:[],calc:function(g,o){
  var n=.06*Math.min(g,9000)+.06*Math.max(0,Math.min(g,108000)-9000),sh=Math.max(300,.0275*g),ah=.015*g;
  var p=Math.max(0,brk(g-n-sh-ah,[[24000,.10],[32333,.25],[500000,.30],[800000,.325],[Infinity,.35]])-2400);
  return {rows:[['nssf',n,-1],['shif',sh,-1],['ahl',ah,-1],['paye',p,-1]],net:g-n-sh-ah-p};
}};
/* SE — 2026: grundavdrag, kommunalskatt Ø 32,38 %, statlig skatt 20 % över 643.000, jobbskatteavdrag (prisbasbelopp 59.200). Utan kyrkoavgift. */
C.SE={cur:'SEK',opts:[],calc:function(g,o){
  var P=59200,F=12*g,ki=.3238,ga;
  if(F<=.99*P)ga=.423*P;else if(F<=2.72*P)ga=.423*P+.2*(F-.99*P);else if(F<=3.11*P)ga=.77*P;else if(F<=7.88*P)ga=.77*P-.1*(F-3.11*P);else ga=.293*P;
  ga=Math.min(F,Math.ceil(ga/100)*100);
  var ti=F-ga,mun=Math.floor(ti*ki),st=.2*Math.max(0,ti-643000),j;
  if(F<=.91*P)j=(F-ga)*ki;else if(F<=3.24*P)j=(.91*P+.3874*(F-.91*P)-ga)*ki;else if(F<=8.08*P)j=(1.813*P+.251*(F-3.24*P)-ga)*ki;else j=(3.027*P-ga)*ki;
  j=Math.min(mun,Math.max(0,Math.floor(j)));
  return {rows:[['kom',mun/12,-1],['stat',st/12,-1],['jsa',j/12,1]],net:g-(mun+st-j)/12};
}};
/* FI — 2026: valtion tuloveroasteikko, kunnallisvero Ø 7,57 %, sairaanhoitomaksu 1,10 %, TyEL 7,30 %, työttömyysvakuutus 0,89 %, päivärahamaksu 0,88 %, Yle-vero, työtulovähennys. Ilman kirkollisveroa. */
C.FI={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var A=12*g,soc=(.073+.0089)*A+(A>=17255?.0088*A:0),ne=Math.max(0,A-soc-750);
  var st=brk(ne,[[22000,.1264],[32600,.19],[40100,.3025],[52100,.3325],[Infinity,.375]]);
  var mb=Math.max(0,ne-Math.max(0,4265-.18*Math.max(0,ne-4265))),mu=.0757*mb,sa=.011*mb,yle=Math.min(160,.025*Math.max(0,ne-15150));
  var cr=Math.max(0,Math.min(.18*A,3430)-.02*Math.min(Math.max(0,ne-35000),15550));cr=Math.min(cr,st+mu+sa);
  var tax=st+mu+sa-cr;
  return {rows:[['soc',soc/12,-1],['tax',tax/12,-1],['yle',yle/12,-1]],net:g-(soc+tax+yle)/12};
}};
/* SI — 2026: prispevki delojemalca 23,1 % (vklj. dolgotrajna oskrba 1 %), splošna olajšava 462,66 €/mes, dohodninska lestvica 16–50 %. */
C.SI={cur:'EUR',dec:2,opts:[],calc:function(g,o){
  var c=.231*g,rel=462.66+(g<1480.51?1736.03-1.17259*g:0),b=Math.max(0,g-c-rel),t=brk(b,[[810.12,.16],[2382.70,.26],[4765.41,.33],[6862.19,.39],[Infinity,.50]]);
  return {rows:[['soc',c,-1],['tax',t,-1]],net:g-c-t};
}};
/* IL — 2026: מדרגות מס (10–50 %), 2,25 נקודות זיכוי × 242 ₪, ביטוח לאומי 1,04 %/7 % ובריאות 3,23 %/5,17 % (סף 7,703; תקרה 51,910). ללא פנסיה. */
C.IL={cur:'ILS',dec:2,opts:[],calc:function(g,o){
  var t=Math.max(0,brk(g,[[7010,.10],[10060,.14],[19000,.20],[25100,.31],[46690,.35],[60130,.47],[Infinity,.50]])-544.5),lo=Math.min(g,7703),hi=Math.max(0,Math.min(g,51910)-7703);
  var ni=.0104*lo+.07*hi,he=.0323*lo+.0517*hi;
  return {rows:[['tax',t,-1],['ni',ni,-1],['health',he,-1]],net:g-t-ni-he};
}};
/* MK — 2026: придонеси 28 % (основица 34.570–1.106.256), личен одбиток 10.932, данок 10 %. */
C.MK={cur:'MKD',dec:2,opts:[],calc:function(g,o){
  var c=.28*Math.min(Math.max(g,34570),1106256),t=.10*Math.max(0,g-c-10932);
  return {rows:[['si',c,-1],['tax',t,-1]],net:g-c-t};
}};
/* AL — 2026: sigurime shoqërore 9,5 % (tavan 186.416), shëndetësore 1,7 %, tatim mbi bruto (0 / 13 % / 23 %). */
C.AL={cur:'ALL',opts:[],calc:function(g,o){
  var s=.095*Math.min(g,186416),h=.017*g,t=g<=50000?0:g<=60000?.13*(g-35000):g<=200000?.13*(g-30000):22100+.23*(g-200000);
  return {rows:[['ss',s,-1],['health',h,-1],['tax',t,-1]],net:g-s-h-t};
}};
/* EG — 2026: تأمينات 11 % (حد أدنى 2.700، أقصى 16.700), إعفاء شخصي 20.000/سنة, شرائح 0–27,5 %, صندوق الشهداء 0,05 %. */
C.EG={cur:'EGP',dec:2,opts:[],calc:function(g,o){
  var si=.11*Math.min(Math.max(g,2700),16700),tx=Math.max(0,12*(g-si)-20000),t=brk(tx,[[40000,0],[55000,.10],[70000,.15],[200000,.20],[400000,.225],[1200000,.25],[Infinity,.275]])/12,mf=.0005*g;
  return {rows:[['si',si,-1],['tax',t,-1],['mf',mf,-1]],net:g-si-t-mf};
}};
window.CFPay={C:C,
 fmt:function(n,cur,dec){var o={style:'currency',currency:cur,minimumFractionDigits:dec,maximumFractionDigits:dec};
  try{return new Intl.NumberFormat(document.documentElement.lang||'en',o).format(n);}catch(e){return cur+' '+n.toFixed(dec);}},
 init:function(cfg){
  var K=C[cfg.country],L=cfg.labels,$=function(i){return document.getElementById(i);};
  function run(){
    var v=+$('pcgross').value||0,per=$('pcperiod').value,o={};
    K.opts.forEach(function(id){var e=$('pcopt_'+id);o[id]=!!(e&&e.checked);});
    var pay=K.pay||12,g=per==='12'?v/pay:v,r=K.calc(g,o),f=function(n){return CFPay.fmt(n,K.cur,K.dec||0);},out=[];
    out.push(L.gross+': <strong>'+f(g)+'</strong>');
    r.rows.forEach(function(x){if(x[2]!==0&&!x[1])return;out.push(L[x[0]]+': '+(x[2]<0?'−':x[2]>0?'+':'')+f(x[1]));});
    out.push('<strong>'+L.net+': '+f(r.net)+'</strong>');
    out.push(L.netYear+': '+f(r.net*pay));
    out.push(L.eff+': '+(g>0?((1-r.net/g)*100).toLocaleString(document.documentElement.lang||'en',{minimumFractionDigits:1,maximumFractionDigits:1}):'0')+'%');
    $('pcResult').innerHTML=out.join('<br>');
  }
  ['pcgross','pcperiod'].concat(K.opts.map(function(i){return 'pcopt_'+i;})).forEach(function(i){
    var e=$(i);if(e){e.addEventListener('input',run);e.addEventListener('change',run);}});
  run();
 }};
})();
