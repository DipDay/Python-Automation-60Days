# Day 43 — API Error Handling, Token Tracking & Cost Estimation

A Python automation project that analyzes customer reviews using the Groq API. This project focuses on handling API failures, retrying failed requests, processing reviews in batches, tracking token usage, and estimating API costs.

## Features

- **API Error Handling:** Handles authentication errors, rate limits, timeouts, and connection errors.
- **Retry Mechanism:** Automatically retries failed API requests up to 3 attempts.
- **Exponential Backoff:** Waits 2 seconds, then 4 seconds between retry attempts.
- **Batch Processing:** Processes customer reviews in batches of 10.
- **Token Tracking:** Tracks input, output, and total tokens used.
- **Cost Estimation:** Estimates API costs based on token usage and example pricing rates.
- **Excel Report:** Generates an Excel workbook with two worksheets.
- **Excel Formatting:** Automatically formats headers, adjusts column widths, enables filters, and freezes the header row.

## Project Structure

```text
day43/
│
├── reviews.xlsx
├── main.py
└── new.xlsx
```

## Technologies Used

- Python
- Pandas
- OpenAI Python SDK
- Groq API
- Python-dotenv
- OpenPyXL
- JSON

## Installation

Install the required libraries:

```bash
pip install openai python-dotenv pandas openpyxl
```

## Environment Setup

Create a `.env` file in your project directory and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Never upload your `.env` file or expose your API key publicly.

## Input File

The program reads customer reviews from `reviews.xlsx`.

Required columns:

| ID | Review |
|---|---|
| 1 | My order arrived broken. |
| 2 | The delivery was very fast. |

## How It Works

1. Loads the API key from the `.env` file.
2. Reads customer reviews from Excel.
3. Divides reviews into batches of 10.
4. Sends each batch to the Groq API for analysis.
5. Retries failed requests using exponential backoff.
6. Extracts category, sentiment, and summary from the API response.
7. Tracks input, output, and total tokens.
8. Estimates API cost using the configured example rates.
9. Generates an Excel report with two worksheets.
10. Applies formatting to the generated workbook.

## Retry Strategy

The project uses exponential backoff:

| Attempt | Waiting Time |
|---|---:|
| 1st retry | 2 seconds |
| 2nd retry | 4 seconds |
| 3rd attempt | No further retry |

The maximum number of attempts is 3.

## Token Usage & Cost Estimation

The program tracks:

- Input Tokens
- Output Tokens
- Total Tokens
- Total Batches
- Estimated Cost (USD)

Example pricing rates used for learning:

| Token Type | Example Price |
|---|---:|
| Input | $0.10 / 1M tokens |
| Output | $0.40 / 1M tokens |

**Note:** These are illustrative rates for practicing cost estimation, not verified current Groq pricing. Actual costs depend on the provider's current pricing and model.

## Output File

The program generates `new.xlsx` with two worksheets.

### 1. Review Results

Contains the analyzed customer reviews:

- ID
- Review
- Category
- Sentiment
- Summary

### 2. Usage Report

Contains API usage statistics and estimated cost.

## What I Learned

- Handling API errors with exception handling.
- Implementing retry mechanisms.
- Understanding exponential backoff.
- Processing API requests in batches.
- Understanding RPM and TPM rate limits.
- Tracking API token usage.
- Calculating estimated API costs.
- Creating multi-sheet Excel reports.
- Formatting Excel files using OpenPyXL.

---

**Day 43 of my 60-Day Python Automation Journey.**