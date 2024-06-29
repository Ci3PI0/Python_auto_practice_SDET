import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Выбрать 1 конкретный чекбокс
# checkbox = driver.find_element(By.XPATH, '//input[@id="tuesday"]')
# checkbox.click()

# Как выбрать множество чекбоксов
day_checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox" and contains(@id, "day")]')
# print(len(day_checkboxes))
# #  -----------Выбор всех чекбоксов
# # # Вариант 1
# for i in range(len(day_checkboxes)):
#     print(i)
#     day_checkboxes[i].click()

# Вариант 2
# for elem in day_checkboxes:
#     print(elem)
#     elem.click()

# -------------------Выбор нескольких чекбоксов из множества(списка)
# for checkbox in day_checkboxes:
#     dayname = checkbox.get_attribute('id')
#
#     if dayname == 'monday' or dayname == 'sunday':
#         checkbox.click()

# ------------------ Выбор последних 2 чекбоксов из списка
# for i in range(len(day_checkboxes)-2,len(day_checkboxes)):
#     print(i)
#     day_checkboxes[i].click()
#     print(day_checkboxes[i].get_attribute("id"))


def elems(r,list): # Выбирает чекбоксы с конца списка, можно указать сколько штук
    for i in range(len(list) - r, len(list)):
        print(i, list[i].get_attribute("id"))
        list[i].click()


def firstElems(r,list): # выбирает на чек боксы в наачле, можно указать сколько штук.
    limit = len(list) - (len(list)-r)
    for i in range(limit):
        print(i)
        list[i].click()


# elems(4, day_checkboxes)
firstElems(4, day_checkboxes)

time.sleep(5)
# Как убрать выделения с чек боксов
for i in range(len(day_checkboxes)):
    if day_checkboxes[i].is_selected():
        day_checkboxes[i].click()

time.sleep(5)
driver.quit()
