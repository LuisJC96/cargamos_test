# Custom Resources
from endpoints.store.resource import StoreResource
from endpoints.whoami.resource import WhoAmIResource
from endpoints.product.resource import ProductResource
from endpoints.inventory.resource import InventoryResource

# Third Party Modules
from flask_cors import CORS
from flask_restful import Api
from flask import Flask

app = Flask(__name__)
api = Api(app)
CORS(app)
# Resources(All the clases developed for GET, POST, UPDATE, PUT)
api.add_resource(WhoAmIResource, '/')
api.add_resource(StoreResource, '/store')
api.add_resource(ProductResource, '/product')
api.add_resource(InventoryResource, '/inventory')


if __name__ == '__main__':
    # app.config['TESTING'] = False
    app.run(port=5000)
