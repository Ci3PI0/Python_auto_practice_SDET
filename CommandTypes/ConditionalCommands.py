from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Conditional commands
# iS_displayed()
# is_enabled()
# is_selected()


driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
driver.maximize_window()

# is_displayed() and is_enabled()
if driver.find_element(By.XPATH, '//button[@type="submit"]').is_displayed():
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    print(driver.find_element(By.XPATH, '//button[@type="submit"]').is_enabled())
print(driver.find_element(By.XPATH, '//button[@type="submit"]').is_displayed())

# is_selected() for radio buttons and checkboxes
driver.get('https://the-internet.herokuapp.com/checkboxes')
driver.find_element(By.XPATH, '//input[@type="checkbox"][1]').click() # Select Checkbox
driver.find_element(By.XPATH, '//input[@type="checkbox"][2]').click() # Diselect Checkbox
print('Checkbox 1 is selected?', driver.find_element(By.XPATH, '//input[@type="checkbox"][1]').is_selected()) # True
print('Checkbox 2 is selected?', driver.find_element(By.XPATH, '//input[@type="checkbox"][2]').is_selected()) # False
driver.find_element(By.XPATH, '//input[@type="checkbox"][1]').click() # Diselect Checkbox
driver.find_element(By.XPATH, '//input[@type="checkbox"][2]').click() # Select Checkbox
print('Checkbox 1 is selected?', driver.find_element(By.XPATH, '//input[@type="checkbox"][1]').is_selected()) # False
print('Checkbox 2 is selected?', driver.find_element(By.XPATH, '//input[@type="checkbox"][2]').is_selected()) # False


driver.quit()
