import openpyxl
from openpyxl.chart import BarChart, Reference, PieChart, LineChart

wb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day19\\data sales.xlsx")
ws = wb.active

# Bar Chat
chart = BarChart()

chart.title = "Monthly Sales"
chart.x_axis.title = "Month"
chart.y_axis.title = "Sales"

data = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_row=6
)

categories = Reference(
    ws,
    min_col=1,
    min_row=2,
    max_row=6
)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "D2")

# ***********************************************************************

# Pie Chart
chart = PieChart()

chart.title = "Sales Distribution"

data = Reference(ws, min_col=2, min_row=1, max_row=6)
categories = Reference(ws, min_col=1, min_row=2, max_row=6)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "D18")

# ***********************************************************************

# Line Chart

chart = LineChart()

chart.title = "Sales Trend"

data = Reference(ws, min_col=2, min_row=1, max_row=6)
categories = Reference(ws, min_col=1, min_row=2, max_row=6)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "M2")

wb.save("E:\\Code\\Python-Automation-60Days\\day19\\data sales 01.xlsx")