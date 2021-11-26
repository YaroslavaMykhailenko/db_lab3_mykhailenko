import csv
import decimal
import psycopg2

username = 'postgres'
password = 'Slava270602'
database = 'mykhailenkoyaroslava'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'products.csv'

query_0 = '''
CREATE TABLE products_new(

    prod_id     char(50)       UNIQUE NOT NULL,
    prod_name   char(200)      NULL,
    prod_price  decimal(8,2)   NULL,
    CONSTRAINT pk_products_new PRIMARY KEY (prod_id)
)
'''

query_1 = '''
DELETE FROM products_new
'''

query_2 = '''
INSERT INTO products_new (prod_id, prod_name, prod_price) VALUES (%s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:

    cur = conn.cursor()
    cur.execute('drop table if exists products_new')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)

        for idx, row in enumerate(reader):
            price = decimal.Decimal(row['Product_Price'])
            values = (row['Product_Id'], row['Product_Name'], price)
            cur.execute(query_2, values)

    conn.commit()