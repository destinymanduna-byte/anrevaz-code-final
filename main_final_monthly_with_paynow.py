from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json, base64

app = FastAPI()

MATS = {}
MATS["Kitchen"] = {"items": [{"name": "Melamine", "price": 85, "need": 6, "unit": "Sheets", "spec": "Base", "supplier": "BoardMart"}]}
MATS["Roof"] = {"items": [{"name": "Chromadek", "price": 18, "need": 85, "unit": "Sheets", "spec": "3.6m", "supplier": "Steel"}]}
MATS["Foundation"] = {"items": [{"name": "Cement", "price": 12, "need": 30, "unit": "Bags", "spec": "50kg", "supplier": "PPC"}]}
MATS["Plumber"] = {"items": [{"name": "Toilet", "price": 180, "need": 2, "unit": "Sets", "spec": "White", "supplier": "PlumbMart"}]}
MATS["Fitted Kitchen (3m x 3m)"] = MATS["Kitchen"]
MATS["Hipped Roof (100sqm)"] = MATS["Roof"]
MATS["Builder Foundation (100sqm)"] = MATS["Foundation"]
MATS["Plumber Full House"] = MATS["Plumber"]

SUBS = {}
SUBS["$3 Starter"] = {"price": 3, "features": ["1 Workspace"]}
SUBS["$7 Pro"] = {"price": 7, "features": ["3 Workspaces"], "popular": True}
SUBS["$12 Premium"] = {"price": 12, "features": ["Unlimited"], "best": True}

FLOOR = {}
FLOOR["127sqm $3627"] = {"price": 3627, "rooms": ["Lounge"], "roof": "Hipped Roof (100sqm)", "ceiling": "Ceilings", "desc": "Popular"}
FLOOR["80sqm Starter"] = FLOOR["127sqm $3627"]
FLOOR["150sqm Family"] = FLOOR["127sqm $3627"]

def handle_whatsapp_message(phone, msg):
    m = msg.lower().strip()
    if m in ["hi", "hello", "menu", "start"]:
        return "ANREVAZ SUPERSONIC QUOTE v12.5 Kai AI\nLanding PREMIUM Any Trade Quote in 3 sec\nWhatsApp 0783788376 EcoCash 0772590884\n"
    return "ANREVAZ SUPERSONIC QUOTE v12.5 Kai AI"

MATS_JSON = json.dumps(MATS)
SUBS_JSON = json.dumps(SUBS)
FLOOR_JSON = json.dumps(FLOOR)

HTML_B64_PARTS = [
    "PCFET0NUWVBFIGh0bWw+PGh0bWw+PGhlYWQ+PG1ldGEgY2hhcnNldD0iVVRGLTgiPjxtZXRhIG5hbWU9InZpZXdwb3J0IiBjb250ZW50PSJ3aWR0aD1kZXZpY2Utd2lkdGgsaW5pdGlhbC1zY2FsZT0xIj48dGl0bGU+QU5SRVZBWiBT",
    "VVBFUlNPTklDIFpVT1RFIC0gS2FpIEFJPC90aXRsZT48c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG4udGFpbHdpbmRjc3MuY29tIj48L3NjcmlwdD48c3R5bGU+LnNjcmVlbnR7ZGlzcGxheTpub25lfS5zY3JlZW4uYWN0aXZle2Rp",
    "c3BsYXk6YmxvY2t9Lm5hdi1hY3RpdmV7YmFja2dyb3VuZDojNWI3Y2ZmIWltcG9ydGFudDtjb2xvcjp3aGl0ZSFpbXBvcnRhbnR9LmdsYXNze2JhY2tncm91bmQ6cmdiYSgyNTUsMjU1LDI1NSwwLjA2KTtib3JkZXI6MXB4",
    "IHNvbGlkIHJnYmEoMjU1LDI1NSwyNTUsMC4xKX08L3N0eWxlPjwvaGVhZD48Ym9keSBzdHlsZT0iYmFja2dyb3VuZDojMGEwZTI2O2NvbG9yOndoaXRlO2ZvbnQtZmFtaWx5OkludGVyO21pbi1oZWlnaHQ6MTAwdmgiPjxkaXYg",
    "Y2xhc3M9Im1heC13LT1bNTYwcHhdIG1heC1hdXRvIHBCLTI4Ij48ZGl2IGlkPSJzY3JlZW4tbGFuZGluZyIgY2xhc3M9InNjcmVlbiBhY3RpdmUgcHgtNSBweS02Ij48ZGl2IGNsYXNzPSJmbGV4IGp1c3RpZnktYmV0d2Vl",
    "biBpdGVtcy1jZW50ZXIiPjxkaXYgY2xhc3M9ImZsZXggZ2FwLTIgaXRlbXMtY2VudGVyIj48ZGl2IGNsYXNzPSJ3LTkgaC05IHJvdW5kZWQteGwgYmctWzViN2NmZl0gZ3JpZCBwbGFjZS1pdGVtcy1jZW50ZXIiPkE8L2Rp",
    "dj48ZGl2IGNsYXNzPSJmb250LWJsYWNrIj5BTlJFVkFaIE9TPC9kaXY+PC9kaXY+PGRpdiBjbGFzcz0iYmctWzViN2NmZl0vMzAgcHgtMyBweS0xIHJvdW5kZWQtZnVsbCB0ZXh0LVsxMHB4XSI+UFJFTUlVTTwvZGl2Pjwv",
    "ZGl2PjxkaXYgY2xhc3M9Im10LTgiPjxkaXYgY2xhc3M9ImZvbnQtYmxhY2sgdGV4dC0zeGwiPkFueSBUcmFkZSBRdW90ZSBpbiAzIHNlYzwvZGl2PjxkaXYgY2xhc3M9ImZvbnQtYmxhY2sgdGV4dC0zeGwgdGV4dC1bNWI3",
    "Y2ZmXSI+QUkgRm9sbG93LXVwIFdpbnMgVGhlIEpvYjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9Im10LTggZ3JpZCBncmlkLWNvbHMtNSBnYXAtMiI+PGRpdiBjbGFzcz0iZ2xhc3Mgcm91bmRlZC0yeGwgcC0zIHRleHQtY2Vu",
    "dGVyIj48ZGl2PkNhcnBlbnRlcjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9ImdsYXNzIHJvdW5kZWQtMnhsIHAzIHRleHQtY2VudGVyIj48ZGl2PldlbGRlcjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9ImdsYXNzIHJvdW5kZWQt",
    "MnhsIHAzIHRleHQtY2VudGVyIj48ZGl2PkJ1aWxkZXI8L2Rpdj48L2Rpdj48ZGl2IGNsYXNzPSJnbGFzcyByb3VuZGVkLTJ4bCBwLTMgdGV4dC1jZW50ZXIiPjxkaXY+UGx1bWJlcjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9
