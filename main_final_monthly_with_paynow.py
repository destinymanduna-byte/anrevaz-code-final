from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
import os, time, json

app = FastAPI(title="ANREVAZ v13.9 Fix Triple Quote")
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
    h += "<title>ANREVAZ v13.9 Fix Triple Quote</title>\n"
    h += "<script src=\"https://cdn.tailwindcss.com\"></script>\n"
    h += "<style>.screen{display:none}.screen.active{display:block}.nav-active{background:#5b7cff!important}.dev-only{display:none}.dev-mode .dev-only{display:block}</style></head>\n"
    h += "<body style=\"background:#0a0e26;color:white\">\n"
    h += "<div class=\"max-w-[560px] mx-auto pb-32\">\n"
    h += "<div id=\"screen-signin\" class=\"screen active p-5\">\n"
    h += "<div class=\"font-black text-xl\">Secure Sign-In - Exact Format As Pictures</div>\n"
    h += "<img id=\"img-signin\" src=\"/img/0\" class=\"mt-4 w-full rounded-2xl border bg-white/10\">\n"
    h += "<div class=\"mt-4 space-y-2\">\n"
    h += "<input id=\"sName\" placeholder=\"Full Name *\" class=\"w-full p-3 rounded text-black text-sm\">\n"
    h += "<input id=\"sPhone\" placeholder=\"Phone *\" class=\"w-full p-3 rounded text-black text-sm\">\n"
    h += "<input id=\"sIdNum\" placeholder=\"National ID *\" class=\"w-full p-3 rounded text-black text-sm\">\n"
    h += "<input id=\"sLocation\" placeholder=\"Location *\" class=\"w-full p-3 rounded text-black text-sm\">\n"
    h += "<input id=\"sYears\" type=\"number\" placeholder=\"Years *\" class=\"w-full p-3 rounded text-black text-sm\">\n"
    h += "<input id=\"sProof\" type=\"file\" accept=\"image/*\" class=\"w-full mt-2 text-[11px]\">\n"
    h += "<button onclick=\"doSignIn()\" class=\"w-full bg-[#5b7cff] py-4 rounded-xl font-black mt-2\">Create Secure Key - Exact Format</button>\n"
    h += "<div id=\"signInError\" class=\"hidden mt-3 bg-red-500/20 border p-3 rounded text-[11px]\"></div>\n"
    h += "</div>\n"
    h += "<div class=\"mt-6 text-center\">\n"
    h += "<button id=\"devUnlock\" onclick=\"tapDevUnlock()\" class=\"mt-2 text-[9px] text-white/20 border px-3 py-1 rounded-full\">Dev Unlock - Tap 5x</button>\n"
    h += "<div id=\"devCodeArea\" class=\"hidden mt-3 bg-yellow-500/10 border rounded-xl p-3\">\n"
    h += "<input id=\"devCodeInput\" placeholder=\"ANR-DEV-MASTER-2026\" class=\"w-full p-3 rounded text-black text-sm text-center font-mono\">\n"
    h += "<button onclick=\"checkDevCode()\" class=\"w-full mt-2 bg-yellow-500 text-black py-2 rounded font-black text-sm\">Unlock Developer - Online Seen + Reorganize</button>\n"
    h += "</div></div></div>\n"
    h += "<div id=\"screen-landing\" class=\"screen p-5\">\n"
    h += "<div class=\"font-black\">LANDING - 1 Sec Inside - Exact Format</div>\n"
    h += "<img id=\"img-landing\" src=\"/img/1\" class=\"mt-4 w-full rounded-2xl border bg-white/10\">\n"
    h += "<button onclick=\"showScreen('workspace')\" class=\"w-full mt-3 bg-[#5b7cff] py-3 rounded font-black\">Enter Workspace - Exact Format</button>\n"
    h += "</div>\n"
    h += "<div id=\"screen-workspace\" class=\"screen p-5\">\n"
    h += "<div class=\"font-black\">My Private Workspace - Exact Format</div>\n"
    h += "<div id=\"idCard\" class=\"mt-4 bg-[#1e2a6b] border rounded-2xl p-4\">\n"
    h += "<div id=\"idName\" class=\"font-black\">Tinashe Moyo</div>\n"
    h += "<div id=\"idTrade\" class=\"text-[#5b7cff] text-xs\">Fitted Kitchens</div>\n"
    h += "<div class=\"text-[10px]\">Key: <span id=\"idKey\">ANR-KD-XXXX</span> / <span id=\"idNumber\">WS-A7K9</span></div>\n"
    h += "</div></div>\n"
    h += "<div id=\"screen-floor-scan\" class=\"screen p-5\">\n"
    h += "<div class=\"font-black\">Scan Floor Plan & Quote - Exact Format</div>\n"
    h += "<img id=\"img-floor-scan\" src=\"/img/2\" class=\"mt-4 w-full rounded-2xl border bg-white/10\">\n"
    h += "</div>\n"
    h += "<div id=\"screen-dev\" class=\"screen p-5\">\n"
    h += "<div class=\"font-black text-xl\">Developer Dashboard - Online Seen + Reorganize - DEV ONLY</div>\n"
    h += "<img id=\"img-dev\" src=\"/img/6\" class=\"mt-4 w-full rounded-2xl border bg-white/10\">\n"
    h += "<div class=\"mt-4 grid grid-cols-2 gap-2\">\n"
    h += "<div class=\"bg-white/5 border rounded-2xl p-3\"><div class=\"text-[10px]\">Online</div><div class=\"font-black\"><span id=\"devOnlineCount\">24</span> / <span id=\"devTotalCount\">38</span></div></div>\n"
    h += "<div class=\"bg-white/5 border rounded-2xl p-3\"><div class=\"text-[10px]\">Quotes Today</div><div class=\"font-black\" id=\"devQuotesToday\">48</div></div>\n"
    h += "</div>\n"
    h += "<div id=\"devArtisansList\" class=\"mt-4 text-[10px] space-y-1\"></div>\n"
    h += "<div class=\"mt-8 dev-only border-t border-yellow-500/20 pt-6\">\n"
    h += "<div class=\"font-black text-sm text-yellow-400\">DEV ONLY - Reorganize Setting</div>\n"
    h += "<div class=\"mt-4 space-y-3\" id=\"assignList\"></div>\n"
    h += "<button onclick=\"saveMapping()\" class=\"w-full mt-4 bg-yellow-500 text-black py-3 rounded font-black\">Save Mapping - Update Exact Format For Users</button>\n"
    h += "</div></div>\n"
    h += "<div id=\"screen-preview\" class=\"screen p-5\">\n"
    h += "<div class=\"font-black\">Invoice Columns - Exact Format</div>\n"
    h += "<img id=\"img-preview\" src=\"/img/4\" class=\"mt-4 w-full rounded-2xl border bg-white/10\">\n"
    h += "</div>\n"
    h += "<div id=\"screen-ai\" class=\"screen p-5\">\n"
    h += "<div class=\"font-black\">Kai AI ChatGPT-6 - Exact Format As Pictures</div>\n"
    h += "<img id=\"img-ai\" src=\"/img/5\" class=\"mt-4 w-full rounded-2xl border bg-white/10\">\n"
    h += "<div class=\"mt-3 bg-[#0f1535] border rounded-2xl p-3\"><div class=\"text-[11px]\">Kai AI - Follow-up Agent - Timeline 0 sec 2h 24h day3 day7 till WON</div></div>\n"
    h += "</div>\n"
    h += "<div id=\"screen-subscribe\" class=\"screen p-5\">\n"
    h += "<div class=\"font-black\">Packages Free Trial - Exact Format</div>\n"
    h += "<img id=\"img-subscribe\" src=\"/img/3\" class=\"mt-4 w-full rounded-2xl border bg-white/10\">\n"
    h += "</div></div>\n"
    h += "<div class=\"fixed bottom-0 left-0 right-0 bg-black/90 border-t border-white/10\">\n"
    h += "<div id=\"userNav\" class=\"max-w-[560px] mx-auto grid grid-cols-8 text-center text-[7px] py-2 gap-1\">\n"
    h += "<button onclick=\"showScreen('signin')\" id=\"nav-signin\" class=\"nav-active py-1 rounded\">Sign-In<br>Key</button>\n"
    h += "<button onclick=\"showScreen('landing')\" id=\"nav-landing\" class=\"text-white/40 py-1\">Landing<br>1 Sec</button>\n"
    h += "<button onclick=\"showScreen('workspace')\" id=\"nav-workspace\" class=\"text-white/40 py-1\">Trade<br>WS</button>\n"
    h += "<button onclick=\"showScreen('floor-scan')\" id=\"nav-floor-scan\" class=\"text-white/40 py-1\">Floor<br>Scan</button>\n"
    h += "<button onclick=\"showScreen('dev')\" id=\"nav-dev\" class=\"text-white/40 py-1\">Dev<br>Online Seen</button>\n"
    h += "<button onclick=\"showScreen('preview')\" id=\"nav-preview\" class=\"text-white/40 py-1\">Quote<br>Invoice</button>\n"
    h += "<button onclick=\"showScreen('ai')\" id=\"nav-ai\" class=\"text-white/40 py-1\">Kai AI<br>Pic</button>\n"
    h += "<button onclick=\"showScreen('subscribe')\" id=\"nav-subscribe\" class=\"text-white/40 py-1\">Packages<br>Pic</button>\n"
    h += "</div>\n"
    h += "<div id=\"devNav\" class=\"hidden max-w-[560px] mx-auto grid grid-cols-9 text-center text-[6px] py-2 gap-1\">\n"
    h += "<button onclick=\"showScreen('dev')\" id=\"nav-dev-dev\" class=\"nav-active py-1 rounded bg-yellow-500 text-black\">Dev<br>Online Seen + Reorganize</button>\n"
    h += "</div></div>\n"
    h += "<script>\n"
    h += "let mapping=JSON.parse(localStorage.getItem(\"anrevaz_mapping\")||'{\"signin\":0,\"landing\":1,\"floor-scan\":2,\"dev\":6,\"preview\":4,\"ai\":5,\"subscribe\":3}');\n"
    h += "let images=[\"IMG-20261029-WA0475.jpg\",\"IMG-20261029-WA1657.jpg\",\"IMG-20261029-WA3003.jpg\",\"IMG-20261029-WA3854.jpg\",\"IMG-20261029-WA6158.jpg\",\"IMG-20261029-WA9207.jpg\",\"IMG-20261029-WA9220.jpg\"];\n"
    h += "let artisansDB=JSON.parse(localStorage.getItem(\"anrevaz_artisans\")||\"{}\");\n"
    h += "let devTapCount=0;let isDevMode=localStorage.getItem(\"anrevaz_dev_mode\")===\"true\";\n"
    h += "function showScreen(id){let saved=localStorage.getItem(\"anrevaz_current\");if(id!==\"signin\" && id!==\"dev\" && !saved){showScreen(\"signin\");return;}document.querySelectorAll(\".screen\").forEach(function(s){s.classList.remove(\"active\");});let el=document.getElementById(\"screen-\"+id);if(el){el.classList.add(\"active\");}window.scrollTo(0,0);if(id===\"dev\"){renderDevDashboard();renderReorganize();}applyMapping();}\n"
    h += "function renderReorganize(){let assignHtml=\"\";let screens=[[\"signin\",\"1. Sign-In\"],[\"landing\",\"2. Landing\"],[\"floor-scan\",\"3. Floor Scan\"],[\"dev\",\"4. Dev Online Seen\"],[\"preview\",\"5. Invoice\"],[\"ai\",\"6. Kai AI\"],[\"subscribe\",\"7. Packages\"]];screens.forEach(function(s){let sid=s[0];let sname=s[1];let currentIdx=mapping[sid]||0;assignHtml+=\"<div class=\\\"bg-white/5 border rounded-xl p-3\\\"><div class=\\\"flex justify-between\\\"><div class=\\\"font-black text-[11px]\\\">\"+sname+\"</div><div class=\\\"text-[9px] bg-[#5b7cff] px-2 py-1 rounded-full\\\">IMG-\"+currentIdx+\"</div></div><div class=\\\"mt-2 grid grid-cols-4 gap-1\\\">\";for(let i=0;i<images.length;i++){let active=(mapping[sid]===i)?\"bg-[#5b7cff]\":\"bg-white/10\";assignHtml+=\"<button onclick=\\\"setMapping('\"+sid+\"',\"+i+\")\\\" class=\\\"border rounded p-1 \"+active+\"\\\"><img src=\\\"/img/\"+i+\"\\\" class=\\\"w-full h-12 object-cover rounded\\\"><div class=\\\"text-[7px]\\\">IMG-\"+i+\"</div></button>\";}assignHtml+=\"</div></div>\";});let el2=document.getElementById(\"assignList\");if(el2){el2.innerHTML=assignHtml;}}\n"
    h += "function setMapping(screen,idx){mapping[screen]=idx;localStorage.setItem(\"anrevaz_mapping\",JSON.stringify(mapping));applyMapping();}\n"
    h += "function saveMapping(){localStorage.setItem(\"anrevaz_mapping\",JSON.stringify(mapping));applyMapping();alert(\"Dev: Mapping saved! Users see exact format as reorganized\");showScreen(\"landing\");}\n"
    h += "function applyMapping(){for(let screen in mapping){let idx=mapping[screen];let imgEl=document.getElementById(\"img-\"+screen);if(imgEl){imgEl.src=\"/img/\"+idx;}}}\n"
    h += "function tapDevUnlock(){devTapCount++;let btn=document.getElementById(\"devUnlock\");btn.innerText=\"Tap \"+(5-devTapCount)+\" more \"+devTapCount+\"/5\";if(devTapCount>=5){document.getElementById(\"devCodeArea\").classList.remove(\"hidden\");btn.innerText=\"Enter Dev Code\";devTapCount=0;}}\n"
    h += "function checkDevCode(){let code=document.getElementById(\"devCodeInput\").value.trim().toUpperCase();if(code===\"ANR-DEV-MASTER-2026\"||code===\"ANR-ACT-MASTER-2026\"){localStorage.setItem(\"anrevaz_dev_mode\",\"true\");isDevMode=true;document.body.classList.add(\"dev-mode\");document.getElementById(\"userNav\").classList.add(\"hidden\");document.getElementById(\"devNav\").classList.remove(\"hidden\");alert(\"Developer Mode Unlocked! Reorganize + Online Seen\");showScreen(\"dev\");}else{alert(\"Invalid - Use ANR-DEV-MASTER-2026\");}}\n"
    h += "function doSignIn(){let name=document.getElementById(\"sName\").value.trim();let phone=document.getElementById(\"sPhone\").value.trim();let idNum=document.getElementById(\"sIdNum\").value.trim();let err=document.getElementById(\"signInError\");err.classList.add(\"hidden\");if(!name||!phone||!idNum){err.innerText=\"All fields required\";err.classList.remove(\"hidden\");return;}let keyId=\"ANR-KD-\"+Math.random().toString(36).substr(2,4).toUpperCase();let wsId=\"WS-\"+Math.random().toString(36).substr(2,4).toUpperCase();let credKey=phone+\"_\"+idNum;if(artisansDB[credKey]){err.innerText=\"Same credentials cannot create second WS\";err.classList.remove(\"hidden\");return;}let artisan={name:name,phone:phone,idNum:idNum,keyId:keyId,wsId:wsId,mapping:mapping};artisansDB[credKey]=artisan;localStorage.setItem(\"anrevaz_artisans\",JSON.stringify(artisansDB));localStorage.setItem(\"anrevaz_current\",JSON.stringify(artisan));document.getElementById(\"idName\").innerText=name;document.getElementById(\"idKey\").innerText=keyId;document.getElementById(\"idNumber\").innerText=wsId;startHeartbeat(wsId);showScreen(\"landing\");}\n"
    h += "function startHeartbeat(wsId){function beat(){fetch(\"/heartbeat\",{method:\"POST\",headers:{\"Content-Type\":\"application/json\"},body:JSON.stringify({wsId:wsId})});}beat();setInterval(beat,30000);}\n"
    h += "function renderDevDashboard(){fetch(\"/dev-stats\").then(function(r){return r.json();}).then(function(data){document.getElementById(\"devOnlineCount\").innerText=data.online;document.getElementById(\"devTotalCount\").innerText=data.total;document.getElementById(\"devQuotesToday\").innerText=data.quotes;});}\n"
    h += "window.onload=function(){let devMode=localStorage.getItem(\"anrevaz_dev_mode\");if(devMode===\"true\"){isDevMode=true;document.body.classList.add(\"dev-mode\");document.getElementById(\"userNav\").classList.add(\"hidden\");document.getElementById(\"devNav\").classList.remove(\"hidden\");}renderReorganize();applyMapping();}\n"
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
    return {"status": "LIVE v13.9 Fix Triple Quote", "dev_code": "ANR-DEV-MASTER-2026"}

@app.get("/manifest.json")
def manifest():
    return JSONResponse({"name": "ANREVAZ", "start_url": "/"})

@app.post("/heartbeat")
async def heartbeat(req: Request):
    try:
        data = await req.json()
        wsId = data.get("wsId", "WS-XXXX")
        HEARTBEAT_DB[wsId] = {"trade": "Carpentry", "last": time.time()}
        return {"ok": True}
    except:
        return {"ok": False}

@app.get("/dev-stats")
def dev_stats():
    return {"online": len(HEARTBEAT_DB) or 24, "total": 38, "quotes": 48, "artisans": []}

@app.post("/whatsapp")
async def wa_backend(req: Request):
    return {"reply": "Kai AI - Exact format as pictures"}
