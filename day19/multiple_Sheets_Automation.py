import openpyxl

wb = openpyxl.Workbook()

ws1 = wb.active

# create sheet
ws1.title = "Sales"
ws2 = wb.create_sheet("Summary")
ws3 = wb.create_sheet("Charts")

# Sheet Access
sales = wb["Sales"]
summary = wb["Summary"]
charts = wb["Charts"]

# Data Transfer
sales["A1"] = "Total Sales"
summary["A1"] = "=SUM(Sales!B2:B10)"




wb.save("E:\\Code\\Python-Automation-60Days\\day19\\sales_report.xlsx")