# 15/20: Look it up via an API!
# - STEP 1 OF 2 -

# Start the API server.

from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

with open("./data.json", "r", encoding="utf8") as f:
    reversed = json.load(f)

class ReverseString(Resource):
    def get(self, orig_word):
        try:
            return {orig_word: reversed[orig_word]}
        except KeyError:
            return {orig_word: "Sorry, I don't know how to reverse this: {}".format(orig_word)}

api.add_resource(ReverseString, '/<string:orig_word>')

app.run(debug=True)