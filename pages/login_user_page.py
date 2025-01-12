from pages.base_page import BasePage
import data


class LoginUserPage(BasePage):

    def login_user(self,  payload, header=None):
        self.post_method(data.LOGIN_USER, header, payload)

    def assert_login_error(self):
        assert self.return_error_msg == "email or password are incorrect"
