import pandas as pd
import re

file_path = "E:\\Code\\Python-Automation-60Days\\day20\\messy_employees 200.csv"
df = pd.read_csv(file_path)

original_rows = len(df)

# df["Name"] = df["Name"].str.strip().str.title()
df["Name"] = (df["Name"].str.strip().str.replace(r"\s+", " ", regex=True).str.title())
df["Email"] = df["Email"].str.strip().str.lower()
df["Department"] = df["Department"].str.strip().str.title()

df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
df["Salary"] = pd.to_numeric(df["Salary"], errors='coerce')
df["Join Date"] = pd.to_datetime(df["Join Date"], errors="coerce")

department_mapping = {
    "Eng": "Engineering",
    "Hr": "Human Resources",
    "It": "IT",
    "I.T.": "IT",
    "Mkt": "Marketing",
    "Ops": "Operations"
}

df["Department"] = df["Department"].replace(
    department_mapping
)

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

cleaned_rows = []
rejected_rows = []

# 3. Remove duplicate emails
duplicate_mask = (
    df["Email"].notna()
    & df.duplicated(subset=["Email"], keep="first")
)

duplicates_removed = int(duplicate_mask.sum())
df = df.loc[~duplicate_mask].copy()

# run loop every row
for index, row in df.iterrows():
    issues = []

    # 1. Name
    if pd.isna(row["Name"]):
        issues.append("Missing Name")

    # 2. email
    if pd.isna(row["Email"]):
        issues.append("Missing Email")
    elif re.fullmatch(email_pattern, str(row["Email"])) is None:
        issues.append("Invalid Email")

    # 3. Age
    if pd.isna(row["Age"]) or row["Age"] <= 0:
        issues.append("Invalid/Missing Age")

    # 4. Salary
    if pd.isna(row["Salary"]) or row["Salary"] <= 0:
        issues.append("Invalid/Missing Salary")

    # 5. Join Date
    if pd.isna(row["Join Date"]):
        issues.append("Invalid/Missing Join Date")

    # 6. Department
    if pd.isna(row["Department"]):
        issues.append("Missing Department")

    # if no problem
    if len(issues) == 0:
        cleaned_rows.append(row)
    else:
        # if row has problem
        row_dict = row.copy()
        row_dict["Issues"] = ", ".join(issues)
        rejected_rows.append(row_dict)

# list to Dataframe convert
cleaned = pd.DataFrame(cleaned_rows)
rejected = pd.DataFrame(rejected_rows)

# 9. Create summary
summary = pd.DataFrame({
    "Metric": [
        "Original Rows",
        "Duplicates Removed",
        "Remaining Rows",
        "Valid Rows",
        "Rejected Rows"
    ],
    "Value": [
        original_rows,
        duplicates_removed,
        len(df),
        len(cleaned),
        len(rejected)
    ]
})

# 10. Export to Excel
with pd.ExcelWriter(
    "E:\\Code\\Python-Automation-60Days\\day20\\cleaned_employees_report 2.xlsx",
    engine="openpyxl"
) as writer:

    cleaned.to_excel(
        writer,
        sheet_name="Cleaned Data",
        index=False
    )

    rejected.to_excel(
        writer,
        sheet_name="Rejected Rows",
        index=False
    )

    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

print(summary)

