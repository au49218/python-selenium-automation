from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.ID, 'nav-cart-count-container')
CART_RESULT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")


@given('Open Amazon main page')
def open_amazon(context):
    # open the URL
    context.driver.get('https://www.amazon.com/')


@when('Click on Amazon cart icon')
def click_search_amazon(context):
    context.driver.find_element(*CART_ICON).click()


@then('Cart results for {result_word} are shown on cart page')
def verify_search_result(context, result_word):
    actual_text = context.driver.find_element(*CART_RESULT).text
    expected_text = f'{result_word}'
    assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
