import pytest
import allure
import data as data


class TestUser:


    @allure.title("Проверка изменения данных авторизованного пользователя пользователя")
    def test_edit_user_data(self, user_page):
        user_page.patch_user(data.patch_user_header, data.patch_payload)
        user_page.assert_status_code(200)
        user_page.assert_user_data_change(data.patch_payload)

    @allure.title("Проверка изменения данных не авторизованного пользователя пользователя")
    @pytest.mark.parametrize('key, value', [('name', 'Edit My Name'), ('email', data.create_user_payload['email'])])
    def test_edit_user_data_without_authorization(self, user_page, key, value):
        user_page.patch_user(None, {key: value})
        user_page.assert_status_code(401)
        user_page.assert_error_change_data_without_authorization()
