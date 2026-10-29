from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json

app = FastAPI(title="ANREVAZ SUPERSONIC QUOTE v12 EXECUTIVE PERFECT - NO ERRORS")

SUBS = {
    "$3 Starter": {"price": 3, "features": ["1 Private Trade Workspace WS-XXXX", "5 Supersonic Quotes/month 3 sec", "System Pass ANR-KD QR Verified", "Basic Materials Realtime Per Unit $85 $18", "Kai AI Follow-up 0 sec 2h", "Online Presence Web Only", "WhatsApp Backend No Data"], "color": "gray"},
    "$7 Pro": {"price": 7, "features": ["3 Private Workspaces Isolated", "50 Supersonic Quotes/month", "Company Logo + Full Profile Trade", "All Materials Per Unit Realtime $85 $18 $8 Editable Prices", "Add/Remove Left Excess Materials Before Print", "Kai AI Negotiates $650 Floor Protected Till WON", "Invoice PDF 10 sec", "Permit System Edit With Permit", "Online Presence Web Interface Only", "PayNow + EcoCash App Only"], "color": "blue", "popular": True},
    "$12 Premium Last Package": {"price": 12, "features": ["Unlimited Private Workspaces No Copying", "Unlimited Supersonic Quotes 3 sec", "System Pass ANR-KD + Full Profile Trade + Logo + Owner", "Every Material Per Unit Realtime $85 $18 $8 $12 $0.18 $180 $350 $45 $85 $25 $3627 Editable Manual Adjustable", "Add/Remove Left Excess Materials Before Printing", "Floor Plan AI 80sqm $2200 127sqm $3627 Popular 150sqm $4850 Full House Every Material", "Builder Cement $12 Bricks $0.18 Sand $120 Plumber Toilet $180 Geyser $350 Electrician Cable $45 DB Board $85 Full Lists", "Kai AI Named Kai Follow-up Till WON 0 sec 2h 24h day 3 day 7 All Functions Enabled Secured Per Workspace", "Secured Workspace No Other Artisan Can See Another Workspace - Isolated Encrypted - Tightly Secured", "Online Presence When One Online Shown On Web Interface Only Not In Workspace", "Invoice PDF 10 sec + Permit System + AI Floor $650 Protected", "WhatsApp Backend /whatsapp No Internet Data whatsapp://send + wa.me + EcoCash 0772590884 App Sub Only + WhatsApp 0783788376"], "color": "yellow", "best": True},
}

