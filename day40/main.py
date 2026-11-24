import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

# user_input = input("You: ")
user_input = [
    "My order arrived broken.",
    "How can I get a refund?",
    "Your service is amazing!",
    "I want to purchase a new laptop.",
    "What are your opening hours?",
    "I received the wrong product.",
    "The delivery was very fast!"
]

output_path = "E:\\Code\\Python-Automation-60Days\\day40\\classification result.xlsx"

def format_excel(file_path):
    wb = load_workbook(file_path)
    ws = wb.active

    # Header styling (Bold, Center Alignment, Background Color)
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment

    # Data cells styling (Text wrap + vertical alignment)
    data_alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        for cell in row:
            cell.alignment = data_alignment

    # Auto-adjust column width (with max width cap so long texts don't break layout)
    for col in ws.columns:
        col_letter = col[0].column_letter
        max_len = 0

        for cell in col:
            val_str = str(cell.value) if cell.value is not None else ""
            longest_line = max((len(line) for line in val_str.splitlines()), default=0)
            if longest_line > max_len:
                max_len = longest_line

        adjusted_width = min(max(max_len + 5, 15), 60)
        ws.column_dimensions[col_letter].width = adjusted_width

    wb.save(file_path)


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

results = {}

for user_message in user_input:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
            {
                "role": "system",
                "content": """
                You are a text classification assistant.

                Classify the user's message into one or more relevant categories.
                1. Complaint
                2. Inquiry
                3. Feedback
                4. Order

                Return all relevant category names, separated by commas.
                If no category matches, return "Other".
                Do not provide any explanation.
                """
            },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0
        )
        # print("Message:", user_message)
        # print("Category:", response.choices[0].message.content)
        # print("-" * 40)

        results[user_message] = response.choices[0].message.content.strip()

    except Exception as e:
        results[user_message] = f"Error: {e}"
        print("Error: ", e)

print(results)

df = pd.DataFrame(list(results.items()), columns=["Message", "Category"])
df.to_excel(output_path, index=False)

format_excel(output_path)
