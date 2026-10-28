from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import os

app = FastAPI(title="ANREVAZ OS v5")

ECOCASH_ONLY = os.getenv("ECOCASH_ONLY", "0772590884")
WHATSAPP_ONLY = os.getenv("WHATSAPP_ONLY", "0783788376")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "ANREVAZ_VERIFY")

# v5 MATERIALS - Full catalog
MATERIALS = [
    {"id":1,"name":"Cement - PPC 42.5N 50kg","price":12.5,"unit":"bag","stock":"142 bags","cat":"Cement"},
    {"id":2,"name":"Concrete Bricks Standard 220mm","price":0.25,"unit":"each","stock":"8,400 units","cat":"Bricks","best":True},
    {"id":3,"name":"Roofing Sheets IBR 0.45mm","price":18,"unit":"sheet","stock":"96 sheets","cat":"Roofing"},
    {"id":4,"name":"Building Sand - Washed River 1 Ton","price":12,"unit":"ton","stock":"5 loads","cat":"Sand"},
    {"id":5,"name":"Quarry Stone 19mm 1 Ton","price":15,"unit":"ton","stock":"4 loads","cat":"Aggregate"},
    {"id":6,"name":"Rebar Steel Y12 6m","price":8.5,"unit":"bar","stock":"120 bars","cat":"Steel"},
]

HTML_V5 = """
<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>ANREVAZ OS v5</title><script src='https://cdn.tailwindcss.com'></script>
<link href='https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=JetBrains+Mono:wght@700&display=swap' rel='stylesheet'>
<style>body{font-family:'Space Grotesk',sans-serif}</style></head>
<body class='bg-black text-white'>
<header class='border-b border-white/10 p-4 flex justify-between'><div class='flex gap-3 items-center'><div class='w-9 h-9 bg-[#C6FF00] text-black grid place-items-center font-bold'>A</div><div class='font-bold'>ANREVAZ OS <span class='text-[#C6FF00]'>v5</span> <span class='text-white/40 text-xs ml-2'>Harare • Frankfurt LIVE</span></div></div><a href='https://wa.me/263783788376' class='bg-[#25D366] text-black px-4 py-2 font-bold text-sm'>WA 0783788376</a></header>
<div class='p-6 md:p-10 bg-[#0f0f0f] border-b-4 border-[#C6FF00]'><h1 class='text-6xl md:text-8xl font-black leading-[0.85] tracking-tighter'>BUILD<br>FASTER<br><span class='bg-[#C6FF00] text-black px-3'>PAY ECOCASH</span></h1>
<p class='mt-4 text-white/60 max-w-xl'>Cement, bricks, roofing, sand • Instant EcoCash checkout • Harare same-day • API Live at anrevaz-code-final-1.onrender.com</p>
<div class='mt-6 flex gap-3'><div class='bg-white text-black px-4 py-2'><div class='text-[10px] opacity-50'>ECOCASH</div><div class='font-bold'>0772590884</div></div><div class='border border-white/20 px-4 py-2'><div class='text-[10px] opacity-50'>WHATSAPP</div><div class='font-bold'>0783788376</div></div></div></div>
<div class='grid md:grid-cols-3 gap-0' id='grid'></div>
<script>
const mats = %s;
document.getElementById('grid').innerHTML = mats.map(m=>`
<div class='border border-white/10 p-6 bg-[#111] hover:bg-[#161616]'><div class='flex justify-between'><span class='text-xs border px-2 py-1'>${m.cat}</span>${m.best?'<span class=\"bg-[#C6FF00] text-black text-[10px] px-2 py-1 font-bold\">BESTSELLER</span>':''}</div>
<div class='mt-8 font-bold text-xl leading-tight'>${m.name}</div><div class='text-white/40 text-xs mt-1'>${m.stock}</div>
<div class='mt-8 flex justify-between items-end'><div class='text-3xl font-black'>$${m.price}<span class='text-sm text-white/40 font-normal'>/${m.unit}</span></div>
<div class='flex gap-2'><a href='https://wa.me/263783788376?text=Hi ANREVAZ - Want ${m.name} - $${m.price}' class='bg-white text-black text-xs px-3 py-2 font-bold'>ORDER WA</a><button onclick="alert('EcoCash: 0772590884\\n${m.name}\\n$${m.price}')" class='bg-[#C6FF00] text-black text-xs px-3 py-2 font-bold'>ECOCASH</button></div></div></div>`).join('');
</script>
<div class='p-4 text-[10px] text-white/30 border-t border-white/10 flex justify-between'><span>ANREVAZ OS v5 • Harare • Frankfurt • LIVE</span><span>128 ORDERS • 12 PENDING • 1.2M ZWL</span></div>
</body></html>
""" % str(MATERIALS)

@app.get("/", response_class=HTMLResponse)
def home_v5():
    return HTML_V5

@app.get("/api/materials")
def get_materials():
    return {"materials": MATERIALS, "ecocash": ECOCASH_ONLY, "whatsapp": WHATSAPP_ONLY, "region": "Frankfurt - Central Africa", "status": "LIVE v5"}

@app.get("/api/paynow/verify")
def verify(): return {"paynow":"ready","v5":True}

@app.get("/webhook")
def verify_webhook(request: Request):
    if request.query_params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(request.query_params.get("hub.challenge",0))
    return JSONResponse({"error":"fail"},403)

@app.post("/webhook")
async def post_webhook(request: Request):
    data = await request.json()
    print(data)
    return {"status":"received"}
