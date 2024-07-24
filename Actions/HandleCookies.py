import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
# driver.get('https://demo.nopcommerce.com/')
driver.get('https://mail.ru/')

allCookies = driver.get_cookies()
print(len(allCookies))  # 24
for cookie in allCookies:
    print(cookie.get('name'), ':', cookie.get('value'))
    # print(f'Cookie name :{cookie['name']} and value:{cookie['value']}')
    print(cookie)

time.sleep(5)
driver.quit()
