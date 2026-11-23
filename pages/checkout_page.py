# checkout_page.py
# =====================
# This class represents the "Checkout Page" in the application.
# It follows the Page Object Model (POM) design pattern to organize
# locators and methods (actions) clearly.
from asyncio import wait

from playwright.sync_api import Page, expect

class CheckoutPage:

    def __init__(self,page:Page):
        self.page = page

        # ===== Locators =====
        # These identify the web elements we want to interact with on the page.
        self.existing_user = page.locator("#input-shipping-existing")
        self.new_address = page.locator("#input-shipping-new")
        self.shipping_method = page.locator("#button-shipping-methods")
        self.shipping_rate = page.locator("#button - shipping - method")
        self.payment_method = page.locator("#button-payment-methods")
        self.cash_on_delivery = page.locator("#button-payment-method")
        self.confirm_order = page.locator("#button-confirm")
        self.first_name = page.locator("#input-firstname")
        self.last_name = page.locator("#input-shipping-lastname")
        self.company = page.locator('#input-shipping-company')
        self.address1 = page.locator('#input-shipping-address-1')
        self.city = page.locator('#input-shipping-city')
        self.post_code = page.locator('#input-shipping-postcode')
        self.country = page.locator('#input-shipping-country')
        self.state = page.locator('#input-shipping-zone')
        self.continue_btn_new = page.locator('#button-shipping-address')
        self.order_success_full = page.locator("h1:has-text('Your order has been placed!')")


    # ===== Page Validation Methods =====
    def get_checkout_page_title(self):
        try:
            return self.page.title()
        except Exception as e:
            print(f"exception while getting checkout page title: {e}")
            return None

    # ===== Checkout Option =====
    def choose_checkout_option(self, checkout_option):
            try:
                self.new_address.click()
            except Exception as e:
                print(f"exception while choosing new address: {e}")
                raise

    def set_first_name(self,first_name):
        self.first_name.fill(first_name)

    def set_last_name(self,last_name):
        self.last_name.fill(last_name)

    def set_company(self,company):
        self.company.fill(company)

    def set_address(self,address):
        self.address1.fill(address)

    def set_city(self,city):
        self.city.fill(city)

    def set_post_code(self,post_code):
        self.post_code.fill(post_code)

    def set_country(self,country):
        self.country.select_option(label=country)

    def set_state(self,state):
        self.state.select_option(label=state)

    def set_shipping_method(self):
        self.shipping_method.click()

    def set_shipping_rate(self):
        self.shipping_rate.click()

    def payment_methods(self):
        self.payment_method.click()

    def cash_on_delivery(self):
        self.cash_on_delivery.click()

    def continue_btn(self):
        self.continue_btn_new.click()

    def confirm_order(self):
        self.confirm_order.click()

    def order_success_full(self):
        self.order_success_full.is_visible()