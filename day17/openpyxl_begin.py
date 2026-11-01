import openpyxl

# Creating a workbook
workbook = openpyxl.Workbook()
sheet1 = workbook.active

sheet1['A1'] = "Hello" 
sheet1['B1'] = "Idiot"
workbook.save("E:\\Code\\Python-Automation-60Days\\day17\\test01.xlsx")

# loading a workbook and reading excel file
wkb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day17\\test01.xlsx")
sheet = wkb['Sheet']
cell_value = sheet['A1'].value
print(cell_value)
print(sheet['B1'].value)

# Adding new worksheet
new_sheet = wkb.create_sheet("Python")
new_sheet['A1'].value = "Bruh..!!"
wkb.save("E:\\Code\\Python-Automation-60Days\\day17\\test01.xlsx")

# Changing sheetname and color
wb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day17\\test01.xlsx")
ws = wb.active
# print(ws)
ws.title = "Sales"
ws.sheet_properties.tabColor = "FF00FF00"           # red: "FFFF0000"     
print(ws.title)
wb.save("E:\\Code\\Python-Automation-60Days\\day17\\test01.xlsx")

# adding data
names = ['Pagol', 'Sagol', 'Ghadha', 'MathaMota', 'Nikomma']
ages = [122, 500000, -1, 0, 0.9]

for i in range(0, len(names)):
    ws['A' + str(i+1)].value = names[i]

for i in range(0, len(ages)):                       # another way   
    ws.cell(row= i+1, column=2).value = ages[i]

wb.save("E:\\Code\\Python-Automation-60Days\\day17\\test01.xlsx")

# Readind data 
for col in ws['A']:
    print(col.value)

print(" ")
for col in ws['A':'B']:                 # for reading all the data in A and B column
  for cell in col:  
    print(cell.value)

print("\n***Another Way***\n")
for row in ws.iter_rows(min_row=1, max_row=5, min_col=1, max_col=2, values_only=True):            # another way
   print(row)