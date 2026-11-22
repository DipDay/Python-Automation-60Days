import requests
from datetime import datetime
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import logging

logging.basicConfig(
    filename="day38/logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Automation started")

output_path = "day38/reports/github_report.xlsx"

owner = "DipDay"
repo = "Prize-Bond-Checker"

url = f"https://api.github.com/repos/{owner}/{repo}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    logging.info("GitHub API request successful")

    data = response.json() 

    # print(data)
    print("========== GITHUB REPOSITORY REPORT ==========")
    print("Repository:", data["name"])
    print("Full Name:", data["full_name"])
    print()

    description = data["description"] or "No description available"
    print("Description:", description)
    print()

    print("Stars:", data["stargazers_count"])
    print("Forks:", data["forks_count"])
    print("Open Issues:", data["open_issues_count"])
    print()

    created_date = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    print("Created:", created_date.strftime("%d %B %Y, %I:%M %p"))


    last_Updated_date = datetime.strptime(data["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
    print("Last Updated:", last_Updated_date.strftime("%d %B %Y, %I:%M %p"))
    print()

    print("GitHub URL:", data["html_url"])

    # Create a Dataframe
    repo_data = {
        "Repository": data["name"],
        "Full Name": data["full_name"],
        "Description": description,
        "Stars": data["stargazers_count"],
        "Forks": data["forks_count"],
        "Open Issues": data["open_issues_count"],
        "Created": created_date.strftime("%d %B %Y, %I:%M %p"),
        "Last Updated": last_Updated_date.strftime("%d %B %Y, %I:%M %p"),
        "GitHub URL": data["html_url"]
    }

    df = pd.DataFrame([repo_data])

    # print(df)

    # save to Excel
    df.to_excel(output_path, index=False)
    logging.info("Excel report created successfully")

    # Excel Report Formatting
    wb = load_workbook(output_path)
    ws = wb.active

    ws.freeze_panes = "A2"           # Freeze Header (Lock the column Head)
    for col in ws.columns:
        max_length = 0
        col_letter = get_column_letter(col[0].column)
                
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
                
        ws.column_dimensions[col_letter].width = max_length + 2

    for cell in ws[1]:
        cell.font = Font(
            bold=True,
            color="FFFFFF"
        )

        cell.fill = PatternFill(
            fill_type="solid",
            fgColor="1565C0"
        )

        cell.alignment = Alignment(
            horizontal="center"
        )

    wb.save(output_path)
    logging.info("Automation completed")

except requests.exceptions.RequestException as e:
    print("API Error:", e)
    logging.error(f"API Error: {e}")
