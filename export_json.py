import json
import psycopg2


username = 'postgres'
password = 'Slava270602'
database = 'mykhailenkoyaroslava'
host = 'localhost'
port = '5432'

TABLES = [
    'products',
    'restaurants',
    'restaurants_products',
    'orderitems',
    'orders'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()
    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]
        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows


with open('Mykhailenko_DB.json', 'w') as outf:
    json.dump(data, outf, default=str)