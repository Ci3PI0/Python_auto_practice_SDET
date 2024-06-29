from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Explicit Wait (Явное ожидание)
# Работает на основе условии (Видимый?, кликабельный? и тд)

driver = webdriver.Chrome()
my_wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[TimeoutException, NoSuchElementException,
                                                                          Exception])  #Явное объявление ожидания

# Timeout Лимит времени
# Poll_frequency частота проверки элемента
# Ignored_exceptions Игнорируемые ошибки/исключения

driver.get("https://www.google.com/")
driver.maximize_window()

text_area = driver.find_element(By.XPATH, '//textarea[@name="q"]')
text_area.send_keys('Selenium')
text_area.submit()

# Явное указания условии для продолжения (ждать пока элемент появиться)
my_wait.until(EC.presence_of_element_located((By.XPATH, '//h3[text()="Seleniumы"]'))).click()

#--------------Плюсы
# Более эффективное чем не явное ожидание так как можем выбивать где ожидать основываясь на условиях, а так же есть
# возможность добавлять игнорирование ошибок (Исключения)

#--------------Минусы
# Необходимость добавлять точки ожидания в ручную
# Сложнее в сравнений с не явным ожиданием


driver.quit()
