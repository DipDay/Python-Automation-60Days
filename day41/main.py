import os
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

file_path = "day41/reviews.xlsx"

df = pd.read_excel(file_path)

# print(df)
# print(type(df))
# print(df.columns)
# print(len(df))

# for index, row in df.iterrows():
#     print("ID no:", row["ID"])
#     print("Customer Review:", row["Review"])
#     print('-' * 40)

# review = df.loc[0, "Review"]

def analyze_review(review):

    prompt = f"""
    Analyze this customer review:

    {review}

    Return JSON with:
    - category
    - sentiment (Positive, Negative, Neutral)
    - summary
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a customer review analyzer. Return only valid JSON."
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

for index, row in df.iterrows():

    review = row["Review"]

    result = analyze_review(review)

    results.append({
        "ID": row["ID"],
        "Review": review,
        "Category": result["category"],
        "Sentiment": result["sentiment"],
        "Summary": result["summary"]
    })

    print(f"Completed: {row['ID']}")

new_df = pd.DataFrame(results)

print(new_df)

output_path = "day41/new.xlsx"

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