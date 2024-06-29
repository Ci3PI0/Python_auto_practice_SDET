import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://letcode.in/dropdowns")



# drcountry = Select(driver.find_element(By.XPATH, '//select[@id="country"]'))

# Select option from dropdown
# drcountry.select_by_index(5)
# print(drcountry.options[5].text)
# time.sleep(4)
# drcountry.select_by_value("Chile")
# print(drcountry.options)
# time.sleep(4)
# drcountry.select_by_visible_text("India")
# print(drcountry.options)
# time.sleep(4)


#Capture all options and print them
# allOptions = drcountry.options
# print(len(allOptions))
#
# # print values of options
#
# for option in allOptions:
#     print(option.text)
time.sleep(2)
allFruits = driver.find_elements(By.XPATH, '//select[@id = "fruits"]/option')
for fruit in allFruits:
    if fruit.text == "Pine Apple":
        fruit.click()

time.sleep(2)
driver.find_element(By.XPATH, '//select[@id = "superheros"]/option[@value = "ds" and contains(text(), "Strange")]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//select[@id = "lang"]/option[@value= "py"]').click()
time.sleep(2)

allCountryOptions = driver.find_elements(By.XPATH, '//select[@id = "country"]/option')

for option in allCountryOptions:
    if option.text == "Brazil":
        option.click()

time.sleep(20)

driver.quit()