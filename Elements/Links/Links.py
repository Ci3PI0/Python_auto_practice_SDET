import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
wait = WebDriverWait(driver,10, poll_frequency=1)

driver.maximize_window()

# Link Types
# 1. Internal links
# 2. External links
# 3. Broken Links

# Click on link
# wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Digital downloads"))).click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "downloads").click()

# Find total number of links
# allLinks = driver.find_elements(By.TAG_NAME, "a")
allLinks = driver.find_elements(By.XPATH, "//a")
print(len(allLinks))
for elem in allLinks:
    print(elem.get_attribute("href"), elem.text)

# time.sleep(10)
driver.quit()
