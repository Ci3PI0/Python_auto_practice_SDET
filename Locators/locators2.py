from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://automationexercise.com/')
driver.maximize_window()

slides = driver.find_elements(By.CLASS_NAME, 'item')
print(len(slides)) ## общее кол-во слайдов на странице
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links)) ## общее кол-во ссылок на странице
