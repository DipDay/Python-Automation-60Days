import pandas as pd

# df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day12\\test01.csv")
df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day12\\test01.csv", index_col='Name')          # change (No. <---> Name) column

# selection column
# print(df['Name'].to_string())
# print(df[['Name', 'Height', 'Weight']].to_string())

# selection row
# print(df.loc[149])
# print(df)
# print(df.loc['Mewtwo'])
# print(df.loc['Mewtwo', ['Height', 'Weight']])
# print(df.loc['Charizard': 'Blastoise', ['Height', 'Weight']])                   # only height & weight info from Charizard to Blastoise
# print(df.iloc[0:10])
# print(df.iloc[0:10:2])                                                            # print only 1, 3, 5, 7, 9 no. pokemon's info
print(df.iloc[0:10, 0:3])                                                           # print only first ten rows and first three colums



