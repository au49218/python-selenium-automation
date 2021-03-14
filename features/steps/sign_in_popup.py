from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-inner")
ORDERS_LINK = (By.XPATH, '//*[@id="nav-orders"]/span[2]')


@when('Click Sign In from popup')
def click_sign_in_popup_btn(context):
    # wait for x seconds until clickable
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP_BTN))
    # click the button
    e.click()


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    # Click on Amazon orders link
    context.driver.find_element(*ORDERS_LINK).click()

    # Click on Amazon orders link using Page Object
    context.app.sign_in.click_amazon_orders_link()


@then('Verify Sign In page opens')
def verify_sign_in_page_opens(context):
    # wait for x seconds until url contains value
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
    # f'URL {context.driver.current_url} does not include https://www.amazon.com/ap/signin')

    # verify actual match the expected
    # assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, \
    # f'URL {context.driver.current_url} does not include https://www.amazon.com/ap/signin'

    # Verify Sign Page Opens using Page Object
    context.app.sign_in.verify_sign_in_page_opens()
