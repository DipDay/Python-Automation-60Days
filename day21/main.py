import pandas as pd
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, PatternFill, Alignment

file_path = "E:\\Code\\Python-Automation-60Days\\day21\\sales.xlsx"
output_path = "E:\\Code\\Python-Automation-60Days\\day21\\sales_report.xlsx"
df = pd.read_excel(file_path)

# Total Sales
df["Sales"] = df["Quantity"] * df["Unit Price"]
total_sales = df["Sales"].sum()
# print(df["Sales"])
print("Total Sales:", total_sales)

# Top product
top_products = (df.groupby("Product")["Sales"].sum().sort_values(ascending=False))
print(top_products)

# Monthly Sales
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
df["Date"] = df["Date"].dt.date

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)
print(monthly_sales)

# Convert the grouping indexes into columns before exporting.
top = top_products.rename("Sales").reset_index()
monthly = monthly_sales.rename("Sales").reset_index()


# Save Report
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        
        df.drop(columns=["Month"]).to_excel(
        writer,
        sheet_name="All products",
        index=False
    )

        top.to_excel(
        writer,
        sheet_name="Top product",
        index=False
    )
        monthly.to_excel(
        writer,
        sheet_name="Monthly Sales",
        index=False
    )

# Excel Chart
wb = load_workbook(output_path)
ws = wb["Top product"]

chart = BarChart()
chart.title = "Sales Report by Product"
chart.x_axis.title = "Product"
chart.y_axis.title = "Sales"

data = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_row=ws.max_row
)

categories = Reference(
    ws,
    min_col=1,
    min_row=2,       
    max_row=ws.max_row
)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "G2")

# Excel Chart
ws = wb["Monthly Sales"]

chart = BarChart()

chart.title = "Monthly Sales Report"
chart.x_axis.title = "Month"
chart.y_axis.title = "Total Sales"

data = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_row=ws.max_row
)

categories = Reference(
    ws,
    min_col=1,
    min_row=2,
    max_row=ws.max_row
)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "D2")

# Excel Report Formatting
for sheet in wb.worksheets:
    for cell in sheet[1]:

        cell.font = Font(
            bold=True,
            color="FFFFFF"
        )

        cell.fill = PatternFill(
            fill_type="solid",
            fgColor="1565C0"
        )

        cell.alignment = Alignment(
            horizontal="center"
        )

# width adjust
for sheet in wb.worksheets:
    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter   # column such as 'A' ,'B'
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = max_length + 2
        sheet.column_dimensions[column].width = adjusted_width

wb.save(output_path)