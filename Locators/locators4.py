from selenium import webdriver
from selenium.webdriver.common.by import By

d = webdriver.Chrome()
d.get('https://mail.ru/')
d.maximize_window()
d.find_element(By.XPATH, '//div[@id="mailbox"]/div/button').click()
d.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[1]/svg').click()

# XPath locators

#Absulute/Full XPath locators
# /html/body/main/div[2]/div[3]/div/div[1]/div/form/div[3]/button

#Relative XPath Locators
# //*[@id="grid"]/div[2]/div[3]/div/div[1]/div/form/div[3]/button