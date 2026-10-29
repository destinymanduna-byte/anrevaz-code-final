from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import json, time, os

app = FastAPI(title="ANREVAZ v13.5 Auth + Organized")

HEARTBEAT_DB = {}
MATS = {"K": {"items": []}, "R": {"items": []}}
MATS["Kitchen"] = MATS["K"]
MATS["Roof"] = MATS["R"]

SUBS = {"$3": {"price": 3}, "$7": {"price": 7}}
FLOOR = {"127sqm $3627": {"price": 3627}}

def handle_wa(p,m):
 return "ANREVAZ v13.5 Auth + Organized"

IMGS = [
"IMG-20261029-WA0475.jpg",
"IMG-20261029-WA1657.jpg",
"IMG-20261029-WA3003.jpg",
"IMG-20261029-WA3854.jpg",
"IMG-20261029-WA6158.jpg",
"IMG-20261029-WA9207.jpg",
"IMG-20261029-WA9220.jpg"
]

@app.get("/", response_class=HTMLResponse)
def home():
 html = """
<!DOCTYPE html><html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">
<title>ANREVAZ v13.5 - Auth + Organized Pictures</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>.screen{display:none}
.screen.active{display:block}
.nav-active{background:#5b7cff!important}
</style></head>
<body style="background:#0a0e26;color:white">
<div class="max-w-[560px] mx-auto pb-32">
<div id="screen-reorganize" class="screen p-5">
<div class="font-black text-xl">REORGANIZE PICTURES - AUTHENTICATED</div>
<div class="text-[11px] text-green-400 mt-2">
Authenticated to work as per organized pictures
- Repo root correct - Store compliant
</div>
<div class="mt-4">
<div class="font-black text-sm">Assign Correct Picture To Each Screen</div>
<div class="mt-3 space-y-3" id="assignList"></div>
</div>
<div class="mt-4 flex gap-2">
<button onclick="saveMapping()"
class="flex-1 bg-green-500 py-3 rounded font-black">
Save & Authenticate - Apply Correct Format
</button>
<button onclick="showScreen('signin')"
class="flex-1 bg-[#5b7cff] py-3 rounded font-black">
Go To Sign-In - Auth Required
</button>
</div>
</div>
<div id="screen-signin" class="screen active p-5">
<div class="flex justify-between items-center">
<div class="font-black text-xl">Secure Sign-In - Auth Required</div>
<div class="bg-green-500/20 border border-green-500/30 px-2 py-1 rounded-full text-[8px]">AUTH + ORGANIZED</div>
</div>
<div class="text-[11px] text-white/60 mt-2">
Key recognized only by website
- Workspace secured - Not accessible by other tradesmen
- Same credentials cannot create second workspace
- Authenticated to work as per organized pictures
</div>
<div class="mt-4 space-y-2">
<input id="sName" placeholder="Full Name *"
class="w-full p-3 rounded text-black text-sm">
<input id="sPhone" placeholder="Phone 0772590884 *"
class="w-full p-3 rounded text-black text-sm">
<input id="sIdNum" placeholder="National ID * - Used for secure key"
class="w-full p-3 rounded text-black text-sm">
<select id="sTrade" class="w-full p-3 rounded text-black text-sm">
<option>Carpenter</option><option>Welder</option>
<option>Electrician</option><option>Plumber</option>
<option>Glazier</option><option>Builder</option>
</select>
<input id="sLocation" placeholder="Location Kadoma CBD *"
class="w-full p-3 rounded text-black text-sm">
<input id="sYears" type="number" placeholder="Years Experience *"
class="w-full p-3 rounded text-black text-sm">
<div class="bg-white/5 border rounded-xl p-3">
<div class="font-bold text-[11px]">Proof of Job * - Required per store policy</div>
<div class="text-[10px] text-white/50">Upload photo of recent work or trade certificate</div>
<input id="sProof" type="file" accept="image/*"
class="w-full mt-2 text-[11px]">
</div>
<div class="bg-yellow-500/10 border border-yellow-500/20 rounded-xl p-3">
<div class="text-[10px]">By continuing you agree to
<a href="/privacy" class="text-[#5b7cff] underline">Privacy Policy</a>
<a href="/terms" class="text-[#5b7cff] underline">Terms</a>
- Data stored locally, not shared
</div>
</div>
<button onclick="doSignIn()"
class="w-full bg-[#5b7cff] py-4 rounded-xl font-black mt-2">
Create Secure Key + Private Workspace - Authenticate
</button>
<div id="signInError"
class="hidden mt-3 bg-red-500/20 border border-red-500/30 p-3 rounded-xl text-[11px]"></div>
<div class="mt-4 text-center text-[10px] text-white/40">
Secure key: <span id="previewKey" class="font-mono text-[#5b7cff]">ANR-KD-XXXX / WS-XXXX</span><br>
Key recognized only by website - Authenticated as per organized pictures
</div>
</div></div>
<div id="screen-landing" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">LANDING - 1 SEC INSIDE - AUTHENTICATED</div>
<div id="authBadgeLanding" class="bg-green-500/20 border border-green-500/30 px-2 py-1 rounded-full text-[8px]">AUTHENTICATED</div>
</div>
<div class="text-[10px] text-white/60">Workspace <span id="landingWsId">WS-A7K9</span> - Key <span id="landingKeyId">ANR-KD-XXXX</span> - Authenticated as per organized pictures</div>
<img id="img-landing" src="/img/1"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-3 bg-white/5 p-3 rounded text-[11px]">
Exact landing picture - Any Trade Quote in 3 sec
- AI Follow-up Wins The Job - PREMIUM - 1 second inside
- Trades: Carpenter Welder Electrician Plumber Glazier Builder
- Authenticated - Organized pictures - Correct format
</div>
<button onclick="showScreen('workspace')"
class="w-full mt-3 bg-[#5b7cff] py-3 rounded font-black">
Enter Private Workspace - Authenticated
</button></div>
<div id="screen-workspace" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">My Private Workspace - AUTHENTICATED</div>
<div class="bg-green-500/20 text-green-300 text-[9px] px-2 py-1 rounded-full border border-green-500/30">● Online - Authenticated - Web Only</div>
</div>
<div id="idCard" class="mt-4 bg-[#1e2a6b] border border-[#5b7cff]/50 rounded-2xl p-4">
<div class="flex justify-between">
<div>
<div id="idName" class="font-black">Tinashe Moyo</div>
<div id="idTrade" class="text-[#5b7cff] text-xs">Fitted Kitchens</div>
<div class="text-[10px] text-white/60 mt-1">Key: <span id="idKey">ANR-KD-XXXX</span> / <span id="idNumber">WS-A7K9</span></div>
<div class="text-[9px] text-white/40 mt-1">Secured - Not accessible by other tradesmen<br>Cannot create second workspace with same credentials<br>Authenticated as per organized pictures</div>
</div>
<div class="w-12 h-12 rounded-full bg-[#5b7cff] grid place-items-center font-black">TM</div>
</div></div>
<div class="mt-4"><div class="font-black text-sm">Select Trade - Everything For That Job - Authenticated</div><div id="projectsList" class="mt-2 space-y-2"></div></div>
<div class="mt-4"><div class="font-black text-sm">Floor Plans - Scan & Quote $3627 - Authenticated</div><div id="floorPlansList" class="mt-2 space-y-2"></div></div>
<div class="mt-4 bg-white/5 border rounded-2xl p-4">
<div class="flex justify-between items-center">
<div class="font-black text-sm">Online Artisans - Web Interface Only - Authenticated</div>
<div class="text-[9px] bg-green-500/20 border border-green-500/30 px-2 py-1 rounded-full">Live - Auth OK</div>
</div>
<div id="onlineList" class="mt-2 space-y-1 text-[11px]"></div>
<div class="mt-2 text-[9px] text-white/40">Online seen helps developer see frequency & usefulness - Data anonymized - Authenticated as per organized pictures</div>
</div></div>
<div id="screen-floor-scan" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">Scan Floor Plan & Quote - AUTHENTICATED</div>
<div class="bg-green-500/20 border px-2 py-1 rounded-full text-[8px]">AUTH + ORGANIZED</div>
</div>
<div class="text-[11px] text-white/60 mt-1">Workspace <span id="floorWsId">WS-A7K9</span> - Authenticated - Ability to scan floor plan and quote from it</div>
<img id="img-floor-scan" src="/img/2"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-3 bg-white/5 p-3 rounded text-[11px]">
Exact floor plan scan picture - Upload or scan floor plan image - AI extracts rooms and dimensions - Materials auto-calculated per floor plan - Hipped Roof, Foundation, etc - Authenticated as per organized pictures
</div>
<input id="floorFile" type="file" accept="image/*" capture="environment"
class="mt-3 w-full text-[11px]">
<button onclick="scanFloorPlan()"
class="mt-2 bg-[#5b7cff] px-4 py-2 rounded-full text-[11px] font-bold">
Scan & Generate Quote - Authenticated
</button>
<div id="floorScanResult" class="hidden mt-3 bg-white text-black p-3 rounded-xl">
<div class="font-black text-sm">Floor Plan Detected - <span id="floorScanTitle">127sqm $3627</span> - Authenticated</div>
<div id="floorScanImage" class="mt-2 bg-gray-100 h-20 rounded grid place-items-center text-[11px]">Plan Preview - Authenticated</div>
<div id="floorScanRooms" class="mt-2 bg-gray-50 p-2 rounded text-[11px]"></div>
<button onclick="useScannedPlan()"
class="mt-2 w-full bg-[#5b7cff] text-white py-2 rounded-xl text-[11px] font-bold">
Use This Plan - Quote $3627 - Authenticated
</button>
</div></div>
<div id="screen-dev" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">Developer Dashboard - Online Seen - AUTHENTICATED</div>
<div class="bg-green-500/20 border px-2 py-1 rounded-full text-[8px]">AUTH + ORGANIZED</div>
</div>
<div class="text-[11px] text-white/60 mt-1">Real-time monitoring for artisans - How frequently app is useful - Last updated: <span id="devLastUpdate">Now</span> - Workspace <span id="devWsId">WS-A7K9</span> - Authenticated as per organized pictures</div>
<img id="img-dev" src="/img/6"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-4 grid grid-cols-2 gap-2">
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Artisans Online</div><div class="font-black text-lg"><span id="devOnlineCount">24</span> / <span id="devTotalCount">38</span> Online</div><div class="text-[9px] text-green-400 mt-1">↑ 3 from yesterday - Live tracking - Authenticated</div></div>
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Quotes Created Today</div><div class="font-black text-lg" id="devQuotesToday">48</div><div class="text-[9px] text-green-400">↑ 12% vs yesterday - Authenticated</div></div>
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Avg. App Usefulness</div><div class="font-black text-lg">4.5 / 5.0</div><div class="text-[9px] text-white/40">Based on 112 responses - Authenticated</div></div>
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Avg. Frequency</div><div class="font-black text-lg">4.2x / week</div><div class="text-[9px] text-green-400">Stable trend - Authenticated as per organized pictures</div></div>
</div>
<div class="mt-4 bg-white/5 border rounded-2xl p-3"><div class="font-black text-[11px]">Artisans — Online Status - Frequency & Usefulness - Authenticated</div><div id="devArtisansList" class="mt-3 space-y-2 text-[10px]"></div></div>
</div>
<div id="screen-materials" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black text-sm">Workspace Materials - Per Unit - Invoice Ready - AUTHENTICATED</div>
<div class="bg-green-500/20 border px-2 py-1 rounded-full text-[8px]">AUTH + ORGANIZED</div>
</div>
<div class="mt-1 text-[10px] text-white/60">Private to <span id="materialsWorkspaceId">WS-A7K9</span> - <span id="materialsProjectName">Fitted Kitchen</span> - Authenticated as per organized pictures</div>
<div id="floorPlanDrawing" class="hidden mt-3 bg-white text-black rounded-xl p-3">
<div class="font-black text-[11px]">Floor Plan Drawing - <span id="floorPlanTitle">127sqm $3627</span> - Authenticated</div>
<div id="floorPlanRooms" class="mt-2 bg-gray-50 p-2 rounded-lg text-[10px]"></div>
<div id="floorPlanIncludes" class="mt-2 bg-blue-50 p-2 rounded-lg text-[10px]"></div>
</div>
<div class="mt-4"><div class="flex justify-between items-center"><div class="font-black text-[11px]">Materials - Proper Columns - Invoice Ready - Authenticated</div><button onclick="addCustomMaterial()" class="bg-[#5b7cff] px-3 py-1 rounded-full text-[10px]">+ Add</button></div>
<div class="mt-2 text-[9px] text-white/40">Columns: Description | Quantities | Price Per Unit | Discount | Total Price + Labour Money for the job - Authenticated</div>
<div class="mt-2 bg-black/40 border border-white/10 rounded-xl overflow-hidden">
<div class="grid grid-cols-12 gap-1 bg-white/10 p-2 text-[8px] font-bold"><div class="col-span-4">Description</div><div class="col-span-2 text-center">Qty</div><div class="col-span-2 text-right">Price/U</div><div class="col-span-1 text-center">Disc</div><div class="col-span
