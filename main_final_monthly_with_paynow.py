from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json

app = FastAPI(title="ANREVAZ OS v10 - Organized Orderly - Professional Landing - Kadoma")

# === GAZETTED SUBSCRIPTION AMOUNTS ===
SUBSCRIPTIONS = {
    "$3 Starter": {"price": 3, "features": ["1 Workspace", "5 Quotes/month", "Safe ID Pass", "Basic Materials Realtime"], "color": "gray"},
    "$7 Pro": {"price": 7, "features": ["3 Workspaces", "50 Quotes/month", "Company Logo", "All Materials Realtime", "AI Agent Follow-up"], "color": "blue", "popular": True},
    "$12 Premium Last Package": {"price": 12, "features": ["Unlimited Workspaces", "Unlimited Quotes", "Safe ID + Logo + Owner", "Every Material Realtime", "AI Agent Negotiate Till WON", "Secured Workspace No Copying", "WhatsApp Backend Offline"], "color": "yellow", "best": True},
}

# === FULL MATERIALS - EVERY MATERIAL NEEDED PER PROJECT - REALTIME PER ITEM ===
PROJECT_MATERIALS = {
    "Fitted Kitchen (3m x 3m)": {
        "items": [
            {"name": "Melamine White 18mm Board", "spec": "2440x1220mm - Base Units", "price": 85, "need": 6, "unit": "Sheets", "supplier": "BoardMart Kadoma"},
            {"name": "Melamine Grey 18mm Board", "spec": "2440x1220mm - Top Units", "price": 88, "need": 3, "unit": "Sheets", "supplier": "BoardMart"},
            {"name": "Quartz Countertop 20mm", "spec": "Black/White - 3m length", "price": 180, "need": 2, "unit": "Sheets", "supplier": "Granite Centre"},
            {"name": "Soft Close Hinges", "spec": "110 degree - Pair", "price": 3.5, "need": 20, "unit": "Each", "supplier": "Hardware"},
            {"name": "Handles Modern Chrome", "spec": "128mm - Stainless", "price": 6, "need": 12, "unit": "Each", "supplier": "Hardware"},
            {"name": "Drawer Slides 500mm", "spec": "Ball bearing - Soft close", "price": 12, "need": 8, "unit": "Pairs", "supplier": "Hardware"},
            {"name": "Edging Tape 1mm", "spec": "White - Iron on", "price": 2.5, "need": 40, "unit": "Meters", "supplier": "BoardMart"},
            {"name": "Sink Stainless Double Bowl", "spec": "860x500mm with drainer", "price": 85, "need": 1, "unit": "Each", "supplier": "PlumbMart"},
            {"name": "Tap Mixer Chrome", "spec": "Single lever - 360 swivel", "price": 45, "need": 1, "unit": "Each", "supplier": "PlumbMart"},
            {"name": "Screws & Fixings Kit", "spec": "Assorted - 500pcs", "price": 25, "need": 1, "unit": "Kit", "supplier": "Hardware"},
        ]
    },
    "Wardrobes (3-Door Sliding 2.4m)": {
        "items": [
            {"name": "Melamine White 18mm", "spec": "2440x1220 - Carcass", "price": 85, "need": 4, "unit": "Sheets", "supplier": "BoardMart"},
            {"name": "Melamine Woodgrain 18mm", "spec": "Doors - Oak/Wenge", "price": 90, "need": 2, "unit": "Sheets", "supplier": "BoardMart"},
            {"name": "Sliding Door Rails 2m", "spec": "Top + Bottom track set", "price": 35, "need": 2, "unit": "Sets", "supplier": "Hardware"},
            {"name": "Sliding Wheels Heavy Duty", "spec": "80kg capacity - 4 wheels per door", "price": 8, "need": 6, "unit": "Each", "supplier": "Hardware"},
            {"name": "Hanging Rails Chrome", "spec": "Oval 30mm x 1.2m", "price": 12, "need": 3, "unit": "Each", "supplier": "Hardware"},
            {"name": "Mirror 4mm Silver", "spec": "1220x600mm - Safety backed", "price": 35, "need": 1, "unit": "Sheet", "supplier": "Glass Centre"},
            {"name": "Handles Recessed", "spec": "Flush pull - Aluminum", "price": 5, "need": 6, "unit": "Each", "supplier": "Hardware"},
            {"name": "Edging Tape 1mm", "spec": "Woodgrain match", "price": 2.5, "need": 25, "unit": "Meters", "supplier": "BoardMart"},
            {"name": "Shelf Brackets", "spec": "200mm - White", "price": 3, "need": 8, "unit": "Each", "supplier": "Hardware"},
        ]
    },
    "Hipped Roof (100sqm)": {
        "items": [
            {"name": "Chromadek 0.5mm Charcoal", "spec": "0.5mm x 3.6m long - AZ150", "price": 18, "need": 85, "unit": "Sheets", "supplier": "SteelSuppliers Kadoma"},
            {"name": "Pine Trusses 114x38", "spec": "SA Pine - 6m length - Treated", "price": 18, "need": 24, "unit": "Lengths", "supplier": "Timber Centre"},
            {"name": "Pine Purlins 76x50", "spec": "SA Pine - 6m - For sheet fixing", "price": 12, "need": 40, "unit": "Lengths", "supplier": "Timber Centre"},
            {"name": "Ridge Capping 2m", "spec": "Charcoal - 2m long - Matching colour", "price": 15, "need": 12, "unit": "Each", "supplier": "SteelSuppliers"},
            {"name": "Hip Capping 2m", "spec": "Charcoal - For hips", "price": 14, "need": 16, "unit": "Each", "supplier": "SteelSuppliers"},
            {"name": "Valley Flashing 2m", "spec": "Charcoal - For valleys", "price": 18, "need": 8, "unit": "Each", "supplier": "SteelSuppliers"},
            {"name": "Barge Boards 225x25", "spec": "Fascia - Pine - 6m", "price": 22, "need": 8, "unit": "Each", "supplier": "Timber Centre"},
            {"name": "Fascia Boards 150x25", "spec": "Pine - 6m", "price": 20, "need": 10, "unit": "Each", "supplier": "Timber Centre"},
            {"name": "Gutters + Downpipes Set 3m", "spec": "Charcoal - Gutter 3m + Downpipe 3m + Brackets", "price": 25, "need": 10, "unit": "Sets", "supplier": "SteelSuppliers"},
            {"name": "Roof Screws 100pcs Box", "spec": "65mm - With rubber washer - Charcoal head", "price": 12, "need": 6, "unit": "Boxes", "supplier": "Hardware"},
            {"name": "Closure Strips", "spec": "Foam - For ridge - 1m", "price": 2, "need": 20, "unit": "Each", "supplier": "SteelSuppliers"},
        ]
    },
    "Gabled Roof (100sqm)": {
        "items": [
            {"name": "Chromadek 0.5mm Blue", "spec": "0.5mm x 3.6m - AZ150", "price": 18, "need": 75, "unit": "Sheets", "supplier": "SteelSuppliers"},
            {"name": "Pine Trusses 114x38", "spec": "SA Pine 6m Treated", "price": 18, "need": 20, "unit": "Lengths", "supplier": "Timber Centre"},
            {"name": "Pine Purlins 76x50", "spec": "SA Pine 6m", "price": 12, "need": 35, "unit": "Lengths", "supplier": "Timber Centre"},
            {"name": "Ridge Capping 2m", "spec": "Blue - 2m", "price": 15, "need": 10, "unit": "Each", "supplier": "SteelSuppliers"},
            {"name": "Barge Boards 225x25", "spec": "Pine 6m", "price": 22, "need": 6, "unit": "Each", "supplier": "Timber Centre"},
            {"name": "Fascia Boards 150x25", "spec": "Pine 6m", "price": 20, "need": 8, "unit": "Each", "supplier": "Timber Centre"},
            {"name": "Gutters Set 3m", "spec": "Blue - Gutter + Downpipe + Brackets", "price": 25, "need": 8, "unit": "Sets", "supplier": "SteelSuppliers"},
            {"name": "Underlay 20m Roll", "spec": "Foil + Moisture barrier", "price": 30, "need": 4, "unit": "Rolls", "supplier": "Hardware"},
            {"name": "Roof Screws 100pcs", "spec": "65mm - Blue head", "price": 12, "need": 5, "unit": "Boxes", "supplier": "Hardware"},
        ]
    },
    "Ceilings (80sqm Room)": {
        "items": [
            {"name": "Ceiling Boards 1200x600mm", "spec": "Gypsum - 9mm - White", "price": 8, "need": 65, "unit": "Boards", "supplier": "BuildMart"},
            {"name": "Brandering 38x38 Pine", "spec": "SA Pine 3.6m - Ceiling battens", "price": 8, "need": 30, "unit": "Lengths", "supplier": "Timber Centre"},
            {"name": "Cornice 3m", "spec": "75mm - Gypsum - Decorative", "price": 6, "need": 20, "unit": "Each", "supplier": "BuildMart"},
            {"name": "Ceiling Screws Box", "spec": "32mm - Sharp point - 500pcs", "price": 8, "need": 4, "unit": "Boxes", "supplier": "Hardware"},
            {"name": "Joint Tape + Compound Set", "spec": "Tape 90m + Compound 20kg", "price": 18, "need": 3, "unit": "Sets", "supplier": "BuildMart"},
            {"name": "Paint Ceiling White 20L", "spec": "PVA - White - One coat", "price": 65, "need": 2, "unit": "Tins", "supplier": "Paint Centre"},
            {"name": "Primer Ceiling 20L", "spec": "Undercoat", "price": 55, "need": 1, "unit": "Tin", "supplier": "Paint Centre"},
        ]
    },
}

