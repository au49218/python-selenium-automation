from selenium import webdriver
from selenium.webdriver.common.by import By

# open the browser
driver = webdriver.Chrome()
# wait for 4 seconds
driver.implicitly_wait(4)
# go to URL
driver.get('https://www.amazon.com/')

# find the web element for search field
search_field = driver.find_element(By.ID, 'twotabsearchtextbox')
# send the keys for value
search_field.send_keys('Watches')
# find the web element for search icon
search_icon = driver.find_element(By.ID, 'nav-search-submit-button')
# click the search icon
search_icon.click()

# verify the expected text matches actual text
actual_text = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
expected_text = '"Watches"'
assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

# quit the browser
driver.quit()
