from playwright.sync_api import Page, expect
from pages.logout_page import LogoutPage
from pages.home_page import Homepage

class Myaccountpage:
    def __init__(self,page:Page):
        self.page = page
        self.lnk_logout = page.get_by_role("link", name="Logout")
        self.msg_heading = page.locator("h1:has-text('My Account')")

    def get_my_account_page_heading(self):
        """
        Returns the locator for the 'My Account' page heading.
        Can be used in test assertions to verify page visibility.

        Example:
            expect(my_account_page.get_my_account_page_heading()).to_be_visible()
        """
        try:
            return self.msg_heading
        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
            return None

    def click_logout(self):
        try:
            self.lnk_logout.click()
        except Exception as e:
            print(f"Unable to click logout button: {e}")
            raise e

    def get_page_title(self):
        try:
            return self.page.title()
        except Exception as e:
            print(f"Unable to get page title: {e}")
            return ""
