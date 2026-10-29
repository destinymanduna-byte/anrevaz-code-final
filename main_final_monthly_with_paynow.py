from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json

app = FastAPI(title="ANREVAZ SUPERSONIC QUOTE v12.2 Kai AI Fixed Line 75")

SUBS = {
    "$3 Starter": {"price": 3, "features": ["1 Workspace WS-XXXX Private", "5 Quotes", "Safe ID Pass QR Verified", "Basic Materials Realtime", "WhatsApp Backend"]},
    "$7 Pro": {"price": 7, "features": ["3 Workspaces", "50 Quotes", "Company Logo", "All Materials Per Unit", "Kai AI Follow-up Till WON", "Invoice 10 sec", "Permit System", "Online Status Web Only"], "popular": True},
    "$12 Premium": {"price": 12, "features": ["Unlimited Workspaces", "Unlimited Quotes", "Safe ID + Logo + Owner Full Profile", "Every Material Per Unit Editable", "Add/Remove Left/Excess", "Manual Adjustable Prices", "Kai AI $650 Floor Till WON", "Secured No Copying", "Online Artisans Web Only", "Floor Plan 80sqm 127sqm 150sqm $3627", "Builder Plumber Electrician Full", "WhatsApp No Data + PayNow + EcoCash App Only"], "best": True},
}

