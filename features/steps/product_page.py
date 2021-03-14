from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')
SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
SIZE_OPTION_0 = (By.ID, 'size_name_0')

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@when('Click on Add to cart button')
def click_add_to_cart(context):
    # find the element for add to cart button
    # context.driver.find_element(*ADD_TO_CART_BTN).click()

    # find the element for add to cart button using Page Object
    context.app.product_page.click_add_to_cart()


@when('Select shoes size')
def select_size(context):
    # find the element for size selection button
    # context.driver.find_element(*SIZE_SELECTION_BTN).click()
    # find the element for size option
    # context.driver.find_element(*SIZE_OPTION_0).click()
    # verify the size tooltip equal 1
    # if len(context.driver.find_elements(*SIZE_TOOLTIP)) == 1:
    #    context.driver.find_element(*SIZE_SELECTION_BTN).click()
    #    context.driver.find_element(*SIZE_OPTION_0).click()
    #    sleep(2)
    #    context.driver.find_element(*ADD_TO_CART_BTN).click()

    # find the element for size selection and size option using Page Object
    context.app.product_page.select_size()


@then('Verify cart has {expected_count} item')
def verify_cart_count(context, expected_count):
    # cart_count = context.driver.find_element(*CART).text
    # verify expected count match cart count
    # assert expected_count == cart_count, f'Expected {expected_count} items'

    # verify expected count match cart count using Page Object
    context.app.product_page.verify_cart_count(expected_count)


@then('Verify user can click through colors')
def verify_can_select_colors(context):
    # find the elements for colors
    # expected_colors = ['Black', 'Blue', 'Burgundy', 'White Lace', 'Off White', 'Pink', 'Navy']
    # colors = context.driver.find_elements(*COLOR_OPTIONS)

    # Web Element 1, Web Element 2, Web Element 3
    # for i in range(len(colors)):
        # colors[i].click()
        # selected_color = context.driver.find_element(*SELECTED_COLOR).text
        # assert expected_colors[i] == selected_color, f'Expected {expected_colors[i]} but got {selected_color}'

    # Verify selection of colors using Page Object
    context.app.product_page.verify_can_select_dress_colors()
