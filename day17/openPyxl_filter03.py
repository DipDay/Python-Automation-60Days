import openpyxl
from datetime import datetime

wkb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day17\\Random Sales Data.xlsx")
order = wkb['Order']

# 1. Create the filtered worksheet
filter_worksheet = wkb.create_sheet(title="Filtered_sheet")

# 2. Extract and append the header row to the new sheet
header = [cell.value for cell in order[1]]
filter_worksheet.append(header)

# 3. Find the 'Sales' column dynamically
sales_idx = header.index('Sales')
filter_condition = 1000

# 4. Filter and append matching rows
for row in order.iter_rows(min_row=2, values_only=True):
    sales_value = row[sales_idx]
    if sales_value is not None and sales_value > filter_condition:
        filter_worksheet.append(row)

# 5. Set the new sheet as active so Excel opens it immediately
wkb.active = filter_worksheet

# 6. Save the workbook (ensure the file is closed in Excel before saving!)
wkb.save("E:\\Code\\Python-Automation-60Days\\day17\\Filtered Sales Data.xlsx")


# Filter by Date
ws1 = wkb.create_sheet(title="Custome Date")
ws1.append(header)
date_index = header.index('Order Date')

filter_date_condition = datetime(2016, 11, 28)
for row in order.iter_rows(min_row=2, values_only=True):
    if row[date_index] > filter_date_condition:
        ws1.append(row)
wkb.save("E:\\Code\\Python-Automation-60Days\\day17\\Filtered Sales Data.xlsx")

print("Filtered data successfully!")