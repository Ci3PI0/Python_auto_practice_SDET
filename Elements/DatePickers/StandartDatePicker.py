import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://jqueryui.com/datepicker/')
# iFrame = driver.find_element(By.XPATH, '//iframe[@class="demo-frame"]')
driver.switch_to.frame(0)
DatePicker = driver.find_element(By.XPATH, '//input[@id="datepicker"]')
# DatePicker.send_keys('06/01/2024')
DatePicker.click()
days = driver.find_elements(By.XPATH, '//td/a')


yr = '2020'
mon = 'March'
day = '15'

# pref date  25 March  1993

while True:
    month = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-month"]').text
    year = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-year"]').text
    PrevButton = driver.find_element(By.XPATH, '//a[@title="Prev"]')
    NextButton = driver.find_element(By.XPATH, '//a[@title="Next"]')

    if month == mon and year == yr:
        break
    # elif int(year) >= int(yr) and month != mon:
    #     PrevButton.click()
    else:
        PrevButton.click()
        # NextButton.click()


links = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]/tbody//a')

for link in links:
    if link.text == '25':
        link.click()
        break

time.sleep(10)

driver.quit()
