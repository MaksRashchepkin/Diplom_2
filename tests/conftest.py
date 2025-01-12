from pages.create_orders_page import CreateOrderPage
from pages.create_user_page import CreateUserPage
from pages.login_user_page import LoginUserPage
from pages.user_page import UserPage
from pages.get_order_page import GetOrderPage
from pages.delete_user_page import DeleteUserPage
import pytest
import requests


@pytest.fixture()
def create_user_page():
    response = requests
    create_user_page = CreateUserPage(response)
    yield create_user_page
    delete_user_page = DeleteUserPage(response)
    if create_user_page.return_auth_token():
        delete_user_page.delete_user({'Authorization': create_user_page.return_auth_token()})

@pytest.fixture()
def login_user_page():
    response = requests
    login_user_page = LoginUserPage(response)
    return login_user_page

@pytest.fixture()
def user_page():
    response = requests
    user_page = UserPage(response)
    return user_page

@pytest.fixture()
def create_order_page():
    response = requests
    create_order_page = CreateOrderPage(response)
    return create_order_page

@pytest.fixture()
def get_order_page():
    response = requests
    get_order_page = GetOrderPage(response)
    return get_order_page
