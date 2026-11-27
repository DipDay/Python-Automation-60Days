# Day 42 — Batch Processing with Python

## Overview

This project demonstrates how to process multiple customer reviews using Batch Processing and the Groq API.

Instead of sending individual API requests for every customer review, this project groups reviews into smaller batches and processes them together.

The project processes 100 customer reviews in batches of 10 and generates AI-powered analysis for each review.

## Features

- Read customer reviews from Excel files using Pandas.
- Process multiple reviews in batches.
- Analyze reviews using the Groq API.
- Generate Category, Sentiment, and Summary for each review.
- Parse structured JSON responses.
- Match AI-generated results with original review IDs.
- Validate the number of AI-generated results.
- Add delays between API requests to reduce rate-limit pressure.
- Export results to a formatted Excel file.

## Technologies Used

- Python
- Pandas
- OpenAI Python SDK
- Groq API
- JSON
- OpenPyXL
- python-dotenv

## Project Structure

```text
day42/
│
├── main.py
├── .env
├── .gitignore
├── reviews.xlsx
└── new.xlsx
```

## How It Works

1. Load customer reviews from `reviews.xlsx`.
2. Convert the Review column into a Python list.
3. Divide reviews into batches of 10 using List Slicing.
4. Send each batch to the Groq API.
5. Receive structured JSON containing individual analysis results.
6. Match each result with its original review ID using `zip()`.
7. Collect all processed results in a list.
8. Export the results to `new.xlsx`.
9. Format the Excel worksheet using OpenPyXL.

## Batch Processing Example

```python
batch_size = 10

for i in range(0, len(reviews), batch_size):
    batch = reviews[i:i + batch_size]

    data = analyze_batch(batch)
```

## Output

The generated Excel file contains five columns:

| Column | Description |
|---|---|
| ID | Original review ID |
| Review | Customer review |
| Category | Review category |
| Sentiment | Positive, Negative, or Neutral |
| Summary | Short review summary |

## API Configuration

Create a `.env` file in your project folder:

```env
GROQ_API_KEY=your_api_key_here
```

Never upload your API key to GitHub.

## Run the Project

Install the required packages:

```bash
pip install pandas openai python-dotenv openpyxl
```

Run the script:

```bash
python main.py
```

## Key Concepts Learned

- Batch Processing
- Python List Slicing
- `range()` and `enumerate()`
- JSON Serialization and Deserialization
- API Integration
- Structured AI Responses
- `zip()` for matching records
- API Rate Limiting
- Excel Automation

## Learning Progress

**Day 42 of Python Automation — 60 Days Challenge**

