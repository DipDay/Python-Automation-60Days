import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv", index_col='Respondent')
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

filt = (df['Country'] == 'India')
india_df = df.loc[filt]
# For csv file
# print(India_df.head())
# india_df.to_csv("E:\\Code\\Python-Automation-60Days\\day13\\modified.csv")

# For Excel file
# india_df. to_excel("E:\\Code\\Python-Automation-60Days\\day13\\modified_01.xlsx")
# test = pd.read_excel("E:\\Code\\Python-Automation-60Days\\day13\\modified_01.xlsx", index_col='Respondent')
# print(test.head())

