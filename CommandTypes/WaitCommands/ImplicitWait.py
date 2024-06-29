from selenium import webdriver
from selenium.webdriver.common.by import By

# Implicit Wait (Не явное ожидание)
# driver.implicitly_wait(10)

# -----------------------------------------Плюсы
# 1 Досточно объявить в одном месте
# 2 НЕ снижаем производительность (Если элемент загрузился в заданном лимите времени)


# ----------------------------------------Минусы
# 1 Если объект не загрузился в заданном лимите времени выдаст ошибку (не существует элемент или что то другое)


driver = webdriver.Chrome()
# Не явное ожидаение, даём лимит времени сколько ждать в случае ниже это 10 секунд
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

text_area = driver.find_element(By.XPATH, '//textarea[@name="q"]')
text_area.send_keys('Selenium')
text_area.submit()
driver.find_element(By.XPATH, '//h3[text()="Selenium"]').click()

driver.quit()