MATS = {
    "Fitted Kitchen (3m x 3m)": {"icon": "Carpenter", "items": [{"name": "Melamine White 18mm", "spec": "2440x1220 Base", "price": 85, "need": 6, "unit": "Sheets", "supplier": "BoardMart"}, {"name": "Quartz 20mm", "spec": "3m length", "price": 180, "need": 2, "unit": "Sheets", "supplier": "Granite"}, {"name": "Sink Double", "spec": "860x500mm", "price": 85, "need": 1, "unit": "Each", "supplier": "PlumbMart"}]},
    "Hipped Roof (100sqm)": {"icon": "Builder", "items": [{"name": "Chromadek Charcoal 0.5mm", "spec": "3.6m AZ150", "price": 18, "need": 85, "unit": "Sheets", "supplier": "SteelSuppliers"}, {"name": "Trusses 114x38", "spec": "6m Treated", "price": 18, "need": 24, "unit": "Lengths", "supplier": "Timber"}, {"name": "Hip Capping 2m", "spec": "Charcoal Hips", "price": 14, "need": 16, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Gutters Set 3m", "spec": "Gutter+Downpipe", "price": 25, "need": 10, "unit": "Sets", "supplier": "SteelSuppliers"}]},
    "Builder Foundation (100sqm)": {"icon": "Builder", "items": [{"name": "Cement PPC 50kg", "spec": "50kg Bag", "price": 12, "need": 30, "unit": "Bags", "supplier": "PPC"}, {"name": "Farm Bricks", "spec": "230x110x75", "price": 0.18, "need": 3000, "unit": "Each", "supplier": "Brick Yard"}, {"name": "River Sand 5ton", "spec": "Load", "price": 120, "need": 2, "unit": "Loads", "supplier": "Sand Pit"}]},
    "Plumber Full House": {"icon": "Plumber", "items": [{"name": "Toilet Close Couple", "spec": "White Ceramic", "price": 180, "need": 2, "unit": "Sets", "supplier": "PlumbMart"}, {"name": "Geyser 100L", "spec": "Kwikot 100L", "price": 350, "need": 1, "unit": "Each", "supplier": "PlumbMart"}]},
    "Electrician Full House": {"icon": "Plumber", "items": [{"name": "Cable 2.5mm 100m", "spec": "Sockets", "price": 45, "need": 3, "unit": "Rolls", "supplier": "Electrical"}, {"name": "DB Board 12 Way", "spec": "Surface", "price": 85, "need": 1, "unit": "Each", "supplier": "Electrical"}]},
}

FLOOR_PLANS = {
    "80sqm 2-Bed Starter": {"icon": "Builder", "rooms": ["Lounge 4x5m 20sqm", "Kitchen 3x3m Fitted Quartz $180", "Bed1 3x3.5m Wardrobes $35", "Bed2 3x3m", "Bath 2x2m Toilet $180"], "price": 2200, "roof": "Gabled Roof (100sqm)", "ceiling": "Ceilings (80sqm)", "desc": "Starter - Gabled 75 sheets $18 + Ceilings 65 boards $8 + Foundation"},
    "127sqm 3-Bed Popular $3627": {"icon": "Builder", "rooms": ["Lounge 5x6m 30sqm", "Kitchen 4x3m Fitted Quartz $180x2 Sink $85", "Bed1 4x4m Wardrobes $35x2 Mirror $35", "Bed2 3.5x3.5m", "Bed3 3x3m", "Bath1 2.5x2.5m Toilet $180 Geyser $350", "Bath2 2x2m Toilet $180"], "price": 3627, "roof": "Hipped Roof (100sqm)", "ceiling": "Ceilings (80sqm)", "desc": "POPULAR - Hipped 85 sheets $18=1530 Hip 16x$14 Valley 8x$18 Ridge 12x$15 Gutters 10x$25 + Ceilings 65 boards $8=520 + Foundation Cement 30x$12 Bricks 3000x$0.18 Full $3627"},
    "150sqm 4-Bed Family": {"icon": "Builder", "rooms": ["Lounge 6x6m 36sqm", "Kitchen 5x4m Fitted Large", "Bed1 4.5x4m Master Ensuite", "Bed2 4x3.5m", "Bed3 3.5x3.5m", "Bed4 3x3m", "Bath1 3x2.5m Master Toilet $180 Geyser $350", "Bath2 2x2m Toilet $180"], "price": 4850, "roof": "Hipped Roof (100sqm)", "ceiling": "Ceilings (80sqm)", "desc": "Family - 4 Beds Wardrobes + 2 Baths + Dining + Verandah"},
}

def handle_whatsapp_message(phone, message):
    msg = message.lower().strip()
    if msg in ["hi", "hello", "menu", "start"]:
        return ("ANREVAZ SUPERSONIC QUOTE v12.2 Kai AI\nLanding PREMIUM Any Trade Quote in 3 sec AI Follow-up Wins The Job\nCarpenter Welder Builder Plumber Glazier\nAI Timeline 0 sec quote 2h 24h day3 day7\nWhatsApp 0783788376 EcoCash 0772590884\nGet Instant Quote Now\nOrder: 1 Landing 2 System Pass Full Profile 3 Trade Workspace 4 Materials Per Unit Add Remove Left Excess Manual Prices 5 Online Web Only No Copying 6 Kai AI 7 Packages $3 $7 $12\n")
    return ("ANREVAZ SUPERSONIC QUOTE v12.2 Kai AI - Floor Plan $3627 Builder $12 Bricks $0.18 Plumber $180 Geyser $350 Electrician $45 - Kai follows up till WON - Private No Copying Online Web Only - Add Remove Manual Prices - Packages $3 $7 $12")

MATS_JSON = json.dumps(MATS)
SUBS_JSON = json.dumps(SUBS)
FLOOR_JSON = json.dumps(FLOOR_PLANS)

HTML_PARTS = []
HTML_PARTS.append('<!DOCTYPE html>\n')
HTML_PARTS.append('<html>\n')
HTML_PARTS.append('<head>\n')
HTML_PARTS.append('<meta charset="UTF-8">\n')
HTML_PARTS.append('<meta name="viewport" content="width=device-width,initial-scale=1">\n')
HTML_PARTS.append('<title>ANREVAZ SUPERSONIC QUOTE - Kai AI</title>\n')
HTML_PARTS.append('<script src="https://cdn.tailwindcss.com"></script>\n')
HTML_PARTS.append('<style>\n')
HTML_PARTS.append('.screen{display:none}\n')
HTML_PARTS.append('.screen.active{display:block}\n')
HTML_PARTS.append('.nav-active{background:#5b7cff!important;color:white!important}\n')
HTML_PARTS.append('.glass{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1)}\n')
HTML_PARTS.append('</style>\n')
HTML_PARTS.append('</head>\n')
HTML_PARTS.append('<body style="background:#0a0e26;color:white;font-family:Inter;min-height:100vh">\n')
HTML_PARTS.append('<div class="max-w-[560px] mx-auto pb-28">\n')
HTML_PARTS.append('<div id="screen-landing" class="screen active px-5 py-6">\n')
HTML_PARTS.append('<div class="flex justify-between items-center">\n')
HTML_PARTS.append('<div class="flex gap-2 items-center">\n')
HTML_PARTS.append('<div class="w-9 h-9 rounded-xl bg-[#5b7cff] grid place-items-center">A</div>\n')
HTML_PARTS.append('<div class="font-black">ANREVAZ OS</div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div class="bg-[#5b7cff]/30 px-3 py-1 rounded-full text-[10px]">PREMIUM</div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div class="mt-8">\n')
HTML_PARTS.append('<div class="font-black text-3xl">Any Trade Quote in 3 sec</div>\n')
HTML_PARTS.append('<div class="font-black text-3xl text-[#5b7cff]">AI Follow-up Wins The Job</div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div class="mt-8 grid grid-cols-5 gap-2">\n')
HTML_PARTS.append('<div class="glass rounded-2xl p-3 text-center"><div>Carpenter</div></div>\n')
HTML_PARTS.append('<div class="glass rounded-2xl p-3 text-center"><div>Welder</div></div>\n')
HTML_PARTS.append('<div class="glass rounded-2xl p-3 text-center"><div>Builder</div></div>\n')
HTML_PARTS.append('<div class="glass rounded-2xl p-3 text-center"><div>Plumber</div></div>\n')
HTML_PARTS.append('<div class="glass rounded-2xl p-3 text-center"><div>Glazier</div></div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div class="mt-8"><div class="font-bold">AI auto followup timeline</div>\n')
HTML_PARTS.append('<div class="mt-3 glass rounded-2xl p-5">\n')
HTML_PARTS.append('<div class="flex justify-between">\n')
HTML_PARTS.append('<div class="text-center"><div class="w-8 h-8 rounded-full bg-[#5b7cff] grid place-items-center">v</div><div class="text-[10px]">0 sec quote</div></div>\n')
HTML_PARTS.append('<div class="text-center"><div class="w-6 h-6 rounded-full border border-white/30"></div><div class="text-[10px]">2h</div></div>\n')
HTML_PARTS.append('<div class="text-center"><div class="w-6 h-6 rounded-full border border-white/30"></div><div class="text-[10px]">24h</div></div>\n')
HTML_PARTS.append('<div class="text-center"><div class="w-6 h-6 rounded-full border border-white/30"></div><div class="text-[10px]">day 3</div></div>\n')
HTML_PARTS.append('<div class="text-center"><div class="w-6 h-6 rounded-full border border-white/30"></div><div class="text-[10px]">day 7</div></div>\n')
HTML_PARTS.append('</div></div></div>\n')
HTML_PARTS.append('<div class="mt-6 grid grid-cols-2 gap-3">\n')
HTML_PARTS.append('<div class="glass rounded-2xl p-4 text-center"><div>WhatsApp</div><div class="font-black">0783788376</div></div>\n')
HTML_PARTS.append('<div class="glass rounded-2xl p-4 text-center"><div>EcoCash</div><div class="font-black">0772590884</div></div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<button onclick="showScreen(&quot;register&quot;)" class="w-full mt-6 bg-[#5b7cff] py-4 rounded-xl font-black">Get Instant Quote Now</button>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div id="screen-register" class="screen px-5 py-6">\n')
HTML_PARTS.append('<div class="font-black">Create Account - System Pass ANR-KD-XXXX - Full Profile</div>\n')
HTML_PARTS.append('<div class="mt-4 space-y-3">\n')
HTML_PARTS.append('<input id="tName" placeholder="Full Name" class="w-full px-4 py-3 rounded-xl text-sm text-black">\n')
HTML_PARTS.append('<select id="tTradeMain" class="w-full px-4 py-3 rounded-xl text-sm text-black">\n')
HTML_PARTS.append('<option>Carpenter</option><option>Builder</option><option>Welder</option><option>Plumber</option><option>Electrician</option><option>Glazier</option><option>Floor Plan 127sqm $3627</option>\n')
HTML_PARTS.append('</select>\n')
HTML_PARTS.append('<input id="tPhone" placeholder="Phone 0772590884" class="w-full px-4 py-3 rounded-xl text-sm text-black">\n')
HTML_PARTS.append('<input id="tLocation" placeholder="Location Kadoma CBD" class="w-full px-4 py-3 rounded-xl text-sm text-black">\n')
HTML_PARTS.append('<input id="tYears" type="number" placeholder="Years Experience 8" class="w-full px-4 py-3 rounded-xl text-sm text-black">\n')
HTML_PARTS.append('<input id="tIdNumber" placeholder="National ID" class="w-full px-4 py-3 rounded-xl text-sm text-black">\n')
HTML_PARTS.append('<input id="tPhoto" type="file" accept="image/*" class="w-full text-[11px] text-white/50">\n')
HTML_PARTS.append('<button onclick="createID()" class="w-full bg-[#5b7cff] py-4 rounded-xl font-black">Create My System Pass + Private Workspace</button>\n')
HTML_PARTS.append('</div></div>\n')
HTML_PARTS.append('<div id="screen-workspace" class="screen px-5 py-6">\n')
HTML_PARTS.append('<div class="font-black">My Private Workspace - Trade Selected - Online Web Only</div>\n')
HTML_PARTS.append('<div id="idCard" class="mt-4 bg-[#1e2a6b] border border-[#5b7cff]/50 rounded-2xl p-4">\n')
HTML_PARTS.append('<div id="idName" class="font-black">Tinashe Moyo</div>\n')
HTML_PARTS.append('<div id="idTrade" class="text-[#5b7cff] text-xs">Fitted Kitchens</div>\n')
HTML_PARTS.append('<div id="workspaceBadge" class="mt-1 bg-green-500/20 text-green-300 text-[9px] px-2 py-1 rounded-full">WS-XXXX PRIVATE ONLINE WEB ONLY</div>\n')
HTML_PARTS.append('<div class="mt-2">Workspace: <span id="idNumber">WS-A7K9</span> - <span id="wsTradeName">Fitted Kitchens ONLY</span></div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div class="mt-4"><div class="font-black">Select Trade - Everything For That Job</div><div id="projectsList" class="mt-2 space-y-2"></div></div>\n')
HTML_PARTS.append('<div class="mt-4"><div class="font-black">Floor Plans</div><div id="floorPlansList" class="mt-2 space-y-2"></div></div>\n')
HTML_PARTS.append('<div class="mt-4 glass rounded-2xl p-4"><div class="font-black text-sm">Online Artisans - Web Interface Only</div><div id="onlineList" class="mt-2"><div class="flex justify-between bg-white/5 p-2 rounded-lg"><span>Tinashe Moyo - Carpenter</span><span class="text-green-400">Online - Web Only</span></div><div class="flex justify-between bg-white/5 p-2 rounded-lg"><span>Blessed - Builder</span><span class="text-green-400">Online - Web Only</span></div></div></div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div id="screen-materials" class="screen px-5 py-6">\n')
HTML_PARTS.append('<div class="font-black">Workspace Materials - Per Unit - Add Remove - Manual Prices</div>\n')
HTML_PARTS.append('<div class="mt-2"><span id="materialsProjectName">Fitted Kitchen</span> - <span id="materialsWorkspaceId">WS-A7K9</span></div>\n')
HTML_PARTS.append('<div id="floorPlanDrawing" class="hidden mt-4 bg-white text-black rounded-xl p-4">\n')
HTML_PARTS.append('<div class="font-black text-sm">Floor Plan Drawing - <span id="floorPlanTitle">127sqm $3627</span></div>\n')
HTML_PARTS.append('<div id="floorPlanRooms" class="mt-2 bg-gray-50 p-3 rounded-lg text-[11px]"></div>\n')
HTML_PARTS.append('<div id="floorPlanIncludes" class="mt-2 bg-blue-50 p-3 rounded-lg text-[11px]"></div>\n')
HTML_PARTS.append('</div>\n')
HTML_PARTS.append('<div class="mt-4"><div class="flex justify-between"><div class="font-black">Materials Per Unit - Add Remove Left Excess - Manual</div><button onclick="addCustomMaterial()" class="bg-[#5b7cff] px-3 py-1 rounded-full text-[11px]">+ Add Material</button></div>\n')
HTML_PARTS.append('<div class="mt-2 bg-black/40 border border-white/10 rounded-xl overflow-hidden">\n')
HTML_PARTS.append('<div class="grid grid-cols-12 gap-2 bg-white/10 p-2 text-[9px] font-bold">\n')
HTML_PARTS.append('<div class="col-span-4">Material</div><div class="col-span-2 text-center">Qty Unit</div><div class="col-span-2 text-right">Price Editable</div><div class="col-span-2 text-right">Total</div><div class="col-span-2 text-center">Action</div>\n')
HTML_PARTS.append('</div><div id="materialsDetailedList"></div></div></div>\n')
HTML_PARTS.append('<div class="mt-4 glass rounded-2xl p-4"><div class="font-black text-sm">Left / Excess Materials - Add Remove Before Printing</div>\n')
HTML_PARTS.append('<div class="mt-3 flex gap-2"><input id="leftMaterialName" placeholder="Left Material" class="flex-1 px-3 py-2 rounded-lg text-sm text-black"><input id="leftMaterialQty" type="number" placeholder="Qty" class="w-20 px-3 py-2 rounded-lg text-sm text-black"><button onclick="addLeftMaterial()" class="bg-white/10 border px-3 py-2 rounded-lg text-[11px]">Add Left</button></div>\n')
HTML_PARTS.append('<div id="leftMaterialsList" class="mt-3 space-y-1 text-[11px]"></div></div>\n')
HTML_PARTS.append('<div class="mt-4 glass rounded-2xl p-4"><input id="clientName" placeholder="Client Full Name" class="w-full px-3 py-2 rounded-lg text-sm text-black"><input id="clientPhone" placeholder="Client Phone" class="w-full px-3 py-2 rounded-lg text-sm text-black mt-2"><input id="clientAddress" placeholder="Address" class="w-full px-3 py-2 rounded-lg text-sm text-black mt-2"><input id="clientProjectDetails" placeholder="Project Details" class="w-full px-3 py-2 rounded-lg text-sm text-black mt-2"><input id="cName" placeholder="Company Name" class="w-full px-3 py-2 rounded-lg text-sm text-black mt-2"><input id="cLogo" type="file" accept="image/*" class="w-full text-[11px] text-white/50 mt-2"></div>\n')
HTML_PARTS.append('<div class="mt-4 glass rounded-2xl p-4 border border-[#5b7cff]/30">\n')
HTML_PARTS.append('<div class="flex justify-between text-sm"><span>Materials Editable Per Unit:</span><span id="matTotal">$0</span></div>\n')
HTML_PARTS.append('<div class="flex justify-between text-sm"><span>Labour 30% $650 Floor:</span><span id="laborTotal">$0</span></div>\n')
HTML_PARTS.append('<div class="flex justify-between text-sm"><span>Transport: $</span><input id="transport" type="number" value="30" class="w-20 px-2 py-1 rounded-lg text-black text-sm" oninput="calcTotal()"></div>\n')
HTML_PARTS.append('<div class="flex justify-between text-sm"><span>Left / Excess:</span><span id="leftTotal">$0</span></div>\n')
HTML_PARTS.append('<div class="flex justify-between font-black text-lg mt-3 pt-3 border-t border-white/10"><span>Total:</span><span id="grandTotal" class="text-[#5b7cff]">$0</span></div>\n')
HTML_PARTS.append('</div><button onclick="generateQuote()" class="w-full mt-4 bg-[#5b7cff] py-3 rounded-xl font-black">Generate Professional Quote + Print</button></div>\n')
HTML_PARTS.append('<div id="screen-preview" class="screen px-5 py-6"><div class="font-black">Professional Quotation - Anrevaz Supersonic Quote - Kai AI</div>\n')
HTML_PARTS.append('<div class="mt-4 bg-white text-black rounded-2xl p-5"><div class="flex justify-between border-b pb-3"><div><div id="previewCompany" class="font-black">Moyo Carpentry</div><div id="previewCompanyAddress" class="text-[9px] text-gray-500">1234 Rimuka Kadoma 0772590884</div></div><div class="text-right"><div class="font-black text-[#5b7cff] text-xs">SUPERSONIC QUOTE + FLOOR PLAN + INVOICE</div><div id="quoteNumber" class="text-[10px]">#WS-A7K9</div><div id="quoteDate" class="text-[9px] text-gray-500">29 Oct 2026</div></div></div><div class="mt-3"><div id="previewTradesman" class="text-[10px]">Name Trade Workspace ANR-KD Verified</div><div id="previewClient" class="text-[10px] mt-2">Client Floor Plan $3627</div></div><div class="mt-3"><div id="previewMaterials" class="text-[8px]"></div><div id="previewLeft" class="mt-2 text-[8px]"></div></div><div class="mt-3 bg-gray-50 rounded-xl p-2.5 text-[10px]"><span id="previewGrand" class="text-[#5b7cff] font-black">$0</span></div></div>\n')
HTML_PARTS.append('<div class="mt-4 grid grid-cols-2 gap-3"><button onclick="window.print()" class="bg-[#5b7cff] py-3 rounded-xl font-bold text-xs">Download PDF</button><a id="waLink1" href="whatsapp://send?phone=263783788376&text=Hi%20Quote%20$3627%20Ready" class="bg-[#25D366] py-3 rounded-xl font-bold text-xs text-center">WhatsApp Kai</a></div>\n')
HTML_PARTS.append('<button onclick="showScreen(&quot;ai&quot;)" class="w-full mt-3 bg-[#5b7cff]/20 border py-2.5 rounded-xl font-bold text-xs">Next: Kai AI Follow-up Till WON</button></div>\n')
HTML_PARTS.append('<div id="screen-ai" class="screen px-5 py-6">\n')
HTML_PARTS.append('<div class="font-black">Kai AI - Follow-up Wins The Job - Supersonic Quote</div>\n')
HTML_PARTS.append('<div class="mt-5 bg-white/5 border rounded-2xl p-3">\n')
HTML_PARTS.append('<div class="h-[380px] flex flex-col">\n')
HTML_PARTS.append('<div id="aiChat" class="flex-1 overflow-y-auto space-y-2 text-[11px]">\n')
HTML_PARTS.append('<div class="bg-[#5b7cff]/20 border rounded-xl p-3">\n')
HTML_PARTS.append('<div class="font-bold">Kai AI Ready - Private</div>\n')
HTML_PARTS.append('<div class="text-[10px] mt-1">Workspace 
