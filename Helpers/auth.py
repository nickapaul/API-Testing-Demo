import requests
import json

def get_auth_endpoint_response(self):
    url = f'{self.url}' + 'auth'

    payload = json.dumps({
        "username": self.username,
        "password": self.password
    })
    headers = {
    'Content-Type': 'application/json'
    }
    return requests.request("POST", url, headers=headers, data=payload)
