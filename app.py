from flask import Flask, render_template, request, jsonify, redirect, url_for
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search']
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_term = request.json['searchInput']  # Make sure to retrieve the search input correctly
    search_result = search_products(search_term)
    return jsonify(search_result)  # Return search results as JSON


def load_products_from_json():
    with open('data/products.json', 'r') as json_file:
        products = json.load(json_file)
    return products


def search_products(search_term):
    products = load_products_from_json()

    if products is None:
        return []

    matching_products = [
        product for product in products
        if (
                isinstance(product.get('name'), str)
                and product.get('name') is not None  # Ensure 'name' attribute is not None
                and search_term
                and isinstance(search_term, str)
                and search_term.lower() in product['name'].lower()
        )
    ]

    return matching_products


if __name__ == '__main__':
    app.run(debug=True, port=5003)
