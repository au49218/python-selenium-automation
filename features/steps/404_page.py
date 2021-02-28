from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

DOG_IMG = (By.CSS_SELECTOR, "a[href='/dogsofamazon'] img")


@when('Store original windows')
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)
    sleep(2)


@when('Click to open blog')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()
    sleep(2)


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print(context.driver.window_handles)
    context.driver.switch_to_window(context.driver.window_handles[1])


@then('User can close new window and switch back to original')
def close_old_switch_to_new_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
    sleep(2)
