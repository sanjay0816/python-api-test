import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def auth_token():
    # Assuming an authentication system in place, mock or fetch an auth token for the buyer
    return "Bearer mock_token"

def test_add_to_cart(auth_token):
    response = client.post(
        "/cart/add",
        headers={"Authorization": auth_token},
        json={"product_id": 1, "quantity": 2}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Product added to cart"

def test_remove_from_cart(auth_token):
    response = client.delete(
        "/cart/remove/1",
        headers={"Authorization": auth_token}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Product removed from cart"

def test_view_cart(auth_token):
    response = client.get(
        "/cart/view",
        headers={"Authorization": auth_token}
    )
    assert response.status_code == 200
    assert isinstance(response.json()["cart_items"], list)

