import psycopg2
import yaml
import os

conf_file = './configurations.yaml'
with open(conf_file, 'r') as f:
    doc = yaml.safe_load(f)

connection = psycopg2.connect(
    database='postgres',
    user=doc['sql_connection']['user'],
    password=doc['sql_connection']['password'],
    host=doc['sql_connection']['host'],
    port=doc['sql_connection']['port']
)
connection.autocommit = True
cursor = connection.cursor()
query = 'Create database %s' % doc['sql_connection']['database']
cursor.execute(query)
tables = [
    """
    create table product(
	    product_id serial primary key,
	    product_name VARCHAR(100) not null,
	    product_description VARCHAR(255),
	    product_cost int not null
    );
    """,
    """
    create table store(
        store_id serial primary key,
        store_name VARCHAR(100) not null,
        store_street VARCHAR(100) not null,
        store_mail VARCHAR(100),
        store_phone_number VARCHAR(25),
        store_city VARCHAR(50),
        store_state VARCHAR(50),
        store_zip_code VARCHAR(25)
    );
    """,
    """
    create table product_store(
        product_store_id serial primary key,
        product_id int references product(product_id),
        store_id int references store(store_id),
        quantity int
    );
    """
]
connection = psycopg2.connect(
    database=doc['sql_connection']['database'],
    user=doc['sql_connection']['user'],
    password=doc['sql_connection']['password'],
    host=doc['sql_connection']['host'],
    port=doc['sql_connection']['port']
)
cursor = connection.cursor()
for command in tables:
    cursor.execute(command)
connection.close()
