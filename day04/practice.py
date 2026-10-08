import requests

url = "https://www.scrapethissite.com/pages/forms/"

r = requests.get(url)
print(r.text)