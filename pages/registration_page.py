from playwright.sync_api import Page

class RegistrationPage:
    """
    Page Object Model class for the Registration Page.
    This class contains web element locators and methods (actions)
    to interact with the registration form.
    """

    def __init__(self, page: Page):
        self.page = page

        # ---Locators---

        self.txt_firstname = self.page.locator('#input-firstname')
        self.txt_lastname = self.page.locator('#input-lastname')
        self.txt_email = self.page.locator('#input-email')
        self.txt_password = self.page.locator('#input-password')
        self.confirm_password = self.page.locator('#input-password')
        # Confirmation message (displayed after successful registration)
        self.msg_confirmation = self.page.get_by_role("heading", name="Your Account Has Been Created!")

        self.continue_btn = self.page.get_by_role("button", name="Continue")
        self.privacy_policy =page.locator("[name='agree']")
    # ===== Action Methods =====

    def set_first_name(self, fname):
        self.txt_firstname.fill(fname)

    def set_last_name(self, lname):
        self.txt_lastname.fill(lname)

    def set_email(self, email):
        self.txt_email.fill(email)

    def set_password(self, password):
        self.confirm_password.fill(password)

    def set_confirm_password(self, password):
        self.confirm_password.click()

    def btn_continue(self):
        self.continue_btn.click()

    def click_privacy_policy(self):
        self.privacy_policy.click()

    def get_msg_confirmation(self):
        return self.msg_confirmation

    # ===== Combined Workflow =====

    def complete_registration(self, user_data):
        self.set_first_name(user_data['firstname'])
        self.set_last_name(user_data['lastname'])
        self.set_email(user_data['email'])
        self.set_password(user_data['password'])
        self.confirm_password()
        self.privacy_policy()
        self.continue_btn()

        return self.msg_confirmation()