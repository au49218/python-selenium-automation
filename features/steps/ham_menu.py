from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

HAM_MENU = (By.ID, 'nav-hamburger-menu')


@then('Verify hamburger menu icon is visible')
def verify_ham_menu_present(context):
    print('Find Element')
    # find the element
    element = context.driver.find_element(*HAM_MENU)
    # print the element
    print(element)
    # print the type element
    print(type(element))

    print('Find Elements')
    elements = context.driver.find_elements(*HAM_MENU)
    # print the elements from the list
    print(elements)
    # print the type elements from the list
    print(type(elements))
    # verify elements equal length of 1
    assert len(elements) == 1
