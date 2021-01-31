from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# open the browser
driver = webdriver.Chrome()
# wait for 4 seconds
driver.implicitly_wait(4)
# go to URL
driver.get('https://www.amazon.com/gp/help/customer/display.html/')

# find the web element for search field
search_field = driver.find_element(By.ID, 'helpsearch')
# send the keys for value
search_field.send_keys('Cancel order')
# send the keys for enter
search_field.send_keys(Keys.ENTER)

# verify the expected text matches actual text
actual_text = driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
expected_text = 'Cancel Items or Orders'
assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

# quit the browser
driver.quit()
