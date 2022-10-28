from flask import Flask

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


# POST - used to receive date
# GET - used to send date back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>') # http://127.0.0.0:5000/store/store_name
def get_store(name):
    pass


# GET /store
@app.route('/store')
def get_store():
    pass


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(debug=True)