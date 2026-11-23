from pages.home_page import Homepage
from pages.login_page import LoginPage
from pages.my_account_page import Myaccountpage
from playwright.sync_api import Page,expect
import time
from utils.data_reader_util import *
import pytest

#csv_data= read_csv_data("../testdata/logindata.csv")
read_json_data = read_json_data("../testdata/logindata.json")

@pytest.mark.parametrize("testName,email,password,expected",read_json_data)
def test_invalid_login_page(page,testName,email,password,expected):
    home_page = Homepage(page)
    login_page = LoginPage(page)
    obj_my_account_page = Myaccountpage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.login(email,password)
    time.sleep(3)

    if expected == "success":
        expect(obj_my_account_page.get_my_account_page_heading()).to_be_visible(timeout=300)










