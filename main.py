import psycopg2
import math
import matplotlib.pyplot as plt

username = 'postgres'
password = 'Slava270602'
database = 'mykhailenkoyaroslava'
host = 'localhost'
port = '5432'


query_1 = '''
CREATE VIEW QuantityOrdersDay AS SELECT order_date, COUNT(*)
AS quantity_orders FROM orders  GROUP BY order_date

'''

query_2 = '''
CREATE VIEW СountOrderRestaunants AS SELECT TRIM(restaurants.rest_name), COUNT(rest_id) FROM restaurants  JOIN orders 
USING(rest_id) GROUP BY rest_id

'''

query_3 = '''
CREATE VIEW PricesOrderedProducts AS SELECT prod_price, sum(quantity)
AS quantity_products  FROM products JOIN orderitems
USING(prod_id) GROUP BY prod_price ORDER BY prod_price

'''


con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)



with con:
    cur = con.cursor()
    cur.execute('drop view if exists QuantityOrdersDay')
    cur.execute(query_1)
    cur.execute('select * from QuantityOrdersDay')

    diagram_bar = {}
    for row in cur:
        diagram_bar[row[0]] = row[1]
        print(row)

    plt.bar(list(map(lambda x: str(x), list(diagram_bar.keys()))),diagram_bar.values())
    plt.xticks(rotation=45)
    plt.title('Кількість зроблених заказів в певний день')
    plt.xlabel('Дні')
    plt.ylabel('Кількість замовлень')
    plt.show()



    cur.execute('drop view if exists СountOrderRestaunants')
    cur.execute(query_2)
    cur.execute('select * from СountOrderRestaunants')

    diagram_pie = {}
    for row in cur:
        diagram_pie[row[0]] = row[1]
        print(row)

    fig, ax = plt.subplots()
    colors = ['#4F6272', '#B7C3F3', '#DD7596', '#8EB897','#B7C3F3']
    ax.pie(diagram_pie.values(), labels = diagram_pie.keys(), autopct='%1.1f%%', colors=colors)
    plt.title('Скільки відсотків ринку належить кожному ресторану')
    plt.show()



    cur.execute('drop view if exists PricesOrderedProducts')
    cur.execute(query_3)
    cur.execute('select * from PricesOrderedProducts')

    price = []
    quantity = []
    for row in cur:
        price.append(row[0])
        quantity.append(row[1])

        print(row)

    fig, ax = plt.subplots()
    ax.plot(price, quantity, marker='o')
    plt.title("Зв'язок між кількістю замовлень того, чи іншого продукту та їх цінами")
    plt.xlabel('Ціни')
    plt.ylabel('Кількість')
    plt.show()
