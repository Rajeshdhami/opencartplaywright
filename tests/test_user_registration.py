from playwright.sync_api import Page,expect
from pages.registration_page import RegistrationPage
from pages.home_page import Homepage
from utils.random_data_util import RandomDataUtil

def test_user_registration(page):
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




