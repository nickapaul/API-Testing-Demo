import requests

def send_request(method, url, payload, headers):
    
    return requests.request(method, url, headers=headers, data=payload)