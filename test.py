# test making GET request from MongoDB, and place into hashmap

import requests
import json


extractECMapURL = "http://127.0.0.1:5000/api"
res = requests.get(extractECMapURL)

# ECMap = dict()

# temp error handling
if res.status_code == 200:
    # print(type(res.json()))
    data = res.json()  # list

    statesList = data[0]["states"]

    ECMap = {
        state["state"]: state["electoral_votes"]
        for state in statesList
    }

    for x, y in ECMap.items():
        print(f'{x} | {y}')


else:
    print('Error: ', res.status_code)
