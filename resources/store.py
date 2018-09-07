from flask_restful import Resource
from models.stores import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store didnt exits'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)

        try:
            if store:
                return {'message': 'store with name {} exists'.format(name)}, 400
        except:
            return {'message': 'error in saving store'}, 500

        store = StoreModel(name)
        store.save_to_database()
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_database()
            return {'message': 'sotre deleted'}
        return {'message': 'store dont exist'}, 404



class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
