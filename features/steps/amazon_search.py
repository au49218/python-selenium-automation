from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon page')
def open_amazon(context):
    # open the URL
    context.driver.get('https://www.amazon.com/')


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):
    # find the web element for search field
    search_field = context.driver.find_element(*SEARCH_FIELD)
    # send the keys for value
    search_field.send_keys(search_query)


@when('Click on Amazon search icon')
def click_search_amazon(context):
    # find the element for search icon
    context.driver.find_element(*SEARCH_ICON).click()


@when('Search for {search_word}')
def input_search(context, search_word):
    # find the element for search field
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)


@then('Product results for {result_word} are shown on Amazon')
def verify_search_result(context, result_word):
    # find the element for result text
    actual_text = context.driver.find_element(*RESULT).text
    expected_text = f'{result_word}'
    # verify the expected match actual
    assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query):
    # verify the query in current url
    assert query in context.driver.current_url, f'{query} not in {context.driver.current_url}'
