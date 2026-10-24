import pandas as pd

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\data.csv")
schema_df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day13\\schema.csv")

print(df.shape)
print(schema_df.shape)
# print(df.info())