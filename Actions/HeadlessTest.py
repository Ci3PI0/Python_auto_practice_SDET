from selenium import webdriver


def headless_chrome():
    option = webdriver.ChromeOptions()
    # option.headless = True
    option.add_argument('--headless=new')
    driver = webdriver.Chrome(options=option)
    # web_driver.maximize_window()
    return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    serv = Service("C:\\WebDrivers\\Firefox\\geckodriver-v0.34.0-win64\\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(service=serv, options=options)
    print(driver.capabilities)
    return driver


def headless_edge():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless")
    driver = webdriver.Edge(options=options)
    return driver


driver = headless_firefox()
driver.get('https://demo.nopcommerce.com/')
print(driver.title)
print(driver.current_url)

driver.quit()