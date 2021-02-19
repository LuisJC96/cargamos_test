from model.store import Store
from utilities.string_builders import conditions_builder
# Third Party Modules
from flask import request
from flask_restful import Resource


class StoreResource(Resource):
    def get(self):
        try:
            """
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
