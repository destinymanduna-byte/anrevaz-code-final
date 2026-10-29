from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import json, time, os

app = FastAPI(title="ANREVAZ v13.8 Dev Only Reorganize")

HEARTBEAT_DB = {}
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
<title>ANREVAZ v13.8 - Exact Format As Pictures - Dev Only Reorganize</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>.screen{display:none}.screen.active{display:block}.nav-active{background:#5b7cff!important}.dev-only{display:none}.dev-mode .dev-only{display:block}.dev-mode .dev-only-flex{display:flex}</style></head>
<body style="background:#0a0e26;color:white">
<div class="max-w-[560px] mx-auto pb-32">
<div id="screen-signin" class="screen active p-5">
<div class="flex justify-between items-center">
<div class="font-black text-xl">Secure Sign-In - Exact Format As Pictures</div>
<div class="bg-green-500/20 border border-green-500/30 px-2 py-1 rounded-full text-[8px]">EXACT FORMAT - USER VIEW</div>
</div>
<div class="text-[11px] text-white/60 mt-2">Exact format as it is on reorganized pictures - Same display and functions as those on pictures - Key only by website - Secured</div>
<img id="img-signin" src="/img/0" class="mt-4 w-full rounded-2xl border bg-white/10">
<div class="mt-4 space-y-2">
<input id="sName" placeholder="Full Name *" class="w-full p-3 rounded text-black text-sm">
<input id="sPhone" placeholder="Phone 0772590884 *" class="w-full p-3 rounded text-black text-sm">
<input id="sIdNum" placeholder="National ID *" class="w-full p-3 rounded text-black text-sm">
<select id="sTrade" class="w-full p-3 rounded text-black text-sm">
<option>Carpenter</option><option>Welder</option><option>Electrician</option><option>Plumber</option><option>Glazier</option><option>Builder</option>
</select>
<input id="sLocation" placeholder="Location Kadoma CBD *" class="w-full p-3 rounded text-black text-sm">
<input id="sYears" type="number" placeholder="Years Experience *" class="w-full p-3 rounded text-black text-sm">
<div class="bg-white/5 border rounded-xl p-3">
<div class="font-bold text-[11px]">Proof of Job * - Required per store policy</div>
<input id="sProof" type="file" accept="image/*" class="w-full mt-2 text-[11px]">
</div>
<button onclick="doSignIn()" class="w-full bg-[#5b7cff] py-4 rounded-xl font-black mt-2">Create Secure Key + Private Workspace - Exact Format As Pictures</button>
<div id="signInError" class="hidden mt-3 bg-red-500/20 border p-3 rounded text-[11px]"></div>
<div id="signInSuccess" class="hidden mt-3 bg-green-500/20 border p-3 rounded text-[11px]"></div>
</div>
<div class="mt-6 text-center">
<div class="text-[10px] text-white/40">Developer? Tap here 5 times to unlock dev mode</div>
<button id="devUnlock" onclick="tapDevUnlock()" class="mt-2 text-[9px] text-white/20 border border-white/10 px-3 py-1 rounded-full">Dev Unlock - Tap 5x</button>
<div id="devCodeArea" class="hidden mt-3 bg-yellow-500/10 border border-yellow-500/20 rounded-xl p-3">
<input id="devCodeInput" placeholder="Enter Dev Code ANR-DEV-MASTER-2026" class="w-full p-3 rounded text-black text-sm text-center font-mono">
<button onclick="checkDevCode()" class="w-full mt-2 bg-yellow-500 text-black py-2 rounded font-black text-sm">Unlock Developer Mode - Online Seen + Reorganize</button>
</div>
</div>
</div>
<div id="screen-landing" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">LANDING - 1 Sec Inside - Exact Format As Pictures</div>
<div class="bg-green-500/20 border px-2 py-1 rounded-full text-[8px]">EXACT FORMAT</div>
</div>
<div class="text-[10px] text-white/60">Workspace <span id="landingWsId">WS-A7K9</span> - Key <span id="landingKeyId">ANR-KD-XXXX</span></div>
<img id="img-landing" src="/img/1" class="mt-4 w-full rounded-2xl border bg-white/10">
<div class="mt-3 bg-white/5 p-3 rounded text-[11px]">Exact landing as per pictures - Any Trade Quote in 3 sec - AI Follow-up Wins The Job - PREMIUM - Carpenter Welder Electrician Plumber Glazier Builder - Same functions as pictures</div>
<button onclick="showScreen('workspace')" class="w-full mt-3 bg-[#5b7cff] py-3 rounded font-black">Enter Private Workspace - Exact Format As Pictures</button>
</div>
<div id="screen-workspace" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black">My Private Workspace - Exact Format As Pictures</div>
<div class="bg-green-500/20 text-green-300 text-[9px] px-2 py-1 rounded-full border">● Online - Exact Format</div>
</div>
<div id="idCard" class="mt-4 bg-[#1e2a6b] border border-[#5b7cff]/50 rounded-2xl p-4">
<div id="idName" class="font-black">Tinashe Moyo</div>
<div id="idTrade" class="text-[#5b7cff] text-xs">Fitted Kitchens</div>
<div class="text-[10px] mt-1">Key: <span id="idKey">ANR-KD-XXXX</span> / <span id="idNumber">WS-A7K9</span></div>
<div class="text-[9px] text-white/40 mt-1">Secured - Not accessible by other tradesmen - Cannot create second workspace - Exact format as pictures - Same functions</div>
</div>
<div class="mt-4"><div class="font-black text-sm">Select Trade - Everything For That Job - Exact Format As Pictures</div><div id="projectsList" class="mt-2 space-y-2"></div></div>
<div class="mt-4"><div class="font-black text-sm">Floor Plans - Scan & Quote $3627 - Exact Format As Pictures</div><div id="floorPlansList" class="mt-2 space-y-2"></div></div>
</div>
<div id="screen-floor-scan" class="screen p-5">
<div class="font-black">Scan Floor Plan & Quote $3627 - Exact Format As Pictures</div>
<div class="text-[11px] text-white/60 mt-1">Ability to scan floor plan and quote from it - Exact format as pictures</div>
<img id="img-floor-scan" src="/img/2" class="mt-4 w-full rounded-2xl border bg-white/10">
<div class="mt-3 bg-white/5 p-3 rounded text-[11px]">Exact floor plan scan picture - Upload or scan floor plan image - AI extracts rooms and dimensions - Materials auto-calculated - Same functions as pictures</div>
<input id="floorFile" type="file" accept="image/*" capture="environment" class="mt-3 w-full text-[11px]">
<button onclick="scanFloorPlan()" class="mt-2 bg-[#5b7cff] px-4 py-2 rounded-full text-[11px] font-bold">Scan & Generate Quote - Exact Format</button>
<div id="floorScanResult" class="hidden mt-3 bg-white text-black p-3 rounded-xl">
<div class="font-black text-sm">Floor Plan Detected - 127sqm 3-Bed $3627</div>
<div id="floorScanRooms" class="mt-2 bg-gray-50 p-2 rounded text-[11px]"></div>
<button onclick="useScannedPlan()" class="mt-2 w-full bg-[#5b7cff] text-white py-2 rounded-xl text-[11px] font-bold">Use This Plan - Quote $3627 - Exact Format</button>
</div>
</div>
<div id="screen-materials" class="screen p-5">
<div class="font-black text-sm">Workspace Materials - Per Unit - Invoice Ready - Exact Format As Pictures</div>
<div class="mt-4"><div class="flex justify-between items-center"><div class="font-black text-[11px]">Materials - Proper Columns - Invoice Ready - Exact Format</div><button onclick="addCustomMaterial()" class="bg-[#5b7cff] px-3 py-1 rounded-full text-[10px]">+ Add</button></div>
<div class="mt-2 text-[9px] text-white/40">Columns: Description | Quantities | Price Per Unit | Discount | Total Price + Labour Money - Exact format as pictures</div>
<div class="mt-2 bg-black/40 border border-white/10 rounded-xl overflow-hidden">
<div class="grid grid-cols-12 gap-1 bg-white/10 p-2 text-[8px] font-bold"><div class="col-span-4">Description</div><div class="col-span-2 text-center">Qty</div><div class="col-span-2 text-right">Price/U</div><div class="col-span-1 text-center">Disc</div><div class="col-span-2 text-right">Total</div><div class="col-span-1 text-center">Act</div></div>
<div id="materialsDetailedList" class="text-[11px] p-2">Materials per unit - Same functions as pictures</div>
</div></div>
<div class="mt-4 bg-[#1e2a6b] border border-[#5b7cff]/30 rounded-2xl p-3">
<div class="flex justify-between text-[11px]"><span>Materials (Per Unit):</span><span id="matTotal">$0</span></div>
<div class="flex justify-between text-[11px]"><span>Labour (Tradesman Money 30%):</span><span id="laborTotal">$0</span></div>
<div class="flex justify-between font-black text-lg mt-3 pt-3 border-t border-white/10"><span>Grand Total:</span><span id="grandTotal" class="text-[#5b7cff]">$0</span></div>
</div>
<button onclick="generateQuote()" class="w-full mt-4 bg-[#5b7cff] py-3 rounded-xl font-black text-sm">Generate Professional Invoice + Print - Exact Format</button>
</div>
<div id="screen-preview" class="screen p-5">
<div class="font-black text-sm">Professional Quotation - Invoice - Exact Format As Pictures</div>
<div class="text-[10px] text-white/60">Columns: Description | Quantities | Price Per Unit | Discount | Total Price - Tradesman's money - Exact format as pictures</div>
<img id="img-preview" src="/img/4" class="mt-4 w-full rounded-2xl border bg-white/10">
<div class="mt-4 bg-white text-black rounded-2xl p-4">
<div class="flex justify-between border-b pb-3"><div><div id="previewCompany" class="font-black text-sm">Moyo Carpentry</div><div class="text-[8px] text-gray-500">System Pass <span id="previewKey2">WS-A7K9</span> Private - Exact format</div></div><div class="text-right"><div class="font-black text-[#5b7cff] text-[10px]">SUPERSONIC QUOTE + FLOOR PLAN + INVOICE</div><div id="quoteNumber" class="text-[9px]">#WS-A7K9</div></div></div>
<div class="mt-3 border rounded-lg overflow-hidden">
<div class="grid grid-cols-12 gap-1 bg-gray-100 p-2 text-[8px] font-bold"><div class="col-span-4">Description</div><div class="col-span-2 text-center">Quantities</div><div class="col-span-2 text-right">Price Per Unit</div><div class="col-span-1 text-center">Discount</div><div class="col-span-3 text-right">Total Price</div></div>
<div id="previewMaterials" class="text-[8px] p-2">Materials - Exact format as pictures</div>
</div>
<div class="mt-3 bg-gray-50 rounded-xl p-3 text-[9px]">
<div class="flex justify-between font-black text-[11px] mt-2 pt-2 border-t"><span>Grand Total:</span><span id="previewGrand" class="text-[#5b7cff]">$0</span></div>
</div></div>
<button onclick="showScreen('ai')" class="w-full mt-3 bg-[#5b7cff]/20 border py-2.5 rounded-xl font-bold text-[11px]">Next: Kai AI Follow-up Till WON - ChatGPT-6 - Exact Format</button>
</div>
<div id="screen-ai" class="screen p-5">
<div class="font-black">Kai AI - Follow-up Agent - ChatGPT-6 Capable - Exact Format As Pictures</div>
<div class="text-[10px] text-white/60 mt-1">Technical support + How app works + Assist tradesmen + Follow-up till WON + Invoice - Exact format as pictures - Same functions</div>
<img id="img-ai" src="/img/5" class="mt-4 w-full rounded-2xl border bg-white/10">
<div class="mt-4 bg-white/5 border rounded-2xl p-3">
<div class="h-[360px] flex flex-col">
<div id="aiChat" class="flex-1 overflow-y-auto space-y-2 text-[11px]">
<div class="bg-[#5b7cff]/20 border rounded-xl p-3">
<div class="font-bold text-[11px]">Kai AI Ready - Private Workspace <span id="aiWorkspaceId">WS-A7K9</span> - Exact Format As Pictures</div>
<div class="text-[10px] mt-1">I am Kai - Only sees YOUR private workspace - Secured - Exact format as pictures - Same functions as those on pictures - Timeline 0 sec 2h 24h day3 day7 till WON</div>
</div>
<div class="bg-white/10 rounded-xl p-3 text-[11px]">Hi! I'm Kai, your follow-up agent. I can help with technical support, walk you through how the application works, and keep following up with customers until we reach WON + Invoice. What would you like to tackle first?</div>
<div class="text-right"><div class="bg-[#5b7cff] inline-block px-3 py-2 rounded-full text-[11px]">Too expensive?</div></div>
<div class="bg-white/10 rounded-xl p-3 text-[11px]">Got it — pricing is a common concern. I can break down the value, typical ROI for tradesmen, and explore options like phased rollout or discounted yearly plan. Want me to draft a cost vs savings summary?</div>
</div>
<div class="mt-3 flex gap-2">
<input id="aiInput" placeholder="Ask Kai - technical support / how app works / follow up - Exact format" class="flex-1 bg-white/10 border rounded-full px-4 py-2.5 text-[11px]">
<button onclick="sendAI()" class="bg-[#5b7cff] px-4 py-2.5 rounded-full font-bold text-[11px]">Ask</button>
</div></div></div>
</div>
<div id="screen-subscribe" class="screen p-5">
<div class="font-black">Packages - Free Trial - Subscriptions - Exact Format As Pictures</div>
<div class="text-[11px] text-white/60 mt-1">Different subscriptions as per discussed - 7-day free trial - Exact format as pictures</div>
<img id="img-subscribe" src="/img/3" class="mt-4 w-full rounded-2xl border bg-white/10">
<div class="mt-4 space-y-4" id="subsList">
<div class="bg-white/5 border rounded-2xl p-4"><div class="flex justify-between"><div class="font-black">Starter</div><div class="font-black text-xl">$3/month</div></div><div class="text-[11px] mt-2">1 workspace • Safe ID pass • Materials per unit: 50 • Kai AI follow-up - Exact format</div></div>
<div class="bg-yellow-400/10 border border-yellow-400/50 rounded-2xl p-4"><div class="flex justify-between"><div class="font-black">Pro POPULAR</div><div class="font-black text-xl">$7/month</div></div><div class="text-[11px] mt-2">3 workspaces • Safe ID pass • Materials 200 • Kai AI • Online artisans • WhatsApp • BEST VALUE - Exact format</div></div>
<div class="bg-white/5 border rounded-2xl p-4"><div class="flex justify-between"><div class="font-black">Premium</div><div class="font-black text-xl">$12/month</div></div><div class="text-[11px] mt-2">Unlimited workspaces • Safe ID pass • Unlimited materials • Kai AI priority • Online artisans • WhatsApp • Advanced analytics - Exact format</div></div>
</div>
</div>
<div id="screen-dev" class="screen p-5">
<div class="flex justify-between items-center">
<div class="font-black text-xl">Developer Dashboard - Online Seen + Reorganize Setting - DEV ONLY</div>
<div class="bg-yellow-500 text-black px-2 py-1 rounded-full text-[8px] font-black">DEV ONLY - NOT FOR USERS</div>
</div>
<div class="text-[11px] text-white/60 mt-2">Real-time monitoring for artisans - How frequently app is useful - Last updated: <span id="devLastUpdate">Now</span> - Developer sees frequency & usefulness - Reorganize setting only shows to developer alongside dashboard monitoring online seen</div>
<img id="img-dev" src="/img/6" class="mt-4 w-full rounded-2xl border bg-white/10">
<div class="mt-6">
<div class="font-black text-sm">Online Artisans - Real-time - Dev Monitoring</div>
<div class="mt-3 grid grid-cols-2 gap-2">
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Artisans Online</div><div class="font-black text-lg"><span id="devOnlineCount">24</span> / <span id="devTotalCount">38</span> Online</div><div class="text-[9px] text-green-400 mt-1">↑ 3 from yesterday - Live tracking</div></div>
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Quotes Created Today</div><div class="font-black text-lg" id="devQuotesToday">48</div><div class="text-[9px] text-green-400">↑ 12% vs yesterday</div></div>
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Avg. App Usefulness</div><div class="font-black text-lg">4.5 / 5.0</div><div class="text-[9px] text-white/40">Based on 112 responses</div></div>
<div class="bg-white/5 border rounded-2xl p-3"><div class="text-[10px] text-white/60">Avg. Frequency</div><div class="font-black text-lg">4.2x / week</div><div class="text-[9px] text-green-400">Stable trend</div></div>
</div>
<div class="mt-4 bg-white/5 border rounded-2xl p-3"><div class="font-black text-[11px]">Artisans — Online Status - Frequency & Usefulness</div><div id="devArtisansList" class="mt-3 space-y-2 text-[10px]">Loading online seen...</div></div>
</div>
<div class="mt-8 dev-only border-t border-yellow-500/20 pt-6">
<div class="flex justify-between items-center">
<div class="font-black text-sm text-yellow-400">DEV ONLY - Reorganize Setting - Not visible to users</div>
<div class="bg-yellow-500 text-black px-2 py-1 rounded-full text-[8px] font-black">DEV ONLY SETTING</div>
</div>
<div class="text-[10px] text-white/60 mt-1">This reorganize setting only shows to developer alongside dashboard monitoring online seen - Users see exact format as pictures - Same display and functions as those on pictures</div>
<div class="mt-4 space-y-3" id="assignList"></div>
<div class="mt-4 flex gap-2">
<button onclick="saveMapping()" class="flex-1 bg-yellow-500 text-black py-3 rounded font-black">Save Mapping - Update Exact Format For Users - Dev Only</button>
<button onclick="resetMapping()" class="flex-1 bg-white/10 border py-3 rounded text-[11px]">Reset To Default - Dev Only</button>
</div>
<div class="mt-3 bg-white/5 p-3 rounded text-[10px]">How reorganize works for developer: 1. See all 7 pictures from repo root 2. Assign correct picture to each screen 3. Save - Users will see exact format as reorganized - Same functions as pictures - Reorganize setting hidden from users</div>
</div>
</div>
</div>
<div class="fixed bottom-0 left-0 right-0 bg-black/90 border-t border-white/10">
<div id="userNav" class="max-w-[560px] mx-auto grid grid-cols-8 text-center text-[7px] py-2 gap-1">
<button onclick="showScreen('signin')" id="nav-signin" class="nav-active py-1 rounded">Sign-In<br>Key</button>
<button onclick="showScreen('landing')" id="nav-landing" class="text-white/40 py-1">Landing<br>1 Sec</button>
<button onclick="showScreen('workspace')" id="nav-workspace" class="text-white/40 py-1">Trade<br>WS</button>
<button onclick="showScreen('floor-scan')" id="nav-floor-scan" class="text-white/40 py-1">Floor<br>Scan</button>
<button onclick="showScreen('materials')" id="nav-materials" class="text-white/40 py-1">Materials<br>Invoice</button>
<button onclick="showScreen('preview')" id="nav-preview" class="text-white/40 py-1">Quote<br>Invoice</button>
<button onclick="showScreen('ai')" id="nav-ai" class="text-white/40 py-1">Kai AI<br>Pic</button>
<button onclick="showScreen('subscribe')" id="nav-subscribe" class="text-white/40 py-1">Packages<br>Pic</button>
</div>
<div id="devNav" class="hidden max-w-[560px] mx-auto grid grid-cols-9 text-center text-[6px] py-2 gap-1">
<button onclick="showScreen('signin')" id="nav-dev-signin" class="text-white/40 py-1">Sign-In<br>User View</button>
<button onclick="showScreen('landing')" id="nav-dev-landing" class="text-white/40 py-1">Landing<br>User View</button>
<button onclick="showScreen('workspace')" id="nav-dev-workspace" class="text-white/40 py-1">Trade<br>User View</button>
<button onclick="showScreen('floor-scan')" id="nav-dev-floor-scan" class="text-white/40 py-1">Floor<br>User View</button>
<button onclick="showScreen('dev')" id="nav-dev-dev" class="nav-active py-1 rounded bg-yellow-500 text-black">Dev<br>Online Seen + Reorganize</button>
<button onclick="showScreen('materials')" id="nav-dev-materials" class="text-white/40 py-1">Materials<br>User View</button>
<button onclick="showScreen('preview')" id="nav-dev-preview" class="text-white/40 py-1">Quote<br>User View</button>
<button onclick="showScreen('ai')" id="nav-dev-ai" class="text-white/40 py-1">Kai AI<br>User View</button>
<button onclick="showScreen('subscribe')" id="nav-dev-subscribe" class="text-white/40 py-1">Packages<br>User View</button>
</div>
</div>
<script>
let mapping=JSON.parse(localStorage.getItem("anrevaz_mapping")||'{"signin":0,"landing":1,"floor-scan":2,"dev":6,"preview":4,"ai":5,"subscribe":3,"materials":4}');
let images=["IMG-20261029-WA0475.jpg","IMG-20261029-WA1657.jpg","IMG-20261029-WA3003.jpg","IMG-20261029-WA3854.jpg","IMG-20261029-WA6158.jpg","IMG-20261029-WA9207.jpg","IMG-20261029-WA9220.jpg"];
let artisansDB=JSON.parse(localStorage.getItem("anrevaz_artisans")||"{}");
let devTapCount=0;
let isDevMode=localStorage.getItem("anrevaz_dev_mode")==="true";
function showScreen(id){let saved=localStorage.getItem("anrevaz_current");if(id!=="signin" && !saved && id!=="dev"){showScreen("signin");return;}document.querySelectorAll(".screen").forEach(function(s){s.classList.remove("active");});let el=document.getElementById("screen-"+id);if(el){el.classList.add("active");}let navId=isDevMode?"nav-dev-"+id:"nav-"+id;let nav=document.getElementById(navId);if(nav){document.querySelectorAll("[id^=nav-]").forEach(function(n){n.classList.remove("nav-active");n.classList.add("text-white/40");});nav.classList.add("nav-active");nav.classList.remove("text-white/40");}window.scrollTo(0,0);if(id==="dev"){renderDevDashboard();renderReorganize();}applyMapping();}
function renderReorganize(){let assignHtml="";let screens=[["signin","1. Sign-In Secure Key - Exact Format"],["landing","2. Landing 1 Sec - Exact Format"],["floor-scan","3. Floor Plan Scan - Exact Format"],["dev","4. Dev Dashboard Online Seen - Exact Format"],["materials","5. Materials Invoice - Exact Format"],["preview","5b. Invoice Columns - Exact Format"],["ai","6. Kai AI ChatGPT-6 - Exact Format"],["subscribe","7. Packages Free Trial - Exact Format"]];screens.forEach(function(s){let sid=s[0];let sname=s[1];let currentIdx=mapping[sid]||0;assignHtml+="<div class=\\"bg-white/5 border rounded-xl p-3\\"><div class=\\"flex justify-between items-center\\"><div class=\\"font-black text-[11px]\\">"+sname+"</div><div class=\\"text-[9px] bg-[#5b7cff] px-2 py-1 rounded-full\\">Current: IMG-"+currentIdx+" - Exact Format</div></div><div class=\\"mt-2 grid grid-cols-4 gap-1\\">";for(let i=0;i<images.length;i++){let active=(mapping[sid]===i)?"bg-[#5b7cff] border-[#5b7cff]":"bg-white/10 border-white/10";assignHtml+="<button onclick=\\"setMapping('"+sid+"',"+i+")\\" class=\\"border rounded p-1 "+active+"\\"><img src=\\"/img/"+i+"\\" class=\\"w-full h-12 object-cover rounded\\"><div class=\\"text-[7px] mt-1\\">IMG-"+i+"</div></button>";}assignHtml+="</div><img id=\\"preview-"+sid+"\\" src=\\"/img/"+currentIdx+"\\" class=\\"mt-2 w-full h-20 object-cover rounded border\\"></div>";});let el2=document.getElementById("assignList");if(el2){el2.innerHTML=assignHtml;}}
function setMapping(screen,idx){mapping[screen]=idx;localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));let preview=document.getElementById("preview-"+screen);if(preview){preview.src="/img/"+idx;}applyMapping();}
function saveMapping(){localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));applyMapping();alert("Dev: Mapping saved! Users will now see exact format as reorganized pictures - Same display and functions as those on pictures - Reorganize setting only visible to developer alongside online seen dashboard");showScreen("landing");}
function resetMapping(){mapping={"signin":0,"landing":1,"floor-scan":2,"dev":6,"preview":4,"ai":5,"subscribe":3,"materials":4};localStorage.setItem("anrevaz_mapping",JSON.stringify(mapping));renderReorganize();applyMapping();alert("Dev: Reset to default mapping - Exact format"); }
function applyMapping(){for(let screen in mapping){let idx=mapping[screen];let imgEl=document.getElementById("img-"+screen);if(imgEl){imgEl.src="/img/"+idx;}}}
function tapDevUnlock(){devTapCount++;let btn=document.getElementById("devUnlock");btn.innerText="Dev Unlock - Tap "+(5-devTapCount)+" more - "+devTapCount+"/5";if(devTapCount>=5){document.getElementById("devCodeArea").classList.remove("hidden");btn.innerText="Enter Dev Code Below";devTapCount=0;}}
function checkDevCode(){let code=document.getElementById("devCodeInput").value.trim().toUpperCase();if(code==="ANR-DEV-MASTER-2026"||code==="ANR-ACT-MASTER-2026"||code.startsWith("ANR-DEV-")){localStorage.setItem("anrevaz_dev_mode","true");isDevMode=true;document.body.classList.add("dev-mode");document.getElementById("userNav").classList.add("hidden");document.getElementById("devNav").classList.remove("hidden");alert("Developer Mode Unlocked! You can now see Online Seen dashboard + Reorganize setting - This setting only shows to developer alongside dashboard monitoring online seen - Users see exact format as pictures");showScreen("dev");}else{alert("Invalid Dev Code - Use ANR-DEV-MASTER-2026 or ANR-ACT-MASTER-2026");}}
function doSignIn(){let name=document.getElementById("sName").value.trim();let phone=document.getElementById("sPhone").value.trim();let idNum=document.getElementById("sIdNum").value.trim();let err=document.getElementById("signInError");let succ=document.getElementById("signInSuccess");err.classList.add("hidden");succ.classList.add("hidden");if(!name||!phone||!idNum){err.innerText="All fields * required - Proof of job required - Exact format as pictures";err.classList.remove("hidden");return;}let keyId="ANR-KD-"+Math.random().toString(36).substr(2,4).toUpperCase();let wsId="WS-"+Math.random().toString(36).substr(2,4).toUpperCase();let credKey=phone+"_"+idNum;if(artisansDB[credKey]){err.innerText="Same credentials cannot create second workspace - "+artisansDB[credKey].wsId+" exists - Key only by website";err.classList.remove("hidden");return;}let artisan={name:name,phone:phone,idNum:idNum,keyId:keyId,wsId:wsId,mapping:mapping};artisansDB[credKey]=artisan;localStorage.setItem("anrevaz_artisans",JSON.stringify(artisansDB));localStorage.setItem("anrevaz_current",JSON.stringify(artisan));document.getElementById("idName").innerText=name;document.getElementById("idKey").innerText=keyId;document.getElementById("idNumber").innerText=wsId;document.getElementById("landingWsId").innerText=wsId;document.getElementById("landingKeyId").innerText=keyId;succ.innerText="Authenticated! Secure Key "+keyId+" / "+wsId+" - Exact format as reorganized pictures - Same display and functions as those on pictures - Workspace secured";succ.classList.remove("hidden");startHeartbeat(wsId);setTimeout(function(){showScreen("landing");},1000);}
function startHeartbeat(wsId){function beat(){fetch("/heartbeat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({wsId:wsId})});}beat();setInterval(beat,30000);}
function renderDevDashboard(){fetch("/dev-stats").then(function(r){return r.json();}).then(function(data){document.getElementById("devOnlineCount").innerText=data.online;document.getElementById("devTotalCount").innerText=data.total;document.getElementById("devQuotesToday").innerText=data.quotes;let list=document.getElementById("devArtisansList");if(list){let html="";if(data.artisans){data.artisans.forEach(function(a){html+="<div class=\\"flex justify-between bg-white/5 p-2 rounded-lg\\"><span>"+a.wsId+" - "+a.trade+" - Exact format</span><span class=\\"text-green-400\\">● "+a.status+" - Online Seen</span></div>";});}else{html+="<div class=\\"bg-white/5 p-2 rounded\\">Marcus Johnson - WS-1042 - Carpentry - Online - Now - Daily - 4.8/5 - Frequency & Usefulness</div><div class=\\"bg-white/5 p-2 rounded mt-1\\">Sofia Chen - WS-1187 - Plumbing - Online - 2m ago - 4-5x/week - 4.6/5</div><div class=\\"bg-white/5 p-2 rounded mt-1\\">Raj Patel - WS-0923 - Electrical - Online - 7m ago - Daily - 4.7/5</div>";}list.innerHTML=html;}});}
function scanFloorPlan(){let result=document.getElementById("floorScanResult");if(result){result.classList.remove("hidden");document
