import openpyxl

fl = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day17\\test02.xlsx", data_only=True)

# delete specific sheet
print(fl.sheetnames)
del fl['C']
fl.save("E:\\Code\\Python-Automation-60Days\\day17\\test02.xlsx")
print(fl.sheetnames)
