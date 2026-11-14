import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, PatternFill, Alignment

input_path = "E:\\Code\\Python-Automation-60Days\\day22\\sales.xlsx"
output_path = "E:\\Code\\Python-Automation-60Days\\day22\\sales_report.xlsx"

df = pd.read_excel(input_path)
print(df.head())

# Calculate Total Sales
df["Sales"] = df["Quantity"] * df["Unit Price (BDT)"]
total_sales = df["Sales"].sum()

# Find Top Products
top_products = (df.groupby("Product")["Sales"].sum().sort_values(ascending=False))

# Monthly Sales Analysis
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
df["Date"] = df["Date"].dt.date

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

# Convert the grouping indexes into columns before exporting
top = top_products.rename("Sales").reset_index()
monthly = monthly_sales.rename("Sales").reset_index()

# 9. Summary
total_orders = len(df)
total_quantity = df["Quantity"].sum()
max_sale = df["Sales"].max()
min_sale = df["Sales"].min()
average_sale = df["Sales"].mean()

summary = pd.DataFrame({
    "Metric": [
        "Total Sales (BDT)", 
        "Total Orders", 
        "Total Products Sold", 
        "Highest Order Value", 
        "Lowest Order Value", 
        "Average Order Value"
    ],
    "Value": [
        total_sales, 
        total_orders, 
        total_quantity, 
        max_sale, 
        min_sale, 
        round(average_sale, 2)
    ]
})

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
    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )


    # Adjust space every column
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        worksheet.freeze_panes = "A2"           # Freeze Header (Lock the column Head)
        for col in worksheet.columns:
            max_length = 0
            col_letter = get_column_letter(col[0].column)
            
            for cell in col:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            
            worksheet.column_dimensions[col_letter].width = max_length + 2

# Excel Chart Top product
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

ws.add_chart(chart, "D2")

# Excel Chart Monthly Sales
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

wb.save(output_path)