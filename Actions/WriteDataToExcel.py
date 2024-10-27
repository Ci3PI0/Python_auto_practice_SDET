import openpyxl

#  Structure of Xcell File
#  File --> Workbook---> Sheets--> Rows-->Cells
file = 'C:\\Users\\Admin\\Desktop\\TestBook.xlsx'
workbook = openpyxl.load_workbook(file)
sheet = workbook['Data']
# sheet = workbook.active      #Get active sheet from excel


for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(r, c).value = "WElcome"

workbook.save(file)
