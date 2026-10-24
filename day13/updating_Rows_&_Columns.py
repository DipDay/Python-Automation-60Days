import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv", index_col='Respondent' )
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
# print(df.columns)

# df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No':False})                
# print(df['Hobbyist'])

df['Hobbyist'] = df['Hobbyist'].replace({'Yes': True, 'No':False})              # replace vs map 
print(df['Hobbyist'])