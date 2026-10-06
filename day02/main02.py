import requests

# url = "https://xkcd.com/353/"
# url = "https://imgs.xkcd.com/comics/python.png"
# r = requests.get(url)

# print(r.text)
# with open("comic.png", "wb") as f:
#     f.write(r.content)

# payload ={'page': 2, 'count': 25}
# r = requests.get("https://httpbin.org/get", params=payload)
# print(r.text)
# print(r.url)

# payload ={'username': 'Dip', 'password': 'test123'}
# r = requests.post("https://httpbin.org/post", data=payload)
# # print(r.text)
# # print(r.json())

# r_dict = r.json()
# print(r_dict['form'])
# print(r_dict['origin'])

# r = requests.get('https://httpbin.org/basic-auth/dip/test123', auth=('dip', 'test123'))
# print(r.text)


r = requests.get('https://httpbin.org/delay/3', timeout=4)
print(r)