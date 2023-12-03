import pysolr

# Connect to a Solr instance running at localhost:8983/solr/mycollection
solr = pysolr.Solr('http://localhost:8983/solr/solr_sample_core', always_commit=True)

# a = solr.ping()
# print(a)

# # 1. Add a document to the Solr index
# document = {'id': '523', 'title': 'My Document Title', 'content': 'This is the content of my document.'}
# solr.add([document])
# solr.commit()


# 2. Search for documents matching the query 'title:My Document Title'
# results = solr.search('title:My Document Title')

# for doc in results.docs:
#     print(doc['id'], doc['title'])


# 3. Delete a document with ID 
# solr.delete(['523'])
# solr.commit()


# 4. Search for documents with 'price' greater than 100
# results = solr.search('price:[100 TO *]', fl='name , id, price, brand')

# for doc in results.docs:
#     print(doc['name'], doc['id'], doc['price'], doc['brand'])


# 5. Search for documents and sort by 'price' in descending order
# results = solr.search('category:cricket', sort='price desc')

# for doc in results.docs:
#     print(doc['name'], doc['price'])


# # 6.Search for documents and facet by 'category'
# results = solr.search('*:*', **{
#     'facet': 'true',
#     'facet.field': 'category'
# })

# # Accessing facet counts
# facet_counts = results.raw_response['facet_counts']['facet_fields']['category']

# # Printing facet counts
# for idx in range(0, len(facet_counts), 2):
#     category = facet_counts[idx]
#     count = facet_counts[idx + 1]
#     print(f"Category: {category}, Count: {count}")


# 7.Search for documents and highlight 'title' and 'content' fields
# results = solr.search('title:My Document Title', **{
#     'hl': 'true',
#     'hl.fl': ['title', 'content']
# })

# for doc in results.docs:
#     print(doc['id'], doc['title'], doc['content'])
#     if 'highlighting' in results:
#         highlights = results.highlighting.get(doc['id'], {})
#         highlighted_title = highlights.get('title', [])
#         if highlighted_title:
#             print("Highlighted Title:", highlighted_title)


# # 8.Find documents similar to the document with ID '123'
# results = solr.more_like_this(q='id:1', mltfl='category', mlt_id='1', rows=10)

# for doc in results.docs:
#     print(doc['id'], doc['title'])


# # 9.Define pagination parameters
# page_number = 1  # Page number you want to retrieve
# # page_number = 2
# page_size = 10   # Number of results per page

# start = (page_number - 1) * page_size  # Calculate the starting index

# # Query with pagination parameters
# results = solr.search('*:*', **{
#     'start': start,
#     'rows': page_size,
#     'sort': 'id asc'  # Optionally, you can specify a sort order
# })

# # Process and print the results
# for doc in results.docs:
#     print(doc['category'], doc['price'])


# 10.optimization (is used to merge index segments and reduce the number of segments)
# import requests
# from urllib.parse import urlencode

# # Replace 'YOUR_SOLR_URL' with your Solr URL
# solr_url = 'http://localhost:8983/solr/solr_sample_core'

# # Define the URL for force merge operation
# url = f'{solr_url}/update?{urlencode({"optimize": "true"})}'

# # Send a POST request to perform force merge
# response = requests.post(url)

# # Check the response status
# if response.status_code == 200:
#     print("Optimization completed successfully.")
# else:
#     print("Optimization failed.")







