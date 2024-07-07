import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')


def dateSelectById(day, month, year, elem_id):
    select_date = driver.find_element(By.XPATH, f'//input[@id="{elem_id}"]')
    select_date.click()

    # Select Month
    month_selector = driver.find_element(By.XPATH, '//select[@data-handler="selectMonth"]')
    datepicker_month = Select(month_selector)
    datepicker_month.select_by_value(month)

    # Select Year
    year_selector = driver.find_element(By.XPATH, '//select[@data-handler="selectYear"]')
    datepicker_year = Select(year_selector)
    datepicker_year.select_by_value(year)

    departure_days = driver.find_elements(By.XPATH, '//table[@class="ui-datepicker-calendar"]//tbody//a')

    for date in departure_days:
        if date.get_attribute('data-date') == day:
            date.click()
            break


driver.find_element(By.XPATH, '//ul[@id="checkout-products"]//input[@id="product_3186"]').click()
driver.find_element(By.XPATH, '//input[@id="travname"]').send_keys('Meyirman Turlybekov')
driver.find_element(By.XPATH, '//input[@id="travlastname"]').send_keys('Maratovich')
# Select Date of Birth
dateSelectById('25', '2', '1993', 'dob')

driver.find_element(By.XPATH, '//input[@id="sex_1"]').click()
driver.find_element(By.XPATH, '//input[@id="fromcity"]').send_keys('Almaty')
driver.find_element(By.XPATH, '//input[@id="tocity"]').send_keys('Melburn')

# Select Departure Day
dateSelectById('15', '11', '2024', 'departon')

driver.find_element(By.XPATH, '//span[@id = "select2-reasondummy-container"]').click()
dummyTicketPurpose = driver.find_elements(By.XPATH, '//ul[@id="select2-reasondummy-results"]/li')
for purpose in dummyTicketPurpose:
    if purpose.text == 'Visa extension':
        purpose.click()
        break

driver.find_element(By.XPATH, '//input[@id="deliverymethod_3"]').click()
driver.find_element(By.XPATH, '//input[@id="billing_phone"]').send_keys('77077770000')
driver.find_element(By.XPATH, '//input[@id="billing_email"]').send_keys('test@googlemail.com')
driver.find_element(By.XPATH, '//input[@id="billing_address_1"]').send_keys('Some Street and City')
driver.find_element(By.XPATH, '//input[@id="billing_address_2"]').send_keys('Flat number 35')
driver.find_element(By.XPATH, '//input[@id="billing_city"]').send_keys('Almaty')
driver.find_element(By.XPATH, '//input[@id="billing_state"]').send_keys('Almaty Obl')
driver.find_element(By.XPATH, '//input[@id="billing_postcode"]').send_keys('051111')

selectedAnount = driver.find_element(By.XPATH, '//li[@class="product-item selected"]//span[@class="price"]')
totAmount = driver.find_element(By.XPATH, '//div[@id= "order_review"]//tfoot//tr[@class="order-total"]//span[@class="woocommerce-Price-amount amount"]')

if selectedAnount.text == totAmount.text:
    print('True')

time.sleep(15)

driver.quit()
