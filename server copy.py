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


# method from ECSIM class (main.py)
# def extractECMap(self):
#      # read ElectoralMap.json file
#      # file = open("ElectoralMap.json", "r")
#      # data = json.load(file)

#      extractECMapURL = "http://127.0.0.1:5000/api"
#       res = requests.get(extractECMapURL)

#        # temp error handling
#        if res.status_code == 200:
#             print(res.json())
#         else:
#             print('Error: ', res.status_code)

#         # data =
#         # for states, ECMapJSONFile in data.items():

#         #     # loop through ElectoralMap.json list:
#         #     for ECMapJSON in ECMapJSONFile:
#         #         self.ECMap[ECMapJSON["state"]] = ECMapJSON["electoral_votes"]


if __name__ == "__main__":
    # use port 8000 for the server in order to work
    app.run(port=8000, debug=True)
