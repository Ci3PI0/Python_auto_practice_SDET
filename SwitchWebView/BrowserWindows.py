import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chromium import service

driver = webdriver.Chrome()
print(driver.service.path)
driver.implicitly_wait(60)
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')

#           Main Commands to work with window switching
#  driver.switch_to.window(IdOfWindow)  need to pass Window ID
#  driver.current_window_handles    Return ID of current window as a String
#  driver.window_handles   Return list of Window IDs, they may be not sorted

# driver.find_element(By.XPATH, '//input[contains(@class, "wikipedia-search-input")]').send_keys('Selenium')
driver.find_element(By.XPATH, '//input[@id="Wikipedia1_wikipedia-search-input"]').send_keys('Selenium')
driver.find_element(By.XPATH, '//input[contains(@class, "wikipedia-search-button")]').click()
links = driver.find_elements(By.XPATH, '//div[@class="wikipedia-search-results"]//a')

for link in links:
    link.click()

allTabs = driver.window_handles
print(allTabs)

# for tab in allTabs:
#     driver.switch_to.window(tab)
#     print(tab, driver.title)
#     driver.close()
#     time.sleep(5)


          # Close specific browser page
for windowID in allTabs:
    driver.switch_to.window(windowID)
    if driver.title == 'Selenium in biology - Wikipedia':
        driver.close()
        time.sleep(3)


driver.quit()
