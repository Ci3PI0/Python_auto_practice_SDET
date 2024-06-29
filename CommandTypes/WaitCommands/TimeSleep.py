import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# time.sleep(TIME in seconds)
# -----------------------------Плюсы-------------------
# Простота в использовании
# -----------------------------Минусы--------------------
# Встроенный в Питон механизм, не как не связан с Selenium
# Фиксированное время, что если станица прогрузилась раньше(потеря времени и снижение скорости) но что если
# страница загрузиться позже? (Тест упадёт так как элемент еще не прогрузился)


driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()

text_area = driver.find_element(By.XPATH, '//textarea[@name="q"]')
text_area.send_keys('Selenium')
text_area.submit()
time.sleep(10)
#Ожидание 10 секунд
driver.find_element(By.XPATH, '//h3[text()="Selenium"]').click()

driver.quit()