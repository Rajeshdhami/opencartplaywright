from playwright.sync_api import Page ,expect
from pages.product_pages import ProductPage

class SearchResultsPage:

    def __init__(self,page:Page):
        self.page = page
        self.search_page_header = page.get_by_placeholder("Search")
        self.search_products=page.locator("h4>a")

    def get_search_result_page_header(self):
        try:
            return self.search_page_header
        except Exception as e:
            print(f"Error while getting search result page {e}")
            return None

    def is_product_exists(self,product_name):
        try:
            count = self.search_products.count()
            for i in range(count):
                product=self.search_products.nth(i)
                title =product.text_content()
                if title and title.strip() == product_name:
                    return product
        except Exception as e:
            print(f"Error while getting product {e}")
        return None

    def select_product(self,product_name):
        try:
            count=self.search_products.count()
            for i in range(count):
                product=self.search_products.nth(i)
                title =product.text_content()
                if title and title.strip() == product_name:
                    product.click()
                    return ProductPage(self.page)
                print(f"product {product_name} not found")
        except Exception as e:
            print(f"Error while getting product {e}")
        return None

    def get_product_count(self):
        try:
            return self.search_products
        except Exception as e:
            print(f"Error while getting product count:{e}")
            return None
