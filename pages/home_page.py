from playwright.sync_api import Page

class Homepage:

    def __init__(self, page:Page):
        self.page = page
        self.lnk_my_account = page.locator("//span[contains(text(),'My Account')]")
        self.lnk_register = page.locator('li a:has-text("Register")')
        self.ln_login =page.locator("li a:has-text('Login')")
        self.txt_search_box =page.locator("input[class$='form-control form-control-lg']")
        self.btn_search =page.locator("button[class$='btn btn-light btn-lg']")

    # ===== Action Methods =====
    # Each method represents a user interaction on the page

    def get_home_page(self):
        title = self.page.title()
        return title

    def click_my_account(self):
        try:
            self.lnk_my_account.click()
        except Exception as e:
            print(f"Exception while clicking my account:{e}")
            raise

    def click_register(self):
        try:
            self.lnk_register.click()
        except Exception as e:
            print(f"Exception while clicking register:{e}")
            raise

    def click_login(self):
        try:
            self.ln_login.click()
        except Exception as e:
            print(f"Exception while clicking login:{e}")
            raise

    def enter_product_name(self, product_name):
        try:
            self.txt_search_box.fill(product_name)
        except Exception as e:
            print(f"Exception while entering product name:{e}")
            raise

    def click_search(self):
        try:
            self.btn_search.click()
        except Exception as e:
            print(f"Exception while clicking search:{e}")
            raise