import sys
from pathlib import Path

from fastapi.testclient import TestClient

# Render's build command can execute from the repository root even when this
# service has a backend root directory. Make the generated app import explicit.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app

client = TestClient(app)

def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_overview_is_labelled_demo_data() -> None:
    response = client.get("/api/overview")
    assert response.status_code == 200
    assert response.json()["demo_data"] is True
