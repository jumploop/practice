import openpyxl

wb=openpyxl.Workbook()
sheet_names=wb.get_sheet_names()
print(sheet_names)
sheet=wb.get_active_sheet()
print(sheet.title)
