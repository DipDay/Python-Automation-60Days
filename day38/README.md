# Day 38 – GitHub Repository Monitor

## Project Overview
A Python automation project that monitors a GitHub repository using the GitHub REST API and automatically generates a formatted Excel report containing repository information.

## Features
- Fetches repository information using the GitHub REST API.
- Extracts repository details such as:
  - Repository Name
  - Full Name
  - Description
  - Stars
  - Forks
  - Open Issues
  - Created Date
  - Last Updated Date
  - GitHub URL
- Converts timestamps into a readable date format.
- Stores extracted data in a Pandas DataFrame.
- Exports repository information to an Excel file.
- Formats the Excel report using OpenPyXL.
- Automatically adjusts column widths.
- Freezes the header row.
- Applies professional header styling.
- Handles API errors using `try-except`.
- Records execution activities and errors using Python Logging.

## Technologies Used
- Python
- Requests
- Pandas
- OpenPyXL
- GitHub REST API
- Datetime
- Logging

## Project Structure

```text
day38/
│
├── main.py
├── reports/
│   └── github_report.xlsx
│
└── logs/
    └── automation.log
```

*Note: Generated report and log files are excluded from version control.*

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install requests pandas openpyxl
```

3. Run the Python script:

```bash
python main.py
```

4. The script will fetch repository information and generate a formatted Excel report.

## What I Learned
- Working with the GitHub REST API.
- Extracting and processing JSON data.
- Using Python's `datetime` module.
- Creating DataFrames with Pandas.
- Exporting and formatting Excel reports.
- Handling API errors and request timeouts.
- Implementing logging in automation projects.

---

**Challenge:** Day 38 of my 60 Days of Python Automation journey.