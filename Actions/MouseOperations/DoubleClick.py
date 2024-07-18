from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#       Mouse Command Types  (Action Chains)
#  1.Mouse Hover            move_to_element(element)
#  2.Right click            context_click(element)
#  3.Double click           double_click(element)
#  4.Drag and drop          drag_and_drop(source_element, target_element)

# Double Click

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://cps-check.com/double-click-test')
button = driver.find_element(By.XPATH, '//button[@id="clicker"]')

act = ActionChains(driver)

act.double_click(button).double_click(button).double_click(button).double_click(button).perform()

sleep(10)

driver.quit()
