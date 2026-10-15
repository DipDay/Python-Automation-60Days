import pandas as pd

data = {
    'Name': ['Iron Man', 'Batman', 'Superman', 'Thor'],
    'Age': [30, 33, 500, 1500]
}
df = pd.DataFrame(data, index=['Hero 1', 'Hero 2', 'Hero 3', 'Hero 4'])
# print(df)
# print(df.loc['Hero 2'])
# print(df.iloc[1])

# add a new column
df['World'] = ['Marvel', 'DC', 'DC', 'Marvel']

# add a new row
new_rows = pd.DataFrame([{'Name': 'Spider-man', 'Age': 16, 'World': 'Marvel'},
                        {'Name': 'Hulk', 'Age': 40, 'World': 'Marvel'}], index=['Hero 5', 'Hero 6'])
df = pd.concat([df, new_rows])
print(df)
