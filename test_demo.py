import pytest
import requests
import json

class TestExample:
    def test_example(self):
        

        url = "https://restful-booker.herokuapp.com/auth"

        payload = json.dumps({
        "username": "admin",
        "password": "password123"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        n=1
