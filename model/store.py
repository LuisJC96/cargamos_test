from persistance.sqlconn import SqlConnector


class Store:
    Table = "store"
    collection_master_query = ""

    def __init__(self):
        self.columns = [
            'store_id',
            'store_name',
            'store_street',
            'store_mail',
            'store_phone_number',
            'store_city',
            'store_state',
            'store_zip_code'
        ]

    def insert_store(self, values):
        sqlconn = SqlConnector()
        sqlconn.insert_data(values, self.Table)
        return None

    def update_store(self, values, conditions=[]):
        sqlconn = SqlConnector()
        return sqlconn.update_data(values, self.Table, conditions=conditions)

    def get_store(self, conditions=[]):
        sqlcon = SqlConnector()
        return sqlcon.get_data(self.columns, self.Table, conditions=conditions)
