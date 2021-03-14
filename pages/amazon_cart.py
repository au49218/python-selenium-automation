from selenium.webdriver.common.by import By
from pages.base_page import Page


class AmazonCartPage(Page):

    CART_ICON = (By.ID, 'nav-cart-count-container')
    CART_RESULT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    def click_search_amazon(self):
        self.click(*self.CART_ICON)

    def verify_search_result(self, result_word):
        actual_text = self.driver.find_element(*self.CART_RESULT).text
        expected_text = f'{result_word}'
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
