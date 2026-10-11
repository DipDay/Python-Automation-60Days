from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://python.org/')

# print(r.text)
# print(r.html.links)
# print(r.html.absolute_links)
about = r.html.find('#about', first=True)
print(about.text)