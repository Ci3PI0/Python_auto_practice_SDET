from selenium import webdriver
from selenium.webdriver.common.by import By

# Xpath axes
# __________
driver = webdriver.Chrome()
driver.get('https://money.rediff.com/gainers')
driver.maximize_window()
#
# Self  (Элемент) точка входа elem/self::elemtag
self_text = driver.find_element(By.XPATH, '//a[contains(text(), "Phoenix Township")]/self::a').text
print(self_text)

# Parent  Родитель элемента   elem/parent::tag

parent_text = driver.find_element(By.XPATH, '//a[contains(text(), "Phoenix Township")]/parent::td/parent::tr').text
print(parent_text)

# Child Дети элемента   elem/child::tag
child_text = driver.find_element(By.XPATH, '//a[contains(text(), "Phoenix Township")]/parent::td/parent::tr/child::td[3]').text
print(child_text)

# Ancestor Предок элемента выше родителя

ancestor_text = driver.find_element(By.XPATH, '//a[contains(text(), "Phoenix Township")]/ancestor::tr').text
print(ancestor_text)

# Descendant Потомки это и дети и то что ниже детей

descendants = driver.find_elements(By.XPATH, '//a[contains(text(), "Phoenix Township")]/ancestor::tbody/descendant::tr')
print(len(descendants))

# Following Следующий в списке(на одном уровне)

followings = driver.find_elements(By.XPATH, '//a[contains(text(), "Phoenix Township")]/ancestor::tr/following::*')
print('Followings:', len(followings))
# Following-sibling следующие в списке

followingsiblings = driver.find_elements(By.XPATH, '//a[contains(text(), "Phoenix Township")]/ancestor::tr/following-sibling::*')
print('Following-siblings:', len(followingsiblings))
# Preceding Предыдущий (на одном уровне)
preceding = driver.find_elements(By.XPATH, '//a[contains(text(), "Phoenix Township")]/ancestor::tr/preceding::*')
print("Preceding:", len(preceding))

# Preceding-sibling Предшествиники элемента
preceding_siblings = driver.find_elements(By.XPATH, '//a[contains(text(), "Phoenix Township")]/ancestor::tr/preceding-sibling::*')
print('Preceding siblings:', len(preceding_siblings))

driver.close()

