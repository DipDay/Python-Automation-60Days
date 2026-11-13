import pandas as pd

# Read CSV
df = pd.read_csv("E:\\Code\\Python-Automation-60Days\\day20\\messy_employees 200.csv")

original_rows = len(df)

# 1. Remove extra spaces
for col in ["Name", "Email", "Department"]:
    df[col] = df[col].astype("string").str.strip()

df = df.replace("", pd.NA)

# 2. Standardize text
df["Name"] = df["Name"].str.title()
df["Email"] = df["Email"].str.lower()
df["Department"] = df["Department"].str.title()

# 3. Remove duplicate emails
duplicate_mask = (
    df["Email"].notna()
    & df.duplicated(subset=["Email"], keep="first")
)

duplicates_removed = int(duplicate_mask.sum())

df = df.loc[~duplicate_mask].copy()

# 4. Handle missing department
df["Department"] = df["Department"].fillna("Unknown")

# 5. Convert data types
df["Age"] = pd.to_numeric(
    df["Age"], errors="coerce"
)

df["Salary"] = pd.to_numeric(
    df["Salary"], errors="coerce"
)

df["Join Date"] = pd.to_datetime(
    df["Join Date"], errors="coerce"
)

# 6. Validate email
email_pattern = (
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

valid_email = df["Email"].str.match(
    email_pattern, na=False
)

# 7. Find invalid rows
def find_issues(row):
    issues = []

    if pd.isna(row["Name"]):
        issues.append("Missing Name")

    if pd.isna(row["Email"]):
        issues.append("Missing Email")
    elif not pd.Series([row["Email"]]).str.match(
        email_pattern
    ).iloc[0]:
        issues.append("Invalid Email")

    if pd.isna(row["Age"]):
        issues.append("Invalid/Missing Age")

    if pd.isna(row["Salary"]):
        issues.append("Invalid/Missing Salary")

    if pd.isna(row["Join Date"]):
        issues.append("Invalid/Missing Join Date")

    return ", ".join(issues)


df["Issues"] = df.apply(find_issues, axis=1)

# 8. Separate clean and rejected data
cleaned = df[df["Issues"] == ""].drop(
    columns=["Issues"]
)

rejected = df[df["Issues"] != ""]

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
    "E:\\Code\\Python-Automation-60Days\\day20\\cleaned_employees_report 1.xlsx",
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

print("Data Cleaning Completed!")
print(summary)
print("Report saved successfully!")

