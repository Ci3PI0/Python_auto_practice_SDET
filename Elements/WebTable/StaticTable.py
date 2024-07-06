from selenium import webdriver
from selenium.webdriver.common.by import By

#   1) Count number of Rows and Columns
#   2) Read specific row and column data
#   3) Read all the rows and columns
#   4) Read data based on conditions(List books name whose author is Mukesh)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')

#   1) Count number of Rows and Columns

#   Number of Rows
tableRows = driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr')
numOfRows = len(tableRows)
print('Number of Rows is', numOfRows)
# for tr in tableRows:
#     print(f'Index of {tr.text} is', tableRows.index(tr))

#   Number of Columns

numOfColumns = len(driver.find_elements(By.XPATH, '//table[@name="BookTable"]//tr/th'))
print('Number of Columns is', numOfColumns)

#   2) Get specific Row and Column data

# SpecData = driver.find_element(By.XPATH, '//table[@name="BookTable"]//tr[4]/td[3]')  # JavaScript
# print(SpecData.text)

#   3) Read All Rows and Columns

# for row in range(2, numOfRows + 1):
#     for col in range(1, numOfColumns + 1):
#         data = driver.find_element(By.XPATH, f'//table[@name="BookTable"]//tr[{row}]/td[{col}]').text
#         print(data,end='      ')
#     print()

listOfBooks = []

#   4) Read data based on conditions(List books name whose author is Mukesh)
for row in range(2, numOfRows+1):
    author = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody//tr[{row}]/td[2]').text
    if author == 'Amit' or author == 'Amod':
        bookName = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody//tr[{row}]/td[1]').text
        bookPrice = driver.find_element(By.XPATH, f'//table[@name="BookTable"]/tbody//tr[{row}]/td[4]').text
        listOfBooks.append({bookName, bookPrice})
        print(author, bookName)

print(listOfBooks)

driver.quit()
