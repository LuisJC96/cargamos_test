from model.inventory import Inventory

# Third Party Modules
from flask import request
from flask_restful import Resource


class AddStockResource(Resource):
    def post(self):
        try:
            """
            adds x quantity of the y product in the given z store
            :returns example:
            {
                "success": True,
            }
            """
            inventory = Inventory()
            json = request.json
            inventory.modify_stock(json['store_id'], json['product_id'], json['quantity'])
            return {'success': True, 'product': json}
        except Exception as e:
            return {'success': False, 'Error': str(e)}
