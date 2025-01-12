import random
import string
import requests


def create_random_string(lenth):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(lenth))
    return random_string

def register_new_user_and_return_params():

    result = []

    email = f'{create_random_string(8)}@mail.ru'
    password = create_random_string(12)
    name = create_random_string(12)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
    access_token = response.json()['accessToken']
    refresh_token = response.json()['refreshToken']

    if response.status_code == 200:
        result.append(email)
        result.append(password)
        result.append(name)
        result.append(access_token)
        result.append(refresh_token)
    else:
        print("Регистрация провалена")

    # возвращаем список
    return result

def get_user_token():

    tokens = []

    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', json={
                                                                                        "email": "Maks123512@mail.ru",
                                                                                        "password": "123123"
                                                                                        })
    access_token = response.json()['accessToken']
    refresh_token = response.json()['refreshToken']

    if response.status_code == 200:
        tokens.append(access_token)
        tokens.append(refresh_token)
    else:
        print("Вход не выполнен")

    return tokens
