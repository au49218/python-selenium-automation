from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SEARCH_DROPDOWN = (By.CSS_SELECTOR, 'select.nav-search-dropdown')

    def open_main_page(self):
        self.open_page('https://www.amazon.com/')

    def input_amazon_search(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)

    def click_search_amazon(self):
        self.click(*self.SEARCH_ICON)
        # self.wait.until()

    def search_for_product(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.find_element(*self.SEARCH_FIELD).send_keys(Keys.Enter)

    def select_department(self, alias: str):
        select = Select(self.find_element(*self.SEARCH_DROPDOWN))
        select.select_by_value(f'search-alias={alias}')
