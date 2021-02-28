from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


TC_LINK_PAGE = 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
APP_LINK = (By.CSS_SELECTOR, "div > p:nth-child(6) > a")
APP_LINK_OPENED = (By.CSS_SELECTOR, "div.unified_widget")

@given('Open Amazon T&C page')
def open_terms_page(context):
    # open the URL
    context.driver.get(TC_LINK_PAGE)


@when('Click on Amazon applications link')
def click_link(context):
    context.driver.find_element(*APP_LINK).click()
    sleep(2)


@then('Amazon app page is opened')
def verify_app_page_opens(context):
    # wait for x seconds until url contains value
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/feature.html?docId=1000625601'),
    f'URL {context.driver.current_url} does not include https://www.amazon.com/gp/feature.html?docId=1000625601')
