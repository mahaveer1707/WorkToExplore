from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_payment():
    payload = {
        "amount": 100.50,
        "currency": "INR"
    }

    create_resp = client.post("/payments", json=payload)
    assert create_resp.status_code == 200

    payment = create_resp.json()
    assert payment["status"] == "CREATED"
    assert payment["amount"] == 100.50

    payment_id = payment["id"]

    get_resp = client.get(f"/payments/{payment_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == payment_id