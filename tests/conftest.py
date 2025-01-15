from pages.create_orders_page import CreateOrderPage
from pages.create_user_page import CreateUserPage
from pages.login_user_page import LoginUserPage
from pages.user_page import UserPage
from pages.get_order_page import GetOrderPage
from pages.delete_user_page import DeleteUserPage
import pytest


@pytest.fixture()
def create_user_page():
    create_user_page = CreateUserPage()
    yield create_user_page
    delete_user_page = DeleteUserPage()
    if create_user_page.return_auth_token():
        delete_user_page.delete_user({'Authorization': create_user_page.return_auth_token()})

@pytest.fixture()
def login_user_page():
    login_user_page = LoginUserPage()
    return login_user_page

@pytest.fixture()
def user_page():
    user_page = UserPage()
    return user_page

@pytest.fixture()
def create_order_page():
    create_order_page = CreateOrderPage()
    return create_order_page

@pytest.fixture()
def get_order_page():
    get_order_page = GetOrderPage()
    return get_order_page
