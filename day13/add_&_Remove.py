import pandas as pd

people = {
    'first': ['Corey', 'Jane', 'John'], 
    'last': ['Schafer', 'Doe', 'Doe'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)

df['full_name'] = df['first'] + ' ' + df['last']

df.drop(columns=['first', 'last'], inplace=True)

df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)

# add another dataframe
people = {
    'first': ['Tony', 'Steve'], 
    'last': ['Stark', 'Rogers'], 
    'email': ['IronMan@avenge.com', 'Cap@avenge.com']
}
df2 = pd.DataFrame(people)
df = pd.concat([df, df2], ignore_index=True, sort=False) 


print(df)
