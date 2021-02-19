from persistance.sqlconn import SqlConnector
from datetime import date


class OrderProduct:
    Table = "order_products"
    collection_master_query = ""

    def __init__(self):
        self.columns = [
            'order_product_id',
            'order_id',
            'product_id',
            'quantity'
        ]

    def insert_order_product(self, values):
        sqlconn = SqlConnector()
        return sqlconn.insert_data(values, self.Table)

    def update_order_product(self, values, conditions=[]):
        sqlconn = SqlConnector()
        return sqlconn.update_data(values, self.Table, conditions=conditions)

    def get_order_product(self, conditions=[]):
        sqlcon = SqlConnector()
        return sqlcon.get_data(self.columns, self.Table, conditions=conditions)
