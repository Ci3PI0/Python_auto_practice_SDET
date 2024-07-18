import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
my_wait = WebDriverWait(driver, 10, 1)
driver.maximize_window()
driver.get('https://text-compare.com/')

textArea = driver.find_element(By.XPATH, '//textarea[@id="inputText1"]')
textArea2 = driver.find_element(By.XPATH, '//textarea[@id="inputText2"]')
compareButton = driver.find_element(By.XPATH, '//button[@id="compareButton"]')
my_wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[@id="inputText1"]'))).send_keys('Hello World')
# textArea.send_keys('Hello World')
act = ActionChains(driver)
# Select Text CTRL + A
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# Copy Text CTRL + C
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# Switch to next element  TAB
act.key_down(Keys.TAB).key_up(Keys.TAB)
# Paste text CTRL + V
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

compareButton.click()
time.sleep(10)
driver.quit()
