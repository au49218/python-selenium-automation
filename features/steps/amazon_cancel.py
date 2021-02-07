from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

HELP_SEARCH_FIELD = (By.ID, 'helpsearch')
HELP_RESULT = (By.XPATH, "//h1[text()='Cancel Items or Orders']")

@given('Open Amazon Help Page')
def open_amazon_help(context):
    # open the URL
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/')


@when('Enter {search_query} into help search field')
def enter_amazon_help_search(context, search_query):
    # find the web element for help search field
    search_field = context.driver.find_element(*HELP_SEARCH_FIELD)
    # send the keys for value
    search_field.send_keys(search_query)
    # send the keys for enter
    search_field.send_keys(Keys.ENTER)


@then('Help results for {result_word} are shown on page')
def verify_search_result(context, result_word):
    actual_text = context.driver.find_element(*HELP_RESULT).text
    expected_text = f'{result_word}'
    assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

