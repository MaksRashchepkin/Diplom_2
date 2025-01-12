import allure
import data as data


class TestGetOrders:


    @allure.title("Проверка получения списка заказов авторизованного пользователя")
    def test_get_my_orders_list(self, get_order_page):
        get_order_page.get_orders({'Authorization': data.my_token['accessToken']})
        get_order_page.assert_status_code(200)
        get_order_page.assert_order_list_not_empty()

    @allure.title("Проверка получения списка заказов не авторизованного пользователя")
    def test_error_get_orders_list_with_unauthorized_user(self, get_order_page):
        get_order_page.get_orders(None)
        get_order_page.assert_status_code(401)
        get_order_page.assert_error_get_order_with_unauthorized_user()
