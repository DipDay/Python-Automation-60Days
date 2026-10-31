import pandas as pd

path = "E:\\Code\\Python-Automation-60Days\\day16\\Customized Sales Data.xlsx"

# print(pd.ExcelFile(path).sheet_names)

with pd.ExcelWriter("E:\\Code\\Python-Automation-60Days\\day16\\new combined Data.xlsx", engine="xlsxwriter") as writer:
    combined_df = pd.DataFrame()

    for sht in pd.ExcelFile(path).sheet_names:
        df = pd.read_excel(path, sheet_name=sht)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    combined_df.to_excel(writer, sheet_name='All Sheets', index=False)

print("Done :)")

