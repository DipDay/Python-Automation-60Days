import openpyxl

wkb = openpyxl.load_workbook("E:\\Code\\Python-Automation-60Days\\day17\\Random Sales Data.xlsx")
order = wkb['Order']

# print([cell.value for cell in order[1]])
# print([cell.value for cell in order[1]].index('State'))

source_column_index = [cell.value for cell in order[1]].index('State')
# Find unique value
unique_value = set()
for row in order.iter_rows(min_row=2, values_only=True):
    value = row[source_column_index]
    unique_value.add(value) 
print(unique_value)
print(len(unique_value))

# Create a new column
new_column_index = order.max_column + 5
order.cell(1, new_column_index).value = "Unique State"
order.cell(1, new_column_index+1).value = "Total Quantity"
order.cell(1, new_column_index+2).value = "Total Quantity2"
order.cell(1, new_column_index+3).value = "Postal Code"
order.cell(1, new_column_index+4).value = "Date Transformation"

# Iterate thorough unique states and apply Sumif formula
for i, state in enumerate(unique_value, start = 2):
    order[f"Z{i}"] = state
    order[f"AA{i}"] = f'=SUMIF($K:$K,"{state}",S:S)'
    order[f"AB{i}"] = f'=SUMIF($K:$K,Z{i},S:S)'
    order[f"AC{i}"] = f'=VLOOKUP(Z{i},$K:$L,2,0)'
    order[f"AD{i}"] = f'=TEXT(C{i},"dddd dd - mmm - yyyy")'

wkb.save("E:\\Code\\Python-Automation-60Days\\day17\\Superstore_Formula1.xlsx")