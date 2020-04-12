from flask_restful import Resource
from models.store import StoreModel 

class Store(Resource): 

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store: 
            return store.json() # returns items as well 

        return {'message': 'Store not found'}, 404  

    def post(self, name):
        if StoreModel.find_by_name(name): 
            return {'message': 'Store is already created'}, 400 

        store = StoreModel(name) 
        try: 
            store.save_to_db()
        except: 
            return {'message': 'An error occurred'}, 500 

        return store.json(), 201 # 201 - has been created 
        

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store: 
            store.delete_from_db() 

        return {'message': 'Store deleted'} 

class StoreList(Resource): 
    def get(self): 
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))} 