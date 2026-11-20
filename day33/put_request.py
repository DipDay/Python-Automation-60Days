import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

updated_post = {
    "id": 1,
    "title": "Learning Python Automation",
    "body": "I am learning REST API with Python.",
    "userId": 1
}

response = requests.put(url, json=updated_post)

print(response.status_code)
print(response.json())