import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from DataDrivenTests.WorkWithExcel import EXCELUtilities as Excel
import mysql.connector


file = 'C:\\Users\\Admin\\Desktop\\Automation Practice\\Python_auto_practice_SDET\\DataDrivenTests\\WorkWithSQL\\doc1.xlsx'
sheetName = 'Лист1'
rows = Excel.getRow(file, sheetName)
columns = Excel.getColumn(file, sheetName)


try:
    connection = mysql.connector.connect(host='localhost', port='3306', user='root', password='root', database='students')
    cursor = connection.cursor()  # Create Cursor
    r = 2
    cursor.execute('select * from persons')
    for row in cursor :
        print(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8])
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('https://www.way2automation.com/way2auto_jquery/registration.php#load_box')
        driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(row[1])
        driver.find_element(By.XPATH, '//fieldset[@class="fieldset"]//p[2]/input').send_keys(row[2])
        MartialStatus = driver.find_elements(By.XPATH, '//label[contains(text(),"Marital Status:")]/following-sibling::div/label')
        for status in MartialStatus:
            if status.text == row[3]:
                status.click()
        Hobbies = driver.find_elements(By.XPATH, '//label[contains(text(),"Hobby:")]/following-sibling::div/label')
        for hobby in Hobbies:
            if hobby.text == row[4]:
                hobby.click()
        phoneInput = driver.find_element(By.XPATH, '//input[@name="phone"]')
        phoneInput.send_keys(row[5])
        UserName = driver.find_element(By.XPATH, '//input[@name="username"]')
        UserName.send_keys(row[6])
        email = driver.find_element(By.XPATH, '//input[@name="email"]')
        email.send_keys(row[7])
        password = driver.find_element(By.XPATH, '//input[@name="password"]')
        password.send_keys(row[8])
        passwordConfirm = driver.find_element(By.XPATH, '//input[@name="c_password"]')
        passwordConfirm.send_keys(row[8])
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        driver.close()
        Excel.writeData(file, sheetName, r, 1, row[1])
        Excel.writeData(file, sheetName, r, 2, row[2])
        Excel.writeData(file, sheetName, r, 3, row[3])
        Excel.writeData(file, sheetName, r, 4, row[4])
        Excel.writeData(file, sheetName, r, 5, row[5])
        Excel.writeData(file, sheetName, r, 6, row[6])
        Excel.writeData(file, sheetName, r, 7, row[7])
        Excel.writeData(file, sheetName, r, 8, row[8])
        r += 1
    connection.close()
    print('Finished')
except mysql.connector.Error as e:
    print(f"Connection failed: {e}")


# for r in range(2, rows+1):
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.get('https://www.way2automation.com/way2auto_jquery/registration.php#load_box')
#     driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(Excel.getData(file, sheetName, r, 1))
#     driver.find_element(By.XPATH, '//fieldset[@class="fieldset"]//p[2]/input').send_keys(Excel.getData(file, sheetName, r, 2))
#     MartialStatus = driver.find_elements(By.XPATH, '//label[contains(text(),"Marital Status:")]/following-sibling::div/label')
#     for status in MartialStatus:
#         if status.text == Excel.getData(file, sheetName, r, 3):
#             status.click()
#     Hobbies = driver.find_elements(By.XPATH, '//label[contains(text(),"Hobby:")]/following-sibling::div/label')
#     for hobby in Hobbies:
#         if hobby.text == Excel.getData(file, sheetName, r, 4):
#             hobby.click()
#     phoneInput = driver.find_element(By.XPATH, '//input[@name="phone"]')
#     phoneInput.send_keys(Excel.getData(file, sheetName, r, 5))
#     UserName = driver.find_element(By.XPATH, '//input[@name="username"]')
#     UserName.send_keys(Excel.getData(file, sheetName, r, 6))
#     email = driver.find_element(By.XPATH, '//input[@name="email"]')
#     email.send_keys(Excel.getData(file, sheetName, r, 7))
#     password = driver.find_element(By.XPATH, '//input[@name="password"]')
#     password.send_keys(Excel.getData(file, sheetName, r, 8))
#     passwordConfirm = driver.find_element(By.XPATH, '//input[@name="c_password"]')
#     passwordConfirm.send_keys(Excel.getData(file, sheetName, r, 8))
#     driver.find_element(By.XPATH, '//input[@type="submit"]').click()
#     driver.close()