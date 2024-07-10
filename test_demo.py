import Helpers.base as base
import Helpers.auth as auth


class TestExample:
    @classmethod
    def setup_class(cls):
        configs = base.read_json_to_dict('config_test.json')
        cls.url = configs['base_url']
        cls.username = configs['auth']['username']
        cls.password = configs['auth']['password']
    
    def test_example(self): 
        response = auth.get_auth_endpoint_response(self)
        assert response.status_code == 200

