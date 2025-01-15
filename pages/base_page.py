import requests
import allure
import data

class BasePage:

    def post_method(self, endpoint, header, payload=None):
        self.response = requests.post(f'{data.URL}{endpoint}', headers=header, data=payload)
        return self.response

    def delete_method(self, endpoint, header):
        self.response = requests.delete(f'{data.URL}{endpoint}', headers=header)
        return self.response

    def patch_method(self, endpoint, header, json):
        self.response = requests.patch(f'{data.URL}{endpoint}', headers=header, json=json)
        return self.response

    def get_method(self, endpoint, header):
        self.response = requests.get(f'{data.URL}{endpoint}', headers=header)
        return self.response

    @property
    def return_response_body(self):
        return self.response.json()

    @property
    def return_error_msg(self):
        return self.response.json().get('message', 'No message provided')

    @allure.step('Проверяем статус код')
    def assert_status_code(self, code):
        assert self.response.status_code == code, f'{self.response.status_code} != {code}'