import pandas as pd

na_vals = ['NA', 'Missing']
df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv", index_col='Respondent' ,  na_values=na_vals)
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# print(df['YearsCode'].head(10))
# print(df['YearsCode'].unique())

df['YearsCode'] = df['YearsCode'].replace('Less than 1 year', 0)
df['YearsCode'] = df['YearsCode'].replace('More than 50 years', 51)
df['YearsCode'] = df['YearsCode'].astype(float)
# print(df['YearsCode'].unique())
print(df['YearsCode'].mean())                               # average value
print(df['YearsCode'].median())