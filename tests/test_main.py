import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.order import Order
from model.store import Store
from model.product import Product
from model.inventory import Inventory


def test_insert_order():
    order = Order()
    order_to_db = {
        'customer_id': 1,
        'store_id': 1,
    }
    assert isinstance(order.insert_order(order_to_db), int)


def test_get_order_by_order_id():
    order = Order()
    order_info = order.get_order_by_order_id(1)
    assert 'order_id' in order_info and 'customer_id' in order_info and 'store_id' in order_info and \
           'order_date' in order_info and 'customer_name' in order_info and 'customer_phone_number' in order_info and \
           'customer_mail' in order_info and 'customer_street' in order_info and 'customer_city' in order_info and \
           'customer_state' in order_info and 'customer_zip_code' in order_info and 'products' in order_info


def test_insert_store():
    store = Store()
    store_to_db = {
        'store_name': 'book seller No. 1',
        'store_street': '5th Avenue',
        'store_mail': 'books@books.com',
        'store_phone_number': '5522887799',
        'store_city': 'City 1',
        'store_state': 'State 1',
        'store_zip_code': '99999',
    }
    ans = store.insert_store(store_to_db)
    assert ans['success']


def test_update_store():
    store = Store()
    updated_values = {
        'store_name': 'I completely love books'
    }
    conditions = ['store_id = 1']
    ans = store.update_store(updated_values, conditions=conditions)
    assert ans['success']


def test_get_store():
    store = Store()
    store_info = store.get_store(conditions=['store_id = 1'])
    assert 'store_id' in store_info[0] and 'store_name' in store_info[0] and 'store_street' in store_info[0] and \
           'store_mail' in store_info[0] and 'store_phone_number' in store_info[0] and 'store_city' in store_info[0] and \
           'store_state' in store_info[0] and 'store_zip_code' in store_info[0]


def test_insert_product():
    product = Product()
    product_to_db = {
        'product_name': 'Book 40',
        'product_description': 'its as good as Book 6',
        'product_cost': 90
    }
    ans = product.insert_product(product_to_db)
    assert ans['success']


def test_update_product():
    product = Product()
    updated_values = {
        'product_cost': 91
    }
    conditions = ['product_id = 1']
    ans = product.update_product(updated_values, conditions=conditions)
    assert ans['success']


def test_get_product():
    product = Product()
    product_info = product.get_product(conditions=['product_id = 1'])
    assert 'product_id' in product_info[0] and 'product_name' in product_info[0] and 'product_description' in \
           product_info[0] and 'product_cost' in product_info[0]


def test_get_store_inventory():
    inventory = Inventory()
    inventory_info = inventory.get_store_inventory(1)
    assert 'product_id' in inventory_info[0] or len(inventory_info) == 0


def test_get_product_availability_all_stores():
    inventory = Inventory()
    inventory_info = inventory.get_product_availability_all_stores(1)
    assert 'product_id' in inventory_info[0] or len(inventory_info) == 0


def test_get_product_availability_in_specific_store():
    inventory = Inventory()
    inventory_info = inventory.get_product_availability_in_specific_store(1, 1)
    assert 'product_id' in inventory_info[0] or len(inventory_info) == 0


def test_get_all_inventory_all_stores():
    inventory = Inventory()
    inventory_info = inventory.get_all_inventory_all_stores()
    assert isinstance(inventory_info, dict)


def test_modify_stock():
    inventory = Inventory()
    inventory_info = inventory.modify_stock(1, 1, 5)
    assert inventory_info['success']
