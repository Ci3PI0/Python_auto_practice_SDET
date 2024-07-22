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


def fireFox():
    preferences = {"download.default_directory": location}
    opt = webdriver.FirefoxOptions()
    opt.set_preference("browser.download.folderList",2) # 0-Desctop,1-default location, 2-desired location
    opt.set_preference("browser.download.dir", location)
    return webdriver.Firefox(options=opt)


def edge():
    preferences = {"download.default_directory": location, "plugins.always_open_MP3_externally": True}
    options = webdriver.EdgeOptions()
    # options.set_experimental_option("prefs", preferences)
    options.add_experimental_option("prefs", preferences)
    return webdriver.Edge(options= options)


driver = chrome()
driver.implicitly_wait(10)

#Edge Specific options
if driver.name == "MicrosoftEdge":
    driver.get('edge://settings/downloads')
    toggle = driver.execute_script('''
                return document.querySelector('input[aria-label="Открывать файлы Office в браузере"]');
        ''')
    toggle.click()

driver.maximize_window()
# driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.get('https://file-examples.com/index.php/sample-audio-files/sample-mp3-download/')
downloadBtn = driver.find_element(By.XPATH, '//table[@id="table-files"]/tbody/tr[3]//a')

# driver.execute_script('arguments[0].scrollIntoView()', downloadBtn)
time.sleep(3)
downloadBtn.click()
time.sleep(15)
driver.quit()