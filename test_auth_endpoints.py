import Helpers.base as base
import Helpers.auth as auth


class TestAuthEndpoints:
    @classmethod
    def setup_class(cls):
        configs = base.read_json_to_dict('config_test.json')
        cls.url = configs['base_url']
        cls.username = configs['auth']['username']
        cls.password = configs['auth']['password']
    
    def test_GIVEN_good_credentials_WHEN_sent_to_auth_api_THEN_200_is_returned_and_no_error_returned(self): 
        response = auth.get_auth_endpoint_response_good_auth(self)
        assert response.status_code == 200
        assert response.text != '{"reason":"Bad credentials"}'

    def test_GIVEN_bad_username_credential_WHEN_sent_to_auth_api_THEN_200_is_returned_and_error_is_returned(self): 
        response = auth.get_auth_endpoint_response_custom_credentials(self, 'Nick', self.password)
        assert response.text == '{"reason":"Bad credentials"}'
        assert response.status_code == 200
    
    def test_GIVEN_bad_password_credential_WHEN_sent_to_auth_api_THEN_200_is_returned_and_error_is_returned(self): 
        response = auth.get_auth_endpoint_response_custom_credentials(self, self.username, 'Paul')
        assert response.text == '{"reason":"Bad credentials"}'
        assert response.status_code == 200

    def test_GIVEN_bad_credentials_WHEN_sent_to_auth_api_THEN_200_is_returned_and_error_is_returned(self): 
        response = auth.get_auth_endpoint_response_custom_credentials(self, 'Nick', 'Paul')
        assert response.text == '{"reason":"Bad credentials"}'
        assert response.status_code == 200
