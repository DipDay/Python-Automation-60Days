import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv", index_col='Respondent' )
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# print(df.columns)
high_salary = (df['ConvertedComp'] > 70000)
# print(df.loc[high_salary])
# print(df.loc[high_salary, ['Country','LanguageWorkedWith', 'ConvertedComp']])

# countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
# filt = df['Country'].isin(countries)
# print(df.loc[filt, 'Country'])

filt = df['LanguageWorkedWith'].str.contains('Python', na=False)
print(df.loc[filt, 'LanguageWorkedWith'])
