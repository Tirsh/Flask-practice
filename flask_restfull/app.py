from flask import Flask, request
from flask_restful import Resource, Api

app = Flask("__name__")
app.secret_key = "valeriy"
api = Api(app)

items = []


class Item(Resource):
    @staticmethod
    def get(name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': None}, 200 if item is not None else 404

    @staticmethod
    def post(name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"message": "An item with name '{}' already exists.".format(name)}
        data = request.get_json()
        item = {'name': name,
                'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    @staticmethod
    def get():
        return {'items': items}


api.add_resource(ItemList, '/items')  # http://127.0.0.1:5000/items
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/chair

app.run(debug=True)
