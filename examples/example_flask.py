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
