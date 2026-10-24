import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv", index_col='Respondent' )
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# print(df.columns)
# print(df.head)
print(schema_df.sort_index())                                # sorting the index
# print(schema_df.columns)
# print(schema_df.loc['Hobbyist'])
# print(schema_df.loc['MgrIdiot'])
# print(schema_df.loc['MgrIdiot', 'QuestionText'])            # to see the full text you need give the column name also

