from csv import excel

from playwright.sync_api import Page,expect
from pages.shopping_cart_page import ShoppingcartPage

class ProductPage():

    def __init__(self,page:Page):

        self.page=page

        self.txt_quantity  = page.locator("#input-quantity")
        self.add_to_cart   = page.locator("#button-cart")
        self.cnf_msg       = page.locator(".alert.alert-success")
        self.btn_items     = page.locator("#cart")
        self.lnk_view_cart =  page.get_by_role("link",name="View Cart")

    def set_quantity(self,qty):
        try:
            self.txt_quantity("")
            self.txt_quantity(qty)
        except Exception as e:
            print(f"Error while setting quantity {qty}")
            raise

    def add_to_cart(self):
        try:
            self.add_to_cart.click()
        except Exception as e:
            print(f"Error while adding to_cart {e}")
            raise
    def get_confirmation(self):
        try:
           return self.cnf_msg
        except Exception as e:
            print(f"Error while getting confirmation {e}")
            raise

    def click_add_to_cart(self):
        try:
            self.btn_items.click()
        except Exception as e:
            print(f"Error while clicking add to_cart {e}")
            raise

    def click_view_cart(self):
        try:
            self.lnk_view_cart.click()
            return ShoppingcartPage(self.page)
        except Exception as e:
            print(f"Error while clicking view cart {e}")
            raise

    def add_product_to_cart(self,quantity):
        try:
            self.set_quantity(quantity)
            self.click_view_cart()
            expect(self.get_confirmation()).to_be_visible()
        except Exception as e:
            print(f"Error while adding product {e}")
            raise









