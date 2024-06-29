import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Команды навигации в браузере
# back()  Команда назад(открыть предыдущее окно)
# forward() Команда вперёд (открыть окно с которого мы вернулись)
# refresh() Обновить страницу


driver = webdriver.Chrome()

driver.get("https://mail.ru/")
time.sleep(5)
driver.get("https://www.google.com/")

driver.back() #Откроет страницу меил ру
time.sleep(10)
driver.refresh() # Обновит страницу меил ру
driver.forward() # Вернётся на страницу Гугл с котрой до этого вернулся на страницу мейл ру

driver.quit()