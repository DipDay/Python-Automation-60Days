from bs4 import BeautifulSoup
import requests
import csv

url1 = 'https://books.toscrape.com/'            # sorry but only work on url1 :,)
# url2 = 'https://quotes.toscrape.com/'

num = 1
try:
    user_url = input("Enter URL: ")
    pages = int(input("Enter number of pages: "))
    file_n = input("Enter output filename: ")
    file_name = f"e:\\Code\\Python-Automation-60Days\\day15\\{file_n}.csv"

    # print(user_url[-1])

    def scrape_page(soup):
        for book in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):

            try:
                book_name = book.find('h3').text
                book_price = book.find('p', class_='price_color').text
                availability = book.find('p', class_='instock availability').text.strip()

            except Exception:
                book_name = None
                book_price = None
                availability = []

            print(book_name)
            csv_writer.writerow({'book_name': book_name, 'book_price': book_price, 'availability': availability})

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        field_names = ['book_name', 'book_price', 'availability']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names)

        csv_writer.writeheader()

        while(num<=pages):
            try:
                if user_url[-1] == "/":
                    url = f"{user_url}catalogue/page-{num}.html"
                else:
                    url = f"{user_url}/catalogue/page-{num}.html"

                r = requests.get(url)
                r.encoding = 'utf-8'                              
                soup = BeautifulSoup(r.text, 'lxml')
                scrape_page(soup)
                num += 1

            except requests.exceptions.MissingSchema:
                print("Invalid URL...")
                break
            except Exception as e:
                print(f'Something Wrong!! Error: {e}')
                break


except ValueError:
    print("Invalid Number!!")
except Exception:
    print("Something Wrong!!")

    

    