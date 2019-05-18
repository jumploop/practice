import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
sheet_name = wb.get_sheet_names()
print(sheet_name)
sheet = wb.get_sheet_by_name('Sheet1')
print(sheet['A1'].value)
c = sheet['B1']
print(c.value)
wb.close()
