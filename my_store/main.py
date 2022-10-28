from flask import Flask, jsonify, request, render_template

app = Flask("__name__")

stores = [
    {
        'name': 'New store',
        'items': [
            {
                'name': 'New item',
                'price': 15.99,
            },
        ],
    },
]


@app.route('/')
def home():
    return render_template("index.html")
# POST - used to receive date
# GET - used to send date back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    new_request = request.get_json()
    new_store = {
        'name': new_request['name'],
        'items': [],
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')  # http://127.0.0.0:5000/store/store_name
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store error!'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    new_request = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': new_request['name'],
                'price': new_request['price'],
            }
            print(new_item)
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store error!'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store error!'})


app.run(debug=True)
