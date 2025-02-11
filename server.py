from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json
# import requests

# ENTER "flask --app server run" to run Flask server
app = Flask(__name__)

# MongoDB connection
app.config["MONGO_URI"] = "mongodb+srv://bryanchan:snhu-cs499@snhu-cs499.6oodr.mongodb.net/"

client = MongoClient(
    "mongodb+srv://bryanchan:snhu-cs499@snhu-cs499.6oodr.mongodb.net/")
db = client["electoral-college-simulator"]
collection = db["ECMap"]
mongo = PyMongo(app)


@app.route('/api', methods=['GET'])
def fetch_ECMap():
    # fetch data from ECMap in MongoDB
    data = list(collection.find({}, {"id": 0}))
    return jsonify(data)


if __name__ == "__main__":
    # use port 8000 for the server in order to work
    app.run(port=8000, debug=True)
