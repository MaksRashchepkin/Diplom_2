import helper as helper

URL = 'https://stellarburgers.nomoreparties.site'

CREATE_USER = '/api/auth/register'
LOGIN_USER = '/api/auth/login'
USER = '/api/auth/user'
ORDER = '/api/orders'

create_user_payload = {
    "email": f'{helper.create_random_string(8)}@mail.ru',
    "password": helper.create_random_string(12),
    "name": helper.create_random_string(12)
}

generate_params = helper.register_new_user_and_return_params()

created_user_payload = {
    "email": generate_params[0],
    "password": generate_params[1],
    "name": generate_params[2]
}

auth_payload = {
    "email": generate_params[0],
    "password": generate_params[1]
}

patch_user_header = {
    'Authorization': generate_params[3]
}
patch_payload = {"email": generate_params[0].lower(),
                "name": "Edit My Name"}

ingredients = {
    'Био-марсианский метеоритный флюоресцентный бургер': ['61c0c5a71d1f82001bdaaa70', '61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa6d'],
    'Фалленианский люминесцентный флюоресцентный минеральный бургер': ["61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa77", "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa6d"],
    'invalid hash': ["61c0c5a71d1f8200asdc21saOSHIBKAf@DS1bdaaa79"]
}

my_token = {
    "accessToken": helper.get_user_token()[0],
    "refreshToken": helper.get_user_token()[1]
}
