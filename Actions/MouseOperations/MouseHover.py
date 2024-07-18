import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.orangehrm.com/')

#       Mouse Command Types  (Action Chains)
#  1.Mouse Hover            move_to_element(element)
#  2.Right click            context_click(element)
#  3.Double click           double_click(element)
#  4.Drag and drop          drag_and_drop(source_element, target_element)

# MOUSER HOVER
orangeHRM = driver.find_element(By.LINK_TEXT, 'Why OrangeHRM')
customers = driver.find_element(By.XPATH, '//a[text()="Why OrangeHRM"]/following::div//li[2]')
ourPartners = driver.find_element(By.LINK_TEXT, 'Our Partners')
act = ActionChains(driver)

act.move_to_element(orangeHRM).move_to_element(customers).move_to_element(ourPartners).click().perform()
time.sleep(2)
driver.quit()