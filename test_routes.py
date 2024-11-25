# tests/test_routes.py

import pytest
from app import create_app
from app.models import Product
from flask import json

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_create_product(client):
    response = client.post('/products', json={"name": "Test Product", "description": "Test", "price": 20.99, "category": "Electronics", "availability": True})
    assert response.status_code == 201

def test_update_product(client):
    product = Product.query.first()
    response = client.put(f'/products/{product.id}', json={"price": 25.99})
    assert response.status_code == 200

def test_delete_product(client):
    product = Product.query.first()
    response = client.delete(f'/products/{product.id}')
    assert response.status_code == 204

def test_list_all_products(client):
    response = client.get('/products')
    assert response.status_code == 200

def test_list_products_by_name(client):
    response = client.get('/products?name=Test Product')
    assert response.status_code == 200

def test_list_products_by_category(client):
    response = client.get('/products?category=Electronics')
    assert response.status_code == 200

def test_list_products_by_availability(client):
    response = client.get('/products?availability=True')
    assert response.status_code == 200
