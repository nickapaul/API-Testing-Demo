import requests
import json

def get_auth_endpoint_response_good_auth(self):    
    payload = json.dumps({
        "username": self.username,
        "password": self.password
    })    
    return post_to_auth_endpoint(self, payload)

def get_auth_endpoint_response_custom_credentials(self, username, password):
    payload = json.dumps({
        "username": username,
        "password": password
    })    
    return post_to_auth_endpoint(self, payload)

def post_to_auth_endpoint(self, payload):
    url = f'{self.url}' + 'auth'
    headers = {
    'Content-Type': 'application/json'
    }
    return requests.request("POST", url, headers=headers, data=payload)

