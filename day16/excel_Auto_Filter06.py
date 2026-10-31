import xlwings as xw
import pandas as pd

filename = "E:\\Code\\Python-Automation-60Days\\day16\\Random Sales Data.xlsx"
sales = xw.Book(filename)

sales.sheets[0].api.Range('A1:I5685').AutoFilter(Field=3, Criteria1='East')             # add filter
# sales.sheets[0].api.Range('A1:I5685').AutoFilter(3, 'East')
sales.sheets[0].api.AutoFilterMode = False                                              # remove filter
# sales.save()

sales.sheets[0].api.Range('A1:I5685').AutoFilter(2,['New York', 'Massachusetts'], Operator:=7)         # add multiple filter
# find useful operator: https://learn.microsoft.com/en-us/office/vba/api/excel.xlautofilteroperator

# how to show all the data but filter is on
sales.sheets[0].api.AutoFilter.ShowAllData()

sales.sheets[0].api.AutoFilterMode = False
 
sales.sheets[0].api.Range('A1').CurrentRegion.AutoFilter(Field=2, Criteria1='Massachusetts')      # apply filter with one column

sales.sheets[0].api.AutoFilterMode = False

sales.sheets[0].api.Range('A1').CurrentRegion.AutoFilter(Field=9, Criteria1="5", Operator=3)      # top 5 sales filter

# column index number
df = pd.DataFrame(xw.load(0))
print(list(df).index("Region") + 1)