from pages.base_page import BasePage
import data


class DeleteUserPage(BasePage):

    def delete_user(self, header):
        self.delete_method(data.USER, header )
