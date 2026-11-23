import pytest

from pages import my_account_page
from pages.registration_page import *
from pages.home_page import *
from pages.registration_page import *
from pages.login_page import *
from pages.my_account_page import *
from pages.logout_page import *
from pages.search_results_pages import *
from pages.product_pages import *
from config import Config
from utils.random_data_util import RandomDataUtil
from playwright.sync_api import expect

def test_end_to_end():
    registered_email,registered_password = perform_registration(page)
    print("Registration completed successfully!")

    perform_login(page,registered_email,registered_password)
    print("Login completed successfully!")

    add_product(page)
    print("product added to cart successfully!")

    verify_shopping_cart(page)
    print("shopping cart verified successfully!")


def perform_registration(page):
    homepage = Homepage(page)
    registration_page = RegistrationPage(page)

    homepage.click_my_account()
    homepage.click_register()

    random_data=RandomDataUtil()
    first_name=random_data.get_first_name()
    last_name=random_data.get_last_name()
    email=random_data.get_email()
    password=random_data.get_password()

    registration_page.set_first_name(first_name)
    registration_page.set_last_name(last_name)
    registration_page.set_email(email)
    registration_page.set_password(password)
    registration_page.click_privacy_policy()
    registration_page.btn_continue()
    confirmation_page = registration_page.get_msg_confirmation()
    expect(confirmation_page).to_have_text("Your Account Has Been Created!")

    return email,password
