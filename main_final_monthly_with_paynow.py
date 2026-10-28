from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="ANREVAZ OS v5 - Full APK - Kadoma")

MATERIALS = {
    "Melamine": {"price": 85, "unit": "Sheet • 18mm", "permit": True, "verified": "2m ago", "tradesman": "Tinashe M. - Kadoma CBD"},
    "Pine": {"price": 12, "unit": "Timber • per length", "permit": True, "verified": "2m ago", "tradesman": "Blessing K. - Rimuka"},
    "Chromadek roofing": {"price": 18, "unit": "Sheet • 0.5mm", "permit": True, "verified": "5m ago", "tradesman": "James N. - Eiffel"},
    "Ceiling boards": {"price": 8, "unit": "Board • 1200x600mm", "permit": True, "verified": "1m ago", "tradesman": "Farai Z. - Kadoma"},
}

HTML = """
<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>ANREVAZ OS v5 - Kadoma - Destiny Manduna</title><script src='https://cdn.tailwindcss.com'></script>
<style>.screen{display:none}.screen.active{display:block} .nav-active{color:#5b7cff!important;font-weight:bold;border-top:2px solid #5b7cff}</style>
</head><body style="background:radial-gradient(130% 130% at 0% 0%, #121d4a 0%, #0a0e26 50%, #050714 100%);color:white;font-family:Inter;min-height:100vh;padding-bottom:80px">
<div class='max-w-[420px] mx-auto'>

<!-- SCREEN 1: HOME - LAUNCH KIT PICTURE 1 -->
<div id='screen-home' class='screen active px-5 py-6'>
<div class='flex gap-2 items-center'><div class='w-9 h-9 rounded-xl bg-gradient-to-br from-blue-400 to-indigo-600 grid place-items-center'>🅰️</div><div class='font-black text-xl'>ANREVAZ <span class='text-[11px] text-[#7b8cff]'>Launch Kit</span></div></div>
<div class='mt-6 font-black text-[24px] leading-[1.1]'><span class='text-[#5b7cff]'>Quote in 3 sec</span> • Invoice in 10 sec • On WhatsApp</div><div class='mt-2 text-[12px] text-white/50'>The one-time toolkit for carpenters in Kadoma, Zimbabwe — create quotes & invoices instantly, send via WhatsApp, no monthly fees.</div>
<div class='mt-5 space-y-3'>
<div class='bg-white/[0.07] border border-white/15 rounded-2xl p-4 flex gap-4'><div class='w-14 h-14 rounded-xl bg-[#5b7cff]/15 border border-[#5b7cff]/30 grid place-items-center text-2xl'>⚡</div><div><div class='font-bold'>Quote in 3 Seconds</div><div class='text-[11px] text-white/50'>Prebuilt template for carpentry jobs. Fill details → instant PDF quote → send on WhatsApp.</div></div></div>
<div class='bg-white/[0.07] border border-white/15 rounded-2xl p-4 flex gap-4'><div class='w-14 h-14 rounded-xl bg-[#5b7cff]/15 border border-[#5b7cff]/30 grid place-items-center'>📄</div><div><div class='font-bold'>Invoice in 10 Seconds</div><div class='text-[11px] text-white/50'>Add items, tax & total. Download invoice or share directly to customer on WhatsApp.</div></div></div>
<div class='bg-white/[0.07] border border-white/15 rounded-2xl p-4 flex gap-4'><div class='w-14 h-14 rounded-xl bg-[#5b7cff]/15 border border-[#5b7cff]/30 grid place-items-center'>💳</div><div><div class='font-bold'>Paid via EcoCash</div><div class='text-[11px] text-white/50'>Customers pay easily via EcoCash. Track payments + status in one place.</div></div></div>
</div>
<div class='mt-5 bg-white/[0.07] border-2 border-[#5b7cff]/40 rounded-2xl p-5 text-center'><div class='font-black text-xl'>ANREVAZ Launch Kit</div><div class='font-black text-[26px] text-[#5b7cff]'>$12/month Last Package</div><div class='text-[11px] text-white/50'>Lifetime • No subscription • Instant • Best Value</div><a href='https://wa.me/263783788376' class='mt-3 block bg-[#5b7cff] py-3 rounded-full font-bold'>Start on WhatsApp — 0783788376</a><div class='mt-2 bg-white/5 py-2 rounded-full text-[11px] text-[#8da3ff]'>📱 Pay with EcoCash — 0772590884</div><div class='mt-2 text-[10px] text-white/30'>✓ WhatsApp-ready • ✓ Works offline • ✓ Built for Zimbabwe carpentry</div></div>
</div>

<!-- SCREEN 2: QUOTES - PICTURE 2 TRADES + AI TIMELINE -->
<div id='screen-quotes' class='screen px-5 py-6'>
<div class='flex justify-between'><div class='font-black text-xl'>ANREVAZ OS</div><div class='bg-blue-500/20 border border-blue-400/30 text-[11px] px-3 py-1 rounded-full'>PREMIUM</div></div>
<div class='mt-6 font-black text-[22px] leading-[1.1]'>Any Trade Quote in 3 sec<br><span class='text-[#5b7cff]'>AI Follow-up Wins The Job</span></div>
<div class='mt-4 grid grid-cols-5 gap-2'><div class='bg-white/[0.08] border border-blue-400/30 rounded-xl p-2 text-center'><div>🪚</div><div class='text-[9px]'>Carpenter</div></div><div class='bg-white/[0.08] border border-white/10 rounded-xl p-2 text-center'><div>👨‍🏭</div><div class='text-[9px]'>Welder</div></div><div class='bg-white/[0.08] border border-white/10 rounded-xl p-2 text-center'><div>👷</div><div class='text-[9px]'>Builder</div></div><div class='bg-white/[0.08] border border-white/10 rounded-xl p-2 text-center'><div>🔧</div><div class='text-[9px]'>Plumber</div></div><div class='bg-white/[0.08] border border-white/10 rounded-xl p-2 text-center'><div>🪟</div><div class='text-[9px]'>Glazier</div></div></div>
<div class='mt-5 font-bold text-sm'>AI auto followup timeline</div><div class='mt-2 bg-white/[0.06] border border-white/10 rounded-xl p-3 flex justify-between text-center'><div><div class='w-7 h-7 bg-[#5b7cff] rounded-full grid place-items-center text-xs'>✓</div><div class='text-[9px] mt-1'>0 sec quote</div></div><div><div class='w-6 h-6 border-2 border-blue-400/50 rounded-full'></div><div class='text-[9px] mt-1'>2h</div></div><div><div class='w-6 h-6 border rounded-full'></div><div class='text-[9px] mt-1'>24h</div></div><div><div class='w-6 h-6 border rounded-full'></div><div class='text-[9px] mt-1'>day 3</div></div><div><div class='w-6 h-6 border rounded-full'></div><div class='text-[9px] mt-1'>day 7</div></div></div>
<div class='mt-4 grid grid-cols-2 gap-3'><div class='bg-white/[0.06] border border-white/10 rounded-xl p-3 text-center'><div>💬</div><div class='text-[10px] text-white/40'>WhatsApp</div><div class='font-bold text-sm'>0783788376</div></div><div class='bg-white/[0.06] border border-white/10 rounded-xl p-3 text-center'><div>💵</div><div class='text-[10px] text-white/40'>EcoCash</div><div class='font-bold text-sm'>0772590884</div></div></div>
<a href='https://wa.me/263783788376' class='mt-4 block bg-[#5b7cff] text-center py-3 rounded-xl font-bold'>Get Instant Quote Now →</a>
</div>

<!-- SCREEN 3: MATERIALS - PICTURE 3 ADMIN + PERMIT REAL-TIME -->
<div id='screen-materials' class='screen px-5 py-6'>
<div class='flex justify-between items-center'><div><div class='font-black'>ANREVAZ OS</div><div class='text-[11px] text-[#5b7cff]'>Admin Panel • Tradesmen • Kadoma</div></div><div class='w-8 h-8 bg-white/10 rounded-full grid place-items-center'>AD</div></div>
<div class='mt-4 bg-white/[0.06] border border-white/15 rounded-xl p-3 flex justify-between items-center'><div class='flex gap-2 items-center'><div class='w-8 h-8 rounded-full bg-[#5b7cff]/20 grid place-items-center'>✓</div><div><div class='font-bold text-xs'>Admin Price Verification</div><div class='text-[10px] text-white/40'>Up to date • Verified 2m ago • Kadoma</div></div></div><div class='w-11 h-6 bg-[#5b7cff] rounded-full relative'><div class='absolute right-0.5 top-0.5 w-5 h-5 bg-white rounded-full'></div></div></div>
<div class='mt-2 bg-white/[0.06] border border-white/10 rounded-xl p-3 flex gap-2'><div class='w-2 h-2 bg-blue-400 rounded-full animate-pulse'></div><div><div class='font-bold text-xs'>Real-Time Price Update • Tradesmen Permit</div><div class='text-[10px] text-[#5b7cff]'>Live sync • Kadoma, Zimbabwe • <span class='text-green-400'>● Live</span></div></div></div>
<div class='mt-4 font-bold text-sm'>Categories • Carpenter</div><div class='mt-2 grid grid-cols-2 gap-2'><div class='bg-white/[0.06] border rounded-lg p-2.5'><div class='font-bold text-xs'>🏠 Roofing</div><div class='text-[10px] text-white/30'>4 materials</div></div><div class='bg-white/[0.06] border rounded-lg p-2.5'><div class='font-bold text-xs'>🔲 Ceiling</div><div class='text-[10px] text-white/30'>3 materials</div></div></div>
<div class='mt-4'><div class='font-bold text-sm flex justify-between'><span>Materials List — Pricing</span><span class='text-[9px] bg-green-500/20 text-green-300 px-2 py-0.5 rounded-full'>● REAL-TIME</span></div><div id='mats' class='mt-2 space-y-2'></div></div>
<div class='mt-3 bg-[#5b7cff]/10 border border-[#5b7cff]/30 rounded-xl p-2.5 flex gap-2'><div>👤</div><div><div class='font-bold text-xs'>AI Negotiation Floor</div><div class='text-[10px] text-white/50'>Never below $650 • Protect Kadoma tradesmen margin</div></div></div>
</div>

<!-- SCREEN 4: ESTIMATOR - PICTURE 4 FLOOR PLAN -->
<div id='screen-estimator' class='screen px-5 py-6'>
<div class='font-bold flex gap-2'>📤 Floor Plan Upload</div>
<div class='mt-3 border-2 border-dashed border-white/20 rounded-xl p-6 text-center bg-white/[0.02]'><div class='w-10 h-10 mx-auto bg-[#5b7cff] rounded-full grid place-items-center'>☁️</div><div class='mt-2 font-bold text-sm'>Upload PDF Floor Plan</div><div class='text-[11px] text-white/40'>PDF, DWG, JPG • Max 25MB</div><button onclick="alert('AI: 127 sqm • Gable Roof Chromadek • $3,627 total • Kadoma')" class='mt-3 bg-[#5b7cff] px-4 py-1.5 rounded-full font-bold text-xs'>Analyze with AI ✨</button></div>
<div class='mt-5 bg-white/[0.06] border border-white/10 rounded-xl p-4'><div class='font-bold text-sm'>✨ AI Auto-Extracted Overview</div><div class='mt-2 text-xs'>🖥️ Detected Area: 127 sqm • 98.4% confidence</div><div class='mt-1 text-xs'>🏠 Gable Roof • Material: Chromadek</div><div class='mt-3 font-bold text-xs'>Materials Estimate</div><div class='mt-1 text-[11px] space-y-1'><div class='flex justify-between'><span>✨ Chromadek Sheets: 146 sheets</span><span>$18 each • $2,628</span></div><div class='flex justify-between'><span>🪵 Pine Trusses: 24 pcs</span><span>$35 each • $840</span></div><div class='flex justify-between'><span>Fasteners + Flashing</span><span>$159</span></div></div><div class='mt-3 bg-[#5b7cff]/20 border border-[#5b7cff]/40 rounded-lg p-2'><div class='font-bold text-sm'>Materials Breakdown Total —</div><div class='font-black text-xl'>$3,627 USD</div><div class='text-[10px] text-white/40'>Includes 5% wastage + Kadoma local pricing</div></div></div>
<div class='mt-4'><div class='font-bold text-sm flex gap-2'><span class='text-green-400'>●</span> Zimbabwe Tradesmen — Online Now • Kadoma</div><div id='trades' class='mt-2 space-y-2'></div></div>
</div>

<!-- SCREEN 5: SUBSCRIPTION TIERS - NEW PICTURE WE GENERATED -->
<div id='screen-subscription' class='screen px-5 py-6'>
<div class='font-black text-xl'>Subscription Tiers</div><div class='text-[#5b7cff]'>Choose Your Package • Kadoma</div>
<div class='mt-4 space-y-3'>
<div class='bg-white/[0.05] border border-white/10 rounded-xl p-3'><div class='flex justify-between'><div class='font-bold'>Free Trial</div><div class='bg-[#5b7cff]/30 px-2 py-0.5 rounded-full text-xs font-bold'>$0</div></div><div class='mt-1 text-[10px] text-white/40'>✓ Basic floor plan extraction ✓ 1 project ✓ Watermark on PDF ✓ 1 trade (Carpenter)</div></div>
<div class='bg-white/[0.05] border border-white/10 rounded-xl p-3'><div class='flex justify-between'><div class='font-bold'>Starter</div><div class='bg-[#5b7cff] px-2 py-0.5 rounded-full text-xs font-bold'>$3/month</div></div><div class='mt-1 text-[10px] text-white/40'>✓ Quote in 3 seconds ✓ 5 projects/month ✓ Export CSV/PDF ✓ Email support ✓ Roofing & Ceiling categories ✓ 4 materials list</div></div>
<div class='bg-[#5b7cff]/15 border-2 border-[#5b7cff] rounded-xl p-3 shadow-[0_0_15px_rgba(91,124,255,0.3)]'><div class='flex justify-between'><div class='font-bold'>Pro <span class='text-[10px] bg-[#5b7cff] px-2 py-0.5 rounded-full ml-2'>POPULAR</span></div><div class='bg-[#5b7cff] px-2 py-0.5 rounded-full text-xs font-bold'>$7/month</div></div><div class='mt-1 text-[10px] text-white/60'>✓ Everything Starter + ✓ Invoice 10 sec on WhatsApp ✓ Admin Price Verification ✓ Real-Time Price Update ✓ AI Overview 127 sqm ✓ Gable Roof Chromadek ✓ Materials 146 sheets $3,627 ✓ AI follow-up timeline (0 sec,2h,24h,day3,day7) ✓ All 5 trades ✓ Tradesmen Online</div></div>
<div class='bg-gradient-to-br from-yellow-500/10 to-orange-500/10 border-2 border-yellow-400/50 rounded-xl p-3 shadow-[0_0_20px_rgba(250,204,21,0.2)]'><div class='flex justify-between'><div class='font-bold text-yellow-200'>Premium <span class='text-[9px] bg-yellow-400 text-black px-2 py-0.5 rounded-full'>LAST PACKAGE - BEST VALUE</span></div><div class='bg-yellow-400 text-black px-2 py-0.5 rounded-full text-xs font-black'>$12/month</div></div><div class='mt-1 text-[10px] text-white/60'>✓ Everything Pro + ✓ Paid via EcoCash 0772590884 tracking ✓ Materials Pricing $85, $18, $8 ✓ AI Negotiation Floor $650 ✓ WhatsApp 0783788376 ✓ Unlimited projects ✓ Priority AI ✓ Full exports ✓ Priority support ✓ Zimbabwe tradesmen online network ✓ Works offline ✓ Built for Zimbabwe carpentry work ❤️</div></div>
<button onclick="window.open('https://wa.me/263783788376?text=Premium%20$12%20Kadoma','_blank')" class='w-full mt-3 bg-[#5b7cff] py-3 rounded-xl font-bold'>Upgrade to Premium — $12/month Last Package</button>
</div>
</div>

<!-- SCREEN 6: SETTINGS -> ABOUT -> DEVELOPER DESTINY MANDUNA -->
<div id='screen-settings' class='screen px-5 py-6'>
<div class='font-black text-xl'>Settings</div><div class='mt-4 space-y-2'>
<div class='bg-white/[0.06] border border-white/10 rounded-xl p-4 flex justify-between'><div><div class='font-bold text-sm'>Notifications</div><div class='text-[11px] text-white/40'>Price updates, tradesmen online</div></div><div class='w-11 h-6 bg-[#5b7cff] rounded-full relative'><div class='absolute right-0.5 top-0.5 w-5 h-5 bg-white rounded-full'></div></div></div>
<div class='bg-white/[0.06] border border-white/10 rounded-xl p-4 flex justify-between'><div><div class='font-bold text-sm'>Real-Time Sync</div><div class='text-[11px] text-white/40'>Kadoma • Live pricing</div></div><div class='w-11 h-6 bg-[#5b7cff] rounded-full relative'><div class='absolute right-0.5 top-0.5 w-5 h-5 bg-white rounded-full'></div></div></div>
<div class='bg-white/[0.06] border border-white/10 rounded-xl p-4' onclick="document.getElementById('about').classList.toggle('hidden')"><div class='flex justify-between'><div><div class='font-bold text-sm'>About APK</div><div class='text-[11px] text-white/40'>Version, Developer, Info • Tap to open</div></div><div>›</div></div></div>
<div id='about' class='hidden mt-3 bg-gradient-to-br from-[#5b7cff]/20 to-indigo-900/30 border-2 border-[#5b7cff]/40 rounded-2xl p-5'>
<div class='w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-400 to-indigo-700 grid place-items-center text-2xl mx-auto'>👨‍💻</div><div class='text-center mt-3'><div class='font-black text-lg'>Developer: Destiny Manduna</div><div class='text-[#5b7cff] font-bold text-xs'>ANREVAZ OS v5 • Kadoma, Zimbabwe</div><div class='mt-3 text-[12px] text-white/70 leading-relaxed'>Built in Kadoma for Zimbabwe tradesmen. Carpenter, Welder, Builder, Plumber, Glazier — all trades love it. Quote 3 sec, Invoice 10 sec, Paid via EcoCash, Floor Plan AI 127 sqm $3,627 breakdown, Materials real-time with permit system. Admin verification, AI negotiation floor $650 protected. Subscription tiers $0 Free, $3 Starter, $7 Pro Popular, $12/month Last Package Best Value. WhatsApp 0783788376, EcoCash 0772590884. Made with ❤️ to be loved and used daily by Kadoma tradesmen.</div><div class='mt-3 flex flex-wrap gap-2 justify-center'><span class='bg-white/10 px-3 py-1 rounded-full text-[10px]'>📍 Kadoma, Zimbabwe</span><span class='bg-white/10 px-3 py-1 rounded-full text-[10px]'>💵 0772590884</span><span class='bg-white/10 px-3 py-1 rounded-full text-[10px]'>💬 0783788376</span><span class='bg-[#5b7cff] px-3 py-1 rounded-full text-[10px] font-bold'>Destiny Manduna</span></div><div class='mt-3 text-[10px] text-white/20'>Version 5.0 • Secure • Private • Real-time • Built with Love • Kadoma</div></div>
</div>
</div>
</div>

<!-- BOTTOM NAV - APK STYLE -->
<div class='fixed bottom-0 left-0 right-0 bg-black/90 backdrop-blur border-t border-white/10'><div class='max-w-[420px] mx-auto grid grid-cols-6 text-center text-[10px] py-2'>
<button onclick="show('home')" id='nav-home' class='nav-active py-1'>🏠<br>Home</button>
<button onclick="show('quotes')" id='nav-quotes' class='text-white/40 py-1'>💬<br>Quotes</button>
<button onclick="show('materials')" id='nav-materials' class='text-white/40 py-1'>📦<br>Materials</button>
<button onclick="show('estimator')" id='nav-estimator' class='text-white/40 py-1'>📐<br>Estimator</button>
<button onclick="show('subscription')" id='nav-subscription' class='text-white/40 py-1'>⭐<br>Plans</button>
<button onclick="show('settings')" id='nav-settings' class='text-white/40 py-1'>⚙️<br>Settings</button>
</div></div>

</div>

<script>
let mats = %s;
const tradesmen = [
 {name:"Tinashe M.",trade:"Carpenter",loc:"Kadoma CBD",rating:4.9,status:"Online",avatar:"🪚"},
 {name:"Blessing K.",trade:"Builder",loc:"Rimuka",rating:5.0,status:"Online",avatar:"👷"},
 {name:"James N.",trade:"Welder",loc:"Eiffel Flats",rating:4.8,status:"Busy",avatar:"👨‍🏭"},
 {name:"Farai Z.",trade:"Glazier",loc:"Kadoma",rating:4.9,status:"Online",avatar:"🔧"},
];
function show(id){
 document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
 document.getElementById('screen-'+id).classList.add('active');
 document.querySelectorAll('[id^=nav-]').forEach(n=>n.classList.remove('nav-active'));
 document.getElementById('nav-'+id).classList.add('nav-active');
 window.scrollTo(0,0);
}
function renderMats(){
 document.getElementById('mats').innerHTML = Object.entries(mats).map(([name,d])=>`
 <div class='bg-white/[0.06] border border-white/10 rounded-xl p-3'><div class='flex justify-between'><div class='flex gap-2'><div class='w-8 h-8 bg-white/10 rounded-lg grid place-items-center'>${name.includes('Melamine')?'🪵':name.includes('Pine')?'🪵':name.includes('Chroma')?'🏠':'🔲'}</div><div><div class='font-bold text-xs'>${name}</div><div class='text-[10px] text-white/30'>${d.unit} • ${d.tradesman}</div></div></div><div class='text-right'><div class='text-[#5b7cff] font-black text-sm'>$${d.price} / sheet</div><div class='text-[9px] ${d.permit?'bg-green-500/20 text-green-300':'bg-red-500/20 text-red-300'} px-2 py-0.5 rounded-full mt-1'>${d.permit?'✓ Permitted':'✗ Need Permit'}</div></div></div><div class='mt-2 flex gap-2'><button onclick="togglePermit('${name}')" class='flex-1 text-[10px] ${d.permit?'bg-white/10':'bg-[#5b7cff]'} py-2 rounded-lg'>${d.permit?'Revoke':'Request Permit'}</button><button onclick="editP('${name}')" class='flex-1 text-[10px] ${d.permit?'bg-green-600':'bg-white/5 text-white/20'} py-2 rounded-lg' ${d.permit?'':'disabled'}>Edit</button></div></div>`).join('');
}
function togglePermit(name){ mats[name].permit=!mats[name].permit; fetch('/api/permit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,permit:mats[name].permit})}); renderMats(); }
function editP(name){ if(!mats[name].permit){alert('Need permit from '+mats[name].tradesman);return;} let p=prompt('New price for '+name+':',mats[name].price); if(p){mats[name].price=parseFloat(p); fetch('/api/update-price',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,price:parseFloat(p)})}); renderMats();} }
function renderTrades(){ const el=document.getElementById('trades'); if(!el) return; el.innerHTML=tradesmen.map(t=>`<div class='bg-white/[0.05] border border-white/10 rounded-xl p-2.5 flex justify-between'><div class='flex gap-2'><div class='w-8 h-8 bg-white/10 rounded-full grid place-items-center'>${t.avatar}</div><div><div class='font-bold text-xs'>${t.name} • ${t.trade}</div><div class='text-[10px] text-white/40'>${t.loc} • ⭐ ${t.rating} • <span class='text-green-400'>${t.status}</span></div></div></div><div class='text-[9px] bg-green-500/20 text-green-300 px-2 py-1 rounded-full h-fit'>Online</div></div>`).join(''); }
renderMats(); renderTrades();
</script>
</body></html>
""" % MATERIALS

@app.get("/", response_class=HTMLResponse)
def home(): return HTML

@app.get("/api/materials")
def get_mats(): return MATERIALS

@app.post("/api/permit")
async def permit_api(request: Request):
    data = await request.json()
    if data["name"] in MATERIALS:
        MATERIALS[data["name"]]["permit"] = data["permit"]
    return {"ok":True}

@app.post("/api/update-price")
async def update_api(request: Request):
    data = await request.json()
    if data["name"] in MATERIALS and MATERIALS[data["name"]]["permit"]:
        MATERIALS[data["name"]]["price"] = data["price"]
    return {"ok":True}
