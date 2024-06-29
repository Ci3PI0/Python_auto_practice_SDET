import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://ui.vision/demo/webtest/frames/')

# -----------------------------------------How to switch to the frame
#           1. switch_to.frame(Name of the frame)
#           2. switch_to.frame(Id of the frame)
#           3. switch_to.frame(WebElement)
#                   Example iFrame = driver.find_element(By.XPATH, '//frame[@src="frame_3.html"]')
#                           driver.switch_to.frame(iFrame)
#           4. switch_to.frame(index of frame)


# -----------------------------------------How to return to main frame(page) and parent frame
#           driver.switch_to.default_content() Return to main Frame(Page)
#           driver.switch_to.parent_frame() Return to parent Frame

# ----------------------------------------- Frame
driver.switch_to.frame(1)
time.sleep(2)
driver.find_element(By.XPATH, '//input[@name="mytext2"]').send_keys('Hello Nigga')
driver.switch_to.parent_frame() # Возврат в родительское окно
driver.switch_to.frame(2)
driver.switch_to.frame(0)
time.sleep(5)
driver.find_element(By.XPATH, '//span[contains(text(), "Hi, I am the UI.Vision IDE")]').click()
driver.switch_to.default_content()
driver.switch_to.frame(4)
driver.find_element(By.LINK_TEXT, 'https://a9t9.com').click()
time.sleep(10)

# ------------------------------------------Inner IFrame

# iFrame = driver.find_element(By.XPATH, '//frame[@src="frame_3.html"]')
# driver.switch_to.frame(iFrame)
# time.sleep(3)
# TextInput = driver.find_element(By.XPATH, '//input[@name="mytext3"]')
# TextInput.send_keys('Hello')
# time.sleep(3)

driver.quit()
