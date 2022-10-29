from flask import Flask
from flask_restful import Resource, Api

app = Flask("__name__")
api = Api(app)

items = []


class Item(Resource):
    @staticmethod
    def get(name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    @staticmethod
    def post(name):
        item = {'name': name,
                'price': 12.00}
        items.append(item)
        return item, 201


api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/chair

app.run(debug=True)
