import os
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
import time

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

file_path = "day42/reviews.xlsx"

def analyze_batch(batch):

    prompt = f"""
    Analyze the following customer reviews.

    {json.dumps(batch, indent=2)}

    Return a JSON object with a "results" list.

    Each item in the results list must contain:
    - category
    - sentiment (Positive, Negative, Neutral)
    - summary

    Generate exactly one result for each input review.
    Maintain the same order as the input reviews.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a customer review analyzer. Return only valid JSON with a results list containing one object per input review."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)

results = []


df = pd.read_excel(file_path)

reviews = df["Review"].tolist()

batch_size = 10

total_batches = len(range(0, len(reviews), batch_size))

print("Total Reviews:", len(reviews))
print("Total Batches:", total_batches)

for batch_no, i in enumerate(range(0, len(reviews), batch_size), start=1):

    batch = reviews[i:i + batch_size]

    print(f"Processing Batch {batch_no}")

    data = analyze_batch(batch)

    batch_results = data["results"]

    if len(batch_results) != len(batch):
        raise ValueError("Mismatch between reviews and AI results")

    batch_df = df.iloc[i:i + batch_size]

    for (_, row), result in zip(batch_df.iterrows(), batch_results):

        results.append({
            "ID": row["ID"],
            "Review": row["Review"],
            "Category": result["category"],
            "Sentiment": result["sentiment"],
            "Summary": result["summary"]
        })

    print(f"Batch {batch_no} completed!")
    time.sleep(3)

new_df = pd.DataFrame(results)

print(new_df)

output_path = "day42/new.xlsx"

new_df.to_excel(output_path, index=False)

print("Excel file created successfully!")

wb = load_workbook(output_path)
ws = wb.active

# Header formatting
for cell in ws[1]:
    cell.font = Font(
        bold=True,
        color="FFFFFF"
    )
    cell.fill = PatternFill(
        start_color="1F4E78",
        end_color="1F4E78",
        fill_type="solid"
    )
    cell.alignment = Alignment(
        horizontal="center",
        vertical="center"
    )

# Column widths
column_widths = {
    "A": 10,
    "B": 55,
    "C": 25,
    "D": 15,
    "E": 65
}

for column, width in column_widths.items():
    ws.column_dimensions[column].width = width

ws.freeze_panes = "A2"
ws.auto_filter.ref = ws.dimensions

# Wrap text
for row in ws.iter_rows(min_row=2):
    for cell in row:
        cell.alignment = Alignment(
            vertical="center",
            wrap_text=True
        )

# Save changes
wb.save(output_path)

print("Excel formatting completed!")
