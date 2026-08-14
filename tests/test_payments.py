import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_payment(client):
    response = client.post(
        "/payments",
        params={"amount": 100.50, "currency": "USD"},
    )
    assert response.status_code == 200
    body = response.json()
    assert "id" in body


def test_get_payment_by_id(client):
    create_response = client.post(
        "/payments",
        params={"amount": 250.00, "currency": "INR"},
    )
    payment_id = create_response.json()["id"]

    get_response = client.get(f"/payments/{payment_id}")
    assert get_response.status_code == 200
    body = get_response.json()
    assert body["id"] == payment_id
    assert float(body["amount"]) == 250.00
    assert body["currency"] == "INR"


def test_get_nonexistent_payment_returns_none(client):
    response = client.get("/payments/999999")
    assert response.status_code == 200
    assert response.json() is None