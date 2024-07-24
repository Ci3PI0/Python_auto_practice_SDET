import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

driver.find_element(By.XPATH, '//span[@id="select2-billing_country-container"]').click()
countryList = driver.find_elements(By.XPATH, '//ul[@id="select2-billing_country-results"]/li')

driver.execute_script('arguments[0].scrollIntoView()', driver.find_element(By.XPATH, '//span[@id="select2-billing_country-container"]'))

for country in countryList:
    if country.text == 'French Polynesia':
        country.click()
        break # To stop process


print(len(countryList))
time.sleep(10)
driver.quit()
