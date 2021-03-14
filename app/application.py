from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.amazon_cart import AmazonCartPage
from pages.sign_in import SignInPage
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.amazon_cart = AmazonCartPage(self.driver)
        self.sign_in = SignInPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
