import requests
import json
import pytest


def test_demo():  
  url = "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='493316'"

  payload={}
  headers = {
    'Cookie': 'cf_use_ob=0'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  test = json.loads(response.content)

  print(response.text)
