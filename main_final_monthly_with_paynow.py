from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
import os, time, json

app = FastAPI(title="ANREVAZ v14.0 Interactive Picture")
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

def build_html():
    h = ""
    h += "<!DOCTYPE html><html><head>\n"
    h += "<meta charset=\"UTF-8\">\n"
    h += "<meta name=\"viewport\" content=\"width=device-width\">\n"
    h += "<title>ANREVAZ v14.0 Interactive Picture Overlay</title>\n"
    h += "<script src=\"https://cdn.tailwindcss.com\"></script>\n"
    h += "<style>.screen{display:none}.screen.active{display:block}.nav-active{background:#5b7cff!important}.pic-container{position:relative;width:100%;}.pic-bg{width:100%;border-radius:16px;display:block;}.overlay-input{position:absolute;background:rgba(255,255,255,0.95);border:2px solid #5b7cff;border-radius:8px;padding:6px 10px;font-size:12px;color:black;outline:none;}.overlay-input:focus{border-color:#00ff88;background:white;box-shadow:0 0 0 3px rgba(91,124,255,0.3);}.overlay-select{position:absolute;background:rgba(255,255,255,0.95);border:2px solid #5b7cff;border-radius:8px;padding:6px 10px;font-size:12px;color:black;}.overlay-upload{position:absolute;background:rgba(255,255,255,0.9);border:2px dashed #5b7cff;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:10px;color:#5b7cff;cursor:pointer;}.overlay-btn{position:absolute;background:#5b7cff;color:white;border-radius:12px;padding:12px;font-weight:900;text-align:center;cursor:pointer;border:none;font-size:14px;}.overlay-btn:hover{background:#4a6ae0;}.green-dot{position:absolute;width:12px;height:12px;background:#00ff88;border-radius:50%;border:2px solid white;box-shadow:0 2px 4px rgba(0,0,0,0.3);}</style></head>\n"
    h += "<body style=\"background:#0a0e26;color:white\">\n"
    h += "<div class=\"max-w-[560px] mx-auto pb-32\">\n"
    h += "<div id=\"screen-signin\" class=\"screen active p-2\">\n"
    h += "<div class=\"font-black text-center\">Create Secure Workspace - SELECT INSIDE PICTURE</div>\n"
    h += "<div class=\"text-[10px] text-center text-green-400 mt-1\">Green strokes are now selectable - Click directly on picture to use options</div>\n"
    h += "<div class=\"pic-container mt-3\">\n"
    h += "<img id=\"img-signin\" src=\"/img/0\" class=\"pic-bg\" style=\"min-height:700px;object-fit:cover;\">\n"
    h += "<!-- Full Name - Green stroke area -->\n"
    h += "<input id=\"sName\" placeholder=\"e.g. Alex Kiptoo\" class=\"overlay-input\" style=\"top:34%;left:8%;width:84%;height:5%;\">\n"
    h += "<div class=\"green-dot\" style=\"top:36%;right:10%;\"></div>\n"
    h += "<!-- National ID - Green stroke area -->\n"
    h += "<input id=\"sIdNum\" placeholder=\"e.g. 34567890\" class=\"overlay-input\" style=\"top:40.5%;left:8%;width:84%;height:5%;\">\n"
    h += "<div class=\"green-dot\" style=\"top:42.5%;right:10%;\"></div>\n"
    h += "<!-- Phone - Green stroke area -->\n"
    h += "<input id=\"sPhone\" placeholder=\"+254 7XX XXX XXX\" class=\"overlay-input\" style=\"top:47%;left:8%;width:84%;height:5%;\">\n"
    h += "<div class=\"green-dot\" style=\"top:49%;right:10%;\"></div>\n"
    h += "<!-- Trade selector - Green stroke area -->\n"
    h += "<select id=\"sTrade\" class=\"overlay-select\" style=\"top:53.5%;left:8%;width:84%;height:5.5%;\">\n"
    h += "<option>Select your trade</option><option>Carpenter</option><option>Welder</option><option>Electrician</option><option>Plumber</option><option>Glazier</option><option>Builder</option>\n"
    h += "</select>\n"
    h += "<div class=\"green-dot\" style=\"top:55.5%;right:10%;\"></div>\n"
    h += "<!-- Years Experience - Green stroke area -->\n"
    h += "<input id=\"sYears\" type=\"number\" placeholder=\"e.g. 5 years\" class=\"overlay-input\" style=\"top:60%;left:8%;width:84%;height:5%;\">\n"
    h += "<div class=\"green-dot\" style=\"top:62%;right:10%;\"></div>\n"
    h += "<!-- Location - Green stroke area -->\n"
    h += "<input id=\"sLocation\" placeholder=\"e.g. Nairobi, Kenya\" class=\"overlay-input\" style=\"top:66.5%;left:8%;width:84%;height:5%;\">\n"
    h += "<div class=\"green-dot\" style=\"top:68.5%;right:10%;\"></div>\n"
    h += "<!-- Photo upload for job proof - Green stroke area -->\n"
    h += "<label class=\"overlay-upload\" style=\"top:73%;left:8%;width:84%;height:8%;\">\n"
    h += "<input id=\"sProof\" type=\"file\" accept=\"image/*\" style=\"display:none;\" onchange=\"showProofName(this)\">\n"
    h += "<span id=\"proofText\">Tap to upload photo / document - JPG/PNG, max 5MB - proof of completed job</span>\n"
    h += "</label>\n"
    h += "<div class=\"green-dot\" style=\"top:76%;right:10%;\"></div>\n"
    h += "<!-- System-Generated Secure Key - Display -->\n"
    h += "<div style=\"position:absolute;top:83%;left:8%;width:84%;height:6%;background:rgba(30,42,107,0.95);border-radius:12px;display:flex;align-items:center;justify-content:space-between;padding:0 12px;border:1px solid #5b7cff;\">\n"
    h += "<span id=\"previewKey\" style=\"font-family:monospace;font-size:11px;color:#5bffcc;\">ANR-KD-XXXX  WS-A7K9</span>\n"
    h += "<button onclick=\"copyKey()\" style=\"background:rgba(255,255,255,0.2);border-radius:6px;padding:4px 8px;font-size:10px;\">Copy</button>\n"
    h += "</div>\n"
    h += "<!-- Create Secure Workspace Button - Green stroke area -->\n"
    h += "<button onclick=\"doSignIn()\" class=\"overlay-btn\" style=\"top:91%;left:8%;width:84%;height:6%;\">\n"
    h += "Create Secure Workspace\n"
    h += "</button>\n"
    h += "<div class=\"green-dot\" style=\"top:93%;right:10%;\"></div>\n"
    h += "</div>\n"
    h += "<div id=\"signInError\" class=\"hidden mt-3 bg-red-500/20 border p-3 rounded text-[11px] mx-2\"></div>\n"
    h += "<div id=\"signInSuccess\" class=\"hidden mt-3 bg-green-500/20 border p-3 rounded text-[11px] mx-2\"></div>\n"
    h += "<div class=\"mt-3 bg-green-500/10 border border-green-500/20 rounded-xl p-3 mx-2\">\n"
    h += "<div class=\"font-black text-[11px] text-green-400\">How to use - Select inside picture:</div>\n"
    h += "<div class=\"text-[10px] text-white/60 mt-1\">1. Tap directly on Full Name field INSIDE the picture (where green stroke was)<br>2. Type your name - It types inside picture, not below<br>3. Tap National ID INSIDE picture - Type ID<br>4. Tap Phone INSIDE picture - Type phone<br>5. Tap Trade selector INSIDE picture - Select trade<br>6. Tap Years INSIDE picture - Type years<br>7. Tap Location INSIDE picture - Type location<br>8. Tap Photo upload INSIDE picture - Upload proof<br>9. Tap Create Secure Workspace button INSIDE picture - Creates workspace</div>\n"
    h += "</div>\n"
    h += "</div>\n"
    h += "<div id=\"screen-landing\" class=\"screen p-2\">\n"
    h += "<div class=\"font-black text-center\">Landing - Select Inside Picture</div>\n"
    h += "<div class=\"pic-container mt-3\">\n"
    h += "<img src=\"/img/1\" class=\"pic-bg\">\n"
    h += "<button onclick=\"showScreen('workspace')\" class=\"overlay-btn\" style=\"top:75%;left:10%;width:80%;height:8%;\">Enter Workspace - Select Inside Picture</button>\n"
    h += "</div></div>\n"
    h += "<div id=\"screen-workspace\" class=\"screen p-5\"><div class=\"font-black\">My Private Workspace</div><div id=\"idCard\" class=\"mt-4 bg-[#1e2a6b] border rounded-2xl p-4\"><div id=\"idName\">Tinashe Moyo</div><div id=\"idTrade\">Fitted Kitchens</div><div class=\"text-[10px]\">Key: <span id=\"idKey\">ANR-KD-XXXX</span> / <span id=\"idNumber\">WS-A7K9</span></div></div></div>\n"
    h += "<div id=\"screen-dev\" class=\"screen p-5\"><div class=\"font-black\">Dev - Online Seen + Reorganize - DEV ONLY</div><img src=\"/img/6\" class=\"pic-bg mt-3\"><div class=\"mt-4\" id=\"assignList\"></div><button onclick=\"saveMapping()\" class=\"w-full mt-4 bg-yellow-500 text-black py-3 rounded font-black\">Save Mapping - Dev Only</button></div>\n"
    h += "<div id=\"screen-floor-scan\" class=\"screen p-2\"><div class=\"font-black text-center\">Floor Scan - Select Inside Picture</div><div class=\"pic-container mt-3\"><img src=\"/img/2\" class=\"pic-bg\"><input type=\"file\" accept=\"image/*\" class=\"overlay-input\" style=\"top:70%;left:10%;width:80%;height:8%;\" onchange=\"scanFloorPlan()\"></div></div>\n"
    h += "<div id=\"screen-preview\" class=\"screen p-2\"><div class=\"font-black text-center\">Invoice - Select Inside Picture</div><img src=\"/img/4\" class=\"pic-bg mt-3\"></div>\n"
    h += "<div id=\"screen-ai\" class=\"screen p-2\"><div class=\"font-black text-center\">Kai AI - Select Inside Picture</div><div class=\"pic-container mt-3\"><img src=\"/img/5\" class=\"pic-bg\"><input id=\"aiInput\" placeholder=\"Ask Kai inside picture\" class=\"overlay-input\" style=\"top:75%;left:5%;width:60%;height:8%;\"><button onclick=\"sendAI()\" class=\"overlay-btn\" style=\"top:75%;left:70%;width:25%;height:8%;font-size:10px;\">Ask</button></div></div>\n"
    h += "<div id=\"screen-subscribe\" class=\"screen p-2\"><div class=\"font-black text-center\">Packages - Select Inside Picture</div><div class=\"pic-container mt-3\"><img src=\"/img/3\" class=\"pic-bg\"><button class=\"overlay-btn\" style=\"top:60%;left:10%;width:80%;height:10%;\">Start Free Trial - Select Inside</button></div></div>\n"
    h += "</div>\n"
    h += "<div class=\"fixed bottom-0 left-0 right-0 bg-black/90 border-t border-white/10\">\n"
    h += "<div id=\"userNav\" class=\"max-w-[560px] mx-auto grid grid-cols-8 text-center text-[7px] py-2 gap-1\">\n"
    h += "<button onclick=\"showScreen('signin')\" id=\"nav-signin\" class=\"nav-active py-1 rounded\">Sign-In<br>Key - Select Inside</button>\n"
    h += "<button onclick=\"showScreen('landing')\" id=\"nav-landing\" class=\"text-white/40 py-1\">Landing<br>Select Inside</button>\n"
    h += "<button onclick=\"showScreen('workspace')\" id=\"nav-workspace\" class=\"text-white/40 py-1\">Trade<br>WS</button>\n"
    h += "<button onclick=\"showScreen('floor-scan')\" id=\"nav-floor-scan\" class=\"text-white/40 py-1\">Floor<br>Scan</button>\n"
    h += "<button onclick=\"showScreen('dev')\" id=\"nav-dev\" class=\"text-white/40 py-1\">Dev<br>Online Seen</button>\n"
    h += "<button onclick=\"showScreen('preview')\" id=\"nav-preview\" class=\"text-white/40 py-1\">Quote<br>Invoice</button>\n"
    h += "<button onclick=\"showScreen('ai')\" id=\"nav-ai\" class=\"text-white/40 py-1\">Kai AI<br>Select Inside</button>\n"
    h += "<button onclick=\"showScreen('subscribe')\" id=\"nav-subscribe\" class=\"text-white/40 py-1\">Packages<br>Select Inside</button>\n"
    h += "</div></div>\n"
    h += "<script>\n"
    h += "let mapping=JSON.parse(localStorage.getItem(\"anrevaz_mapping\")||'{\"signin\":0,\"landing\":1,\"floor-scan\":2,\"dev\":6,\"preview\":4,\"ai\":5,\"subscribe\":3}');\n"
    h += "let artisansDB=JSON.parse(localStorage.getItem(\"anrevaz_artisans\")||\"{}\");\n"
    h += "function showScreen(id){let saved=localStorage.getItem(\"anrevaz_current\");if(id!==\"signin\" && id!==\"dev\" && !saved){showScreen(\"signin\");return;}document.querySelectorAll(\".screen\").forEach(function(s){s.classList.remove(\"active\");});let el=document.getElementById(\"screen-\"+id);if(el){el.classList.add(\"active\");}window.scrollTo(0,0);if(id===\"dev\"){renderReorganize();}applyMapping();}\n"
    h += "function renderReorganize(){let assignHtml=\"\";let screens=[[\"signin\",\"1. Sign-In\"],[\"landing\",\"2. Landing\"],[\"floor-scan\",\"3. Floor Scan\"],[\"dev\",\"4. Dev\"],[\"preview\",\"5. Invoice\"],[\"ai\",\"6. Kai AI\"],[\"subscribe\",\"7. Packages\"]];screens.forEach(function(s){let sid=s[0];let sname=s[1];let currentIdx=mapping[sid]||0;assignHtml+=\"<div class=\\\"bg-white/5 border rounded-xl p-3\\\"><div class=\\\"flex justify-between\\\"><div class=\\\"font-black text-[11px]\\\">\"+sname+\"</div><div class=\\\"text-[9px] bg-[#5b7cff] px-2 py-1 rounded-full\\\">IMG-\"+currentIdx+\"</div></div><div class=\\\"mt-2 grid grid-cols-4 gap-1\\\">\";for(let i=0;i<7;i++){let active=(mapping[sid]===i)?\"bg-[#5b7cff]\":\"bg-white/10\";assignHtml+=\"<button onclick=\\\"setMapping('\"+sid+\"',\"+i+\")\\\" class=\\\"border rounded p-1 \"+active+\"\\\"><img src=\\\"/img/\"+i+\"\\\" class=\\\"w-full h-12 object-cover rounded\\\"></button>\";}assignHtml+=\"</div></div>\";});let el2=document.getElementById(\"assignList\");if(el2){el2.innerHTML=assignHtml;}}\n"
    h += "function setMapping(screen,idx){mapping[screen]=idx;localStorage.setItem(\"anrevaz_mapping\",JSON.stringify(mapping));applyMapping();}\n"
    h += "function saveMapping(){localStorage.setItem(\"anrevaz_mapping\",JSON.stringify(mapping));applyMapping();alert(\"Dev: Mapping saved!\");showScreen(\"landing\");}\n"
    h += "function applyMapping(){for(let screen in mapping){let idx=mapping[screen];let imgEl=document.getElementById(\"img-\"+screen);if(imgEl){imgEl.src=\"/img/\"+idx;}}}\n"
    h += "function showProofName(input){let text=document.getElementById(\"proofText\");if(input.files[0]){text.innerText=input.files[0].name+\" - Selected inside picture\";}}\n"
    h += "function copyKey(){let key=document.getElementById(\"previewKey\").innerText;navigator.clipboard.writeText(key);alert(\"Copied: \"+key+\" - From inside picture\");}\n"
    h += "function doSignIn(){let name=document.getElementById(\"sName\").value.trim();let phone=document.getElementById(\"sPhone\").value.trim();let idNum=document.getElementById(\"sIdNum\").value.trim();let trade=document.getElementById(\"sTrade\").value;let loc=document.getElementById(\"sLocation\").value;let years=document.getElementById(\"sYears\").value;let proof=document.getElementById(\"sProof\").files[0];let err=document.getElementById(\"signInError\");let succ=document.getElementById(\"signInSuccess\");err.classList.add(\"hidden\");succ.classList.add(\"hidden\");if(!name||!phone||!idNum||!loc||!years){err.innerText=\"All green-marked fields inside picture are required - Tap inside picture to fill\";err.classList.remove(\"hidden\");return;}if(!proof){err.innerText=\"Photo upload for job proof required - Tap inside picture to upload\";err.classList.remove(\"hidden\");return;}let keyId=\"ANR-KD-\"+Math.random().toString(36).substr(2,4).toUpperCase();let wsId=\"WS-\"+Math.random().toString(36).substr(2,4).toUpperCase();let credKey=phone+\"_\"+idNum;if(artisansDB[credKey]){err.innerText=\"Same credentials cannot create second workspace - \"+artisansDB[credKey].wsId;err.classList.remove(\"hidden\");return;}let artisan={name:name,phone:phone,idNum:idNum,trade:trade,loc:loc,years:years,keyId:keyId,wsId:wsId,mapping:mapping};artisansDB[credKey]=artisan;localStorage.setItem(\"anrevaz_artisans\",JSON.stringify(artisansDB));localStorage.setItem(\"anrevaz_current\",JSON.stringify(artisan));document.getElementById(\"idName\").innerText=name;document.getElementById(\"idKey\").innerText=keyId;document.getElementById(\"idNumber\").innerText=wsId;document.getElementById(\"previewKey\").innerText=keyId+\" \"+wsId;succ.innerText=\"Workspace created by selecting inside picture - Key \"+keyId+\" / \"+wsId;succ.classList.remove(\"hidden\");startHeartbeat(wsId);setTimeout(function(){showScreen(\"landing\");},1000);}\n"
    h += "function startHeartbeat(wsId){function beat(){fetch(\"/heartbeat\",{method:\"POST\",headers:{\"Content-Type\":\"application/json\"},body:JSON.stringify({wsId:wsId})});}beat();setInterval(beat,30000);}\n"
    h += "window.onload=function(){renderReorganize();applyMapping();}\n"
    h += "</script></body></html>\n"
    return h

@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(build_html())

@app.get("/img/{idx}")
def get_img(idx: str):
    try:
        i = int(idx)
        if i < 0: i = 0
        if i > 6: i = 6
        fname = IMGS[i]
        path = os.path.join(".", fname)
        if os.path.exists(path):
            return FileResponse(path)
        files = [f for f in os.listdir(".") if f.startswith("IMG-")]
        files.sort()
        if i < len(files):
            return FileResponse(os.path.join(".", files[i]))
        return JSONResponse({"status": "not found"}, status_code=200)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=200)

@app.get("/health")
def health():
    return {"status": "LIVE v14.0 Interactive Picture - Select Inside Picture"}

@app.post("/heartbeat")
async def heartbeat(req: Request):
    try:
        data = await req.json()
        wsId = data.get("wsId", "WS-XXXX")
        HEARTBEAT_DB[wsId] = {"last": time.time()}
        return {"ok": True}
    except:
        return {"ok": False}

@app.get("/dev-stats")
def dev_stats():
    return {"online": len(HEARTBEAT_DB) or 24, "total": 38, "quotes": 48, "artisans": []}
