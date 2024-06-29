import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
driver.maximize_window()

EmailInput = driver.find_element(By.XPATH, '//input[@id="Email"]')
EmailInput.clear()
EmailInput.send_keys("abs@gmail.com")
# Text возвращяет внутренний текст элемента
print("Result of text is", EmailInput.text)

# Get_attribute возвращяет значение в заданном атрибудет(name, value, data и тд.)
print("Result of get_attribute is", EmailInput.get_attribute("data-val-regex-pattern"))
time.sleep(5)

driver.quit()
