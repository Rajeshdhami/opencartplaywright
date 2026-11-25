import pytest

from pages import my_account_page
from pages.home_page import Homepage
from pages.login_page import LoginPage
from pages.my_account_page import Myaccountpage
from playwright.sync_api import Page,expect
from config import Config
import time

@pytest.mark.sanity
def test_invalid_login_page(page):
    home_page = Homepage(page)
    login_page = LoginPage(page)

    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email(Config.invalid_email)
    login_page.set_password(Config.invalid_password)

    login_page.click_login()
    time.sleep(3)

    expect(login_page.get_login_error()).to_be_visible(timeout=300)
@pytest.mark.sanity
@pytest.mark.regression
def test_login_valid_page(page):
    home_page = Homepage(page)
    login_page = LoginPage(page)
    obj_my_account_page = Myaccountpage(page)

    home_page.click_my_account()
    home_page.click_login()
    login_page.set_email(Config.email)
    login_page.set_password(Config.password)

    login_page.click_login()
    time.sleep(3)

    expect(obj_my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)









