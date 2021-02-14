from behave import when, then, given
from selenium.webdriver.common.by import By

BEST_SELLERS_LINKS = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']")


@given('Open Amazon Best Sellers page')
def open_best_sellers(context):
    # open the URL
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify {expected_links} links are displayed')
def verify_links(context, expected_links):
    # find the elements from the list
    actual_links = context.driver.find_elements(*BEST_SELLERS_LINKS)
    # print the elements from the list
    # print(actual_links)
    # print the type expected links
    # print(type(expected_links))
    # verify the actual links equal to 5
    assert len(actual_links) == int(expected_links), f'Expected {expected_links} boxes, but we see {len(actual_links)}'
