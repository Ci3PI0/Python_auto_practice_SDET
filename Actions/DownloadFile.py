import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

location = os.getcwd()
def chrome():
    preferences = {"download.default_directory": location}
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("prefs", preferences)
    # driver = webdriver.Chrome(options = opt)
    return webdriver.Chrome(options = opt)
    # return driver

#
# def fireFox():
#     from selenium.webdriver.firefox.options import Options
#     from selenium.webdriver.firefox.service import Service
#     return webdriver.Firefox()
#
#
# def edge():
#     from selenium.webdriver.edge.options import Options
#     from selenium.webdriver.edge.service import Service
#     return webdriver.Edge()


driver = chrome()
driver.maximize_window()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')

downloadBtn = driver.find_element(By.XPATH, '//table[@id="table-files"]/tbody/tr[2]//a')
downloadBtn.click()
time.sleep(15)
driver.quit()