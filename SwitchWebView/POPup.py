import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
login = 'admin'
password = 'admin'

# Когда у нас есть всплывающее окно авторизации мы передаём логин и пароль в ссылке.
# Пример ниже без передачи логина и пароля, откроется всплывающее окно ввода логин и пароль
# driver.get("https://@the-internet.herokuapp.com/basic_auth") # Откроется окно ввода логина и пароля

# Пример ниже когда мы передаём и логин и пароль для авторизации в системе в самой ссылке.
driver.get(f"https://{login}:{password}@the-internet.herokuapp.com/basic_auth")
# driver.get(f"https://{login}:@the-internet.herokuapp.com/basic_auth")
time.sleep(10)

driver.quit()
