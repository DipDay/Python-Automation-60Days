from requests_html import HTMLSession
# Beautifulsoup >> requests_html , so 'selector_practice_1.py' more recomended!

s = HTMLSession()
r = s.get('https://books.toscrape.com/')

book_cards = r.html.find('article.product_pod')

for book in book_cards:
  title = book.find('h3 a', first=True).text
  price = book.find('p.price_color', first=True).text
  img = book.find('div.image_container img', first=True)
  stock = book.find('p.instock.availability', first=True).text
  image_url = img.attrs['src']

  print(f'Books Name: {title}')
  print(f'Price: {price}')
  print(f'Cover Page Link: https://books.toscrape.com/{image_url}')
  print(f'Availability: {stock}')
  print()


# images = r.html.find('div.image_container img')

# for img in images:
#   image_url = img.attrs['src']
#   print(f'Image link: https://books.toscrape.com/{image_url}')