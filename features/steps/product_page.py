from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    # find the element for add to cart button
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Select shoes size')
def select_size(context):
    # find the element for size selection button
    context.driver.find_element(*SIZE_SELECTION_BTN).click()
    # find the element for size option
    context.driver.find_element(*SIZE_OPTION_0).click()
    # verify the size tooltip equal 1
    # if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
    #    context.driver.find_element(*SIZE_SELECTION_BTN).click()
    #    context.driver.find_element(*SIZE_OPTION_0).click()
    #    sleep(2)
    #    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    # verify expected count match cart count
    assert expected_count == cart_count, f'Expected {expected_count} items'