def handle_whatsapp_message(phone, message):
    msg = message.lower().strip()
    if msg in ["hi", "hello", "menu", "start"]:
        return """*ANREVAZ OS v10 - ORGANIZED ORDERLY - Kadoma* ✅
_Professional Landing - Easy to Use_

*ORDERLY STEPS - Follow in Order:*

*STEP 1:* Create Safe ID Pass 🪪 - Your credentials - Encrypted
*STEP 2:* Select Trade Inline - Fitted Kitchen OR Hipped Roof etc - Private Workspace WS-XXXX created - Isolated - No copying
*STEP 3:* Add Company Logo + Details 🏢 - Makes quote professional
*STEP 4:* Select Project Inside Workspace - See EVERY material needed with realtime price per item $85 $18 $8 etc
*STEP 5:* Add Client/Owner Details 👤 - Who owns quotation
*STEP 6:* Generate Professional Quote - Logo + Safe ID + Owner + Full materials realtime
*STEP 7:* AI Agent Negotiates + Follow-up Till WON 🤖 - 0 sec,2h,24h,day3,day7
*STEP 8:* Subscribe - EcoCash 0772590884 App ONLY $3,$7,$12 - NOT client payments

*💳 ECOCASH CLARIFICATION:*
EcoCash 0772590884 = ONLY for app subscription $3,$7,$12
Client payments = Cash / Bank / Their EcoCash separate - Private

*🔒 SECURED WORKSPACE:*
Each tradesman gets workspace inline with his job only - Tightly secured - No copying skills/prices

*Reply in order:*
1 = Create Safe ID
2 = My Workspace
3 = Fitted Kitchen - Full Materials $85 $180 $3.5 etc
4 = Hipped Roof - 85 sheets $18 Full List
5 = Gabled Roof - 75 sheets
6 = Ceilings
7 = AI Agent Till WON
8 = Subscribe $3,$7,$12
9 = Client Payment Methods

*WhatsApp Link Works Even Without Internet Data:*
Open WhatsApp directly: whatsapp://send?phone=263783788376
Or https://wa.me/263783788376 - No internet data needed - Uses WhatsApp data!

*Website: anrevaz-code-final-1.onrender.com*
"""
    return f"You said: {message}\n\n" + handle_whatsapp_message(phone, "hi")

