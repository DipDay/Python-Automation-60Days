import requests

url = "https://www.prothomalo.com/"
r = requests.get(url)
print(r.text)

with open('test_main03.txt', 'w', encoding='utf-8') as f:       # adding (encoding='utf-8') for Bangla text
    f.write(r.text)
print("Txt file writing is done!")

# print(r.status_code)
# print(r.headers)