# login_page.py
# =====================
# This class represents the "Login Page" of the application.
# It is designed using the Page Object Model (POM) pattern,
# which helps to keep locators and actions separate from the test logic.
from logging import exception

from playwright.sync_api import Page,expect

class LoginPage:

        def __init__(self,page:Page):
            self.page = page

            self.txt_email_address=page.locator('#input-email')
            self.txt_password=page.locator('#input-password')
            self.btn_login = page.get_by_role("button", name="Login")
            self.txt_error_message = page.locator('.alert.alert-danger.alert-dismissible')
        # ===== Action Methods =====
        # These methods represent user interactions on the Login Page.

        def set_email(self,email):
            try:
                self.txt_email_address.fill(email)
            except exception as e:
                print(f"Exception while entering email: {e}")
                raise

        def set_password(self,password):
            try:
                self.txt_password.fill(password)
            except exception as e:
                print(f"Exception while entering password: {e}")
                raise

        def click_login(self):
            try:
                self.btn_login.click()
            except exception as e:
                print(f"Exception while clicking login: {e}")
                raise

        def login(self,email:str,password:str):
            self.set_email(email)
            self.set_password(password)
            self.click_login()

        def get_login_error(self):
            """
            Return the error message element if login fails.
            Example use:
                error_text = login_page.get_login_error().inner_text()
            """
            try:
                return self.txt_error_message
            except Exception as e:
                print(f" Exception while fetching login error message: {e}")
                return None