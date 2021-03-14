from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(Page):

    SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
    ORDERS_LINK = (By.CSS_SELECTOR, '#nav-orders > span.nav-line-2')

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    def click_amazon_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def verify_sign_in_page_opens(self):
        # wait for x seconds until url contains value
        self.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
                                  f'URL {self.driver.current_url} does not include https://www.amazon.com/ap/signin')

        # verify actual match the expected
        assert 'https://www.amazon.com/ap/signin' in self.driver.current_url, \
            f'URL {self.driver.current_url} does not include https://www.amazon.com/ap/signin'
