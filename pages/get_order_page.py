from pages.base_page import BasePage
import data


class GetOrderPage(BasePage):

    def get_orders(self, token):
        self.get_method(data.ORDER, token)

    def assert_order_list_not_empty(self):
        assert len(self.return_response_body['orders']) != 0

    def assert_error_get_order_with_unauthorized_user(self):
        assert self.return_error_msg == 'You should be authorised'
