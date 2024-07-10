import Helpers.base as base
import Helpers.auth as auth


class TestAuthEndpoints:
    @classmethod
    def setup_class(cls):
        configs = base.read_json_to_dict('config_test.json')
        cls.url = configs['base_url']
        cls.username = configs['auth']['username']
        cls.password = configs['auth']['password']
    
    def test_GIVEN_good_credentials_WHEN_sent_to_auth_api_THEN_200_is_returned(self): 
        response = auth.get_auth_endpoint_response(self)
        assert response.status_code == 200

