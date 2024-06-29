from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get('https://google.com')
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, '.gLFyf').send_keys('Auto Search')
# driver.find_element(By.CSS_SELECTOR, '.gNO89b').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'қаз').click()
driver.find_element(By.LINK_TEXT, 'русский').click()

driver.close()