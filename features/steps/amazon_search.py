from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@given('Open Amazon page')
def open_amazon(context):

    # open the URL
    # context.driver.get('https://www.amazon.com/')

    # open the URL using Page Object
    context.app.main_page.open_main_page()


@when('Input {search_query} into Amazon search field')
def input_amazon_search(context, search_query):

    # find the web element for search field
    # search_field = context.driver.find_element(*SEARCH_FIELD)
    # send the keys for value
    # search_field.send_keys(search_query)

    # find the web element for search field using Page Object
    context.app.main_page.input_amazon_search(search_query)


@when('Click on Amazon search icon')
def click_search_amazon(context):

    # find the element for search icon
    # context.driver.find_element(*SEARCH_ICON).click()

    # find the element for search icon using Page Object
    context.app.main_page.click_search_amazon()


@when('Search for {search_word}')
def input_search(context, search_word):

    # find the element for search field
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word, Keys.ENTER)

    # find the element for search field using Page Object
    context.app.main_page.input_amazon_search(search_word)
    context.app.main_page.click_search_amazon()


@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.main_page.select_department(alias)


@then('Product results for {result_word} are shown on Amazon')
def verify_search_result(context, result_word):

    # find the element for result text
    # actual_text = context.driver.find_element(*RESULT).text
    # expected_text = f'{result_word}'
    # verify the expected match actual
    # assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

    # find and verify using Page Object
    context.app.search_results_page.verify_search_result(result_word)


@then('Page URL has {query} in it')
def verify_url_contains_query(context, query):

    # verify the query in current url
    # assert query in context.driver.current_url, f'{query} not in {context.driver.current_url}'

    # verify the query in current url using Page Object
    context.app.search_results_page.verify_url_contains_query(query)


@given('Open Amazon Dress {productid} page')
def open_dress_page(context, productid):

    # open product ID page
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}')


@when('Click on the first product')
def click_first_product(context):
    context.app.search_results_page.click_first_product()


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_results_page.verify_department(department)
