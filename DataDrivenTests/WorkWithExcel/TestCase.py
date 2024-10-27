from selenium import webdriver
from selenium.webdriver.common.by import By
from DataDrivenTests.WorkWithExcel import EXCELUtilities as Excel

# Install Openpyxl to work with Excel

file = 'C:\\Users\\Admin\\Desktop\\booktest.xlsx'
sheetName = 'Лист1'

rows = Excel.getRow(file, sheetName)
columns = Excel.getColumn(file, sheetName)

print(rows)
print(columns)

for r in range(2, rows+1):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.way2automation.com/way2auto_jquery/registration.php#load_box')
    driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(Excel.getData(file, sheetName, r, 1))
    driver.find_element(By.XPATH, '//fieldset[@class="fieldset"]//p[2]/input').send_keys(Excel.getData(file, sheetName, r, 2))
    MartialStatus = driver.find_elements(By.XPATH, '//label[contains(text(),"Marital Status:")]/following-sibling::div/label')
    for status in MartialStatus:
        if status.text == Excel.getData(file, sheetName, r, 3):
            status.click()
    Hobbies = driver.find_elements(By.XPATH, '//label[contains(text(),"Hobby:")]/following-sibling::div/label')
    for hobby in Hobbies:
        if hobby.text == Excel.getData(file, sheetName, r, 4):
            hobby.click()
    phoneInput = driver.find_element(By.XPATH, '//input[@name="phone"]')
    phoneInput.send_keys(Excel.getData(file, sheetName, r, 5))
    UserName = driver.find_element(By.XPATH, '//input[@name="username"]')
    UserName.send_keys(Excel.getData(file, sheetName, r, 6))
    email = driver.find_element(By.XPATH, '//input[@name="email"]')
    email.send_keys(Excel.getData(file, sheetName, r, 7))
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    password.send_keys(Excel.getData(file, sheetName, r, 8))
    passwordConfirm = driver.find_element(By.XPATH, '//input[@name="c_password"]')
    passwordConfirm.send_keys(Excel.getData(file, sheetName, r, 8))
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    driver.close()
