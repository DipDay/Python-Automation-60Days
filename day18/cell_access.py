import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# Method 1
ws['A1'] = 'Name'
ws['B1'] = 'Age'

# Method 2
ws.cell(row=2, column=1, value='Dip')
ws.cell(row=2, column=2, value=20)

wb.save('day18\\cell access.xlsx')

# ***Accessing many cells***

# cell_range = ws['A1':'C2']
# colC = ws['C']
# col_range = ws['C:D']
# row10 = ws[10]
# row_range = ws[5:10]

for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell)

for row in ws.rows:                             # print all the value
    for cell in row:
        print(cell.value)