import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Answer in simple language."
    }
]

print("=" * 45)
print("             PYTHON AI CHATBOT")
print("=" * 45)
print("Ask me anything!")
print("Type 'exit' to quit.")
print("-" * 45)

while True:
    user_input = input("\nYou: ").strip()

    if not user_input:
        continue

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    try:
        messages.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )

        ai_reply = response.choices[0].message.content

        print()
        print("Chatbot:", ai_reply)
        print("=" * 95)


        messages.append({
            "role": "assistant",
            "content": ai_reply
        })

    except Exception as e:
        messages.pop()
        print("Error: ", e)