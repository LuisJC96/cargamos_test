from model.inventory import Inventory
from utilities.string_builders import conditions_builder
# Third Party Modules
from flask import request
from flask_restful import Resource


class InventoryResource(Resource):
    def get(self):
        try:
            """
            gets an specific store inventory, book inventory across all stores or all the inventory of all the stores 
            to get an store inventory:
                json example:
                    {
                        "store_id":123
                    }
            :returns example:
                {
                    "success":true,
                    "Inventory":[
                        {
                            "product_id":1,
                            "product_name": "Product_name_1",
                            "quantity":1
                        },
                        .
                        .
                        .
                    ]
                }
            to get product inventory across all stores:
                json example:
                    {
                        "product_id":123
                    }
            :returns example:
                {
                    "success": true,
                    "inventory": [
                        {
                            "product_id":123,
                            "store_id":1,
                            "quantity":1,
                            "product_name": "Product_name"
                        }
                    ]
                }
            to get an specific product on an specific store:
                json example:
                    {
                        "store_id":123,
                        "product_id":123
                    }
            :returns example:
                {
                    "success": true,
                    "inventory":[
                        {   
                            "product_id":123,
                            "store_id":123,
                            "quantity":123,
                            "product_name":"product_name"
                        }
                    ]
                }     
            to obtain all the inventory across all stores, simply send no JSON at all:
            :returns example
                {
                    "success": true,
                    inventory:
                    {
                        {
                            "1"(store_id):{
                                "store_name": "This_is_a_name",
                                "store_inventory":[
                                    {
                                        "product_name":5(quantity)
                                    },
                                    ...
                                ],
                                ...
                            }
                            ...
                        }
                    }
                }
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
            return {'success': True, 'inventory': ans}
        except Exception as e:
            return {'success': False, 'Error': str(e)}
