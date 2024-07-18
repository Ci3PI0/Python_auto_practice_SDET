import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(60)
driver.maximize_window()
# driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.get('https://animedia.onl/')

#   1. Scroll down page by pixel
# driver.execute_script('window.scrollBy(0,3000)', '')
#
# pixelValue = driver.execute_script('return window.pageYOffset;')
# print(pixelValue)

#   2. Scroll till the element is visible
# kzFlag = driver.find_element(By.XPATH, '//img[@alt="Flag of Kazakhstan"]')
# driver.execute_script('arguments[0].scrollIntoView()', kzFlag)
# pixelValue = driver.execute_script('return window.pageYOffset;')
# print(pixelValue)


#   3. Scroll till the end of the page
driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
pixelValue = driver.execute_script('return window.pageYOffset;')
print(pixelValue)

time.sleep(5)
driver.execute_script('window.scrollBy(0,-document.body.scrollHeight)')
pixelValue = driver.execute_script('return window.pageYOffset;')
print(pixelValue)
time.sleep(5)

driver.quit()
