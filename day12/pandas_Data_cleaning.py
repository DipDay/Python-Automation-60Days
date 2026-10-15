import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day12\\test01.csv")

# 1. Delete any column
# df = df.drop(columns=['Legendary'])

# 2. Handle missing data
# df = df.dropna(subset=['Type2'])
# df = df.fillna({'Type2': 'None'})

# 3. Fix inconsistent values
# df['Type1'] = df['Type1'].replace({'Grass': 'GRASS', 'Fire':'FIRE'})                       # Make uppercase Grass ---> GRASS

# 4. Standardize data
# df['Name'] = df['Name'].str.lower()

# 5. Fix data types
# df['Legendary'] = df['Legendary'].astype(bool)

# 6. Remove dublicate values
df =df.drop_duplicates()
print(df.to_string())
