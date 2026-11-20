import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,
    "id": 3
}

response = requests.get(url, params=params)

data = response.json()

print("Total Posts:", len(data))

for item in data:
    print("ID:", item["id"])
    print("Title:", item["title"])
    print()