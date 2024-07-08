import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#       Mouse Command Types  (Action Chains)
#  1.Mouse Hover            move_to_element(element)
#  2.Right click            context_click(element)
#  3.Double click           double_click(element)
#  4.Drag and drop          drag_and_drop(source_element, target_element)

# Right Click

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

button = driver.find_element(By.XPATH, '//div[@role="main"]/p/span')
copyButton = driver.find_element(By.XPATH, '//li[@class="context-menu-item context-menu-icon context-menu-icon-copy"]')
act = ActionChains(driver)

act.context_click(button).move_to_element(copyButton).click().perform()
time.sleep(10)

alert_view = driver.switch_to.alert
alert_view.accept()
time.sleep(10)

driver.quit()
