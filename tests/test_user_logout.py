import pytest
from playwright.sync_api import expect

from pages import home_page, my_account_page
from pages.home_page import *
from pages.login_page import LoginPage
from pages.my_account_page import *
from config import Config

@pytest.mark.regression
def test_user_logout(page):
    home_page = Homepage(page)
    login_page = LoginPage(page)
    my_account_page=Myaccountpage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.set_email(Config.email)
    login_page.set_password(Config.password)
    login_page.click_login()

    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)

    logout_page = my_account_page.click_logout()


