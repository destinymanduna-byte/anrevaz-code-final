from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="ANREVAZ OS - Central Africa")

# Your business numbers
ECOCASH_ONLY = os.getenv("ECOCASH_ONLY", "0772590884")
WHATSAPP_ONLY = os.getenv("WHATSAPP_ONLY", "0783788376")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "ANREVAZ_VERIFY")

@app.get("/")
def home():
    return {"status": "ANREVAZ OS LIVE", "region": "Central Africa - Frankfurt/JNB", "ecocash": ECOCASH_ONLY}

@app.get("/api/materials")
def materials(): no
    return {
        "materials": [
            {"id": 1, "name": "Cement", "price": 12.5, "unit": "bag"},
            {"id": 2, "name": "Bricks", "price": 0.25, "unit": "each"},
            {"id": 3, "name": "Roofing Sheets", "price": 18, "unit": "sheet"}
        ],
        "ecocash_payment": ECOCASH_ONLY,
        "whatsapp_orders": WHATSAPP_ONLY
    }

@app.get("/api/paynow/verify")
def verify_paynow():
    return {"paynow": "ready", "monthly": True}

@app.get("/webhook")
def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge) if challenge else 0
    return JSONResponse(content={"error": "verification failed"}, status_code=403)

@app.post("/webhook")
async def webhook_post(request: Request):
    data = await request.json()
    print("Webhook received:", data)
    return {"status": "received"}
