This "Flask Project" repository is intended to give a class about how to create a Flask app with Python. There is also some advanced Python programming (decorators), some tips about git and some bad jokes.

# Prerequisites
* Python lists - Dictionaries
* Object oriented programming (python classes)
* Github account!
* Programs listed below installed!

# What will (should..?) you know at the end of the lesson
* Create a git repo
* Decorators? Decorators
* Create a Flask application
* Create a REST API with Flask
* Add authentication to your REST API
## Next Steps (not in this lesson haha salu2, but we can talk a little bit)
* Swagger UI (similar to Postman, but integrated as a Python module)
* Use SQL database (MySQL - Postgres) / Firebase (NoSQL)
* Deploy Flask API to Heroku/DigitalOcean/OVH/Amazon

# Installation
## Programs
* Git: https://git-scm.com/downloads
* Sourcetree (recommended): https://www.sourcetreeapp.com/
* Postman: https://www.getpostman.com/products
* Pycharm community IDE (recommended): https://www.jetbrains.com/pycharm/download/
    * Other IDEs: Atom/Visual Studio Code/Sublime Text


## Dependencies - Virtual Environment
Let's create a virtual environment! Such a great idea! It lets you isolate 
all your projects so that they don't depend on modules of other projects

In case you don't have Pycharm -> Create Virtual Environment and activate
```bash
$ cd <your dir>
$ pip3 install virtualenv
$ virtualenv venv --python=python3.6
$ source venv/bin/activate
```
Now that you have a Virtual Environment, install all the libraries needed:
```bash
$ pip3 install -r requirements.txt
```
### .gitignore
Gitignore file at the root of the project makes git ignore all files that match a pattern 
so that they don't get committed. Useful for files with keys/tokens/passwords or huge files that you don't want 
to be pushed (e.g. virtual Env)

There is one webpage that generates this file for you, kinda helpful:
https://www.gitignore.io/

# Concepts
## HTTP Verbs
![HTTP Verbs](/screenshots/httpverbs.png)

## Decorators
Decorator example (more inside examples/example_decorator.py)

```python
def dec_returns(func):
    def wrapper(*args, **kwargs):
        print("I do something before")
        aux_out = func(*args, **kwargs)
        print("I do something after")
        return aux_out
    return wrapper


@dec_returns
def los_hahas():
    return "LOL"


a = los_hahas()
print(a)
```

Out: 
```bash
I do something before
I do something after
LOL
```

# First Flask App
```python
from flask import Flask, jsonify, request

# __name__ == "__main__" if executed. It will give the module name if imported and printed
app = Flask(__name__)


# main page (like 'index.html')
@app.route("/")
def home():
    # Flash automatically looks at the 'templates' folder, very important to have the same folder name
    return "Hello world!"


# POST - Used to receive data
# GET - Used to send data back only

# POST /endpoint data:
@app.route("/endpoint", methods=['GET'])
def return_something():
    d_return = {
        "something": "this is a return message",
        "type": "dummy one ofc"
    }
    return jsonify(d_return)


# test with postman/swagger
# POST /post data:
@app.route("/post", methods=['POST'])
def return_post():
    data = request.get_json()
    return jsonify({"data_received": data})


app.run(port=5000)
```

## Lets add this sheet to github
* Create a project in github
* in the root folder of your project in the terminal, type: `git init`
* go to github and follow the instructions to add the local repo or follow this:
```bash
git add .
git commit -m "First commit"
git remote add origin remote repository URL
git push -u origin master
``` 


# Add data management to Flask
```python
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
    # Flash automatically looks at the 'templates' folder, very important to have the same folder name
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
```

## TestDrivenDevelopment
TDD - BDD, o como debería ser SEAT

Open Postman, we will test the endpoints there and create new test for our app


# Flask-RESTful API module
This module does the same as Flask module, although it ensures you follow the rules of the REST 
APIs, so it's more restrictive than Flask. But it's good because this way other programmers know that 
your API applies to REST API rules.
```python
from flask import Flask, request  # , jsonify   # no need to jsonify, because Flask RESTful does it for us
from flask_restful import Resource, Api  # resource is everything that the API can return

app = Flask(__name__)

api = Api(app)

items = []


class Item(Resource):
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


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(ItemList, "/items")

api.add_resource(Item, "/item/<string:name>")  # the same as @app.route("/student/<string:name>")

app.run(port=5000, debug=True)
```

## JWT - Json Web token authentication - If there is enough time
Basically, a token that is passed with the Header attribute of the HTTP Verb

### Ideas lokas to do with Flask:
* send chistes to a list of users ;)
* Tweet generator
* Shakespeare Insult Generator: http://www.pangloss.com/seidel/shake_rule.html
* QR Generator
* Automatic watering for plants with Raspberry: https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc
* Free apis: https://github.com/toddmotto/public-apis


