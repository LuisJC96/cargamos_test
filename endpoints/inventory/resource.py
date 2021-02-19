from model.inventory import Inventory
from utilities.string_builders import conditions_builder
# Third Party Modules
from flask import request
from flask_restful import Resource


class InventoryResource(Resource):
    def get(self):
        try:
            """
            """
            inventory = Inventory()
            json = request.json
            ans = None
            if bool(json) or json is not None:
                if 'store_id' in json:
                    if 'product_id' in json:
                        ans = inventory.get_product_availability_in_specific_store(json['product_id'],
                                                                                   json['store_id'])
                    else:
                        ans = inventory.get_store_inventory(json['store_id'])
                elif 'product_id' in json:
                    ans = inventory.get_product_availability_all_stores(json['product_id'])
            else:
                ans = inventory.get_all_inventory_all_stores()
            return {'success': True, 'Inventory': ans}
        except Exception as e:
            return {'success': False, 'Error': str(e)}
