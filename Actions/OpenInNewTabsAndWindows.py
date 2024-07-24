import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demo.nopcommerce.com/')
# driver.find_element(By.LINK_TEXT, 'Register').click()
# time.sleep(5)
# NewTab = Keys.CONTROL + Keys.RETURN
# driver.find_element(By.LINK_TEXT, 'Register').send_keys(NewTab)
# driver.find_element(By.LINK_TEXT, 'Register').send_keys(NewTab)
# driver.find_element(By.LINK_TEXT, 'Register').send_keys(NewTab)
# time.sleep(5)
# parent_handle = driver.current_window_handle
# allTabs = driver.window_handles
# driver.switch_to.window(allTabs[3])
# time.sleep(5)
parent_handle = driver.current_window_handle

#  Selenium 4 Features
driver.switch_to.new_window('tab')  # Open new tab and switches to it
# driver.switch_to.new_window('window')  # Open new window and switches to it
driver.get('https://www.google.com/')
allTabs = driver.window_handles

driver.switch_to.window(parent_handle)

time.sleep(5)
driver.quit()
