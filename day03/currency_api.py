import json
import requests

url = "https://open.er-api.com/v6/latest/USD"

r = requests.get(url)

# print(r.text)

data = json.loads(r.text)
# print(json.dumps(data, indent=2))
# print(len(data['rates']))

for name, price in data['rates'].items():
    print(name, price)
