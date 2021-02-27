from flask import Flask
from flask_restful import Api, Resource, reqparse
import binanceAPI

app = Flask(__name__)
api = Api(app)


api.add_resource(binanceAPI.Route, "/")
api.add_resource(binanceAPI.Crypto, "/<string:name>")

if __name__ == "__main__":
    app.run(debug = True)