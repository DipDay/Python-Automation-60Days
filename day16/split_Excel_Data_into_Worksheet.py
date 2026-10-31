import pandas as pd

df = pd.read_excel("E:\\Code\\Python-Automation-60Days\\day16\\Random Sales Data.xlsx")
# print(df.head())
# print(df['Location'].unique())

with pd.ExcelWriter("E:\\Code\\Python-Automation-60Days\\day16\\Customized Sales Data.xlsx", engine="xlsxwriter") as writer:
    for state in df['Location'].unique():
        new_df = df[df['Location'] == state]
        new_df.to_excel(writer, sheet_name=state, index=False)

print("Done!")