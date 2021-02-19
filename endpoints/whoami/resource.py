# Third Party Modules
from flask import request
from flask_restful import Resource


class WhoAmIResource(Resource):
    def __init__(self):
        pass

    def get(self):
        return 'Hello from the store!!'

    def post(self):
        args = request.args
        json = request.json
        return {'success': True, 'args': args, 'json': json}