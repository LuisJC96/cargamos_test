from model.product import Product
from utilities.string_builders import conditions_builder
# Third Party Modules
from flask import request
from flask_restful import Resource


class ProductResource(Resource):
    def get(self):
        try:
            """
            """
            product = Product()
            json = request.json
            ans = []
            if json is not None:
                conditions = conditions_builder(json)
                ans = product.get_product(conditions)
            return {'success': True, 'products': ans}
        except Exception as e:
            return {'success': False, 'Error': str(e)}

    def post(self):
        try:
            """
            """
            product = Product()
            json = request.json
            product.insert_product(json)
            return {'success': True, 'product': json}
        except Exception as e:
            return {'success': False, 'Error': str(e)}

    def put(self):
        try:
            """
            """
            product = Product()
            json = request.json
            print(request.json)
            conditions = conditions_builder({'product_id': json['product_id']})
            json.pop('product', None)
            product.update_product(json, conditions=conditions)
            return {'success': True, 'product': json}
        except Exception as e:
            return {'success': False, 'Error': str(e)}
