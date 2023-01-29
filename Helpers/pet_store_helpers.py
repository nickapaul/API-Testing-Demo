import Helpers.common_helpers as c_help
import json

def create_pet(pet_name):    
    url = c_help.read_json_file('Config/pet_store_urls.json')['create_pet']

    payload = c_help.read_json_file('Resource/create_pet.json')
    payload['name'] = pet_name
    payload['category']['id'] = 74
    payload['category']['name']= 'pitbull'
    headers = {
    'Content-Type': 'application/json'
    }
    result = c_help.send_request("Post", url, json.dumps(payload), headers)
    if result.status_code is not 200:
        raise Exception(f'{result.status_code}: {result.text}')
    return result

def get_pet_via_pet_id(pet_id):
    base_url = c_help.read_json_file('Config/pet_store_urls.json')['get_pet']
    url_with_id = f'{base_url}{str(pet_id)}'

    payload={}
    headers = {}
    result = c_help.send_request("Get", url_with_id, payload, headers)
    if result.status_code is not 200:
        raise Exception(f'{result.status_code}: {result.text}')
    return json.loads(result.content)  



def create_pet_and_return_pet_id(pet_name='Brady'):
    return json.loads(create_pet(pet_name).content)['id']    
