from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):

    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

    def click_first_product(self):
        self.click(*self.PRODUCT_RESULT)

    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.SEARCH_RESULT)
