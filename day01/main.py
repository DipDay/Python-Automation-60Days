import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

print("API-requesting...")

response = requests.get(url)

if response.status_code == 200:
    print("Data collected successfully!\n")
    data = response.json()
    print(f"Task Title: {data.get('title')}")
    print(f"Completed Status: {data.get('completed')}")
    print(f"User ID: {data.get('userId')}")
else:
    print(f"Problem detected! Status Code: {response.status_code}")