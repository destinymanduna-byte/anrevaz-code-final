from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json, base64

app = FastAPI(title="ANREVAZ SUPERSONIC QUOTE v12.3 Kai AI Fixed Line 149")

SUBS = {"$3 Starter": {"price": 3, "features": ["1 Workspace"]}, "$7 Pro": {"price": 7, "features": ["3 Workspaces"], "popular": true}, "$12 Premium": {"price": 12, "features": ["Unlimited"], "best": true}}
MATS = {"Fitted Kitchen (3m x 3m)": {"icon": "Carpenter", "items": [{"name": "Melamine White 18mm", "spec": "2440x1220 Base", "price": 85, "need": 6, "unit": "Sheets", "supplier": "BoardMart"}]}, "Hipped Roof (100sqm)": {"icon": "Builder", "items": [{"name": "Chromadek Charcoal 0.5mm", "spec": "3.6m AZ150", "price": 18, "need": 85, "unit": "Sheets", "supplier": "SteelSuppliers"}]}, "Builder Foundation (100sqm)": {"icon": "Builder", "items": [{"name": "Cement PPC 50kg", "spec": "50kg Bag", "price": 12, "need": 30, "unit": "Bags", "supplier": "PPC"}]}, "Plumber Full House": {"icon": "Plumber", "items": [{"name": "Toilet Close Couple", "spec": "White Ceramic", "price": 180, "need": 2, "unit": "Sets", "supplier": "PlumbMart"}]}}
FLOOR = {"127sqm 3-Bed Popular $3627": {"icon": "Builder", "rooms": ["Lounge 5x6m"], "price": 3627, "roof": "Hipped Roof (100sqm)", "ceiling": "Ceilings (80sqm)", "desc": "Popular"}}

def handle_whatsapp_message(phone, message):
    msg = message.lower().strip()
    if msg in ["hi", "hello", "menu", "start"]:
        return ("ANREVAZ SUPERSONIC QUOTE v12.3 Kai AI\nLanding PREMIUM Any Trade Quote in 3 sec AI Follow-up Wins The Job\nCarpenter Welder Builder Plumber Glazier\nAI Timeline 0 sec quote 2h 24h day3 day7\nWhatsApp 0783788376 EcoCash 0772590884\nGet Instant Quote Now\n")
    return ("ANREVAZ SUPERSONIC QUOTE v12.3 Kai AI - Floor Plan $3627 Builder $12 Bricks $0.18 Plumber $180 Geyser $350 Electrician $45 - Kai follows up till WON")

MATS_JSON = json.dumps(MATS)
SUBS_JSON = json.dumps(SUBS)
FLOOR_JSON = json.dumps(FLOOR)

HTML_B64 = "PCFET0NUWVBFIGh0bWw+CjxodG1sPgo8aGVhZD4KPG1ldGEgY2hhcnNldD0iVVRGLTgiPgo8bWV0YSBuYW1lPSJ2aWV3cG9ydCIgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLGluaXRpYWwtc2NhbGU9MSI+Cjx0aXRsZT5BTlJFVkFaIFNVUEVSU09OSUMgUVVPVEUgLSBLYWkgQUk8L3RpdGxlPgo8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG4udGFpbHdpbmRjc3MuY29tIj48L3NjcmlwdD4KPHN0eWxlPi5zY3JlZW57ZGlzcGxheTpub25lfS5zY3JlZW4uYWN0aXZle2Rpc3BsYXk6YmxvY2t9Lm5hdi1hY3RpdmV7YmFja2dyb3VuZDojNWI3Y2ZmIWltcG9ydGFudDtjb2xvcjp3aGl0ZSFpbXBvcnRhbnR9LmdsYXNze2JhY2tncm91bmQ6cmdiYSgyNTUsMjU1LDI1NSwwLjA2KTtib3JkZXI6MXB4IHNvbGlkIHJnYmEoMjU1LDI1NSwyNTUsMC4xKX08L3N0eWxlPgo8L2hlYWQ+Cjxib2R5IHN0eWxlPSJiYWNrZ3JvdW5kOiMwYTBlMjY7Y29sb3I6d2hpdGU7Zm9udC1mYW1pbHk6SW50ZXI7bWluLWhlaWdodDoxMDB2aCI+CjxkaXYgY2xhc3M9Im1heC13LT1bNTYwcHhdIG1heC1hdXRvIHBCLTI4Ij4KPGRpdiBpZD0ic2NyZWVuLWxhbmRpbmciIGNsYXNzPSJzY3JlZW4gYWN0aXZlIHB4LTUgcHktNiI+CjxkaXYgY2xhc3M9ImZsZXgganVzdGlmeS1iZXR3ZWVuIGl0ZW1zLWNlbnRlciI+PGRpdiBjbGFzcz0iZmxleCBnYXAtMiBpdGVtcy1jZW50ZXIiPjxkaXYgY2xhc3M9Inc5IGg5IHJvdW5kZWQteGwgYmctWzViN2NmZl0gZ3JpZCBwbGFjZS1pdGVtcy1jZW50ZXIiPkE8L2Rpdj48ZGl2IGNsYXNzPSJmb250LWJsYWNrIj5BTlJFVkFaIE9TPC9kaXY+PC9kaXY+PGRpdiBjbGFzcz0iYmctWzViN2NmZl0vMzAgcHgtMyBweS0xIHJvdW5kZWQtZnVsbCB0ZXh0LVsxMHB4XSI+UFJFTUlVTTwvZGl2PjwvZGl2Pgo8ZGl2IGNsYXNzPSJtdC04Ij48ZGl2IGNsYXNzPSJmb250LWJsYWNrIHRleHQtM3hsIj5BbnkgVHJhZGUgUXVvdGUgaW4gMyBzZWM8L2Rpdj48ZGl2IGNsYXNzPSJmb250LWJsYWNrIHRleHQtM3hsIHRleHQtWzViN2NmZl0iPkFJIEZvbGxvdy11cCBXaW5zIFRoZSBKb2I8L2R
