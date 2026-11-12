import openpyxl
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Series, Reference
# style : https://openpyxl.readthedocs.io/en/stable/styles.html

wb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day18\\practice01.xlsx")
ws = wb.active

# c = ws['A9']
# c.value = 'hello, world'
# print(c.value)

for row in ws.values:
   for value in row:
     print(value)

ft = Font(bold=True)
for row in ws["A1:C1"]:
    for cell in row:
        cell.font = ft

# Create Chart
chart = BarChart()
chart.type = "col"
chart.title = "Salary"
# chart.y_axis.title = 'Money'
# chart.x_axis.title = 'Name'
chart.legend = None

# Select Data
data = Reference(ws, min_col=3, min_row=1, max_row=6)               # Salary data (Column C)
categories = Reference(ws, min_col=1, min_row=2, max_row=6)         # Employee names (Column A)

# Add Data and Categories
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
# Axis labels visibility
chart.x_axis.delete = False
chart.y_axis.delete = False

chart.x_axis.tickLblPos = "low"
chart.y_axis.tickLblPos = "low"

chart.y_axis.numFmt = '#,##0'

# Add Chart to Worksheet
ws.add_chart(chart, "E1")

wb.save('day18\\practice 02.xlsx')