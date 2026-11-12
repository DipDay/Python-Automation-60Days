import openpyxl

wb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day19\\data.xlsx")
ws = wb.active

ws["B6"] = "=SUM(B2:B5)"
ws["B7"] = "=AVERAGE(B2:B5)"
ws["B8"] = "=MAX(B2:B5)"
ws["B9"] = "=MIN(B2:B5)"
ws["B10"] = "=COUNT(B2:B5)"
ws["B11"] = "=COUNTA(A2:A5)"

ws["C2"] = '=IF(B2>=25000,"High","Low")'

ws["B12"] = '=SUMIF(A2:A5,"Sales",B2:B5)'

wb.save("E:\\Code\\Python-Automation-60Days\\day19\\salary.xlsx")