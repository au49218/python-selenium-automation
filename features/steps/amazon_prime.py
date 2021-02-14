from behave import when, then, given
from selenium.webdriver.common.by import By

BENEFIT_BOXES = (By.CSS_SELECTOR, '.benefit-box')


@given('Open Amazon Prime page')
def open_prime(context):
    # open the URL
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {expected_boxes} benefit boxes are displayed')
def verify_boxes(context, expected_boxes):
    # find the elements from the list
    actual_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    # print the elements from the list
    print(actual_boxes)
    # print the type expected boxes
    print(type(expected_boxes))
    # verify the actual boxes equal to 8
    assert len(actual_boxes) == int(expected_boxes), f'Expected {expected_boxes} boxes, but we see {len(actual_boxes)}'
