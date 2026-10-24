import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv", index_col='Respondent' )
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)
# print(df[['Country', 'ConvertedComp']].head(50))                                            # show first 50 people

# print(df['ConvertedComp'].nlargest(10))                                     # show first 10 people
print(df.nsmallest(10, 'ConvertedComp'))