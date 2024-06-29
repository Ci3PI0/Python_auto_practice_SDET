from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()

# driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys('Name')
# find element wich contain selected text by using contains() function
driver.find_element(By.XPATH, '//input[contains(@id,"first")]').send_keys('Name')
# driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys('Surname')
# find element which start same as selected text  by using starts-with() function
driver.find_element(By.XPATH, '//input[starts-with(@id,"last")]').send_keys('Surname')
driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys('mail@email.com')
# Find elements wich contain inner text by using text() function
driver.find_element(By.XPATH, '//label[text()="Male"]').click()
# driver.find_element(By.XPATH, '//label[contains(text(),"Male")]').click()
driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys('7079322400')
driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
# driver.switch_to.frame()
# driver.find_element(By.XPATH, '//select[@class="react-datepicker__month-select"]').click()
# driver.find_element(By.XPATH, '//select[@class="react-datepicker__month-select"]/option[contains(text(), "March")]').click()
driver.close()
