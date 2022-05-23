from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'Store One',
        'items': [
            {
                'name': 'Item One',
                'price': 1.99
            },
            {
                'name': 'Item Two',
                'price': 2.99
            },
            {
                'name': 'Item Three',
                'price': 3.99
            },
        ]
    },
    {
        'name': 'Store Two',
        'items': [
            {
                'name': 'Item Four',
                'price': 4.99
            },
            {
                'name': 'Item Five',
                'price': 5.99
            },
            {
                'name': 'Item Six',
                'price': 6.99
            },
        ]
    },
    {
        'name': 'Store Three',
        'items': [
            {
                'name': 'Item Seven',
                'price': 7.99
            },
            {
                'name': 'Item Eight',
                'price': 8.99
            },
            {
                'name': 'Item Nine',
                'price': 9.99
            },
        ]
    },
]


@app.route('/store', methods=['POST'])
def create_store():
    return "create store"


@app.route('/store/<string:name>')
def get_store(name):
    return "get store"


@app.route('/store')
def get_stores():
    return "get stores"


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    return "create item in store"


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    return "get items in store"


app.run(port=5000)
