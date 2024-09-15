import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def buyer_token():
    # Mock a token for the buyer
    return "Bearer buyer_token"

@pytest.fixture
def seller_token():
    # Mock a token for the seller
    return "Bearer seller_token"

def test_place_order(buyer_token):
    response = client.post(
        "/order/place",
        headers={"Authorization": buyer_token},
        json={"cart_id": 1, "shipping_address": "123 Main St"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Order placed successfully"

def test_update_order_status(seller_token):
    response = client.put(
        "/order/update_status/1",
        headers={"Authorization": seller_token},
        json={"status": "shipped"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Order status updated"

