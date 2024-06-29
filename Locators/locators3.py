from  selenium import webdriver
from  selenium.webdriver.common.by import By

# Селекторы CSS и их комбинации

browser = webdriver.Chrome()

browser.get('https://www.facebook.com/')
browser.maximize_window()

# Комбинации CSS селекторов
# TAG ID
# TAG CLASS
# TAG Attribute
# TAG CLASS ATTRIBUTE


# TAG & ID

# browser.find_element(By.CSS_SELECTOR, 'input#email').send_keys('test@test.com') #tag#id
# browser.find_element(By.CSS_SELECTOR, '#email').send_keys('test@test.com') # id is added with # symbol

# TAG and CLASS
# browser.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys('test@test.com') # tag and class added with . between
# browser.find_element(By.CSS_SELECTOR, '.inputtext').send_keys('test@test.com') # class added with . between


# TAG and ATTRIBUTE
# browser.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('abc@gmail.com') # Tag and Attribute tag[attribute='value']
browser.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys('abc@gmail.com') # By only attribute [attribute='value']


# TAG&CLASS&ATTRIBUTE   tag.class[attrubute="value"]

browser.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid=royal_email]').send_keys('test@gmail.com')

