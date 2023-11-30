import mysql.connector
import json

# Load JSON data
with open('/home/abinesh/Users/Abinesh/Solr/data/products.json') as file:
    data = json.load(file)

# Establish MySQL connection
connection = mysql.connector.connect(
    host='localhost',
    user='abinesh',
    password='abinesh@123',
    database='abinesh_solr'
)
cursor = connection.cursor()

# Create table (replace column names and data types as per your JSON)
create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        uid VARCHAR(255),
        gid VARCHAR(255),
        category VARCHAR(255),
        sub_category VARCHAR(255),
        brand VARCHAR(255),
        model VARCHAR(255),
        quantity INT,
        name VARCHAR(255),
        price INT
    )
"""
cursor.execute(create_table_query)

# Insert JSON data into the MySQL table
for item in data:
    insert_query = """
        INSERT INTO products 
        (uid, gid, category, sub_category, brand, model, quantity, name, price) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        item['uid'],
        item['gid'],
        item['category'],
        item['sub_category'],
        item['brand'],
        item['model'],
        item['quantity'],
        item['name'],
        item['price']
    )
    cursor.execute(insert_query, values)

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()
