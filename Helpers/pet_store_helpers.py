import Helpers.common_helpers as c_help
import json

def create_pet(pet_name):  
    # grabs the url from the config  
    url = c_help.read_json_file('Config/pet_store_urls.json')['pet']['create_pet']

    # Reads in the resource json into a dict
    payload = c_help.read_json_file('Resource/create_pet.json')
    
    # Changes some of the variables in runtime
    payload['name'] = pet_name
    payload['category']['id'] = 74
    payload['category']['name']= 'pitbull'
    
    # Create headers
    headers = {
    'Content-Type': 'application/json'
    }
    
    # Executes the rerquest
    result = c_help.send_request("Post", url, json.dumps(payload), headers)
    
    # Asserts that the request comes back 200
    if result.status_code is not 200:
        raise Exception(f'{result.status_code}: {result.text}')
    return result

def get_pet_via_pet_id(pet_id):
    # grabs the url from the config
    base_url = c_help.read_json_file('Config/pet_store_urls.json')['pet']['get_pet']
    
    # Injects the active petID into the url
    url_with_id = f'{base_url}{str(pet_id)}'

    # no payload or header
    payload={}
    headers = {}
    
    # Executes the rerquest
    result = c_help.send_request("Get", url_with_id, payload, headers)
    
    # Asserts that the request comes back 200
    if result.status_code is not 200:
        raise Exception(f'{result.status_code}: {result.text}')
    return json.loads(result.content)  



def create_pet_and_return_pet_id(pet_name='Brady'):
    return json.loads(create_pet(pet_name).content)['id']    
