import psycopg2
import yaml

conf_file = './configurations.yaml'
with open(conf_file, 'r') as f:
    doc = yaml.safe_load(f)

connection = psycopg2.connect(
    database=doc['sql_connection']['database'],
    user=doc['sql_connection']['user'],
    password=doc['sql_connection']['password'],
    host=doc['sql_connection']['host'],
    port=doc['sql_connection']['port']
)
commands = [
    """
    insert  into customer(customer_first_name, customer_last_name, customer_phone_number, customer_mail, customer_street,customer_city, customer_state,customer_zip_code)
    values('John', 'Doe', '+525555555555', 'johndoe@test.com', '1st street', '1st City', '1st state', '00000')
    """,
    """
    insert  into customer(customer_first_name, customer_last_name, customer_phone_number, customer_mail, customer_street,customer_city, customer_state,customer_zip_code)
    values('Jane', 'Doe', '+525511447788', 'janedoe@test.com', '2st street', '2st City', '2st state', '11111')
    """,
    """
    insert  into customer(customer_first_name, customer_last_name, customer_phone_number, customer_mail, customer_street,customer_city, customer_state,customer_zip_code)
    values('Richard', 'Parker', '+52553164978256', 'rparker@test.com', '1st street', '1st City', '1st state', '00000')
    """,
    """
    insert into product(product_name, product_description, product_cost)
    values('Book Alpha', 'Its the Alpha book', 5000)
    """,
    """
    insert into product(product_name, product_description, product_cost)
    values('Book Beta', 'Its the Beta book', 5000)
    """,
    """
    insert into product(product_name, product_description, product_cost)
    values('Book Gamma', 'Its the Gamma book', 5000)
    """,
    """
    insert into store (store_name, store_street, store_mail, store_phone_number, store_city, store_state, store_zip_code)
    Values('Store1','Avenue1', 'store1@store1.com', '+5255239996', 'City1', 'State1', '11111')
    """,
    """
    insert into store (store_name, store_street, store_mail, store_phone_number, store_city, store_state, store_zip_code)
    Values('Store2','Avenue2', 'store1@store2.com', '+521234567895', 'City2', 'State2', '22222')
    """,
    """
    insert into store (store_name, store_street, store_mail, store_phone_number, store_city, store_state, store_zip_code)
    Values('Store3','Avenue3', 'store1@store3.com', '+521473692580', 'City3', 'State3', '33333')
    """,
    """
    insert into orders(customer_id, store_id, order_date)
    values(1,1,'2020-02-19')
    """,
    """
    insert into orders(customer_id, store_id, order_date)
    values(2,2,'2020-02-19')
    """,
    """
    insert into orders(customer_id, store_id, order_date)
    values(3,3,'2020-02-19')
    """,
    """
    insert into order_products(order_id, product_id, quantity)
    values(1,1,1)
    """,
    """
    insert into order_products(order_id, product_id, quantity)
    values(2,2,2)
    """,
    """
    insert into order_products(order_id, product_id, quantity)
    values(3,3,3)
    """,
    """
    insert into product_store (product_id, store_id, quantity)
    values(1,1,100)
    """,
    """
    insert into product_store (product_id, store_id, quantity)
    values(2,2,100)
    """,
    """
    insert into product_store (product_id, store_id, quantity)
    values(3,3,100)
    """
]
cursor = connection.cursor()
for command in commands:
    cursor.execute(command)
connection.close()
