import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')

dateOfBirthInput = driver.find_element(By.XPATH, '//input[@id="dob"]')
dateOfBirthInput.click()

# Select Month
month = driver.find_element(By.XPATH, '//select[@data-handler="selectMonth"]')
datepicker_month = Select(month)
datepicker_month.select_by_value('2')

# Select Year
year = driver.find_element(By.XPATH, '//select[@data-handler="selectYear"]')
datepicker_year = Select(year)
datepicker_year.select_by_value('2015')


days = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]//tbody//a')

for day in days:
    if day.get_attribute('data-date') == '25':
        day.click()
        break

time.sleep(15)

driver.quit()
