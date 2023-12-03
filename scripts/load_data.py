import pysolr
import json

with open('../data/products.json', 'r') as file:
    data = json.load(file)

solr = pysolr.Solr("http://localhost:8983/solr/solr_sample_core2", always_commit=True)


solr.add(data)