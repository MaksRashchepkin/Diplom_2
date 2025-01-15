import pytest
import allure
import data


class TestCreateUser:

    @allure.title("Проверка создания пользователя")
    def test_create_user(self, create_user_page):
        create_user_page.create_user(data.create_user_payload)
        create_user_page.assert_status_code(200)
        create_user_page.assert_create_user_successfully()

    @allure.title("Проверка вывода ошибки при создании пользователя без обязательных параметров")
    @pytest.mark.parametrize('key', ["email", "password", "name"])
    def test_create_user_error_on_empty_params(self, create_user_page, key):
        payload = data.create_user_payload.copy()
        payload[key] = None
        create_user_page.create_user(payload)
        create_user_page.assert_status_code(403)
        create_user_page.assert_registration_error()

    @allure.title("Проверка вывода ошибки при создании пользователя с данными которые уже есть в базе")
    def test_error_create_dublicate_users(self, create_user_page):
        create_user_page.create_user(data.created_user_payload)
        create_user_page.assert_status_code(403)
        create_user_page.assert_create_user_failed()
        create_user_page.assert_user_already_exist_error()