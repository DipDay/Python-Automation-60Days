import openpyxl

wb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day18\\practice01.xlsx")
ws = wb.active

# for row in ws.iter_rows(min_row=2, max_col=3, max_row=6):
#     for cell in row:
#         if cell.column == 2:  # Column B skip
#             continue
#         print(cell.value)

for row_idx in range(2, 7):
    col_a = ws.cell(row=row_idx, column=1).value  # Column A
    col_c = ws.cell(row=row_idx, column=3).value  # Column C
    print(col_a, col_c)

print()

for col in ws.iter_cols(min_row=1, max_row=6, min_col=2, max_col=2, values_only=True):
    for cell in col:
        print(cell)

print()

for row in ws.iter_rows(min_row=1, max_row=3, max_col=3, values_only=True):
    for cell in row:
        print(cell)

print()

for row_idx in range(2, 7):
    col_a = ws.cell(row=row_idx, column=1).value  # Column A
    col_c = ws.cell(row=row_idx, column=3).value  # Column C

    # if col_c > 28000:
    #     print(col_a, col_c)
    if col_c is not None and col_c > 28000:
        print(col_a, col_c)
