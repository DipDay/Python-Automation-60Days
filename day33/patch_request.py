import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

updated_data = {
    "title": "Changing only the title"
}

response = requests.patch(url, json=updated_data)

print(response.status_code)
print(response.json())