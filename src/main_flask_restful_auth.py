from flask import Flask, request  # , jsonify   # no need to jsonify, because Flask RESTful does it for us
from flask_restful import Resource, Api  # resource is everything that the API can return
from flask_jwt import JWT, jwt_required

from src.security import authenticate, identity

app = Flask(__name__)

app.secret_key = "jose"

api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)  # give next item, else None
        return {"item": item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None) is not None:
            return {"message": "An item with name {} already exists".format(name)}, 400  # bad request

        request_data = request.get_json()

        item = {'name': name, 'price': request_data["price"]}
        items.append(item)
        return item, 201  # 201 means created

    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "item {} deleted".format(name)}


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(ItemList, "/items")

api.add_resource(Item, "/item/<string:name>")  # the same as @app.route("/student/<string:name>")

app.run(port=5000, debug=True)
