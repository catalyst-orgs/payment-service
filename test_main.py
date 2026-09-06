from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["service"] == "payment-service"


def test_list_items():
    resp = client.get("/api/v1/items")
    assert resp.status_code == 200
    items = resp.json()
    assert len(items) >= 3
    assert items[0]["name"] == "alpha"


def test_get_item_found():
    resp = client.get("/api/v1/items/1")
    assert resp.status_code == 200
    assert resp.json()["id"] == 1


def test_get_item_not_found():
    resp = client.get("/api/v1/items/9999")
    assert resp.status_code == 404


def test_create_item():
    resp = client.post(
        "/api/v1/items",
        json={"name": "delta", "description": "created in test"},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "delta"
    assert body["id"] > 3