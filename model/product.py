from persistance.sqlconn import SqlConnector


class Product:
    Table = "product"
    collection_master_query = ""

    def __init__(self):
        self.columns = [
            'product_id',
            'product_name',
            'product_description',
            'product_cost']

    def insert_product(self, values):
        try:
            sqlconn = SqlConnector()
            sqlconn.insert_data(values, self.Table)
            return {'success': True}
        except Exception as e:
            return {'success': False}

    def update_product(self, values, conditions=[]):
        try:
            sqlconn = SqlConnector()
            sqlconn.update_data(values, self.Table, conditions=conditions)
            return {'success': True}
        except Exception as e:
            return {'success': False}

    def get_product(self, conditions=[]):
        sqlcon = SqlConnector()
        return sqlcon.get_data(self.columns, self.Table, conditions=conditions)
