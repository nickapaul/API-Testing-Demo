import requests
import json

# Common helper method used with all api requests
def send_request(method, url, payload, headers):    
    return requests.request(method, url, headers=headers, data=payload)

# common method for reading a json into a dict 
def read_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data
