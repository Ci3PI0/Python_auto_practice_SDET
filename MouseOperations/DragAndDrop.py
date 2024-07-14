from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#       Mouse Command Types  (Action Chains)
#  1.Mouse Hover                move_to_element(element)
#  2.Right click                context_click(element)
#  3.Double click               double_click(element)
#  4.Drag and drop              drag_and_drop(source_element, target_element)
#      Drag and drop by offset  drag_and_drop_by_offset(element, Xoffset, Yoffset)

# Drag and Drop

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
act = ActionChains(driver)

seoul = driver.find_element(By.XPATH, '//div[@id="box5"]')
rome = driver.find_element(By.XPATH, '//div[@id="box6"]')
oslo = driver.find_element(By.XPATH, '//div[@id="box1"]')
stockholm = driver.find_element(By.XPATH, '//div[@id="box2"]')
washington = driver.find_element(By.XPATH, '//div[@id="box3"]')
copenhagen = driver.find_element(By.XPATH, '//div[@id="box4"]')
madrid = driver.find_element(By.XPATH, '//div[@id="box7"]')

italy = driver.find_element(By.XPATH, '//div[@id="box106"]')
spain = driver.find_element(By.XPATH, '//div[@id="box107"]')
norway = driver.find_element(By.XPATH, '//div[@id="box101"]')
denmark = driver.find_element(By.XPATH, '//div[@id="box104"]')
south_korea = driver.find_element(By.XPATH, '//div[@id="box105"]')
sweden = driver.find_element(By.XPATH, '//div[@id="box102"]')
united_states = driver.find_element(By.XPATH, '//div[@id="box103"]')

(act.drag_and_drop(seoul, south_korea).drag_and_drop(rome, italy).drag_and_drop(oslo, norway)
 .drag_and_drop(stockholm, sweden).drag_and_drop(washington, united_states).drag_and_drop(copenhagen, denmark)
 .drag_and_drop(madrid, spain).perform())

sleep(10)
driver.quit()