from model.store import Store
from utilities.string_builders import conditions_builder
# Third Party Modules
from flask import request
from flask_restful import Resource


class StoreResource(Resource):
    def get(self):
        try:
            """
            Obtains a Product given the corresponding filters on the JSON
            json example:
            {
                "store_name":"Buy and sell books",
            }
            :returns example:
            {
                "success": true,
                "stores":[
                    {
                        "store_id":1,
                        "store_name":"Buy and sell books",
                        "store_address": "1st Avenue",
                    },
                    ...
                ]
            }
            """
            store = Store()
            json = request.json
            ans = []
            if json is not None:
                conditions = conditions_builder(json)
                ans = store.get_store(conditions)
            return {'success': True, 'stores': ans}
        except Exception as e:
            print(e)
            return {'success': False, 'Error': str(e)}

    def post(self):
        try:
            """
            inserts a store on the DB given by the JSON, for more information of the model refer to this project on
            model/store
            :returns example:
            {
                "success": True,
                "product": store_of_product
            }
            """
            store = Store()
            json = request.json
            store.insert_store(json)
            return {'success': True, 'store': json}
        except Exception as e:
            return {'success': False, 'Error': str(e)}

    def put(self):
        try:
            """
            updates a store on the DB with the given JSON values and filtered by store_id, for more information 
            of the model refer to this project on model/store
            :returns example:
            {
                "success": True,
                "product": store_of_product
            }
            """
            store = Store()
            json = request.json
            print(request.json)
            conditions = conditions_builder({'store_id':json['store_id']})
            json.pop('store_id', None)
            store.update_store(json, conditions=conditions)
            return {'success': True, 'store': json}
        except Exception as e:
            return {'success': False, 'Error': str(e)}
