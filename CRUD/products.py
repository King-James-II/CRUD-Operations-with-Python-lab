from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]


# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


# Get a product by its id
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)


# Add a product
@app.route('/products', methods=['POST'])
def add_product():
    products.append(request.get_json())
    return '', 201


# Update a product by its id
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    updated_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in updated_product.items():
        product[key] = value
    return '', 204


# Delete a product by its id
@app.route('/products/<int:id>', methods=['DELETE'])
def remove_product(id):
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204

app.run(port=5000,debug=True)
