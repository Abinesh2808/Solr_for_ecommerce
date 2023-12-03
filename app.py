from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)
solr_core_url = "http://localhost:8983/solr/solr_sample_core"
# solr_core_url = "http://localhost:8983/solr/testing"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search']
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    search_term = request.json['searchInput']  # Make sure to retrieve the search input correctly
    search_result = search_products_solr(search_term)
    return jsonify(search_result)  # Return search results as JSON


# Function to perform a Solr search
def search_products_solr(search_term):
    solr_url = f"{solr_core_url}/select"  # Modify this URL to match your Solr setup
    params = {
        # Define your query parameters as needed
        'q': f'name:{search_term} OR brand:{search_term} OR model:{search_term} OR category:{search_term} OR sub_category:{search_term}',
        'start': 0,
        'rows': 1000  # Number of rows/results to fetch
    }
    
    response = requests.get(solr_url, params=params)
    if response.status_code == 200:
        solr_data = response.json()
        return solr_data.get('response', {}).get('docs', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


if __name__ == '__main__':
    app.run(debug=True, port=5003)