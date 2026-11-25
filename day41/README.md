# Day 41 — AI-Powered Excel Review Analyzer

## Project Overview

An AI-powered Excel automation project that analyzes customer reviews using the Groq API and generates a structured Excel report.

The project automatically processes customer reviews and extracts:
- **Category:** Classifies the type of customer feedback.
- **Sentiment:** Identifies whether the review is Positive, Negative, or Neutral.
- **Summary:** Generates a short summary of each review.

## Technologies Used

- Python
- Pandas
- OpenAI Python SDK
- Groq API
- JSON
- OpenPyXL
- Python-dotenv

## Project Structure

```text
day41/
│
├── main.py
├── reviews.xlsx
├── new.xlsx
├── .env
└── README.md
```

## How It Works

1. Reads customer reviews from `reviews.xlsx` using Pandas.
2. Sends each review to the Groq API.
3. Uses AI to classify the review and determine its sentiment.
4. Extracts structured JSON responses.
5. Stores the results in a Python list.
6. Converts the results into a Pandas DataFrame.
7. Exports the analyzed data into `new.xlsx`.
8. Formats the Excel report using OpenPyXL.

## Excel Output

The generated Excel report contains:

| Column | Description |
|---|---|
| ID | Customer review ID |
| Review | Original customer review |
| Category | AI-generated category |
| Sentiment | Positive, Negative, or Neutral |
| Summary | AI-generated short summary |

### Excel Formatting Features

- Bold white headers
- Dark blue header background
- Custom column widths
- Text wrapping and alignment
- Frozen header row
- Auto Filter support

## Setup & Installation

Install the required packages:

```bash
pip install pandas openpyxl python-dotenv openai
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the project:

```bash
python day41/main.py
```

**Note:** Never upload your `.env` file or expose your API key on GitHub.

## Learning Outcomes

- Working with Excel files using Pandas
- Integrating AI APIs into Python automation
- Processing structured JSON responses
- Building reusable Python functions
- Automating batch text classification
- Generating formatted Excel reports using OpenPyXL

---

**Day 41 of Python Automation — 60 Days Challenge.**