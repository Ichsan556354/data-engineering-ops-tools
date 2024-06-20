from flask import Flask, request, jsonify

app = Flask(__name__)
products = []

# Create
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = {
        'id': len(products) + 1,
        'nama': data['nama'],
        'harga': data['harga'],
        'deskripsi': data['deskripsi']
    }
    products.append(product)
    return jsonify({'message': 'Product berhasil dibuat', 'product': product}), 201

# read data
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return jsonify({'message': 'menemukan produk', 'produk': product}), 201
    else:
        return jsonify({'message': 'Product not found'}), 404


# update data
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        product.update(data)
        return jsonify({'message': 'Berhasil update', 'product': product}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

# delete data
@app.route('/products', methods=['DELETE'])
def delete_product():
    global products
    products = []  # Mengosongkan daftar produk
    return jsonify({'message': 'All products deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
