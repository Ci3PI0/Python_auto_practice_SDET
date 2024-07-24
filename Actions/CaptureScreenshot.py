import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.nopcommerce.com/')

# driver.save_screenshot(f'{os.getcwd()}//main.png')
driver.get_screenshot_as_file('main3.png')  # By Default saves on the same location
# driver.get_screenshot_as_png() driver.get_screenshot_as_base64()  Saves in binary format

time.sleep(10)
driver.quit()
