import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
# driver.get('https://practice.expandtesting.com/upload')
# file_path = 'C:\\Projects\\Python_auto_practice_SDET\\Actions\\file-example_PDF_500_kB.pdf'
# fileSelector = driver.find_element(By.XPATH, '//input[@id="fileInput"]')
# fileSelector.send_keys(file_path)
#
# uploadBtn = driver.find_element(By.XPATH, '//button[@id="fileSubmit"]')
# uploadBtn.click()
#
# time.sleep(10)
# driver.quit()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('Admin')
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin123')
driver.find_element(By.XPATH, '//button[contains(@class,"orangehrm-login-button")]').click()
