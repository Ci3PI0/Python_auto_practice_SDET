import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
# driver.get('https://demo.nopcommerce.com/')
driver.get('https://mail.ru/')

allCookies = driver.get_cookies()
# Print cookies count
print(len(allCookies))  # 20

# Print all cookies
# for cookie in allCookies:
#     print(cookie.get('name'), ':', cookie.get('value'))
#     # print(f'Cookie name :{cookie['name']} and value:{cookie['value']}')
#     print(cookie)


# Add new cookie to Browser

driver.add_cookie({'name': 'Meyirman', 'value': '10', 'count': '15'})

allCookies = driver.get_cookies()
# print(len(allCookies))  # 21
# for cookie in allCookies:
#     print(cookie.get('name'), ':', cookie.get('value'))
    # print(f'Cookie name :{cookie['name']} and value:{cookie['value']}')
    # print(cookie)



# Delete specific cookies from browser
driver.delete_cookie('Meyirman')  # Deleting by the name
allCookies = driver.get_cookies()
print(len(allCookies))  # 20

#  Delete all cookies
driver.delete_all_cookies()
allCookies = driver.get_cookies()
print(f'After deleting all cookies result is {len(allCookies)}')  # 0

time.sleep(5)
driver.quit()
