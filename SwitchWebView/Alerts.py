import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
text = "Hello World"
driver.find_element(By.XPATH, '//button[text()= "Click for JS Prompt"]').click()

# Main commands to work wi Alerts
# alert = driver.switch_to.alert  Switches to alert window and initiolize the result ro variable
# alert.text  Return Title of Alert
# alert.accept  Press OK Button on alert window
# alert.dismiss Press Cancel button on alert window


alert_view = driver.switch_to.alert
print(alert_view.text)

time.sleep(2)
alert_view.send_keys(text)
time.sleep(2)
# alert_view.accept()  # Press OK Button on the alert window
alert_view.dismiss()  # Press Cancel Button on the alert page
time.sleep(2)

print(driver.find_element(By.XPATH, '//p[@id="result"]').text)
time.sleep(2)
driver.quit()
