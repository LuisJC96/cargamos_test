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
        sqlconn = SqlConnector()
        sqlconn.insert_data(values, self.Table)
        return None

    def update_product(self, values, conditions=[]):
        sqlconn = SqlConnector()
        return sqlconn.update_data(values, self.Table, conditions=conditions)

    def get_product(self, conditions=[]):
        sqlcon = SqlConnector()
        return sqlcon.get_data(self.columns, self.Table, conditions=conditions)
