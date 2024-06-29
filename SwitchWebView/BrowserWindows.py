import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

#           Main Commands to work with window switching
#  driver.switch_to.window(IdOfWindow)  need to pass Window ID
#  driver.current_window_handles    Return ID of current window as a String
#  driver.window_handles   Return list of Window IDs, they may be not sorted

# MainTab = driver.current_window_handle
# print(MainTab)

link = driver.find_element(By.LINK_TEXT, 'OrangeHRM, Inc')
link.click()
time.sleep(3)
link.click()
time.sleep(3)
link.click()

windowsIds = driver.window_handles

#           Close specific browser page
for windowID in windowsIds:
    driver.switch_to.window(windowID)
    if driver.title == 'Human Resources Management Software | OrangeHRM':
        driver.close()
        time.sleep(3)


driver.quit()
