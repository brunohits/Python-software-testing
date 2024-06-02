import json

import requests

BASE_URL = 'http://127.0.0.1:5000/'


def get_form():
    response = requests.get(BASE_URL)
    return response


def post_form(data):
    json_data = json.dumps(data)
    response = requests.post(BASE_URL + 'result', data=json_data, headers={'Content-Type': 'application/json'})
    return response