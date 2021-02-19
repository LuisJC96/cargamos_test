from model.order import Order
from utilities.string_builders import conditions_builder
# Third Party Modules
from flask import request
from flask_restful import Resource


class OrderResource(Resource):
    def get(self):
        try:
            order = Order()
            json = request.json
            ans = []
            if json is not None and 'order_id'in json:
                ans = order.get_order_by_order_id(json['order_id'])
                print('THIS IS ANS')
                print(ans)
            return {'success': True, 'products': ans}
        except Exception as e:
            return {'success': False, 'Error': str(e)}

    def post(self):
        try:
            order = Order()
            json = request.json
            order.insert_order(json)
            return {'success': True, 'product': json}
        except Exception as e:
            return {'success': False, 'Error': str(e)}