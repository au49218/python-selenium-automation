from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    # open the URL
    context.driver.get('https://www.amazon.com/')

@when('Input Watches into Amazon search field')
def input_amazon_search(context):
    # find the web element for search field
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    # send the keys for value
    search_field.send_keys('Watches')
