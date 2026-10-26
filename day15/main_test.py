from bs4 import BeautifulSoup
import requests
import csv

num = 1
# url1 = 'https://books.toscrape.com/'
# url2 = 'https://quotes.toscrape.com/'
try:
    user_url = input("Enter URL: ")
    pages = int(input("Enter number of pages: "))
    file_n = input("Enter output filename: ")
    file_name = f"e:\\Code\\Python-Automation-60Days\\day15\\{file_n}.csv"              # csv file path

    if pages <= 0:
        print("Number of pages must be greater than zero.")
        raise SystemExit
    
    def scrape_page(soup, csv_writer):
        for book in soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
            try:
                book_name = book.find('h3').text.strip()
                book_price = book.find('p', class_='price_color').text.strip()
                availability = book.find('p', class_='instock availability').text.strip()
            except Exception:
                book_name = None
                book_price = None
                availability = None

            print(book_name)
            csv_writer.writerow({
                'book_name': book_name, 
                'book_price': book_price, 
                'availability': availability
            })

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        field_names = ['book_name', 'book_price', 'availability']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names)
        csv_writer.writeheader()

        while num <= pages:
            try:
                if user_url.endswith("/"):
                    url = f"{user_url}catalogue/page-{num}.html"
                else:
                    url = f"{user_url}/catalogue/page-{num}.html"

                r = requests.get(url, timeout=10)
                r.raise_for_status()
                r.encoding = 'utf-8'                           
                soup = BeautifulSoup(r.text, 'lxml')
                
                scrape_page(soup, csv_writer)
                num += 1

            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                break
            except Exception as e:
                print(f"Something Wrong!! Error: {e}")
                break

except ValueError:
    print("Invalid Number!! Please enter a valid integer for pages.")
except Exception as e:
    print(f"Something Wrong!! Error: {e}")