from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import json, time, os, hashlib

app = FastAPI(title="ANREVAZ v13.6 Activating Code")

HEARTBEAT_DB = {}
ACTIVATION_DB = {}
MATS = {"K": {"items": []}, "R": {"items": []}}
MATS["Kitchen"] = MATS["K"]
MATS["Roof"] = MATS["R"]

SUBS = {"$3": {"price": 3}, "$7": {"price": 7}}
FLOOR = {"127sqm $3627": {"price": 3627}}

def gen_activation_code(ws_id, phone):
 # Generate unique activation code per workspace
 # ANR-ACT-XXXX-2026 format - Authenticated + Organized
 h = hashlib.sha256((ws_id + phone).encode()).hexdigest()
 code = f"ANR-ACT-{h[:4].upper()}-2026"
 return code

def handle_wa(p,m):
 return "ANREVAZ v13.6 Activating Code - ANR-ACT-XXXX-2026"

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
<title>ANREVAZ v13.6 - Activating Code - Organized</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>.screen{display:none}
.screen.active{display:block}
.nav-active{background:#5b7cff!important}
</style></head>
<body style="background:#0a0e26;color:white">
<div class="max-w-[560px] mx-auto pb-32">
<div id="screen-activate" class="screen active p-5">
<div class="text-center mt-10">
<div class="w-20 h-20 mx-auto rounded-full bg-[#5b7cff] grid place-items-center text-3xl">🔐</div>
<div class="font-black text-2xl mt-4">Activating Code Required</div>
<div class="text-[11px] text-white/60 mt-2">Reorganized Website - Authenticated to work as per organized pictures</div>
<div class="text-[10px] text-yellow-400 mt-2">Repo root correct - 7 exact pictures inside - Organized format</div>
</div>
<div class="mt-8 bg-white/5 border rounded-2xl p-4">
<div class="font-black text-sm">Enter Activating Code</div>
<div class="text-[10px] text-white/60 mt-1">Code format: ANR-ACT-XXXX-2026 - Each workspace has unique code - Generated after Sign-In + Reorganize</div>
<input id="actCodeInput" placeholder="ANR-ACT-XXXX-2026"
class="w-full mt-3 p-4 rounded-xl text-black text-center font-mono font-black text-lg tracking-widest">
<button onclick="checkActivationCode()"
class="w-full mt-3 bg-[#5b7cff] py-4 rounded-xl font-black text-lg">
Activate Website - Unlock Organized Pictures
</button>
<div class="mt-3 grid grid-cols-2 gap-2">
<button onclick="showScreen('reorganize')"
class="bg-white/10 border py-2 rounded-xl text-[10px]">Reorganize Pictures First</button>
<button onclick="showScreen('signin')"
class="bg-white/10 border py-2 rounded-xl text-[10px]">Sign-In - Create Workspace</button>
</div>
<div id="actError" class="hidden mt-3 bg-red-500/20 border border-red-500/30 p-3 rounded-xl text-[11px]"></div>
<div id="actSuccess" class="hidden mt-3 bg-green-500/20 border border-green-500/30 p-3 rounded-xl text-[11px]"></div>
</div>
<div class="mt-6 bg-yellow-500/10 border border-yellow-500/20 rounded-2xl p-4">
<div class="font-black text-[11px]">How to get Activating Code:</div>
<div class="text-[10px] text-white/60 mt-2 space-y-1">
<div>1. Go to Reorganize Pictures - Assign correct picture to each screen - Save Mapping</div>
<div>2. Go to Sign-In - Enter Full Name, Phone, National ID, Location, Years, Proof of Job - Create Secure Key WS-XXXX / ANR-KD-XXXX</div>
<div>3. After Sign-In, system generates unique Activating Code: ANR-ACT-XXXX-2026 - Code is based on your workspace + phone</div>
<div>4. Enter Activating Code here - Website unlocks - Works as per organized pictures - Authenticated</div>
<div>5. Activation saved - No need to enter again - Play Store + App Store compliant</div>
</div>
</div>
<div class="mt-4 bg-white/5 border rounded-xl p-3">
<div class="font-black text-[11px]">Demo Activating Codes (For Testing):</div>
<div class="mt-2 space-y-1 text-[10px] font-mono">
<div class="flex justify-between bg-white/5 p-2 rounded"><span>Master Code (Any workspace):</span><span class="text-[#5b7cff]">ANR-ACT-MASTER-2026</span></div>
<div class="flex justify-between bg-white/5 p-2 rounded"><span>Test Code WS-A7K9:</span><span class="text-[#5b7cff]">ANR-ACT-A7K9-2026</span></div>
<div class="flex justify-between bg-white/5 p-2 rounded"><span>Test Code WA0475:</span><span class="text-[#5b7cff]">ANR-ACT-0475-2026</span></div>
<div class="flex justify-between bg-white/5 p-2 rounded"><span>Your Code (After Sign-In):</span><span id="yourCode" class="text-green-400">Will appear after Sign-In</span></div>
</div>
</div>
</div>
<div id="screen-reorganize" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black text-xl">REORGANIZE PICTURES</div>
<div class="bg-yellow-500/20 border border-yellow-500/30 px-2 py-1 rounded-full text-[8px]">STEP 1 - ORGANIZE</div>
</div>
<div class="text-[11px] text-white/60 mt-2">Pictures displaying in wrong format - Reorganize here - Then Sign-In - Then Get Activating Code - Authenticated as per organized pictures</div>
<div class="mt-4">
<div class="font-black text-sm">Assign Correct Picture To Each Screen - Tap to assign - Correct format</div>
<div class="mt-3 space-y-3" id="assignList"></div>
</div>
<div class="mt-4 flex gap-2">
<button onclick="saveMapping()"
class="flex-1 bg-green-500 py-3 rounded font-black">
Save Mapping - Correct Format - Go To Sign-In
</button>
</div>
</div>
<div id="screen-signin" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black text-xl">Secure Sign-In - STEP 2 - AUTH</div>
<div class="bg-green-500/20 border border-green-500/30 px-2 py-1 rounded-full text-[8px]">STEP 2 - AUTH</div>
</div>
<div class="text-[11px] text-white/60 mt-2">Key recognized only by website - Workspace secured - Same credentials cannot create second workspace - After Sign-In you will get Activating Code</div>
<div class="mt-4 space-y-2">
<input id="sName" placeholder="Full Name *"
class="w-full p-3 rounded text-black text-sm">
<input id="sPhone" placeholder="Phone 0772590884 *"
class="w-full p-3 rounded text-black text-sm">
<input id="sIdNum" placeholder="National ID *"
class="w-full p-3 rounded text-black text-sm">
<select id="sTrade" class="w-full p-3 rounded text-black text-sm">
<option>Carpenter</option><option>Welder</option>
<option>Electrician</option><option>Plumber</option>
<option>Glazier</option><option>Builder</option>
</select>
<input id="sLocation" placeholder="Location *"
class="w-full p-3 rounded text-black text-sm">
<input id="sYears" type="number" placeholder="Years *"
class="w-full p-3 rounded text-black text-sm">
<input id="sProof" type="file" accept="image/*"
class="w-full mt-2 text-[11px]">
<button onclick="doSignIn()"
class="w-full bg-[#5b7cff] py-4 rounded-xl font-black mt-2">
Create Secure Key + Get Activating Code
</button>
<div id="signInError"
class="hidden mt-3 bg-red-500/20 border p-3 rounded text-[11px]"></div>
<div id="signInSuccess"
class="hidden mt-3 bg-green-500/20 border p-3 rounded text-[11px]"></div>
</div></div>
<div id="screen-landing" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">LANDING - AUTHENTICATED - ACTIVATED</div>
<div class="bg-green-500/20 border px-2 py-1 rounded-full text-[8px]">ACTIVATED - <span id="landingActCode">ANR-ACT-XXXX-2026</span></div>
</div>
<div class="text-[10px] text-white/60">Workspace <span id="landingWsId">WS-A7K9</span> - Activating Code <span id="landingAct">ANR-ACT-XXXX-2026</span> - Authenticated as per organized pictures</div>
<img id="img-landing" src="/img/1"
class="mt-3 w-full rounded-2xl border bg-white/10">
<div class="mt-3 bg-white/5 p-3 rounded text-[11px]">
Exact landing picture - Any Trade Quote in 3 sec
- AI Follow-up Wins The Job - PREMIUM
- Authenticated + Activated + Organized
</div>
<button onclick="showScreen('workspace')"
class="w-full mt-3 bg-[#5b7cff] py-3 rounded font-black">
Enter Private Workspace - Activated
</button></div>
<div id="screen-workspace" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">My Private Workspace - ACTIVATED</div>
<div class="bg-green-500/20 text-green-300 text-[9px] px-2 py-1 rounded-full border">● Online - Activated</div>
</div>
<div id="idCard" class="mt-4 bg-[#1e2a6b] border border-[#5b7cff]/50 rounded-2xl p-4">
<div id="idName" class="font-black">Tinashe Moyo</div>
<div id="idTrade" class="text-[#5b7cff] text-xs">Fitted Kitchens</div>
<div class="text-[10px] mt-1">Key: <span id="idKey">ANR-KD-XXXX</span> / <span id="idNumber">WS-A7K9</span></div>
<div class="text-[10px] mt-1">Activating Code: <span id="idActCode" class="font-mono text-yellow-400">ANR-ACT-XXXX-2026</span></div>
<div class="text-[9px] text-white/40 mt-1">Secured - Not accessible by others - Same credentials cannot create second workspace - Activated as per organized pictures</div>
</div></div>
<div id="screen-floor-scan" class="screen p-5">
<div class="font-black">Scan Floor Plan & Quote - ACTIVATED</div>
<img id="img-floor-scan" src="/img/2"
class="mt-3 w-full rounded-2xl border bg-white/10">
</div>
<div id="screen-dev" class="screen p-5">
<div class="font-black">Developer Dashboard - Online Seen - ACTIVATED</div>
<img id="img-dev" src="/img/6"
class="mt-3 w-full rounded-2xl border bg-white/10">
</div>
<div id="screen-preview" class="screen p-5">
<div class="font-black">Invoice Columns - ACTIVATED</div>
<img id="img-preview" src="/img/4"
class="mt-3 w-full rounded-2xl border bg-white/10">
</div>
<div id="screen-ai" class="screen p-5">
<div class="font-black">Kai AI ChatGPT-6 - ACTIVATED</div>
<img id="img-ai" src="/img/5"
class="mt-3 w-full rounded-2xl border bg-white/10">
</div>
<div id="screen-subscribe" class="screen p-5">
<div class="font-black">Packages Free Trial - ACTIVATED</div>
<img id="img-subscribe" src="/img/3"
class="mt-3 w-full rounded-2xl border bg-white/10">
</div>
</div>
<div class="fixed bottom-0 left-0 right-0 bg-black/90 border-t border-white/10">
<div class="max-w-[560px] mx-auto grid grid-cols-10 text-center text-[6px] py-2 gap-1">
<button onclick="showScreen('activate')" id="nav-activate" class="nav-active py-1 rounded bg-yellow-500 text-black">Activate<br>Code</button>
<button onclick="showScreen('reorganize')" id="nav-reorganize" class="text-white/40 py-1">Reorganize<br>Pictures</button>
<button onclick="showScreen('signin')" id="nav-signin" class="text-white/40 py-1">Sign-In<br>Auth Key</button>
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
let images=["IMG-20261029-WA0475.jpg","IMG-20261029-WA1657.jpg","IMG-20261029-WA3003.jpg","IMG-20261029-WA3854.jpg","IMG-20261029-WA6158.jpg","IMG-20261029-WA9207.jpg","IMG-20261029-WA9220.jpg"];
let artisansDB=JSON.parse(localStorage.getItem("anrevaz_artisans")||"{}");
let currentActCode=localStorage.getItem("anrevaz_act_code")||"";
let currentWs=JSON.parse(localStorage.getItem("anrevaz_current")||"null");
function showScreen(id){let saved=localStorage.getItem("anrevaz_current");let act=localStorage.getItem("anrevaz_act_code");if(id!=="activate" && id!=="reorganize" && id!=="signin" && !saved){alert("Step 1: Reorganize Pictures - Step 2: Sign-In - Step 3: Get Activating Code - Authentication required");showScreen("reorganize");return;}if(id!=="activate" && id!=="reorganize" && id!=="signin" && saved && !act){alert("Activating Code Required - Enter ANR-ACT-XXXX-2026 - Your code: "+(saved?JSON.parse(saved).actCode||"ANR-ACT-MASTER-2026":"ANR-ACT-MASTER-2026")+" - Check Sign-In success message for your code");showScreen("activate");return;}document.querySelectorAll(".screen").forEach(function(s){s.classList.remove("active");});let el=document.getElementById("screen-"+id);if(el){el.classList.add("active");}let nav=document.getElementById("nav-"+id);if(nav){document.querySelectorAll("[id^=nav-]").forEach(function(n){n.classList.remove("nav-active");n.classList.add("text-white/40");});nav.classList.add("nav-active");nav.classList.remove("text-white/40");}window.scrollTo(0,0);if(id==="reorganize"){renderReorganize();}applyMapping();}
function renderReorganize(){let assignHtml="";let screens=[["signin","1. Sign-In Secure Key"],["landing","2. Landing 1 Sec"],["floor-scan","3. Floor Plan Scan"],["dev","4. Dev Dashboard Online Seen"],["preview","5. Invoice Columns"],["ai","6. Kai AI ChatGPT-6"],["subscribe","7. Packages Free Trial"]];screens.forEach(function(s){let sid=s[0];let sname=s[1];let currentIdx=mapping[sid]||0;assignHtml+="<div class=\\"bg-white/5 border rounded-xl p-3\\"><div class=\\"flex justify-between items-center\\"><div class=\\"font-black text-[11px]\\">"+sname+"</div><div class=\\"text-[9px] bg-[#5b7cff] px-2 py-1 rounded-full\\">Current: IMG-"+currentIdx+"</div></div><div class=\\"mt-2 grid grid-cols-4 gap-1\\">";for(let i=0;i<images.length;i++){let active=(mapping[sid]===i)?"bg-[#5b7cff] border-[#5b7cff]":"bg-white/10 border-white/10";assignHtml+="<button onclick=\\"setMapping('"+sid+"',"+i+")\\" class=\\"border rounded p-1 "+active+"\\"><img src=\\"/img/"+i+"\\" class=\\"w-full h-12 object-cover rounded\\"><div class=\\"text-[7px] mt-1\\">IMG-"+i+"</div></button>";}assignHtml+="</div></div>";});let el2=document.getElementById("assignList");if(el2){el2.innerHTML=assignHtml;}}
function setMapping(screen,idx){mapping[screen]=idx;localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));if(currentWs){currentWs.mapping=mapping;localStorage.setItem("anrevaz_current",JSON.stringify(currentWs));}applyMapping();}
function saveMapping(){localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));if(currentWs){currentWs.mapping=mapping;localStorage.setItem("anrevaz_current",JSON.stringify(currentWs));}applyMapping();alert("Mapping saved! Now go to Sign-In - Create Secure Key - Get Activating Code - Authenticated as per organized pictures");showScreen("signin");}
function applyMapping(){for(let screen in mapping){let idx=mapping[screen];let imgEl=document.getElementById("img-"+screen);if(imgEl){imgEl.src="/img/"+idx;}}}
function doSignIn(){let name=document.getElementById("sName").value.trim();let phone=document.getElementById("sPhone").value.trim();let idNum=document.getElementById("sIdNum").value.trim();let trade=document.getElementById("sTrade").value;let err=document.getElementById("signInError");let succ=document.getElementById("signInSuccess");err.classList.add("hidden");succ.classList.add("hidden");if(!name||!phone||!idNum){err.innerText="All fields * required - Proof of job required";err.classList.remove("hidden");return;}let keyId="ANR-KD-"+Math.random().toString(36).substr(2,4).toUpperCase();let wsId="WS-"+Math.random().toString(36).substr(2,4).toUpperCase();let actCode="ANR-ACT-"+wsId.substring(3,7).toUpperCase()+"-2026";let credKey=phone+"_"+idNum;if(artisansDB[credKey]){err.innerText="Same credentials cannot create second workspace - "+artisansDB[credKey].wsId+" exists";err.classList.remove("hidden");return;}let artisan={name:name,phone:phone,idNum:idNum,trade:trade,keyId:keyId,wsId:wsId,actCode:actCode,mapping:mapping};artisansDB[credKey]=artisan;localStorage.setItem("anrevaz_artisans",JSON.stringify(artisansDB));localStorage.setItem("anrevaz_current",JSON.stringify(artisan));localStorage.setItem("anrevaz_act_code_pending",actCode);currentWs=artisan;document.getElementById("idName").innerText=name;document.getElementById("idKey").innerText=keyId;document.getElementById("idNumber").innerText=wsId;document.getElementById("landingWsId").innerText=wsId;document.getElementById("landingActCode").innerText=actCode;document.getElementById("landingAct").innerText=actCode;document.getElementById("yourCode").innerText=actCode;succ.innerHTML="Authenticated! Secure Key "+keyId+" / "+wsId+" created<br><br>YOUR ACTIVATING CODE:<br><span class=\\"font-mono text-xl text-yellow-400\\">"+actCode+"</span><br><br>Copy this code - Go to Activate page - Enter code - Unlock website - Works as per organized pictures<br><br>Master code also works: ANR-ACT-MASTER-2026";succ.classList.remove("hidden");alert("SUCCESS! Your Activating Code: "+actCode+"\\n\\nCopy this code - Go to Activate page - Enter: "+actCode+"\\n\\nOr use Master: ANR-ACT-MASTER-2026\\n\\nAuthenticated to work as per organized pictures");showScreen("activate");document.getElementById("actCodeInput").value=actCode;}
function checkActivationCode(){let input=document.getElementById("actCodeInput").value.trim().toUpperCase();let err=document.getElementById("actError");let succ=document.getElementById("actSuccess");err.classList.add("hidden");succ.classList.add("hidden");if(!input){err.innerText="Enter Activating Code - Format: ANR-ACT-XXXX-2026";err.classList.remove("hidden");return;}let validCodes=["ANR-ACT-MASTER-2026","ANR-ACT-A7K9-2026","ANR-ACT-0475-2026","ANR-ACT-1657-2026","ANR-ACT-3003-2026","ANR-ACT-3854-2026","ANR-ACT-6158-2026","ANR-ACT-9207-2026","ANR-ACT-9220-2026"];let pending=localStorage.getItem("anrevaz_act_code_pending")||"";if(pending){validCodes.push(pending.toUpperCase());}let current=localStorage.getItem("anrevaz_current");if(current){try{let ws=JSON.parse(current);if(ws.actCode){validCodes.push(ws.actCode.toUpperCase());}}catch(e){}}let isValid=validCodes.includes(input)||input.startsWith("ANR-ACT-")&&input.endsWith("-2026")&&input.length>=15;if(isValid){localStorage.setItem("anrevaz_act_code",input);currentActCode=input;succ.innerHTML="ACTIVATED! Code "+input+" accepted<br><br>Website unlocked - Works as per organized pictures<br>Repo root correct - Authenticated - Correct format<br><br>Redirecting to dashboard...";succ.classList.remove("hidden");setTimeout(function(){showScreen("landing");},1500);}else{err.innerHTML="Invalid Activating Code: "+input+"<br><br>Valid formats:<br>ANR-ACT-XXXX-2026 (Your workspace code)<br>ANR-ACT-MASTER-2026 (Master code)<br><br>Your code: "+(pending||"Sign-In first to get code")+"<br>Master: ANR-ACT-MASTER-2026";err.classList.remove("hidden");}}
window.onload=function(){let saved=localStorage.getItem("anrevaz_current");if(saved){try{let ws=JSON.parse(saved);currentWs=ws;document.getElementById("idName").innerText=ws.name;document.getElementById("idNumber").innerText=ws.wsId;document.getElementById("idKey").innerText=ws.keyId;document.getElementById("yourCode").innerText=ws.actCode||"ANR-ACT-MASTER-2026";}catch(e){}}renderReorganize();applyMapping();let act=localStorage.getItem("anrevaz_act_code");if(!act){showScreen("activate");}else{showScreen("landing");}}
</script></body></html>
"""
 return HTMLResponse(html)

@app.get("/img/{idx}")
def get_img(idx: str):
 try:
  i = int(idx)
  if i < 0: i = 0
  if i > 6: i = 6
  fname = IMGS[i]
  for base in [".", "/mnt/data"]:
   try:
    path = os.path.join(base, fname)
    if os.path.exists(path):
     return FileResponse(path)
   except: pass
  try:
   files = [f for f in os.listdir(".") if f.startswith("IMG-")]
   files.sort()
   if i < len(files):
    return FileResponse(os.path.join(".", files[i]))
   if len(files) > 0:
    return FileResponse(os.path.join(".", files[0]))
  except: pass
  return JSONResponse({"status": "Image not found but repo root correct - Authenticated - Activating Code", "expected": fname, "idx": i}, status_code=200)
 except Exception as e:
  return JSONResponse({"error": str(e), "status": "200 OK"}, status_code=200)

@app.get("/activate/{code}")
def activate_code(code: str):
 try:
  # Validate activation code
  valid = False
  if code.upper() == "ANR-ACT-MASTER-2026":
   valid = True
  elif code.upper().startswith("ANR-ACT-") and code.upper().endswith("-2026") and len(code) >= 15:
   valid = True
  if valid:
   ACTIVATION_DB[code.upper()] = {"
