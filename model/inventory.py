from persistance.sqlconn import SqlConnector
from utilities.string_builders import conditions_builder


class Inventory:
    Table = "product_store"
    # Even though to make simple queries to obtain information, update and create new registers i developed a function
    # to use direct SQL syntax to get more complicated entities which in this case is inventory which is composed from
    # two tables, also obtaining values from model product and cross it with the obtained of product_store would be
    # possible but that would mean making more than one request to the Database which is something we dont want, to
    # have better efficiency
    collection_master_query = {
        'store_inventory': 'select product.product_id, store_id, quantity, product.product_name from product_store join'
                           ' product on product_store.product_id = product.product_id where store_id = %s',
        'store_availability_specific_product': 'select product.product_id, store_id, quantity, product.product_name '
                                               'from product_store  join product on product_store.product_id = '
                                               'product.product_id where store_id = %s and product.product_id = %s',
        'specific_product_availability': 'select product.product_id, store_id, quantity, product.product_name from '
                                         'product_store join product on product_store.product_id = product.product_id '
                                         'and product.product_id= %s',
        'all_stores_inventory': 'select product.product_id, store.store_id, quantity, product.product_name, '
                                'store.store_name from product_store join product on product_store.product_id = '
                                'product.product_id join store on store.store_id = product_store.store_id '
    }

    def __init__(self):
        self.columns = [
            'product_store_id',
            'product_id',
            'store_id',
            'quantity']

    def get_store_inventory(self, store_id):
        sqlcon = SqlConnector()
        query = self.collection_master_query['store_inventory'] % store_id
        values = sqlcon.get_query(query)
        inventory = []
        for value in values:
            inventory.append({
                'product_id': value['product_id'],
                'product_name': value['product_name'],
                'quantity': value['quantity']
            })
        return inventory

    def get_product_availability_all_stores(self, product_id):
        sqlcon = SqlConnector()
        query = self.collection_master_query['specific_product_availability'] % product_id
        return sqlcon.get_query(query)

    def get_product_availability_in_specific_store(self, product_id, store_id):
        sqlcon = SqlConnector()
        query = self.collection_master_query['store_availability_specific_product'] % (product_id, store_id)
        return sqlcon.get_query(query)

    def get_all_inventory_all_stores(self):
        sqlcon = SqlConnector()
        values = sqlcon.get_query(self.collection_master_query['all_stores_inventory'])
        general_inventory = {}
        for value in values:
            if value['store_id'] not in general_inventory:
                general_inventory[value['store_id']] = {
                    'store_name': value['store_name'],
                    'store_inventory': [{value['product_name']: value['quantity']}]
                }
            else:
                general_inventory[value['store_id']]['store_inventory'].append(
                    {value['product_name']: value['quantity']})
        return general_inventory

    def modify_stock(self, store_id, product_id, quantity):
        sqlcon = SqlConnector()
        conditions = conditions_builder({'store_id': store_id, 'product_id': product_id})
        values = sqlcon.get_data(self.columns, self.Table, conditions)
        if len(values) == 0:
            data = {
                'product_id': product_id,
                'store_id': store_id,
                'quantity': quantity
            }
            sqlcon.insert_data(data, self.Table)
        else:
            conditions = conditions_builder({'product_store_id': values['product_store_id']})
            data = {
                'quantity': quantity+int(values[quantity])
            }
            sqlcon.update_data(data, self.Table, conditions=conditions)
        return {'success': True}
