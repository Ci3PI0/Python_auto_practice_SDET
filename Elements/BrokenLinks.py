from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# we need install requests package from settings

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

broken_count = 0
count = 0

for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print('this is broken link', link.get_attribute("href"))
        broken_count += 1
    else:
        print(url, "is not broken")

print("Total number of broken links", broken_count)


print(broken_count)
print(count)