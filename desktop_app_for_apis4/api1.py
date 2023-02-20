# Deploy this api to server

from flask import Flask, request

from flask import *
from flask import request



app = Flask(__name__)


@app.route('/Hello', methods=['POST'])
def hello():
    data = request.json
    name = data.get('Name')
    city = data.get('City')
    if not name or not city:
        return {
            "Message": "Name and City fields are required"
        }, 403
    return {
        "Greeting": f"Hello {name}",
        "Message": f"How are things at {city}?",
    }, 200

@app.route("/add", methods=["POST"])

def json_example():
    if request.is_json:

        req = request.json
        print(req)
        Number1 = req.get("Number1")
        Number2 = req.get("Number2")
        if not Number1 or not Number2:
            return {
                       "Message": "Number1 and Number2 keys are required"
                   }, 403

        response_body = {
            "sum": req.get("Number1")+req.get("Number2")
        }
        res = make_response(jsonify(response_body), 200)
        return res

    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)


if __name__ == "__main__":
    app.run()