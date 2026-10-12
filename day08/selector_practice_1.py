import requests
from bs4 import BeautifulSoup

r = requests.get('https://books.toscrape.com/')
r.encoding = 'utf-8'                                # just to make all the symbole and chracter perfect 
soup = BeautifulSoup(r.text, 'lxml')
book_cards = soup.select('article.product_pod')

for book in book_cards:
  title = book.select_one('h3 a').text
  price = book.select_one('p.price_color').text
  img = book.select_one('div.image_container img')
  stock = book.select_one('p.instock.availability').text.strip()
  image_url = img.attrs['src']

  print(f'Books Name: {title}')
  print(f'Price: {price}')
  print(f'Cover Page Link: https://books.toscrape.com/{image_url}')
  print(f'Availability: {stock}')
  print()

