from fastapi.testclient import TestClient
from app.main import app

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app


client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={"id": 1, "name": "Test", "price": 10.5, "in_stock": True})
    assert response.status_code == 200
    assert response.json()["name"] == "Test"

def test_get_item():
    client.post("/items", json={"id": 2, "name": "Test2", "price": 5.0, "in_stock": False})
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2

def test_update_item():
    client.post("/items", json={"id": 3, "name": "Test3", "price": 9.0, "in_stock": True})
    response = client.put("/items/3", json={"id": 3, "name": "Updated", "price": 9.0, "in_stock": True})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"

def test_delete_item():
    client.post("/items", json={"id": 4, "name": "Test4", "price": 7.0, "in_stock": False})
    response = client.delete("/items/4")
    assert response.status_code == 200
    
    response = client.get("/items/4")
    assert response.status_code == 404

