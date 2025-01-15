from pages.base_page import BasePage
import data


class CreateOrderPage(BasePage):

    def create_order(self, header, payload):
        self.post_method(data.ORDER, header, payload)

    def assert_order_has_been_created(self, burger):
        assert (self.return_response_body['name'] == burger) and (self.return_response_body['success'] == True)

    def assert_error_create_order(self):
        assert self.return_error_msg == 'Ingredient ids must be provided'
