from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Run An Compass', version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://[a-z0-9-]+\.vercel\.app",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
PRODUCT = {"project_id": "15c56046-6bcd-4997-b4a4-a7a1a5e05648", "product_name": "Run An Compass", "idea": "Run an evidence-backed pilot for the first customer segment implied by this brief: Build an AI product that predicts machine failures using IOT sensor data and schedules preventive maintenance automatically. Help that segment improve one measurable outcome versus its current alternative in a 30-day pilot, with human approval for consequential recommendations.", "problem": "Merchant, sales, and customer-success teams need a safer, faster way to spot the next customer or operational action with measurable commercial impact. The opportunity should be tested through one repeatable decision workflow.", "elevator_pitch": "Run An Compass helps merchant, sales, and customer-success teams turn scattered evidence into a human-approved next action and prove whether the workflow improves a measurable outcome.", "target_users": ["merchant, sales, and customer-success teams", "domain specialists", "a revenue or operations leader"], "features": ["Structured case or workflow intake", "Evidence-backed recommendation with confidence and rationale", "Human approval and override with an audit trail", "Pilot dashboard for time, quality, and adoption outcomes"], "market_gap": "A narrow commerce operations workflow that links evidence, a human approval, and a measurable outcome remains more defensible than another general AI chat surface."}

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "generated-mvp-api"}

@app.get("/api/overview")
def overview() -> dict:
    return {
        "product_name": PRODUCT["product_name"],
        "pitch": PRODUCT["elevator_pitch"],
        "problem": PRODUCT["problem"],
        "target_users": PRODUCT["target_users"],
        "features": PRODUCT["features"],
        "demo_data": True,
    }
