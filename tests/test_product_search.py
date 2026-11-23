import time
import pytest
from playwright.sync_api import expect

from pages import search_results_pages
from pages.home_page import Homepage
from pages.search_results_pages import SearchResultsPage
from config import Config

def test_product_search(page):

    product__name=Config.product_name
    homepage = Homepage(page)
    search_results_page =SearchResultsPage(page)

    homepage.enter_product_name(product__name)
    homepage.click_search()

    expect(search_results_page.get_search_result_page_header()).to_be_visible(timeout=3000)
    expect(search_results_page.is_product_exists(product__name)).to_be_visible(timeout=3000)


