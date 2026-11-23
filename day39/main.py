import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python teacher. Explain concepts in maximum 3 simple sentences. Always give one short example."
        },
        {
            "role": "user",
            "content": "What is a variable in Python?"
        }
    ]
)

# print(response)
print(response.choices[0].message.content)
