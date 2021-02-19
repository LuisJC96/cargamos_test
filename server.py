# Custom Resources
from endpoints.order.resource import OrderResource
from endpoints.store.resource import StoreResource
from endpoints.whoami.resource import WhoAmIResource
from endpoints.product.resource import ProductResource
from endpoints.inventory.resource import InventoryResource
from endpoints.modify_stock.resource import ModifyStockResource

# Third Party Modules
from flask_cors import CORS
from flask_restful import Api
from flask import Flask

app = Flask(__name__)
api = Api(app)
CORS(app)
# Resources(All the clases developed for GET, POST, UPDATE, PUT)
api.add_resource(WhoAmIResource, '/')
api.add_resource(OrderResource, '/order')
api.add_resource(StoreResource, '/store')
api.add_resource(ProductResource, '/product')
api.add_resource(InventoryResource, '/inventory')
api.add_resource(ModifyStockResource, '/modify_stock')


if __name__ == '__main__':
    # app.config['TESTING'] = False
    app.run(port=5000)
