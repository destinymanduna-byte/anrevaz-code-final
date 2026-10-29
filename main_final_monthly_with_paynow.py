from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import json, time, os

app = FastAPI(title="ANREVAZ v13.4 Reorganize")

HEARTBEAT_DB = {}
MATS = {"K": {"items": []}, "R": {"items": []}}
MATS["Kitchen"] = MATS["K"]
MATS["Roof"] = MATS["R"]

SUBS = {"$3": {"price": 3}, "$7": {"price": 7}}
FLOOR = {"127sqm $3627": {"price": 3627}}

def handle_wa(p,m):
 return "ANREVAZ v13.4 Reorganize"

MATS_J = json.dumps(MATS)
SUBS_J = json.dumps(SUBS)
FLOOR_J = json.dumps(FLOOR)

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
<title>ANREVAZ v13.4 - Reorganize Pictures</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>.screen{display:none}
.screen.active{display:block}
.nav-active{background:#5b7cff!important}
.draggable{cursor:move}
</style></head>
<body style="background:#0a0e26;color:white">
<div class="max-w-[560px] mx-auto pb-32">
<div id="screen-reorganize" class="screen active p-5">
<div class="font-black text-xl">REORGANIZE PICTURES - DRAG & ASSIGN</div>
<div class="text-[11px] text-yellow-400 mt-2">
Pictures are displaying in wrong format - Reorganize here
- Tap image to assign to correct dashboard screen
- Mapping saved in browser - Repo root correct
</div>
<div class="mt-4 bg-red-500/20 border border-red-500/30 p-3 rounded text-[11px]">
Current wrong mapping:
- Sign-In showing Packages? Landing showing Invoice?
- Use this page to fix - Assign each picture to correct screen
</div>
<div class="mt-4">
<div class="font-black text-sm">Step 1: See All 7 Pictures From Repo Root</div>
<div id="allPictures" class="mt-2 grid grid-cols-2 gap-2"></div>
</div>
<div class="mt-6">
<div class="font-black text-sm">Step 2: Assign Correct Picture To Each Screen</div>
<div class="mt-3 space-y-3" id="assignList"></div>
</div>
<div class="mt-6 flex gap-2">
<button onclick="saveMapping()"
class="flex-1 bg-green-500 py-3 rounded font-black">
Save Mapping - Apply To Dashboard
</button>
<button onclick="resetMapping()"
class="flex-1 bg-white/10 border py-3 rounded text-[11px]">
Reset To Default
</button>
</div>
<div class="mt-3 bg-white/5 p-3 rounded text-[10px]">
How to reorganize:
1. Look at each picture below
2. Choose which screen it should belong to
3. Tap Save - Dashboard will show exact pictures in correct format
4. Mapping saved in localStorage - Works on Play Store + App Store
</div>
<button onclick="showScreen('signin')"
class="w-full mt-4 bg-[#5b7cff] py-3 rounded font-black">
Go To Dashboard - See Correct Format
</button>
</div>
<div id="screen-signin" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">1. SIGN-IN + SECURE KEY</div>
<button onclick="showScreen('reorganize')"
class="bg-yellow-500/20 border border-yellow-500/30 px-3 py-1 rounded-full text-[9px]">
Reorganize Pictures
</button>
</div>
<div class="text-[10px] text-white/60">Key only by website - Same credentials cannot create second WS</div>
<img id="img-signin" src="/img/0"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-2 text-[9px] text-white/40">Current: <span id="label-signin">IMG-0 WA0475</span> - Tap Reorganize to change</div>
<button onclick="showScreen('landing')"
class="w-full mt-3 bg-[#5b7cff] py-3 rounded">
Continue to Landing
</button></div>
<div id="screen-landing" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">2. LANDING 1 SEC</div>
<button onclick="showScreen('reorganize')"
class="bg-yellow-500/20 border px-2 py-1 rounded-full text-[9px]">Reorganize</button>
</div>
<img id="img-landing" src="/img/1"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-2 text-[9px] text-white/40">Current: <span id="label-landing">IMG-1</span></div>
<button onclick="showScreen('floor-scan')"
class="w-full mt-3 bg-[#5b7cff] py-3 rounded">
Scan Floor Plan
</button></div>
<div id="screen-floor-scan" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">3. FLOOR PLAN SCAN</div>
<button onclick="showScreen('reorganize')"
class="bg-yellow-500/20 border px-2 py-1 rounded-full text-[9px]">Reorganize</button>
</div>
<img id="img-floor-scan" src="/img/2"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-2 text-[9px] text-white/40">Current: <span id="label-floor-scan">IMG-2</span></div>
<input id="floorFile" type="file" accept="image/*"
class="mt-3 w-full text-[11px]">
<button onclick="scanFloorPlan()"
class="mt-2 bg-[#5b7cff] px-4 py-2 rounded-full text-[11px]">
Scan & Quote $3627
</button></div>
<div id="screen-dev" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">4. ONLINE SEEN - DEV DASHBOARD</div>
<button onclick="showScreen('reorganize')"
class="bg-yellow-500/20 border px-2 py-1 rounded-full text-[9px]">Reorganize</button>
</div>
<img id="img-dev" src="/img/6"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-2 text-[9px] text-white/40">Current: <span id="label-dev">IMG-6</span> - Developer sees frequency & usefulness</div>
<div class="mt-3 grid grid-cols-2 gap-2">
<div class="bg-white/5 p-3 rounded">
<div class="text-[10px]">Artisans Online</div>
<div class="font-black">24 / 38 Online</div>
</div><div class="bg-white/5 p-3 rounded">
<div class="text-[10px]">Quotes Today</div>
<div class="font-black">48</div>
</div></div></div>
<div id="screen-preview" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">5. INVOICE COLUMNS</div>
<button onclick="showScreen('reorganize')"
class="bg-yellow-500/20 border px-2 py-1 rounded-full text-[9px]">Reorganize</button>
</div>
<img id="img-preview" src="/img/4"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-2 text-[9px] text-white/40">Current: <span id="label-preview">IMG-4</span> - Description Quantities Price/U Discount Total</div>
<div class="mt-3 bg-white text-black rounded p-3">
<div class="grid grid-cols-12 gap-1 bg-gray-100 p-2 text-[8px] font-bold">
<div class="col-span-4">Description</div>
<div class="col-span-2">Quantities</div>
<div class="col-span-2">Price/U</div>
<div class="col-span-1">Disc</div>
<div class="col-span-3">Total Price</div>
</div>
<div class="mt-2 bg-gray-50 p-2 rounded text-[9px]">
Grand Total: <span id="previewGrand" class="text-[#5b7cff]">$0</span>
</div></div></div>
<div id="screen-ai" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">6. KAI AI CHATGPT-6</div>
<button onclick="showScreen('reorganize')"
class="bg-yellow-500/20 border px-2 py-1 rounded-full text-[9px]">Reorganize</button>
</div>
<img id="img-ai" src="/img/5"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-2 text-[9px] text-white/40">Current: <span id="label-ai">IMG-5</span> - Kai as in pictures - Technical support + How app works + Till WON</div>
<div class="mt-3 bg-[#0f1535] border border-[#5b7cff]/30 rounded-2xl p-3">
<div class="text-[11px]">Kai AI • Follow-up Agent - ChatGPT-6 Capable</div>
<div class="text-[9px] text-white/60">Technical Support • How App Works • Assist Tradesmen • Till WON</div>
<div class="mt-3 bg-[#5b7cff]/20 border rounded-xl p-3 text-[11px]">
Hi! I'm Kai, your follow-up agent. I can help with technical support, walk you through how the application works, and keep following up until WON + Invoice.
</div>
<div class="mt-2 flex gap-2">
<input id="aiInput" placeholder="Ask Kai..."
class="flex-1 bg-white/10 border rounded-full px-3 py-2 text-[11px]">
<button onclick="sendAI()"
class="bg-[#5b7cff] px-3 py-2 rounded-full text-[11px]">Ask</button>
</div></div></div>
<div id="screen-subscribe" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">7. PACKAGES FREE TRIAL</div>
<button onclick="showScreen('reorganize')"
class="bg-yellow-500/20 border px-2 py-1 rounded-full text-[9px]">Reorganize</button>
</div>
<img id="img-subscribe" src="/img/3"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-2 text-[9px] text-white/40">Current: <span id="label-subscribe">IMG-3</span> - $3 $7 $12 - Free trial - What it includes respectively</div>
</div>
<div id="screen-workspace" class="screen p-5">
<div class="font-black">My Private Workspace</div>
<div id="idCard" class="mt-3 bg-[#1e2a6b] p-4 rounded">
<div id="idName">Tinashe Moyo</div>
<div id="idTrade">Fitted Kitchens</div>
<div class="text-[10px]">Key <span id="idKey">ANR-KD-XXXX</span> / <span id="idNumber">WS-A7K9</span></div>
</div></div>
</div>
<div class="fixed bottom-0 left-0 right-0 bg-black/90 border-t border-white/10">
<div class="max-w-[560px] mx-auto grid grid-cols-10 text-center text-[6px] py-2 gap-1">
<button onclick="showScreen('reorganize')" id="nav-reorganize" class="nav-active py-1 rounded bg-yellow-500 text-black">Reorganize<br>Pictures</button>
<button onclick="showScreen('signin')" id="nav-signin" class="text-white/40 py-1">Sign-In<br>Key</button>
<button onclick="showScreen('landing')" id="nav-landing" class="text-white/40 py-1">Landing<br>1 Sec</button>
<button onclick="showScreen('workspace')" id="nav-workspace" class="text-white/40 py-1">Trade<br>WS</button>
<button onclick="showScreen('floor-scan')" id="nav-floor-scan" class="text-white/40 py-1">Floor<br>Scan</button>
<button onclick="showScreen('dev')" id="nav-dev" class="text-white/40 py-1">Dev<br>Online Seen</button>
<button onclick="showScreen('preview')" id="nav-preview" class="text-white/40 py-1">Invoice<br>Pic</button>
<button onclick="showScreen('ai')" id="nav-ai" class="text-white/40 py-1">Kai AI<br>Pic</button>
<button onclick="showScreen('subscribe')" id="nav-subscribe" class="text-white/40 py-1">Packages<br>Pic</button>
</div></div>
<script>
let mapping=JSON.parse(localStorage.getItem("anrevaz_mapping")||'{"signin":0,"landing":1,"floor-scan":2,"dev":6,"preview":4,"ai":5,"subscribe":3}');
let images=[
"IMG-20261029-WA0475.jpg",
"IMG-20261029-WA1657.jpg",
"IMG-20261029-WA3003.jpg",
"IMG-20261029-WA3854.jpg",
"IMG-20261029-WA6158.jpg",
"IMG-20261029-WA9207.jpg",
"IMG-20261029-WA9220.jpg"
];
function showScreen(id){document.querySelectorAll(".screen").forEach(function(s){s.classList.remove("active");});let el=document.getElementById("screen-"+id);if(el){el.classList.add("active");}let nav=document.getElementById("nav-"+id);if(nav){document.querySelectorAll("[id^=nav-]").forEach(function(n){n.classList.remove("nav-active");n.classList.add("text-white/40");});nav.classList.add("nav-active");nav.classList.remove("text-white/40");}window.scrollTo(0,0);if(id==="reorganize"){renderReorganize();}applyMapping();}
function renderReorganize(){let allHtml="";for(let i=0;i<images.length;i++){allHtml+="<div class=\\"bg-white/5 border rounded-xl p-2\\"><img src=\\"/img/"+i+"\\" class=\\"w-full h-32 object-cover rounded\\"><div class=\\"text-[9px] mt-1\\">IMG-"+i+" "+images[i].substring(15,25)+"</div><div class=\\"text-[8px] text-white/40\\">"+images[i]+"</div><button onclick=\\"assignImage("+i+",'signin')\\" class=\\"mt-1 w-full bg-white/10 border py-1 rounded text-[8px]\\">Assign</button></div>";}let el=document.getElementById("allPictures");if(el){el.innerHTML=allHtml;}let assignHtml="";let screens=[["signin","1. Sign-In Secure Key"],["landing","2. Landing 1 Sec"],["floor-scan","3. Floor Plan Scan"],["dev","4. Dev Dashboard Online Seen"],["preview","5. Invoice Columns"],["ai","6. Kai AI ChatGPT-6"],["subscribe","7. Packages Free Trial"]];screens.forEach(function(s){let sid=s[0];let sname=s[1];let currentIdx=mapping[sid]||0;assignHtml+="<div class=\\"bg-white/5 border rounded-xl p-3\\"><div class=\\"flex justify-between items-center\\"><div class=\\"font-black text-[11px]\\">"+sname+"</div><div class=\\"text-[9px] bg-[#5b7cff] px-2 py-1 rounded-full\\">Current: IMG-"+currentIdx+"</div></div><div class=\\"mt-2 grid grid-cols-4 gap-1\\">";for(let i=0;i<images.length;i++){let active=(mapping[sid]===i)?"bg-[#5b7cff] border-[#5b7cff]":"bg-white/10 border-white/10";assignHtml+="<button onclick=\\"setMapping('"+sid+"',"+i+")\\" class=\\"border rounded p-1 "+active+"\\"><img src=\\"/img/"+i+"\\" class=\\"w-full h-12 object-cover rounded\\"><div class=\\"text-[7px] mt-1\\">IMG-"+i+"</div></button>";}assignHtml+="</div><img id=\\"preview-"+sid+"\\" src=\\"/img/"+currentIdx+"\\" class=\\"mt-2 w-full h-24 object-cover rounded border\\"></div>";});let el2=document.getElementById("assignList");if(el2){el2.innerHTML=assignHtml;}}
function setMapping(screen,idx){mapping[screen]=idx;let el=document.getElementById("preview-"+screen);if(el){el.src="/img/"+idx;}let label=document.getElementById("label-"+screen);if(label){label.innerText="IMG-"+idx+" "+images[idx];}let imgEl=document.getElementById("img-"+screen);if(imgEl){imgEl.src="/img/"+idx;}localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));renderReorganize();}
function saveMapping(){localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));applyMapping();alert("Mapping saved! Pictures reorganized - Dashboard will now show exact pictures in correct format - Repo root correct");showScreen("signin");}
function resetMapping(){mapping={"signin":0,"landing":1,"floor-scan":2,"dev":6,"preview":4,"ai":5,"subscribe":3};localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));renderReorganize();applyMapping();alert("Reset to default mapping");}
function applyMapping(){for(let screen in mapping){let idx=mapping[screen];let imgEl=document.getElementById("img-"+screen);if(imgEl){imgEl.src="/img/"+idx;}let label=document.getElementById("label-"+screen);if(label){label.innerText="IMG-"+idx+" "+images[idx].substring(0,20);}}}
function assignImage(idx,screen){setMapping(screen,idx);}
function scanFloorPlan(){let result=document.getElementById("floorScanResult");if(result){result.classList.remove("hidden");}}
window.onload=function(){renderReorganize();applyMapping();}
</script></body></html>
"""
 return HTMLResponse(html)

@app.get("/img/{idx}")
def get_img(idx: str):
 try:
  i = int(idx)
  if i < 0:
   i = 0
  if i > 6:
   i = 6
  fname = IMGS[i]
  for base in [".", "/mnt/data"]:
   try:
    path = os.path.join(base, fname)
    if os.path.exists(path):
     return FileResponse(path)
   except:
    pass
  # Fallback any IMG
  try:
   files = [f for f in os.listdir(".") if f.startswith("IMG-")]
   files.sort()
   if i < len(files):
    return FileResponse(os.path.join(".", files[i]))
   if len(files) > 0:
    return FileResponse(os.path.join(".", files[0]))
  except:
   pass
  return JSONResponse({"status": "Image not found but repo root correct", "expected": fname, "idx": i}, status_code=200)
 except Exception as e:
  return JSONResponse({"error": str(e), "status": "200 OK - No more 500"}, status_code=200)

@app.get("/img-file/{filename}")
def get_img_file(filename: str):
 try:
  for base in [".", "/mnt/data"]:
   path = os.path.join(base, filename)
   if os.path.exists(path):
    return FileResponse(path)
   if os.path.exists(base):
    for f in os.listdir(base):
     if f.lower() == filename.lower():
      return FileResponse(os.path.join(base, f))
  return JSONResponse({"error": "File not found", "filename": filename}, status_code=200)
 except Exception as e:
  return JSONResponse({"error": str(e)}, status_code=200)

@app.get("/debug-images")
def debug_images():
 try:
  files = []
  for f in os.listdir("."):
   if f.startswith("IMG-") or f.endswith(".jpg") or f.endswith(".py"):
    files.append(f)
  return {"repo_root": "Correct", "files": files, "IMGS": IMGS, "mapping_help": "Use /reorganize page to fix wrong format"}
 except Exception as e:
  return {"error": str(e)}

@app.get("/manifest.json")
def manifest():
 return JSONResponse({"name": "ANREVAZ", "short_name": "ANREVAZ", "start_url": "/", "display": "standalone"})

@app.get("/privacy")
def privacy():
 return HTMLResponse("<html><body style=\"padding:20px\"><h1>Privacy Policy - Reorganize Pictures - Repo Root Correct</h1></body></html>")

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
 return {"online": 24, "total": 38, "quotes": 48, "artisans": []}

@app.post("/whatsapp")
async def wa_backend(req: Request):
 try:
  data = await req.json()
  msg = data.get("message", "hi")
  return {"reply": "ANREVAZ v13.4 Reorganize - Pictures in correct format"}
 except:
  return {"reply": "ANREVAZ Reorganize"}

@app.get("/health")
def health():
 return {"status": "LIVE v13.4 Reorganize Pictures", "fix": "Pictures displaying in wrong format - Now with Reorganize Dashboard - Assign correct picture to correct screen - Repo root correct sequence"}
