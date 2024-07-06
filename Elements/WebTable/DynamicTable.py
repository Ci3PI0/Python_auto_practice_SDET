import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# Login
driver.find_element(By.XPATH, '//input[@name="username"]').send_keys('Admin')
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('admin123')
driver.find_element(By.XPATH, '//button[@type = "submit"]').click()

driver.find_element(By.XPATH, '//span[text()="Admin"]').click()

numOfRows = len(driver.find_elements(By.XPATH, '//div[@class="oxd-table-body"]//div[@role="row"]'))
numOfColumns = len(driver.find_elements(By.XPATH, '//div[@role="columnheader"]'))

print('Number of Rows:', numOfRows)
print('Number of Columns:', numOfColumns)
Admin = 0
ESS = 0

# for elem in range(1, numOfRows):
#     print(elem)

for row in range(1, numOfRows+1):
    print(row, 'out of', numOfRows)
    # print(driver.find_element(By.XPATH, f'//div[@class="oxd-table-body"]/div[{row}]/div/div[3]').text)
    if driver.find_element(By.XPATH, f'//div[@class="oxd-table-body"]/div[{row}]/div/div[3]').text == 'ESS':
        ESS += 1
        print(driver.find_element(By.XPATH, f'//div[@class="oxd-table-body"]/div[{row}]/div/div[2]').text)
    # elif driver.find_element(By.XPATH, f'//div[@class="oxd-table-body"]/div[{row}]/div/div[3]').text == 'Admin':
    #     Admin += 1

# print('Admin user count:', Admin)
print('ESS user count:', ESS)

time.sleep(30)
driver.quit()
