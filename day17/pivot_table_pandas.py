import pandas as pd
# import numpy as np

df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day17\\sample.csv")
# print(df.head(5))
# print(df.columns)
# print(pd.pivot_table(data=df, index=["State"], values=["Profit", "Sales"], aggfunc=np.sum))
# print(pd.pivot_table(data=df, index=["State"], values=["Profit", "Sales"], aggfunc=["sum", len]))
# print(pd.pivot_table(data=df, index=["State"], values=["Profit", "Sales"], aggfunc=["sum", len], fill_value=0))
print(pd.pivot_table(data=df, index=["State"], values=["Profit", "Sales"], aggfunc={"Sales":"sum", "Profit":"mean"}, fill_value=0))


