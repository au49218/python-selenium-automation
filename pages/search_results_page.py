from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):

    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    SELECTED_DPT_CATEGORY = (By.CSS_SELECTOR, "#nav-subnav[data-category='{DPT_SBSTR}']")

    def _get_locator(self, department: str):
        return [self.SELECTED_DPT_CATEGORY[0], self.SELECTED_DPT_CATEGORY[1].replace('{DPT_SBSTR}', department)]

    def click_first_product(self):
        self.click(*self.PRODUCT_RESULT)

    def verify_search_result(self, result_word):
        self.verify_text(result_word, *self.SEARCH_RESULT)

    def verify_department(self, department):
        locator = self._get_locator(department)
        self.wait_for_element_appear(*locator)
