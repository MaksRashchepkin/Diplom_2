from pages.base_page import BasePage
import data


class CreateUserPage(BasePage):

    def create_user(self, payload, header=None):
        self.post_method(data.CREATE_USER, header, payload)

    def return_auth_token(self):
        response_body = self.return_response_body
        if 'accessToken' in response_body:
            return response_body['accessToken']
        else:
            return None

    def assert_create_user_successfully(self):
        assert self.return_response_body['success'] == True

    def assert_create_user_failed(self):
        assert self.return_response_body['success'] == False

    def assert_registration_error(self):
        assert self.return_error_msg == "Email, password and name are required fields"

    def assert_user_already_exist_error(self):
        assert self.return_error_msg == "User already exists"
