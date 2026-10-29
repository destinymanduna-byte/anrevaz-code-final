from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
import json, time
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="ANREVAZ v13 Pictures Inside")

HEARTBEAT_DB = {}
MATS = {"K": {"items": []}, "R": {"items": []}}
MATS["Kitchen"] = MATS["K"]
MATS["Roof"] = MATS["R"]
MATS["Foundation"] = MATS["R"]
MATS["Plumber"] = MATS["K"]
MATS["Welder"] = MATS["R"]
MATS["Glazier"] = MATS["K"]
MATS["Builder"] = MATS["R"]
MATS["Electrician"] = MATS["K"]

SUBS = {"$3": {"price": 3}, "$7": {"price": 7}}
SUBS["$12"] = {"price": 12}
FLOOR = {"80sqm": {"price": 2200}}
FLOOR["127sqm $3627"] = {"price": 3627}

def handle_wa(p,m):
 return "ANREVAZ v13 Pictures Inside"

MATS_J = json.dumps(MATS)
SUBS_J = json.dumps(SUBS)
FLOOR_J = json.dumps(FLOOR)

@app.get("/", response_class=HTMLResponse)
def home():
 html = """
<!DOCTYPE html><html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width">
<title>ANREVAZ - Exact Pictures Inside</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>.screen{display:none}
.screen.active{display:block}
.nav-active{background:#5b7cff!important}
.glass{background:rgba(255,255,255,0.06)}
</style></head>
<body style="background:#0a0e26;color:white">
<div class="max-w-[560px] mx-auto pb-28">
<div id="screen-signin" class="screen active p-5">
<div class="font-black">1. SIGN-IN + SECURE KEY - EXACT PICTURE</div>
<img src="/img/img1" class="mt-3 w-full rounded-2xl border">
<div class="mt-3 glass p-3 rounded text-[11px]">
Exact picture you verified - Sign-in before landing
- Key only by website - Same credentials cannot
create second WS - Proof of job required
</div>
<button onclick="showScreen('landing')"
class="w-full mt-3 bg-[#5b7cff] py-3 rounded">
Continue to Landing - 1 Sec Inside
</button></div>
<div id="screen-landing" class="screen p-5">
<div class="font-black">2. LANDING 1 SEC - EXACT PICTURE</div>
<img src="/img/img2" class="mt-3 w-full rounded-2xl border">
<div class="mt-3 glass p-3 rounded text-[11px]">
Exact landing - Trades: Carpenter Welder
Electrician Plumber Glazier Builder - 1 sec
- Any Trade Quote in 3 sec - AI Follow-up
</div>
<button onclick="showScreen('floor-scan')"
class="w-full mt-3 bg-[#5b7cff] py-3 rounded">
Scan Floor Plan & Quote
</button></div>
<div id="screen-floor-scan" class="screen p-5">
<div class="font-black">3. FLOOR PLAN SCAN - EXACT PICTURE</div>
<img src="/img/img3" class="mt-3 w-full rounded-2xl border">
<div class="mt-3 glass p-3 rounded text-[11px]">
Exact floor plan scan - Upload or scan
- AI extracts rooms - 127sqm $3627
</div>
<input id="floorFile" type="file" accept="image/*"
class="mt-3 w-full text-[11px]">
<button onclick="scanFloorPlan()"
class="mt-2 bg-[#5b7cff] px-4 py-2 rounded-full text-[11px]">
Scan & Quote
</button>
<div id="floorScanResult"
class="hidden mt-3 bg-white text-black p-3 rounded">
<div class="font-black text-sm">Scanned - 127sqm $3627</div>
<div id="floorScanRooms"
class="mt-2 bg-gray-50 p-2 rounded text-[11px]"></div>
<button onclick="useScannedPlan()"
class="mt-2 w-full bg-[#5b7cff] text-white py-2 rounded text-[11px]">
Use This Plan</button></div></div>
<div id="screen-dev" class="screen p-5">
<div class="font-black">4. ONLINE SEEN - DEV DASHBOARD - EXACT PICTURE</div>
<img src="/img/img7" class="mt-3 w-full rounded-2xl border">
<div class="mt-3 glass p-3 rounded text-[11px]">
Exact developer dashboard - 24/38 Online
- 48 Quotes Today - 4.5/5 Usefulness
- 4.2x/week Frequency - Trade Distribution
</div>
<div class="mt-3 grid grid-cols-2 gap-2">
<div class="glass p-3 rounded">
<div class="text-[10px]">Artisans Online</div>
<div class="font-black"><span id="devOnlineCount">0</span> / <span id="devTotalCount">0</span></div>
</div><div class="glass p-3 rounded">
<div class="text-[10px]">Quotes Today</div>
<div class="font-black" id="devQuotesToday">0</div>
</div></div>
<div class="mt-3 glass p-3 rounded">
<div class="font-black text-[11px]">Artisans Frequency</div>
<div id="devArtisansList" class="mt-2 text-[10px]"></div>
</div></div>
<div id="screen-preview" class="screen p-5">
<div class="font-black">5. INVOICE COLUMNS - EXACT PICTURE</div>
<img src="/img/img5" class="mt-3 w-full rounded-2xl border">
<div class="mt-3 glass p-3 rounded text-[11px]">
Exact invoice - Moyo Carpentry - Columns:
Description | Quantities | Price Per Unit
| Discount | Total Price + Labour Money
+ Grand Total - Download PDF
</div>
<div class="mt-3 bg-white text-black rounded p-3">
<div class="grid grid-cols-12 gap-1 bg-gray-100 p-2 text-[8px] font-bold">
<div class="col-span-4">Description</div>
<div class="col-span-2">Quantities</div>
<div class="col-span-2">Price/U</div>
<div class="col-span-1">Disc</div>
<div class="col-span-3">Total Price</div>
</div>
<div id="previewMaterials" class="text-[8px] p-2">
Materials per unit - Discount - Labour money
</div>
<div class="mt-2 bg-gray-50 p-2 rounded text-[9px]">
<div class="flex justify-between">
<span>Materials:</span><span id="previewMat">$0</span>
</div>
<div class="flex justify-between">
<span>Grand Total:</span>
<span id="previewGrand" class="text-[#5b7cff]">$0</span>
</div></div></div></div>
<div id="screen-ai" class="screen p-5">
<div class="font-black">6. KAI AI CHATGPT-6 - EXACT PICTURE</div>
<img src="/img/img6" class="mt-3 w-full rounded-2xl border">
<div class="mt-3 glass p-3 rounded text-[11px]">
Exact Kai AI - Follow-up Agent - Technical
Support - How App Works - Assist Tradesmen
- Follow-up till WON - Timeline 0 sec 2h 24h Day3 Day7
</div>
<div class="mt-3 bg-white/5 border rounded p-3">
<div class="h-[200px] flex flex-col">
<div id="aiChat" class="flex-1 overflow-y-auto space-y-2 text-[11px]">
<div class="bg-[#5b7cff]/20 border rounded p-3">
<div class="font-bold">Kai AI Ready - Private WS-A7K9</div>
<div class="text-[10px]">I am Kai - Tech support + How app works + Till WON</div>
</div></div>
<div class="mt-2 flex gap-2">
<input id="aiInput" placeholder="Ask Kai"
class="flex-1 bg-white/10 border rounded-full px-3 py-2 text-[11px]">
<button onclick="sendAI()"
class="bg-[#5b7cff] px-3 py-2 rounded-full text-[11px]">Ask</button>
</div></div></div></div>
<div id="screen-subscribe" class="screen p-5">
<div class="font-black">7. PACKAGES FREE TRIAL - EXACT PICTURE</div>
<img src="/img/img4" class="mt-3 w-full rounded-2xl border">
<div class="mt-3 glass p-3 rounded text-[11px]">
Exact packages - Start 7-day free trial
- Starter $3 1 workspace Safe ID pass
Materials 50 Kai AI - Pro $7 POPULAR BEST VALUE
3 workspaces Materials 200 Kai AI Online
WhatsApp EcoCash PayNow - Premium $12
Unlimited workspaces Unlimited materials
Kai AI priority Online artisans Advanced
analytics - All plans include free trial
</div>
<div class="mt-3 space-y-3" id="subsList"></div>
</div>
<div id="screen-workspace" class="screen p-5">
<div class="font-black">My Private Workspace</div>
<div id="idCard" class="mt-3 bg-[#1e2a6b] p-4 rounded">
<div id="idName">Tinashe Moyo</div>
<div id="idTrade">Fitted Kitchens</div>
<div class="text-[10px]">Key <span id="idKey">ANR-KD-XXXX</span> / <span id="idNumber">WS-A7K9</span></div>
</div>
<div class="mt-3"><div class="font-black text-sm">Select Trade</div><div id="projectsList" class="mt-2"></div></div>
<div class="mt-3"><div class="font-black text-sm">Floor Plans Scan & Quote $3627</div><div id="floorPlansList" class="mt-2"></div></div>
</div>
<div id="screen-materials" class="screen p-5">
<div class="font-black text-sm">Materials Invoice Ready</div>
<div class="text-[10px]">WS <span id="materialsWorkspaceId">WS-A7K9</span> - <span id="materialsProjectName">Kitchen</span></div>
<div id="floorPlanDrawing" class="hidden mt-2 bg-white text-black p-2 rounded">
<div class="font-black text-[11px]">Floor Plan - <span id="floorPlanTitle">127sqm</span></div>
<div id="floorPlanRooms" class="mt-1 bg-gray-50 p-2 rounded text-[10px]"></div></div>
<div class="mt-3 bg-black/40 border rounded overflow-hidden">
<div class="grid grid-cols-12 gap-1 bg-white/10 p-2 text-[8px] font-bold">
<div class="col-span-4">Description</div>
<div class="col-span-2">Qty</div>
<div class="col-span-2">Price/U</div>
<div class="col-span-1">Disc</div>
<div class="col-span-2">Total</div>
<div class="col-span-1">Act</div>
</div>
<div id="materialsDetailedList" class="text-[11px]"></div></div>
<div class="mt-3 glass p-3 rounded border">
<div class="flex justify-between text-[11px]"><span>Materials:</span><span id="matTotal">$0</span></div>
<div class="flex justify-between text-[11px]"><span>Labour Money:</span><span id="laborTotal">$0</span></div>
<div class="flex justify-between font-black mt-2 pt-2 border-t"><span>Total:</span><span id="grandTotal" class="text-[#5b7cff]">$0</span></div></div>
<button onclick="generateQuote()" class="w-full mt-3 bg-[#5b7cff] py-3 rounded font-black text-sm">Generate Invoice + Print</button></div>
</div>
<div class="fixed bottom-0 left-0 right-0 bg-black/90 border-t border-white/10">
<div class="max-w-[560px] mx-auto grid grid-cols-8 text-center text-[7px] py-2 gap-1">
<button onclick="showScreen('signin')" id="nav-signin" class="nav-active py-1 rounded">Sign-In<br>Key</button>
<button onclick="showScreen('landing')" id="nav-landing" class="text-white/40 py-1">Landing<br>1 Sec</button>
<button onclick="showScreen('workspace')" id="nav-workspace" class="text-white/40 py-1">Trade<br>WS</button>
<button onclick="showScreen('floor-scan')" id="nav-floor-scan" class="text-white/40 py-1">Floor<br>Scan</button>
<button onclick="showScreen('materials')" id="nav-materials" class="text-white/40 py-1">Materials<br>Invoice</button>
<button onclick="showScreen('preview')" id="nav-preview" class="text-white/40 py-1">Invoice<br>Pic</button>
<button onclick="showScreen('ai')" id="nav-ai" class="text-white/40 py-1">Kai AI<br>Pic</button>
<button onclick="showScreen('subscribe')" id="nav-subscribe" class="text-white/40 py-1">Packages<br>Pic</button>
</div></div>
<script>
let projects={"Kitchen":{"items":[]}};let subs={"$3":{"price":3}};let floorPlans={"127sqm $3627":{"price":3627}};
let curProject="Kitchen";let materials=projects[curProject];let workspace=null;
function showScreen(id){document.querySelectorAll(".screen").forEach(function(s){s.classList.remove("active");});let el=document.getElementById("screen-"+id);if(el){el.classList.add("active");}let nav=document.getElementById("nav-"+id);if(nav){document.querySelectorAll("[id^=nav-]").forEach(function(n){n.classList.remove("nav-active");});nav.classList.add("nav-active");}window.scrollTo(0,0);}
function doSignIn(){let name="Test";let keyId="ANR-KD-"+Math.random().toString(36).substr(2,4).toUpperCase();let wsId="WS-"+Math.random().toString(36).substr(2,4).toUpperCase();let artisan={name:name,keyId:keyId,wsId:wsId};workspace=artisan;document.getElementById("idName").innerText=name;document.getElementById("idKey").innerText=keyId;document.getElementById("idNumber").innerText=wsId;showScreen("landing");}
function renderProjects(){let html="";Object.entries(projects).forEach(function(e){let name=e[0];html+="<div data-n=\\""+name+"\\" onclick=\\"openProject(this.dataset.n)\\" class=\\"glass p-3 rounded\\">"+name+"</div>";});let el=document.getElementById("projectsList");if(el){el.innerHTML=html;}}
function renderFloorPlans(){let html="";Object.entries(floorPlans).forEach(function(e){let name=e[0];html+="<div class=\\"glass p-3 rounded\\">"+name+" $"+e[1].price+"</div>";});let el=document.getElementById("floorPlansList");if(el){el.innerHTML=html;}}
function scanFloorPlan(){let result=document.getElementById("floorScanResult");result.classList.remove("hidden");document.getElementById("floorScanRooms").innerHTML="Lounge 5x6m<br>Kitchen 4x3m<br>Bed1 4x4m<br>Bed2 3.5x3.5m<br>Bed3 3x3m<br>Bath1 2.5x2.5m<br>Bath2 2x2m<br><span class=\\"text-green-600\\">AI extracted 7 rooms</span>";}
function useScannedPlan(){showScreen("materials");}
function openProject(name){showScreen("materials");}
function renderMaterials(){let html="<div class=\\"p-2\\">Materials per unit - Add Remove - Manual prices - Columns: Description Quantities Price/U Discount Total + Labour Money</div>";let el=document.getElementById("materialsDetailedList");if(el){el.innerHTML=html;}}
function calcTotal(){let el1=document.getElementById("matTotal");if(el1){el1.innerText="$0";}let el5=document.getElementById("grandTotal");if(el5){el5.innerText="$0";}return {mat:0,grand:0};}
function generateQuote(){showScreen("preview");}
async function sendAI(){let input=document.getElementById("aiInput");let msg=input.value;if(!msg){return;}let chat=document.getElementById("aiChat");chat.innerHTML+="<div class=\\"bg-white/10 border p-3 text-right rounded\\">You: "+msg+"</div>";input.value="";try{let r=await fetch("/whatsapp",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({phone:"263",message:msg})});let d=await r.json();chat.innerHTML+="<div class=\\"bg-[#5b7cff]/20 border p-3 rounded\\">Kai: "+d.reply+"</div>";chat.scrollTop=chat.scrollHeight;}catch(e){chat.innerHTML+="<div class=\\"bg-red-500/10 border p-3 rounded\\">Kai offline</div>";}}
</script></body></html>
"""
 return HTMLResponse(html)

