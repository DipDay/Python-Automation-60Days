import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv", index_col='Respondent' )
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv", index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# print(df['ConvertedComp'].head(15))
# print(df['ConvertedComp'].median())
# print(df.median(numeric_only=True))                 # Instruct Pandas to ignore string/text columns automatically
# print(df.describe())
# print(df['ConvertedComp'].count())

# print(df['Hobbyist'])
# print(df['Hobbyist'].value_counts())

# print(df['SocialMedia'])
# print(schema_df.loc['SocialMedia'])
# print(df['SocialMedia'].value_counts())
# print(df['SocialMedia'].value_counts(normalize=True))

# print(df['Country'].value_counts())
country_grp = df.groupby('Country')
# print(country_grp.groups.keys())                             # Print all unique group names to see the exact spelling
print(country_grp.get_group('Afghanistan').head(50))