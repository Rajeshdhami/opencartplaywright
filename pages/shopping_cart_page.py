from playwright.sync_api import Page, expect
from pages.checkout_page import CheckoutPage

class ShoppingcartPage:

    def __init__(self,page:Page):
        self.page = page

        self.total_price = self.locator('#checkout-total tr:nth-child(2) td:nth-child(2)')

        self.btn_checkout = page.locator("a.btn.btn-primary")

    def get_total_price(self):
        try:
            return self.total_price
        except Exception as e:
            print(f"unable to fetch total price: {e}")
            return None

    def click_checkout(self):
        try:
            self.btn_checkout.click()
            return CheckoutPage(self.page)
        except Exception as e:
            print(f"unable to click checkout: {e}")
            raise e

    def is_page_loaded(self):
        try:
            return self.btn_checkout
        except Exception as e:
            print(f"unable to load checkout: {e}")
            return None