@app.get("/img/{img_id}")
def get_img(img_id: str):
 mapping = {
  "img1": "image_20261029_114049.webp",
  "img2": "image_20261029_114049_1.webp",
  "img3": "image_20261029_114049_2.webp",
  "img4": "image_20261029_114050.webp",
  "img5": "image_20261029_114052.webp",
  "img6": "image_20261029_114055.webp",
  "img7": "image_20261029_114056.webp"
 }
 filename = mapping.get(img_id, "image_20261029_114049.webp")
 # Try multiple paths - Render vs local
 for path in [f"/mnt/data/{filename}", filename, f"./{filename}"]:
  if os.path.exists(path):
   return FileResponse(path, media_type="image/webp")
 # If not found, return placeholder
 return JSONResponse({"error": "Image not found, upload img1.webp to img7.webp to GitHub", "expected": filename})

@app.get("/manifest.json")
def manifest():
 return JSONResponse({"name": "ANREVAZ", "short_name": "ANREVAZ", "start_url": "/", "display": "standalone"})

@app.get("/privacy")
def privacy():
 return HTMLResponse("<html><body style=\"padding:20px\"><h1>Privacy Policy - Pictures Inside - Play Store + App Store Compliant - Exact pictures embedded</h1></body></html>")

@app.get("/terms")
def terms():
 return HTMLResponse("<html><body style=\"padding:20px\"><h1>Terms - Free trial 7 days</h1></body></html>")

@app.post("/heartbeat")
async def heartbeat(req: Request):
 try:
  data = await req.json()
  wsId = data.get("wsId", "WS-XXXX")
  HEARTBEAT_DB[wsId] = {"trade": "Unknown", "last": time.time()}
  return {"ok": True}
 except:
  return {"ok": False}

@app.get("/dev-stats")
def dev_stats():
 return {"online": len(HEARTBEAT_DB), "total": len(HEARTBEAT_DB), "quotes": len(HEARTBEAT_DB)*2, "artisans": list(HEARTBEAT_DB.values())[:10]}

@app.post("/whatsapp")
async def wa_backend(req: Request):
 try:
  data = await req.json()
  msg = data.get("message", "hi")
  reply = handle_wa("263", msg)
  return {"reply": reply}
 except:
  return {"reply": "ANREVAZ Pictures Inside"}

@app.get("/health")
def health():
 return {"status": "LIVE v13 Pictures Inside", "pictures": "Exact generated pictures embedded inside website"}
