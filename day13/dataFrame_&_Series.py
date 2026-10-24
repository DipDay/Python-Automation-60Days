import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv")
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv")

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# print(df.to_string())
# print(df.head())                                                   # print first 5 rows
# print(df)                                               
# print(schema_df)
# print(df.columns)
# print(df['Hobbyist'])
# print(df['Hobbyist'].value_counts())
# print(df.loc[[0], 'Hobbyist'])                              # 1st person's answer for 'Hobbyist' question
# print(df.loc[0:2, 'Hobbyist'])                                # 1st three persons answers for 'Hobbyist' question
print(df.loc[0:2, 'Hobbyist': 'Employment'])                 # 1st three persons answers for 'Hobbyist' to 'Employment' question