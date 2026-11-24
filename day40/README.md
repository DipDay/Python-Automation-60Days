# Day 40 — AI Text Classification

## Overview
An AI-powered customer message classification system built with Python and Groq API.

The program analyzes customer messages, identifies their categories using an AI model, and exports the classification results into a formatted Excel spreadsheet.

## Features
- AI-powered text classification using Groq API.
- Supports multiple customer messages.
- Classifies messages into multiple relevant categories.
- Handles API errors using `try-except`.
- Stores classification results in a Python dictionary.
- Exports results to Excel using Pandas.
- Automatically formats Excel reports using OpenPyXL.
- Automatically adjusts column widths.
- Applies header styling and text wrapping.

## Categories
1. Complaint
2. Inquiry
3. Feedback
4. Order
5. Other (for unmatched messages)

## Technologies Used
- Python
- Groq API
- OpenAI Python SDK
- Pandas
- OpenPyXL
- Python-dotenv

## Project Structure

```text
day40/
│
├── .env
├── main.py
└── classification_result.xlsx
```

## Installation

Install the required packages:

```bash
pip install openai python-dotenv pandas openpyxl
```

## Environment Variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

**Important:** Never upload your `.env` file or expose your API key publicly.

## Usage

Run the program:

```bash
python main.py
```

The program processes the customer messages and generates a formatted Excel report.

## Output

The generated Excel file contains two columns:

| Message | Category |
|---|---|
| My order arrived broken. | Complaint |
| How can I get a refund? | Inquiry |
| Your service is amazing! | Feedback |
| I want to purchase a new laptop. | Order |

## Learning Outcomes
- Working with Large Language Model (LLM) APIs.
- Understanding AI text classification.
- Writing effective system prompts.
- Processing multiple API requests using loops.
- Handling API errors.
- Converting dictionaries into Pandas DataFrames.
- Creating and formatting Excel reports using OpenPyXL.

---

**Part of my 60 Days Python Automation Learning Journey.**