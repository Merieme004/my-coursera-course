# tests/test_models.py

import pytest
from app.models import Product  # Assuming the product model is defined here
from app import db

@pytest.fixture
def product():
    """Create a product fixture."""
    return Product(name="Test Product", description="A test product", price=20.99, category="Electronics", availability=True)

def test_create_product(product):
    db.session.add(product)
    db.session.commit()
    assert product.id is not None

def test_update_product(product):
    product.price = 25.99
    db.session.commit()
    updated_product = Product.query.get(product.id)
    assert updated_product.price == 25.99

def test_delete_product(product):
    db.session.delete(product)
    db.session.commit()
    deleted_product = Product.query.get(product.id)
    assert deleted_product is None

def test_list_all_products():
    products = Product.query.all()
    assert len(products) > 0

def test_find_product_by_name():
    product = Product.query.filter_by(name="Test Product").first()
    assert product is not None

def test_find_product_by_category():
    products = Product.query.filter_by(category="Electronics").all()
    assert len(products) > 0

def test_find_product_by_availability():
    products = Product.query.filter_by(availability=True).all()
    assert len(products) > 0
