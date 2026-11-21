import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found!")

url = "https://httpbin.org/bearer"

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    # response = requests.get(url)

    if response.status_code == 200:
        print(response.status_code)
        print("Authentication successful!")
        print(response.json())

    elif response.status_code == 401:
        print(response.status_code)
        print("Authentication failed!")

    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)