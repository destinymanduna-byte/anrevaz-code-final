from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json

app = FastAPI(title="ANREVAZ OS v10.1 - Fixed - Organized Orderly")

SUBSCRIPTIONS = {
    "$3 Starter": {"price": 3, "features": ["1 Workspace", "5 Quotes/month", "Safe ID Pass", "Basic Materials Realtime"]},
    "$7 Pro": {"price": 7, "features": ["3 Workspaces", "50 Quotes/month", "Company Logo", "All Materials Realtime", "AI Agent Follow-up"], "popular": True},
    "$12 Premium Last Package": {"price": 12, "features": ["Unlimited Workspaces", "Unlimited Quotes", "Safe ID + Logo + Owner", "Every Material Realtime", "AI Agent Till WON", "Secured Workspace No Copying", "WhatsApp Backend Offline"], "best": True},
}

PROJECT_MATERIALS = {
    "Fitted Kitchen (3m x 3m)": {"items": [{"name": "Melamine White 18mm Board", "spec": "2440x1220 Base", "price": 85, "need": 6, "unit": "Sheets", "supplier": "BoardMart"}, {"name": "Quartz Countertop 20mm", "spec": "3m length", "price": 180, "need": 2, "unit": "Sheets", "supplier": "Granite Centre"}, {"name": "Soft Close Hinges", "spec": "110 degree Pair", "price": 3.5, "need": 20, "unit": "Each", "supplier": "Hardware"}, {"name": "Handles Chrome", "spec": "128mm", "price": 6, "need": 12, "unit": "Each", "supplier": "Hardware"}, {"name": "Sink Double Bowl", "spec": "860x500mm", "price": 85, "need": 1, "unit": "Each", "supplier": "PlumbMart"}, {"name": "Tap Mixer", "spec": "360 swivel", "price": 45, "need": 1, "unit": "Each", "supplier": "PlumbMart"}]},
    "Wardrobes (3-Door)": {"items": [{"name": "Melamine White 18mm", "spec": "Carcass", "price": 85, "need": 4, "unit": "Sheets", "supplier": "BoardMart"}, {"name": "Melamine Woodgrain", "spec": "Doors Oak", "price": 90, "need": 2, "unit": "Sheets", "supplier": "BoardMart"}, {"name": "Sliding Rails 2m", "spec": "Top+Bottom set", "price": 35, "need": 2, "unit": "Sets", "supplier": "Hardware"}, {"name": "Mirror 4mm", "spec": "1220x600 Safety", "price": 35, "need": 1, "unit": "Sheet", "supplier": "Glass Centre"}]},
    "Hipped Roof (100sqm)": {"items": [{"name": "Chromadek 0.5mm Charcoal", "spec": "3.6m AZ150", "price": 18, "need": 85, "unit": "Sheets", "supplier": "SteelSuppliers"}, {"name": "Pine Trusses 114x38", "spec": "6m Treated", "price": 18, "need": 24, "unit": "Lengths", "supplier": "Timber"}, {"name": "Hip Capping 2m", "spec": "Charcoal For hips", "price": 14, "need": 16, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Valley Flashing 2m", "spec": "Charcoal For valleys", "price": 18, "need": 8, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Ridge Capping 2m", "spec": "Charcoal 2m", "price": 15, "need": 12, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Gutters Set 3m", "spec": "Gutter+Downpipe+Brackets", "price": 25, "need": 10, "unit": "Sets", "supplier": "SteelSuppliers"}]},
    "Gabled Roof (100sqm)": {"items": [{"name": "Chromadek 0.5mm Blue", "spec": "3.6m AZ150", "price": 18, "need": 75, "unit": "Sheets", "supplier": "SteelSuppliers"}, {"name": "Pine Trusses 114x38", "spec": "6m Treated", "price": 18, "need": 20, "unit": "Lengths", "supplier": "Timber"}, {"name": "Ridge Capping 2m", "spec": "Blue 2m", "price": 15, "need": 10, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Gutters Set 3m", "spec": "Blue", "price": 25, "need": 8, "unit": "Sets", "supplier": "SteelSuppliers"}]},
    "Ceilings (80sqm)": {"items": [{"name": "Ceiling Boards 1200x600mm", "spec": "Gypsum 9mm White", "price": 8, "need": 65, "unit": "Boards", "supplier": "BuildMart"}, {"name": "Brandering 38x38 Pine", "spec": "3.6m battens", "price": 8, "need": 30, "unit": "Lengths", "supplier": "Timber"}, {"name": "Cornice 3m", "spec": "75mm Gypsum", "price": 6, "need": 20, "unit": "Each", "supplier": "BuildMart"}, {"name": "Paint White 20L", "spec": "PVA One coat", "price": 65, "need": 2, "unit": "Tins", "supplier": "Paint Centre"}]},
}

def handle_whatsapp_message(phone, message):
    msg = message.lower().strip()
    if msg in ["hi", "hello", "menu", "start"]:
        return "ANREVAZ OS v10.1 ORGANIZED ORDERLY - Kadoma\n\nORDERLY STEPS:\n1 Safe ID Pass\n2 Private Workspace WS-XXXX Inline Job Only - Secured No Copying\n3 Company Logo\n4 Project Inside Workspace - Every Material Per Item $85 $18 $8 Realtime\n5 Client Owner\n6 Pro Quote Logo+ID+Owner+Materials\n7 AI Agent Negotiate Till WON 0 sec,2h,24h,day3,day7\n8 Subscribe EcoCash 0772590884 App ONLY $3,$7,$12 NOT client payments\n\nECOCASH: 0772590884 = App Sub ONLY\nClient payments = Cash/Bank/Their EcoCash separate\n\nWhatsApp Links Work Without Internet Data:\nwhatsapp://send?phone=263783788376\nhttps://wa.me/263783788376\n\nWebsite: anrevaz-code-final-1.onrender.com"
    if "expensive" in msg:
        return "AI Agent Negotiation: Realtime $85 Melamine $18 Chromadek. Options: 1 Labour 30->20% Save $120, 2 Alternative Save $85, 3 50% deposit+50% completion. Reply 1,2,3 - Follow-up till WON!"
    if "follow" in msg:
        return "AI Timeline Till WON:\n0 sec Quote sent\n2h Reviewed?\n24h Free transport $30 off\nDay3 Prices rising\nDay7 10% off\nWON Job confirmed! Invoice sent!"
    if "won" in msg:
        return "JOB WON! AI Success! Client confirmed! AI stopped! Invoice sent! Deposit Cash/Bank NOT via app EcoCash! Job scheduled!"
    return "ANREVAZ AI Ready - Say hi, kitchen, hipped, gabled, workspace, subscribe, my prices, client payment, too expensive, follow up, won - Backend encoded /whatsapp"

MATS_JSON = json.dumps(PROJECT_MATERIALS)
SUBS_JSON = json.dumps(SUBSCRIPTIONS)

HTML_PAGE = '''
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ANREVAZ OS v10.1 Organized</title><script src="https://cdn.tailwindcss.com"></script>
<style>.screen{display:none}.screen.active{display:block}.nav-active{background:#5b7cff!important;color:white!important}.step-active{border-color:#5b7cff!important;background:rgba(91,124,255,0.15)!important}</style>
</head><body style="background:radial-gradient(130% 130% at 0% 0%, #121d4a 0%, #0a0e26 50%, #050714 100%);color:white;font-family:Inter;min-height:100vh">
<div class="max-w-[500px] mx-auto pb-28">

<div class="bg-gradient-to-r from-[#5b7cff]/30 to-[#22c55e]/20 border-b border-white/10 px-4 py-2 flex justify-between items-center text-[10px]"><div class="flex gap-2 items-center"><div class="w-6 h-6 rounded-lg bg-[#5b7cff] grid place-items-center font-black">A</div><div class="font-black">ANREVAZ OS v10.1 ORGANIZED ORDERLY</div></div><div class="text-[8px] bg-black/40 px-2 py-1 rounded-full">Secured + AI Till WON</div></div>

<div id="screen-landing" class="screen active px-5 py-6">
<div class="text-center"><div class="w-16 h-16 mx-auto rounded-2xl bg-gradient-to-br from-blue-400 to-indigo-600 grid place-items-center text-3xl">A</div><div class="mt-3 font-black text-2xl">ANREVAZ OS</div><div class="text-[#5b7cff] font-bold text-sm">Professional Quoting - Kadoma</div><div class="mt-2 text-[12px] text-white/60 max-w-[320px] mx-auto">Safe ID + Private Workspace + Every Material Per Item Realtime + Pro Quote + AI Till WON - Organized Orderly - Easy to Use</div></div>

<div class="mt-6 bg-white/[0.06] border border-white/10 rounded-2xl p-4">
<div class="font-black text-sm">How It Works - 8 Orderly Steps</div>
<div class="mt-3 space-y-2.5">
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-[#5b7cff] grid place-items-center text-xs font-black">1</div><div><div class="font-bold text-xs">Create Safe ID Pass</div><div class="text-[11px] text-white/50">Encrypted - QR Verified ANR-KD - Proves real tradesman</div></div></div>
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs">2</div><div><div class="font-bold text-xs">Private Workspace Inline Job Only</div><div class="text-[11px] text-white/50">WS-XXXX created inline with job only - Isolated - No copying skills/prices - Tightly secured</div></div></div>
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs">3</div><div><div class="font-bold text-xs">Company Logo + Details</div><div class="text-[11px] text-white/50">Logo on quote = professional</div></div></div>
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs">4</div><div><div class="font-bold text-xs">Select Project Inside Workspace - Every Material Per Item</div><div class="text-[11px] text-white/50">Inside WS-XXXX see table: Material Name + Spec | Qty+Unit | Price Per Item Realtime $85 $18 | Total = Qty x Price | Supplier - Every material needed - Clear orderly</div></div></div>
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs">5</div><div><div class="font-bold text-xs">Client/Owner Details</div><div class="text-[11px] text-white/50">Who owns quotation</div></div></div>
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-white/10 grid place-items-center text-xs">6</div><div><div class="font-bold text-xs">Generate Pro Quote 3 sec</div><div class="text-[11px] text-white/50">Logo+Safe ID+Owner+Full materials per item realtime</div></div></div>
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-[#25D366]/30 grid place-items-center text-xs">7</div><div><div class="font-bold text-xs">AI Agent Till WON</div><div class="text-[11px] text-white/50">Negotiates + Follow-up 0 sec,2h,24h,day3,day7 till WON</div></div></div>
<div class="flex gap-3"><div class="w-7 h-7 rounded-full bg-yellow-400 text-black grid place-items-center text-xs font-black">8</div><div><div class="font-bold text-xs">Subscribe Gazetted $3,$7,$12</div><div class="text-[11px] text-white/50">EcoCash 0772590884 = App Sub ONLY - NOT client payments - Client pays Cash/Bank separate</div></div></div>
</div>
<button onclick="showScreen('register')" class="w-full mt-5 bg-[#5b7cff] py-3.5 rounded-xl font-black">Start Now - Create Safe ID → Step 1</button>
</div>

<div class="mt-4 grid grid-cols-2 gap-3">
<a href="whatsapp://send?phone=263783788376&text=Hi%20ANREVAZ%20OS%20v10%20Organized" class="bg-[#25D366]/20 border border-[#25D366]/40 rounded-xl p-3 text-center block"><div class="text-xl">💬</div><div class="font-bold text-xs mt-1">WhatsApp - Works Without Internet Data</div><div class="text-[9px] text-white/50 mt-1">Tap opens WhatsApp directly - whatsapp://send?phone=263783788376 - No internet data needed - Uses WhatsApp bundle - Same backend</div></a>
<a href="https://wa.me/263783788376?text=Hi%20ANREVAZ%20OS%20v10%20Organized" class="bg-white/5 border border-white/10 rounded-xl p-3 text-center block"><div class="text-xl">🌐</div><div class="font-bold text-xs mt-1">Alternative: wa.me/263783788376</div><div class="text-[9px] text-white/50 mt-1">Works with WhatsApp Data Bundle - https://wa.me/263783788376</div></a>
</div>
</div>

<div id="screen-register" class="screen px-5 py-6">
<div class="flex gap-2 items-center"><button onclick="showScreen('landing')" class="w-8 h-8 rounded-full bg-white/10 grid place-items-center">←</button><div><div class="font-black">Step 1: Safe ID Pass</div><div class="text-[11px] text-[#5b7cff]">Encrypted • QR Verified • ANR-KD</div></div></div>
<div class="mt-5 bg-white/[0.06] border border-[#5b7cff]/30 rounded-2xl p-4 step-active">
<div class="font-bold text-sm">Your Credentials - Safe</div>
<div class="mt-3 space-y-3">
<input id="tName" placeholder="Full Name - Tinashe Moyo" class="w-full px-4 py-3 rounded-xl text-sm text-black">
<select id="tTradeMain" class="w-full px-4 py-3 rounded-xl text-sm text-black"><option>Carpenter - Fitted Kitchens</option><option>Carpenter - Wardrobes</option><option>Carpenter - Hipped Roof</option><option>Carpenter - Gabled Roof</option><option>Carpenter - Ceilings</option><option>Builder</option><option>Welder</option><option>Plumber</option><option>Electrician</option><option>Painter</option><option>Tiler</option></select>
<input id="tPhone" placeholder="Phone 0772590884" class="w-full px-4 py-3 rounded-xl text-sm text-black">
<input id="tLocation" placeholder="Location Kadoma CBD" class="w-full px-4 py-3 rounded-xl text-sm text-black">
<input id="tYears" type="number" placeholder="Years Experience 8" class="w-full px-4 py-3 rounded-xl text-sm text-black">
<input id="tPhoto" type="file" accept="image/*" class="w-full text-[10px] text-white/50">
<div class="bg-green-500/10 border border-green-400/20 rounded-xl p-2 text-[11px] text-green-300">Encrypted, safe, QR Verified - Tightly secured</div>
<button onclick="createID()" class="w-full bg-[#5b7cff] py-3 rounded-xl font-bold">Create Safe ID + Private Workspace → Step 2</button>
</div>
</div>
</div>

<div id="screen-workspace" class="screen px-5 py-6">
<div class="flex gap-2 items-center"><button onclick="showScreen('register')" class="w-8 h-8 rounded-full bg-white/10">←</button><div><div class="font-black">Step 2-3: Private Workspace + Company Logo</div><div class="text-[11px] text-green-300">Isolated • No Copying • Tightly Secured</div></div></div>
<div id="idCard
