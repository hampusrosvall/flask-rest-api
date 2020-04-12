from flask import Flask
from flask_restful import Api 
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister 
from resources.item import Item, ItemList 
from resources.store import Store, StoreList

from db import db 

app = Flask(__name__)
app.secret_key = 'hampus'
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

jwt = JWT(app, authenticate, identify)

@app.before_first_request
def crete_tables(): 
    db.create_all()

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': 
    db.init_app(app)
    app.run(port = 5000, debug = True)

