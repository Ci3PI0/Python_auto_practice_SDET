from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\\WebDrivers\\Chrome 125.0.6422.78\\chromedriver.exe")

# 1. Application(get) commands
# get() --- Method to open app URL
# title --- to Capture title of current web page
# current_url  --- to Capture current pages URL
# page_source --- to Capture Page source code

# 2. Conditional commands
# 3. Browser Commands
# 4. Navigational Commands
# 5. Wait Commands


driver = webdriver.Chrome(service=serv_obj)

# Get Func
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
print(driver.title)  # OrangeHRM
print(driver.current_url)  # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)  # Retunr Source of page

driver.close()
