from playwright.sync_api import Page,expect
from pages.home_page import Homepage

class LogoutPage:
    def __init__(self,page:Page):
        self.return_homepage = page.locator("i.fa-home")

    # ===== Action Methods =====

    def return_homepage(self):
        try:
            self.return_homepage.click()
        except Exception as e:
            print(f"Exception while clicking homepage:{e}")
            raise

    def get_return_homepage(self):
        try:
            return self.return_homepage
        except Exception as e:
            print(f"Exception while clicking homepage:{e}")
            return None

