from persistance.sqlconn import SqlConnector
from model.order_product import OrderProduct
from datetime import date


class Order:
    Table = "orders"
    collection_master_query = {
        'get_order_by_order_id': 'select orders.order_id, orders.customer_id, orders.store_id, orders.order_date, '
                                 'order_products.product_id, order_products.quantity, product.product_cost, '
                                 'product.product_name, customer.customer_first_name, customer.customer_last_name, '
                                 'customer.customer_phone_number, customer.customer_mail, customer.customer_street, '
                                 'customer.customer_city, customer_state, customer_zip_code from orders join '
                                 'order_products on orders.order_id = order_products.order_id join product on '
                                 'product.product_id = order_products.product_id join customer on customer.customer_id '
                                 '= orders.customer_id where orders.order_id = %s',
    }

    def __init__(self):
        self.columns = [
            'order_id',
            'customer_id',
            'store_id',
            'order_date'
        ]

    def insert_order(self, values):
        sqlconn = SqlConnector()
        values['date'] = date.today().strftime("%Y-%m-%d")
        order_product = OrderProduct()
        sqlconn.insert_data(values, self.Table)
        for product in values['products']:
            order_product.insert_order_product(product)

    def get_order_by_order_id(self, order_id):
        sqlcon = SqlConnector()
        query = self.collection_master_query['get_order_by_order_id'] % order_id
        values = sqlcon.get_query(query)
        formated_order = {
            'order_id': order_id,
            'customer_id': values[0]['customer_id'],
            'store_id': values[0]['store_id'],
            'order_date': str(values[0]['order_date']),
            'customer_name': values[0]['customer_first_name'] + ' ' + values[0]['customer_last_name'],
            'customer_phone_number': values[0]['customer_phone_number'],
            'customer_mail': values[0]['customer_mail'],
            'customer_street': values[0]['customer_street'],
            'customer_city': values[0]['customer_city'],
            'customer_state': values[0]['customer_state'],
            'customer_zip_code': values[0]['customer_zip_code'],
            'products': []
        }
        total_cost = 0
        for value in values:
            formated_order['products'].append(
                {
                    'product_id': value['product_id'],
                    'quantity': value['quantity'],
                    'product_unit': value['product_cost'],
                    'product_total_cost': float(value['product_cost']) * int(value['quantity']),
                    'prduct_name': value['product_name']
                }
            )
            total_cost += float(value['product_cost']) * int(value['quantity'])
        formated_order['total_cost'] = total_cost
        print(formated_order)
        return formated_order
