from flask import Flask, jsonify, request, render_template

# __name__ == "__main__" if executed. It will give the module name if imported and printed
app = Flask(__name__)

stores = [
    {
        'name': 'MaltrALTRAN Store',
        'items': [
            {
                'name': 'esclavo 1',
                'price': 3.99
            }
        ]
    }
]


@app.route("/")
def home():
    # Flash automatically looks at the 'templates' folder, very important to have the same name
    return render_template("index.html")


# POST - Used to receive data
# GET - Used to send data back only

# POST /store data: {name:}
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data["name"],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>", methods=["GET"])  # http://127.0.0.1/5000/store/some_name
def get_store(name):
    for store in stores:
        if name == store["name"]:
            return jsonify({"store": store})
    else:
        return jsonify({"message": "Store not found!"})


# GET /store
@app.route("/store", methods=["GET"])
def get_stores():
    # jsonify converts a python dictionary to json for the browser
    return jsonify({"stores": stores})


# POST /store/<string:name>/item data: {name:}
@app.route("/store/<string:name>/item", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if name == store["name"]:
            store["items"].append({"name": request_data["name"], "price": request_data["price"]})
            return jsonify(store)
    else:
        return jsonify({"message": "Store not found!"})


# GET /store/<string:name>
@app.route("/store/<string:name>/item", methods=["GET"])
def get_items_in_store(name):
    for store in stores:
        if name == store["name"]:
            return jsonify({"items": store['items']})
    else:
        return jsonify({"message": "Store not found!"})


app.run(port=5000)
