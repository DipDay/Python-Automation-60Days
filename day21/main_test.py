
import pandas as pd

from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter


# -----------------------------
# 1. Read Input File
# -----------------------------

input_file = "E:\\Code\\Python-Automation-60Days\\day21\\sales.xlsx"
output_file = "E:\\Code\\Python-Automation-60Days\\day21\\sales_report.xlsx"

df = pd.read_excel(input_file)

required_columns = ["Date", "Product", "Quantity", "Unit Price"]

if not all(col in df.columns for col in required_columns):
    raise ValueError("Missing required columns in Excel file!")


# -----------------------------
# 2. Data Cleaning
# -----------------------------

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit Price"] = pd.to_numeric(df["Unit Price"], errors="coerce")

df = df.dropna(subset=required_columns)

df = df[
    (df["Quantity"] >= 0) &
    (df["Unit Price"] >= 0)
].copy()


# -----------------------------
# 3. Calculate Sales
# -----------------------------

df["Sales"] = df["Quantity"] * df["Unit Price"]

total_sales = df["Sales"].sum()
total_transactions = len(df)
total_units = df["Quantity"].sum()


# -----------------------------
# 4. Top Products
# -----------------------------

product_sales = (
    df.groupby("Product", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)


# -----------------------------
# 5. Monthly Sales
# -----------------------------

df["Month"] = df["Date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Month", as_index=False)["Sales"]
    .sum()
)


# -----------------------------
# 6. Create Excel Sheets
# -----------------------------

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    df.to_excel(writer, sheet_name="Raw Data", index=False)

    product_sales.to_excel(
        writer,
        sheet_name="Product Sales",
        index=False
    )

    monthly_sales.to_excel(
        writer,
        sheet_name="Monthly Sales",
        index=False
    )


# -----------------------------
# 7. Create Summary Sheet
# -----------------------------

wb = load_workbook(output_file)

ws = wb.create_sheet("Summary", 0)

ws.merge_cells("A1:B1")
ws["A1"] = "AUTOMATED SALES REPORT"

ws["A3"] = "Total Sales"
ws["B3"] = total_sales

ws["A4"] = "Total Transactions"
ws["B4"] = total_transactions

ws["A5"] = "Total Units Sold"
ws["B5"] = total_units

ws["A7"] = "Top Products"

ws["A8"] = "Product"
ws["B8"] = "Total Sales"

for row in product_sales.itertuples(index=False):
    ws.append([]) if False else None

for index, row in enumerate(
    product_sales.itertuples(index=False),
    start=9
):
    ws.cell(index, 1, row.Product)
    ws.cell(index, 2, row.Sales)


# -----------------------------
# 8. Create Monthly Sales Chart
# -----------------------------

monthly_ws = wb["Monthly Sales"]

chart = BarChart()

chart.title = "Monthly Sales"
chart.x_axis.title = "Month"
chart.y_axis.title = "Revenue"

data = Reference(
    monthly_ws,
    min_col=2,
    min_row=1,
    max_row=monthly_ws.max_row
)

categories = Reference(
    monthly_ws,
    min_col=1,
    min_row=2,
    max_row=monthly_ws.max_row
)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

chart.height = 8
chart.width = 16

ws.add_chart(chart, "D3")


# -----------------------------
# 9. Format Excel Sheets
# -----------------------------

for sheet in wb.worksheets:

    sheet.freeze_panes = "A2"

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

    for column in sheet.columns:

        max_length = 0
        column_letter = get_column_letter(column[0].column)

        for cell in column:

            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        sheet.column_dimensions[column_letter].width = max_length + 4


# Summary Title Formatting

ws["A1"].font = Font(
    bold=True,
    size=16,
    color="FFFFFF"
)

ws["A1"].fill = PatternFill(
    fill_type="solid",
    fgColor="1565C0"
)

ws["A1"].alignment = Alignment(
    horizontal="center"
)


# Currency Formatting

for sheet_name in ["Summary", "Product Sales", "Monthly Sales", "Raw Data"]:

    sheet = wb[sheet_name]

    if sheet_name == "Summary":
        cells = [f"B3", f"B9"]

        for row in range(9, sheet.max_row + 1):
            sheet[f"B{row}"].number_format = '#,##0.00'

        sheet["B3"].number_format = '#,##0.00'

    elif sheet_name == "Product Sales":
        for row in range(2, sheet.max_row + 1):
            sheet[f"B{row}"].number_format = '#,##0.00'

    elif sheet_name == "Monthly Sales":
        for row in range(2, sheet.max_row + 1):
            sheet[f"B{row}"].number_format = '#,##0.00'

    else:
        for row in range(2, sheet.max_row + 1):
            sheet[f"E{row}"].number_format = '#,##0.00'


# -----------------------------
# 10. Save Final Report
# -----------------------------

wb.save(output_file)

print("Sales Report Generated Successfully!")
print(f"Total Sales: {total_sales:,.2f}")
print(f"Output File: {output_file}")
