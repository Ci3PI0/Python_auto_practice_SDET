import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

location = os.getcwd()


def chrome():
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("prefs", preferences)
    # driver = webdriver.Chrome(options = opt)
    return webdriver.Chrome(options=opt)
    # return driver


def fire_fox():
    preferences = {"download.default_directory": location}
    opt = webdriver.FirefoxOptions()
    opt.set_preference("browser.download.folderList", 2)  # 0-Desktop,1-default location, 2-desired location
    opt.set_preference("browser.download.dir", location)
    opt.set_preference("pdfjs.disabled", True)
    return webdriver.Firefox(options=opt)


def edge():
    preferences = {"download.default_directory": location}
    options = webdriver.EdgeOptions()
    # options.set_experimental_option("prefs", preferences)
    options.add_experimental_option("prefs", preferences)

    return webdriver.Edge(options=options)


driver = edge()
driver.implicitly_wait(10)

driver.maximize_window()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')
downloadBtn = driver.find_element(By.XPATH, '//table[@id="table-files"]/tbody/tr[2]//a')
driver.execute_script('arguments[0].scrollIntoView()', downloadBtn)
downloadBtn.click()
time.sleep(15)
driver.quit()
