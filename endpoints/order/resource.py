from model.order import Order
from model.order import OrderProduct
from model.inventory import Inventory
# Third Party Modules
from flask import request
from flask_restful import Resource


class OrderResource(Resource):
    def get(self):
        try:
            order = Order()
            json = request.json

            ans = []
            if json is not None and 'order_id' in json:
                ans = order.get_order_by_order_id(json['order_id'])
                # inventory.modify_stock()
            return {'success': True, 'products': ans}
        except Exception as e:
            return {'success': False, 'Error': str(e)}

    def post(self):
        try:
            order = Order()
            order_product = OrderProduct()
            json = request.json
            inventory = Inventory()
            order_to_db = {
                'customer_id': json['customer_id'],
                'store_id': json['store_id'],
            }
            order_id = order.insert_order(order_to_db)
            for product in json['products']:

                store_inventory = inventory.get_product_availability_in_specific_store(product['product_id'], json['store_id'])
                if product['quantity'] > store_inventory[0]['quantity']:
                    return {'success': False, 'Error': 'product unavailable '+product['product_id']}
                product['order_id'] = order_id
                order_product.insert_order_product(product)
                inventory.modify_stock(json['store_id'], product['product_id'], int(product['quantity'])*-1)
            return {'success': True, 'product': json}
        except Exception as e:
            return {'success': False, 'Error': str(e)}
