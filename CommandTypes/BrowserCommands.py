import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Browser commands   there is only 2 of them. Quit() and close() difference will be shown below
time.sleep(2)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(2)
driver.maximize_window()
time.sleep(2)

# close() закрывает браузер но не убивает процесс браузера
# close() закоываеь только одну вкладку
# quit() закрывает браузер и убивает процесс
# quit() закрывает все вкладки

driver.find_element(By.XPATH, '//a[contains(text(),"Orange")]').click()
driver.find_element(By.XPATH, '//a[contains(text(),"Orange")]').click()
time.sleep(2)

time.sleep(5)
driver.close() # Закрывает только корневую вкладку

time.sleep(5)
driver.quit() # Закрывает весь процесс driver (браузер полностью закроется)

