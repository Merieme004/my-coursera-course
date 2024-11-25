# service/routes.py

from flask import Blueprint, request, jsonify
from app.models import Product
from app import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(name=data['name'], description=data['description'], price=data['price'], category=data['category'], availability=data['availability'])
    db.session.add(product)
    db.session.commit()
    return jsonify(product), 201

@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get(id)
    if product:
        product.price = data['price']
        db.session.commit()
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Product not found"}), 404

@products_bp.route('/products', methods=['GET'])
def list_all_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@products_bp.route('/products', methods=['GET'])
def list_products_by_filter():
    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('availability')
    
    query = Product.query
    if name:
        query = query.filter(Product.name.contains(name))
    if category:
        query = query.filter(Product.category.contains(category))
    if availability:
        query = query.filter(Product.availability == availability)
    
    products = query.all()
    return jsonify([product.to_dict() for product in products])
