import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def auth_token():
    # Mock a token for the seller
    return "Bearer seller_token"

def test_add_product(auth_token):
    response = client.post(
        "/product/add",
        headers={"Authorization": auth_token},
        json={
            "name": "Test Product",
            "description": "This is a test product",
            "price": 19.99,
            "stock": 100,
            "category_id": 1
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"

def test_update_product(auth_token):
    response = client.put(
        "/product/update/1",
        headers={"Authorization": auth_token},
        json={
            "name": "Updated Product",
            "description": "Updated description",
            "price": 24.99,
            "stock": 50
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"

def test_delete_product(auth_token):
    response = client.delete(
        "/product/delete/1",
        headers={"Authorization": auth_token}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted"

def test_list_products():
    response = client.get("/product/list")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

