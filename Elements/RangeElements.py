import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.jqueryscript.net/demo/Powerful-Range-Slider-Plugin-jQRangeSlider/demo/')


minSlider = driver.find_element(By.XPATH, '//div[@id="slider"]//div[contains(@class,"ui-rangeSlider-leftHandle")]')
maxSlider = driver.find_element(By.XPATH, '//div[@id="slider"]//div[contains(@class,"ui-rangeSlider-rightHandle")]')
minSliderLabel = driver.find_element(By.XPATH, '//div[@id="slider"]//div[contains(@class,'
                                               '"ui-rangeSlider-leftLabel")]/div[@class = '
                                               '"ui-rangeSlider-label-value"]')

#  Drag and Drop by Offset
print(f'Location before moving minSlider:{minSlider.location} and maxSlider {maxSlider.location}')
#   Location before moving minSlider:{'x': 311, 'y': 254} and maxSlider {'x': 748, 'y': 254}

act = ActionChains(driver)
act.drag_and_drop_by_offset(minSlider, -292, 0).perform()
act.drag_and_drop_by_offset(maxSlider, 730, 0).perform()

print(f'Location after moving minSlider:{minSlider.location} and maxSlider {maxSlider.location}')
time.sleep(10)

driver.quit()
