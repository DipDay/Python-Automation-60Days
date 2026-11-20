import requests
import json

output_path = "E:\\Code\\Python-Automation-60Days\\day33\\filtered_posts.json"
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,
}

response = requests.get(url, params=params)

if response.status_code == 200:
    filtered_posts = response.json()

    print("Total Filtered Posts:", len(filtered_posts))

    with open(output_path, "w") as file:
        json.dump(filtered_posts, file, indent=4)

    print("Successful!")

else:
    print("Something wrong!")
