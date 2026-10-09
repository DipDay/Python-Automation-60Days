from bs4 import BeautifulSoup
import requests
import csv

# with open('E:/Code/Python-Automation-60Days/day05/simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup)
# print(soup.prettify())

# match = soup.title.text
# print(match)

# match = soup.find('div', class_='footer')
# print(match)
 
# for article in soup.find_all('div', class_='article'):
#     # print(article)
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)
#     print()

source = requests.get('https://quotes.toscrape.com/').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

csv_file = open('E:/Code/Python-Automation-60Days/day05/quote.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quote', 'Author', 'Tags'])

for quote in soup.find_all('div', class_='quote'):

    try:
        quote_line = quote.find('span', class_='text').text
        quote_author = quote.find('small', class_='author').text
        quote_tags = quote.find_all('a', class_='tag')

    except Exception:
        quote_line = None
        quote_author = None
        quote_tags = []

    print(quote_line)
    print(f'Quote by: {quote_author}')

    tag_list = []
    for tag in quote_tags:
        tag_list.append(tag.text)

    all_tags = ", ".join(tag_list)
    print(f'Tags: {all_tags}')
    print()

    csv_writer.writerow([quote_line, quote_author, all_tags])

csv_file.close()