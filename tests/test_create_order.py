import pytest
import allure
import data


class TestCreateOrder:

    @allure.title("Проверка создания заказа с добавлением ингредиентов авторизованным и не авторизованным пользователем")
    @pytest.mark.parametrize('ingregients, header', [('Био-марсианский метеоритный флюоресцентный бургер', None),
                                                     ('Фалленианский люминесцентный флюоресцентный минеральный бургер', {'Authorization': data.my_token['accessToken']})])
    def test_create_order(self, create_order_page, ingregients, header):
        create_order_page.create_order(header, {'ingredients': data.ingredients[ingregients]})
        create_order_page.assert_status_code(200)
        create_order_page.assert_order_has_been_created(ingregients)

    @allure.title("Проверка создания заказа без ингредиентов авторизованным и не авторизованным пользователем ")
    @pytest.mark.parametrize('header', [None, {'Authorization': data.my_token['accessToken']}])
    def test_order_creation_with_no_ingredients(self, create_order_page, header):
        create_order_page.create_order(header, {'ingredients': None})
        create_order_page.assert_status_code(400)
        create_order_page.assert_error_create_order()

    @allure.title("Проверка создания заказа с добавлением битого хеша ингредиента")
    @pytest.mark.parametrize('header', [None, {'Authorization': data.my_token['accessToken']}])
    def test_order_creation_with_valid_ingredients(self, create_order_page, header):
        create_order_page.create_order(header, {'ingredients': data.ingredients['invalid hash']})
        create_order_page.assert_status_code(500)
