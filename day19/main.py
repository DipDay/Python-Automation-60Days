import openpyxl
from openpyxl.chart import BarChart, PieChart, Reference

wb = openpyxl.Workbook()

# Sales Sheet
ws = wb.active
ws.title = "Sales"

data = [
    ["Month", "Sales"],
    ["January", 12000],
    ["February", 18000],
    ["March", 15000],
    ["April", 25000],
    ["May", 30000],
]

for row in data:
    ws.append(row)

# Summary Sheet
summary = wb.create_sheet("Summary")

summary["A1"] = "Total Sales"
summary["B1"] = "=SUM(Sales!B2:B6)"

summary["A2"] = "Average Sales"
summary["B2"] = "=AVERAGE(Sales!B2:B6)"

summary["A3"] = "Maximum Sales"
summary["B3"] = "=MAX(Sales!B2:B6)"

summary["A4"] = "Minimum Sales"
summary["B4"] = "=MIN(Sales!B2:B6)"

# Charts Sheet
charts = wb.create_sheet("Charts")

data_ref = Reference(
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

# Bar Chart
bar = BarChart()
bar.title = "Monthly Sales"
bar.y_axis.title = "Sales"
bar.x_axis.title = "Month"

bar.add_data(data_ref, titles_from_data=True)
bar.set_categories(categories)

charts.add_chart(bar, "A1")

# Pie Chart
pie = PieChart()
pie.title = "Sales Distribution"

pie.add_data(data_ref, titles_from_data=True)
pie.set_categories(categories)

charts.add_chart(pie, "A18")

# Save
wb.save("E:\\Code\\Python-Automation-60Days\\day19\\monthly_sales_report.xlsx")

print("Report generated successfully!")