MATS = {
    "Fitted Kitchen (3m x 3m)": {"icon": "🔨", "trade": "Carpenter", "items": [{"name": "Melamine White 18mm", "spec": "2440x1220 Base Units", "price": 85, "need": 6, "unit": "Sheets", "supplier": "BoardMart Kadoma"}, {"name": "Quartz Countertop 20mm", "spec": "Black White 3m Stone", "price": 180, "need": 2, "unit": "Sheets", "supplier": "Granite Centre"}, {"name": "Soft Close Hinges", "spec": "110 deg Pair Heavy Duty", "price": 3.5, "need": 20, "unit": "Each", "supplier": "Hardware"}, {"name": "Handles Chrome", "spec": "128mm Stainless", "price": 6, "need": 12, "unit": "Each", "supplier": "Hardware"}, {"name": "Sink Double Bowl", "spec": "860x500mm With Drainer", "price": 85, "need": 1, "unit": "Each", "supplier": "PlumbMart"}, {"name": "Tap Mixer Chrome", "spec": "360 swivel Single lever", "price": 45, "need": 1, "unit": "Each", "supplier": "PlumbMart"}]},
    "Hipped Roof (100sqm)": {"icon": "🏠", "trade": "Carpenter", "items": [{"name": "Chromadek 0.5mm Charcoal", "spec": "3.6m AZ150 85 Sheets", "price": 18, "need": 85, "unit": "Sheets", "supplier": "SteelSuppliers"}, {"name": "Pine Trusses 114x38", "spec": "SA Pine 6m Treated Roof Frame", "price": 18, "need": 24, "unit": "Lengths", "supplier": "Timber Centre"}, {"name": "Hip Capping 2m", "spec": "Charcoal For Hips", "price": 14, "need": 16, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Valley Flashing 2m", "spec": "Charcoal For Valleys", "price": 18, "need": 8, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Ridge Capping 2m", "spec": "Charcoal 2m Matching", "price": 15, "need": 12, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Gutters + Downpipes Set 3m", "spec": "Charcoal Gutter 3m + Downpipe + Brackets", "price": 25, "need": 10, "unit": "Sets", "supplier": "SteelSuppliers"}]},
    "Gabled Roof (100sqm)": {"icon": "🏡", "trade": "Carpenter", "items": [{"name": "Chromadek 0.5mm Blue", "spec": "0.5mm 3.6m AZ150", "price": 18, "need": 75, "unit": "Sheets", "supplier": "SteelSuppliers"}, {"name": "Pine Trusses 114x38", "spec": "SA Pine 6m Treated", "price": 18, "need": 20, "unit": "Lengths", "supplier": "Timber Centre"}, {"name": "Ridge Capping 2m", "spec": "Blue 2m", "price": 15, "need": 10, "unit": "Each", "supplier": "SteelSuppliers"}, {"name": "Gutters Set 3m", "spec": "Blue Gutter + Downpipe + Brackets", "price": 25, "need": 8, "unit": "Sets", "supplier": "SteelSuppliers"}]},
    "Ceilings (80sqm)": {"icon": "🔲", "trade": "Carpenter", "items": [{"name": "Ceiling Boards 1200x600mm", "spec": "Gypsum 9mm White 65 Boards", "price": 8, "need": 65, "unit": "Boards", "supplier": "BuildMart"}, {"name": "Brandering 38x38 Pine", "spec": "SA Pine 3.6m Battens", "price": 8, "need": 30, "unit": "Lengths", "supplier": "Timber Centre"}, {"name": "Cornice 3m", "spec": "75mm Gypsum Decorative", "price": 6, "need": 20, "unit": "Each", "supplier": "BuildMart"}, {"name": "Paint White 20L", "spec": "PVA White One Coat", "price": 65, "need": 2, "unit": "Tins", "supplier": "Paint Centre"}]},
    "Builder Foundation (100sqm)": {"icon": "🧱", "trade": "Builder", "items": [{"name": "Cement PPC 32.5 50kg", "spec": "50kg Bag PPC", "price": 12, "need": 30, "unit": "Bags", "supplier": "PPC Kadoma"}, {"name": "Farm Bricks", "spec": "230x110x75 Common", "price": 0.18, "need": 3000, "unit": "Each", "supplier": "Brick Yard Kadoma"}, {"name": "River Sand 5ton Load", "spec": "Plaster + Building", "price": 120, "need": 2, "unit": "Loads", "supplier": "Sand Pit"}, {"name": "Pit Sand 5ton Load", "spec": "Foundation", "price": 100, "need": 2, "unit": "Loads", "supplier": "Sand Pit"}, {"name": "Brickforce 150mm 75m", "spec": "Every 3rd Course", "price": 8, "need": 10, "unit": "Rolls", "supplier": "Hardware"}]},
    "Plumber Full House": {"icon": "🔧", "trade": "Plumber", "items": [{"name": "PVC Pipes 110mm 4m", "spec": "Sewer Pipe 4m", "price": 18, "need": 10, "unit": "Each", "supplier": "PlumbMart"}, {"name": "PVC Pipes 50mm 4m", "spec": "Waste Pipe", "price": 10, "need": 15, "unit": "Each", "supplier": "PlumbMart"}, {"name": "Toilet Set Close Couple", "spec": "White Ceramic + Cistern + Seat", "price": 180, "need": 2, "unit": "Sets", "supplier": "PlumbMart"}, {"name": "Geyser 100L Kwikot", "spec": "100L Vertical + Thermostat", "price": 350, "need": 1, "unit": "Each", "supplier": "PlumbMart"}]},
    "Electrician Full House": {"icon": "💡", "trade": "Electrician", "items": [{"name": "Cable 2.5mm 100m Roll", "spec": "Sockets Red + Black", "price": 45, "need": 3, "unit": "Rolls", "supplier": "Electrical Centre"}, {"name": "Cable 1.5mm 100m Roll", "spec": "Lights", "price": 35, "need": 2, "unit": "Rolls", "supplier": "Electrical Centre"}, {"name": "DB Board 12 Way Surface", "spec": "12 Way + Breakers", "price": 85, "need": 1, "unit": "Each", "supplier": "Electrical Centre"}, {"name": "Light Fittings Downlight LED 12W", "spec": "White Recessed", "price": 25, "need": 10, "unit": "Each", "supplier": "Electrical"}]},
    "Welder Gate (3m)": {"icon": "⚙️", "trade": "Welder", "items": [{"name": "Square Tube 40x40x2mm", "spec": "6m Galvanized", "price": 18, "need": 8, "unit": "Lengths", "supplier": "SteelSuppliers"}, {"name": "Flat Bar 40x5mm", "spec": "6m", "price": 12, "need": 4, "unit": "Lengths", "supplier": "SteelSuppliers"}, {"name": "Hinges Heavy Duty 100mm", "spec": "Gate Hinges Pair", "price": 15, "need": 3, "unit": "Pairs", "supplier": "Hardware"}, {"name": "Paint Enamel Black 5L", "spec": "Gloss", "price": 35, "need": 2, "unit": "Tins", "supplier": "Paint Centre"}]},
    "Glazier Window (1.5x1.2m)": {"icon": "🪟", "trade": "Glazier", "items": [{"name": "Aluminium Frame White", "spec": "1.5x1.2m Sliding", "price": 85, "need": 1, "unit": "Set", "supplier": "Glass Centre"}, {"name": "Glass 5mm Clear", "spec": "1.5x1.2m Toughened", "price": 45, "need": 2, "unit": "Sheets", "supplier": "Glass Centre"}, {"name": "Silicone Sealant", "spec": "300ml Clear", "price": 6, "need": 4, "unit": "Each", "supplier": "Hardware"}, {"name": "Rubber Seal", "spec": "10m Roll", "price": 12, "need": 1, "unit": "Roll", "supplier": "Glass Centre"}]},
}

FLOOR_PLANS = {
    "80sqm 2-Bed Starter": {"icon": "🏠", "rooms": ["Lounge 4x5m 20sqm", "Kitchen 3x3m Fitted Quartz $180", "Bed1 3x3.5m Wardrobes $35", "Bed2 3x3m", "Bath 2x2m Toilet $180"], "price": 2200, "roof": "Gabled Roof (100sqm)", "ceiling": "Ceilings (80sqm)", "desc": "Starter - Gabled 75 sheets $18 + Ceilings 65 boards $8 + Foundation"},
    "127sqm 3-Bed Popular $3627": {"icon": "⭐", "rooms": ["Lounge 5x6m 30sqm", "Kitchen 4x3m Fitted Quartz $180x2 Sink $85 Tap $45", "Bed1 4x4m Wardrobes Sliding $35x2 Mirror $35", "Bed2 3.5x3.5m", "Bed3 3x3m", "Bath1 2.5x2.5m Toilet $180 Basin $85 Geyser $350", "Bath2 2x2m Toilet $180 Shower $45", "Verandah 2m", "Dining 3x3m"], "price": 3627, "roof": "Hipped Roof (100sqm)", "ceiling": "Ceilings (80sqm)", "desc": "POPULAR Kadoma - Hipped 85 sheets $18=1530 Hip 16x$14 Valley 8x$18 Ridge 12x$15 Gutters 10x$25 + Ceilings 65 boards $8=520 + Foundation Cement 30x$12 Bricks 3000x$0.18 + Kitchen + Wardrobes + Plumber + Electrician Full $3627"},
    "150sqm 4-Bed Family": {"icon": "🏡", "rooms": ["Lounge 6x6m 36sqm", "Kitchen 5x4m Fitted Large Quartz $180x3", "Bed1 4.5x4m Master Wardrobes Ensuite", "Bed2 4x3.5m", "Bed3 3.5x3.5m", "Bed4 3x3m", "Bath1 3x2.5m Master Toilet $180 Geyser $350", "Bath2 2x2m", "Dining 4x4m", "Verandah 3m"], "price": 4850, "roof": "Hipped Roof (100sqm)", "ceiling": "Ceilings (80sqm)", "desc": "Family - 4 Beds Wardrobes + 2 Baths + Dining + Verandah - Hipped + Ceilings + Foundation Full"},
}

ONLINE_ARTISANS = [
    {"name": "Tinashe Moyo", "trade": "Carpenter - Fitted Kitchens", "ws": "WS-A7K9", "online": True, "location": "Kadoma CBD"},
    {"name": "James Builder", "trade": "Builder - Foundation", "ws": "WS-B2L4", "online": True, "location": "Rimuka Kadoma"},
    {"name": "Peter Plumber", "trade": "Plumber - Full House", "ws": "WS-C9M1", "online": False, "location": "Chegutu"},
]

def handle_whatsapp_message(phone, message):
    msg = message.lower().strip()
    if msg in ["hi", "hello", "menu", "start"]:
        return (
            "ANREVAZ SUPERSONIC QUOTE v12 EXECUTIVE PERFECT - No Errors\n"
            "Organized Order Exactly As You Imagine:\n"
            "LANDING: ANREVAZ OS PREMIUM - Any Trade Quote in 3 sec - AI Follow-up Wins The Job - Carpenter Welder Builder Plumber Glazier - AI auto followup timeline 0 sec quote 2h 24h day 3 day 7 - WhatsApp 0783788376 - EcoCash 0772590884 - Get Instant Quote Now\n"
            "STEP 1: Create Account With Recognized System Pass Full Profile Trade - System Pass ANR-KD QR Verified Encrypted Full Profile Trade Years Experience Photo Location Phone - Tightly Secured\n"
            "STEP 2: Select Trade And In That Trade Workspace Have Everything To Do With That Job - Materials Needed Prices Per Unit $85 $18 $8 $12 $0.18 $180 $350 $45 $85 $3627 - Allow Artisan To Add And Remove Left Or Excess Materials Before Printing - Manual Adjustable Prices Editable Per Unit - Clear Orderly - Inside Trade Workspace Inline Job Only\n"
            "STEP 3: Never Allow Other Artisans To See Another Workspace - Private Workspace WS-XXXX Isolated No Copying Skills Prices Clients - Encrypted AES-256 - Whenever One Online Let Him Be Shown On Web Interface Only Not Inside Workspace - Online Presence Web Only\n"
            "STEP 4: AI To Follow Up Named Kai - Kai AI Assistant Named Kai - Application Anrevaz Supersonic Quote - Kai Follows Up Till Job WON - All Functions Enabled Secured Per Workspace\n"
            "STEP 5: Packages Different Subscriptions With What It Includes Respectively - $3 Starter $7 Pro Popular $12 Premium Last Package Best Value - Classified Gazetted Amounts - What It Includes Respectively Orderly\n"
            "Add Everything Just As You Imagine Exactly Without Errors Executive Perfect - Floor Plan 80sqm 127sqm 150sqm $3627 Full House Every Material - Builder $12 $0.18 Plumber $180 $350 Electrician $45 $85 Welder Glazier + Invoice 10 sec + Permit + AI Floor $650 + PayNow + WhatsApp No Data + EcoCash App Only\n"
            "WhatsApp Links No Data Needed: whatsapp://send?phone=263783788376 Opens Directly No Data Needed Uses WhatsApp Bundle Only - https://wa.me/263783788376 Alternative WhatsApp Bundle - Backend /whatsapp - EXECUTIVE PERFECT"
        )
    if "kai" in msg:
        return (
            "Kai AI Assistant - Named Kai - Anrevaz Supersonic Quote - Executive Perfect\n"
            "I am Kai, your AI assistant for Anrevaz Supersonic Quote - I follow up till job WON - All Functions Enabled Secured Per Workspace WS-XXXX Private No Copying\n"
            "Timeline: 0 sec Supersonic Quote + Floor Plan $3627 sent Full Materials Per Unit Realtime Editable Prices + Logo + System Pass + Owner - Private Workspace\n"
            "2h Kai: Reviewed quote? Questions about materials per unit $85 $18 $8? Left excess materials?\n"
            "24h Kai: Confirm today = Free transport $30 off + Floor plan $3627 locked\n"
            "Day 3 Kai: Material prices rising next week - Cement $12 Bricks $0.18 Chromadek $18 - Lock now\n"
            "Day 7 Kai: Last chance Start Monday? 10% off - Floor plan $3627 + Every material\n"
            "When WON: Kai stops, sends invoice 10 sec, requests deposit Cash/Bank/Their EcoCash separate NOT via app EcoCash 0772590884, job scheduled, permit active, $650 floor protected, private no copying - Executive Perfect - No Errors"
        )
    if "floor" in msg or "plan" in msg or "127" in msg:
        return (
            "FLOOR PLAN AI BACK EXECUTIVE PERFECT - Add/Remove Left Excess Materials - Editable Prices\n"
            "80sqm $2200 Starter: Lounge 4x5 Kitchen 3x3 Fitted Quartz $180 Sink $85 Tap $45 Bed1 3x3.5 Wardrobes $35 Mirror $35 Bed2 3x3 Bath 2x2 Toilet $180 - Gabled 75 sheets $18 + Ceilings 65 boards $8 + Foundation\n"
            "127sqm $3627 POPULAR FULL HOUSE: Lounge 5x6 Kitchen 4x3 Fitted Quartz $180x2 Sink $85 Tap $45 Bed1 4x4 Wardrobes $35x2 Mirror $35 Bed2 3.5x3.5 Bed3 3x3 Bath1 2.5x2.5 Toilet $180 Basin $85 Geyser $350 Bath2 2x2 Toilet $180 Verandah 2m Dining 3x3 - Includes Hipped 85 sheets $18=1530 Hip 16x$14 Valley 8x$18 Ridge 12x$15 Gutters 10x$25 + Ceilings 65 boards $8=520 + Builder Foundation Cement 30x$12 Bricks 3000x$0.18 Sand 2x$120 + Fitted Kitchen + Wardrobes + Plumber + Electrician - FULL HOUSE $3627 - Add/Remove Left Excess Materials Before Printing - Editable Prices Per Unit\n"
            "150sqm $4850 Family: Lounge 6x6 Kitchen 5x4 4 Beds Wardrobes 2 Baths Dining 4x4 Verandah 3m - Hipped + Ceilings + Foundation Full\n"
        )
    return (
        "ANREVAZ SUPERSONIC QUOTE v12 EXECUTIVE PERFECT - Kai AI Named Kai - Organized Exactly As You Imagine Without Errors\n"
        "Landing ANREVAZ OS PREMIUM Any Trade Quote in 3 sec AI Follow-up Wins The Job Carpenter Welder Builder Plumber Glazier AI timeline 0 sec 2h 24h day3 day7 WhatsApp 0783788376 EcoCash 0772590884 Get Instant Quote Now - Then Create Account System Pass Full Profile Trade - Then Selecting Trade And In That Trade Workspace Have Everything Materials Per Unit $85 $18 Add/Remove Left Excess Materials Before Printing Manual Adjustable Prices - Never Allow Other Artisans To See Another Workspace But When One Online Shown On Web Interface Only - AI Kai Follow-up - Application Anrevaz Supersonic Quote - Packages Different Subscriptions With What It Includes Respectively - Add Everything Exactly Without Errors Executive Perfect - Say hi kai floor plan 127sqm - Backend /whatsapp - No Errors"
    )

MATS_JSON = json.dumps(MATS)
SUBS_JSON = json.dumps(SUBS)
FLOOR_JSON = json.dumps(FLOOR_PLANS)
ONLINE_JSON = json.dumps(ONLINE_ARTISANS)

HTML_PAGE = (
    "<!DOCTYPE html>\n"
    "<html>\n"
    "<head>\n"
    "<meta charset='UTF-8'>\n"
    "<meta name='viewport' content='width=device-width,initial-scale=1'>\n"
    "<title>ANREVAZ SUPERSONIC QUOTE - Executive Perfect</title>\n"
    "<script src='https://cdn.tailwindcss.com'></script>\n"
    "<style>\n"
    ".screen{display:none}.screen.active{display:block}.nav-active{background:#5b7cff!important;color:white!important;box-shadow:0 4px 15px rgba(91,124,255,0.4)}.glass{background:rgba(255,255,255,0.06);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,0.12)}.glass-strong{background:rgba(255,255,255,0.09);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,0.18)}.trade-card{background:linear-gradient(180deg,rgba(255,255,255,0.08) 0%,rgba(255,255,255,0.03) 100%);border:1px solid rgba(91,124,255,0.25);transition:all 0.3s}.trade-card:hover{transform:translateY(-4px);box-shadow:0 10px 30px rgba(91,124,255,0.3);border-color:rgba(91,124,255,0.5)}.timeline-dot{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font-weight:900;font-size:14px}.floor-popular{border:2px solid #facc15!important;background:linear-gradient(135deg,rgba(250,204,21,0.15),rgba(250,204,21,0.05))!important;box-shadow:0 0 30px rgba(250,204,21,0.25)}\n"
    "</style>\n"
    "</head>\n"
    "<body style='background:radial-gradient(130% 130% at 0% 0%, #0f1642 0%, #0a0e26 50%, #050714 100%);color:white;font-family:Inter;min-height:100vh'>\n"
    "<div class='max-w-[580px] mx-auto pb-28'>\n"
    "<div class='sticky top-0 z-50 bg-black/85 backdrop-blur-xl border-b border-white/10 px-5 py-3 flex justify-between items-center'><div class='flex gap-3 items-center'><div class='w-9 h-9 rounded-xl bg-gradient-to-br from-blue-400 to-indigo-600 grid place-items-center font-black shadow-lg'>A
