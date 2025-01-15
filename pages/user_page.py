from pages.base_page import BasePage
import data


class UserPage(BasePage):

    def patch_user(self, header, payload):
        self.patch_method(data.USER, header, payload)

    def assert_user_data_change(self, expected_data):
        assert self.return_response_body['user'] == expected_data

    def assert_error_change_data_without_authorization(self):
        assert self.return_error_msg == 'You should be authorised'