MATERIALS_JSON = json.dumps(PROJECT_MATERIALS)
SUBS_JSON = json.dumps(SUBSCRIPTIONS)

HTML_TEMPLATE = """
<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>ANREVAZ OS v10 - Organized Orderly - Professional - Kadoma</title><script src='https://cdn.tailwindcss.com'></script>
<style>.screen{display:none}.screen.active{display:block} .nav-active{background:#5b7cff!important;color:white!important} .step-done{border-color:#22c55e!important;background:rgba(34,197,94,0.1)!important} .step-active{border-color:#5b7cff!important;background:rgba(91,124,255,0.15)!important;box-shadow:0 0 20px rgba(91,124,255,0.3)}</style>
</head><body style="background:radial-gradient(130% 130% at 0% 0%, #121d4a 0%, #0a0e26 50%, #050714 100%);color:white;font-family:Inter;min-height:100vh">
<div class='max-w-[500px] mx-auto pb-28'>

<!-- TOP BANNER ORGANIZED -->
<div class='bg-gradient-to-r from-[#5b7cff]/30 to-[#22c55e]/20 border-b border-white/10 px-4 py-2 flex justify-between items-center text-[10px]'><div class='flex gap-2 items-center'><div class='w-6 h-6 rounded-lg bg-[#5b7cff] grid place-items-center font-black'>A</div><div class='font-black'>ANREVAZ OS v10 • ORGANIZED ORDERLY</div></div><div class='text-[8px] bg-black/40 px-2 py-1 rounded-full'>🔒 Secured Workspace + 🤖 AI Till WON</div></div>

<!-- SCREEN 1: PROFESSIONAL LANDING PAGE - EASY TO USE -->
<div id='screen-landing' class='screen active px-5 py-6'>
<div class='text-center'><div class='w-16 h-16 mx-auto rounded-2xl bg-gradient-to-br from-blue-400 to-indigo-600 grid place-items-center text-3xl shadow-[0_0_30px_rgba(91,124,255,0.5)]'>🅰️</div><div class='mt-3 font-black text-2xl'>ANREVAZ OS</div><div class='text-[#5b7cff] font-bold text-sm'>For Kadoma Tradesmen - Professional Quoting</div><div class='mt-2 text-[12px] text-white/60 max-w-[320px] mx-auto'>The only app that gives you Safe ID Pass, Private Workspace, Every Material Needed with Realtime Prices, Professional Quote with Logo, and AI Agent that follows up till job is WON.</div></div>

<div class='mt-6 bg-white/[0.06] border border-white/10 rounded-2xl p-4'>
<div class='font-black text-sm'>How It Works - 8 Orderly Steps - Easy to Use</div>
<div class='mt-3 space-y-2.5'>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-[#5b7cff] grid place-items-center text-xs font-black flex-shrink-0'>1</div><div><div class='font-bold text-xs'>Create Safe ID Pass 🪪</div><div class='text-[11px] text-white/50'>Your credentials - Encrypted - Proves you are real tradesman - QR Verified - ANR-KD-XXXX</div></div></div>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs font-black flex-shrink-0'>2</div><div><div class='font-bold text-xs'>Select Trade Inline - Private Workspace 🔒</div><div class='text-[11px] text-white/50'>Choose Fitted Kitchen OR Hipped Roof etc - System creates private workspace WS-XXXX inline with your job only - Tightly secured - No other tradesman can copy your skills or negotiated prices</div></div></div>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs font-black flex-shrink-0'>3</div><div><div class='font-bold text-xs'>Add Company Logo + Details 🏢</div><div class='text-[11px] text-white/50'>Upload logo, company name, address - Makes quotation look professional - Like big company</div></div></div>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs font-black flex-shrink-0'>4</div><div><div class='font-bold text-xs'>Select Project Inside Workspace - See Every Material 📦</div><div class='text-[11px] text-white/50'>Inside your private workspace, select project - System shows EVERY material needed to finish project with realtime price per item $85 $18 $8 - Clear - Per item - Includes supplier name</div></div></div>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs font-black flex-shrink-0'>5</div><div><div class='font-bold text-xs'>Add Client / Owner Details 👤</div><div class='text-[11px] text-white/50'>Client name, phone, address, project location - Owner of quotation - Clear</div></div></div>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs font-black flex-shrink-0'>6</div><div><div class='font-bold text-xs'>Generate Professional Quote 3 sec ⚡</div><div class='text-[11px] text-white/50'>Logo + Safe ID + Owner + Every material realtime per item + Total - PDF professional</div></div></div>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-[#25D366]/30 grid place-items-center text-xs font-black flex-shrink-0'>7</div><div><div class='font-bold text-xs'>AI Agent Negotiates + Follow-up Till WON 🤖</div><div class='text-[11px] text-white/50'>Built-in ChatGPT-style - If client says expensive, AI negotiates - Auto follow-up 0 sec, 2h, 24h, day 3, day 7 till job WON - Stops when WON</div></div></div>
<div class='flex gap-3'><div class='w-7 h-7 rounded-full bg-yellow-400 text-black grid place-items-center text-xs font-black flex-shrink-0'>8</div><div><div class='font-bold text-xs'>Subscribe - Gazetted Amounts $3,$7,$12 💳</div><div class='text-[11px] text-white/50'><span class='text-yellow-200 font-bold'>EcoCash 0772590884 = App subscription ONLY</span> - NOT client payments - Client pays you Cash/Bank/Their EcoCash separate - Private income - Secured</div></div></div>
</div>
<button onclick="show('register')" class='w-full mt-5 bg-[#5b7cff] py-3.5 rounded-xl font-black shadow-[0_0_20px_rgba(91,124,255,0.4)]'>Start Now - Create Safe ID Pass → Step 1</button>
<div class='mt-3 text-center text-[10px] text-white/30'>Developer: Destiny Manduna - Kadoma, Zimbabwe - WhatsApp Backend Encoded</div>
</div>

<div class='mt-5 grid grid-cols-2 gap-3'>
<a href='whatsapp://send?phone=263783788376&text=Hi%20ANREVAZ%20OS%20v10%20Organized%20Orderly' class='bg-[#25D366]/20 border border-[#25D366]/40 rounded-xl p-3 text-center block'><div class='text-xl'>💬</div><div class='font-bold text-xs mt-1'>WhatsApp - Works Without Internet Data</div><div class='text-[9px] text-white/50 mt-1'>Tap opens WhatsApp directly - No internet data needed - Uses WhatsApp bundle - 0783788376 - Same backend as website</div></a>
<div class='bg-white/5 border border-white/10 rounded-xl p-3 text-center'><div class='text-xl'>🌐</div><div class='font-bold text-xs mt-1'>Website - With Internet</div><div class='text-[9px] text-white/50 mt-1'>anrevaz-code-final-1.onrender.com - Full features - Same backend as WhatsApp</div></div>
</div>
</div>

<!-- SCREEN 2: REGISTER - STEP 1 - SAFE ID -->
<div id='screen-register' class='screen px-5 py-6'>
<div class='flex items-center gap-2'><button onclick="show('landing')" class='w-8 h-8 rounded-full bg-white/10 grid place-items-center'>←</button><div><div class='font-black'>Step 1: Create Safe ID Pass</div><div class='text-[11px] text-[#5b7cff
