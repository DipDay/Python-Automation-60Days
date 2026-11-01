import pandas as pd
from openpyxl import workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook

df = pd.read_excel("E:\\Code\\Python-Automation-60Days\\day17\\Random Sales Data order only.xlsx")
# print(df.head(5))
# print(df.columns)

# Creating reports based on pivot table
pivot_table = pd.pivot_table(data=df, values=["Sales", "Quantity","Profit"], index=["Category"],
                             columns=["Segment"] ,aggfunc={"Sales":"sum","Quantity":"sum" ,"Profit":"sum"}, fill_value=0)
# print(pivot_table)


wkb = load_workbook("E:\\Code\\Python-Automation-60Days\\day17\\Random Sales Data order only.xlsx")
wkb.create_sheet("PT_SalesQTProfit")
cateagory = wkb["PT_SalesQTProfit"]
# Write the pivot table to the worksheet 
for row in dataframe_to_rows(pivot_table, index=True, header=True):
    cateagory.append(row)
wkb.save("E:\\Code\\Python-Automation-60Days\\day17\\Piovt Table sales data.xlsx")



pivot_table1 = pd.pivot_table(data=df, values=["Sales", "Quantity","Profit"], index=["State"], margins=True, margins_name="Grand Total",
                             columns=["Region"] ,aggfunc={"Sales":"sum","Quantity":"sum" ,"Profit":"sum"}, fill_value=0)
# print(pivot_table1)
wkb.create_sheet("PT_StateRegion")
state = wkb["PT_StateRegion"]
for row in dataframe_to_rows(pivot_table1, index=True, header=True):
    state.append(row)

wkb.save("E:\\Code\\Python-Automation-60Days\\day17\\Piovt Table sales data.xlsx")
print("Done!")