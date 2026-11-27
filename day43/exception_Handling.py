import os
from dotenv import load_dotenv
from openai import OpenAI
from openai import AuthenticationError, RateLimitError, APITimeoutError, APIConnectionError
import time
import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

file_path = "day43/reviews.xlsx"

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

    for attempt in range(max_retries):
        try:
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

            data = json.loads(response.choices[0].message.content)

            if len(data["results"]) != len(batch):
                raise ValueError("Mismatch between reviews and AI results")

            return data, response.usage

        except AuthenticationError:
            raise

        except (RateLimitError, APITimeoutError, APIConnectionError) as e:

            print(f"Attempt {attempt + 1} failed:", e)

            if attempt < max_retries - 1:
                retry_time = 2 ** (attempt + 1)
                print(f"Retrying in {retry_time} seconds...")
                time.sleep(retry_time)

            else:
                raise RuntimeError("Maximum retries reached!") from e

results = []
total_input_tokens = 0
total_output_tokens = 0
total_tokens = 0
max_retries = 3

client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
        max_retries=0
    )

df = pd.read_excel(file_path)

reviews = df["Review"].tolist()

batch_size = 10

total_batches = len(range(0, len(reviews), batch_size))

print("Total Reviews:", len(reviews))
print("Total Batches:", total_batches)

for batch_no, i in enumerate(range(0, len(reviews), batch_size), start=1):

    batch = reviews[i:i + batch_size]

    print(f"Processing Batch {batch_no}")

    data, usage = analyze_batch(batch)

    total_input_tokens += usage.prompt_tokens
    total_output_tokens += usage.completion_tokens
    total_tokens += usage.total_tokens

    print("Input Tokens:", usage.prompt_tokens)
    print("Output Tokens:", usage.completion_tokens)
    print("Total Tokens:", usage.total_tokens)

    batch_results = data["results"]
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
# Imagine Input: $0.10 / 1 million tokens & Output: $0.40 / 1 million tokens
input_cost = (total_input_tokens * 0.1) / 1000000
output_cost = (total_output_tokens * 0.4) / 1000000
total_cost = input_cost + output_cost

new_df = pd.DataFrame(results)

usage_df = pd.DataFrame({
    "Metric": [
        "Input Tokens",
        "Output Tokens",
        "Total Tokens",
        "Total Batches",
        "Estimated Cost (USD)"
    ],
    "Value": [
        total_input_tokens,
        total_output_tokens,
        total_tokens,
        total_batches,
        total_cost
    ]
})

print(new_df)
print("Total Input Tokens:", total_input_tokens)
print("Total Output Tokens:", total_output_tokens)
print("Total Tokens:", total_tokens)

output_path = "day43/new.xlsx"
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    new_df.to_excel(writer, sheet_name="Review Results", index=False)
    usage_df.to_excel(writer, sheet_name="Usage Report", index=False)

print("Excel file created successfully!")

wb = load_workbook(output_path)

for sheet in wb.worksheets:

    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions

    for cell in sheet[1]:
        cell.font = Font(
            bold=True,
            color="FFFFFF"
        )
        cell.fill = PatternFill(
            fill_type="solid",
            fgColor="1565C0"
        )
        cell.alignment = Alignment(
            horizontal="center",
            vertical="center"
        )

    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(
                vertical="center",
                wrap_text=True
            )

    for col in sheet.columns:
        max_length = 0
        col_letter = get_column_letter(col[0].column)

        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))

        sheet.column_dimensions[col_letter].width = min(max_length + 2, 65)

usage_sheet = wb["Usage Report"]

for row in range(2, usage_sheet.max_row + 1):
    if usage_sheet.cell(row=row, column=1).value == "Estimated Cost (USD)":
        usage_sheet.cell(row=row, column=2).number_format = '$0.000000'

wb.save(output_path)

print("Excel formatting completed!")
