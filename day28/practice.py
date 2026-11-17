from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pandas as pd
import openpyxl

BASE_DIR = Path(__file__).resolve().parent
output_path = BASE_DIR / "books_report.xlsx"

pages = int(input("How many pages: "))

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/index.html")
wait = WebDriverWait(driver, 10)

all_books = []
all_prices = []

for page in range(pages):

    # Multiple Pages and Data Extraction

    books = driver.find_elements(
        By.CSS_SELECTOR,
        "article.product_pod h3 a",
    )

    prices = driver.find_elements(
        By.CSS_SELECTOR,
        "article.product_pod .price_color"
    )

    for book in books:
        all_books.append(book.get_attribute("title"))

    for price in prices:
        all_prices.append(price.text)

    print(f"Page {page + 1} completed!")


    # Next Button
    if page < (pages - 1):

        old_url = driver.current_url

        next_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "li.next a")
            )
        )

        next_button.click()

        wait.until(EC.url_changes(old_url))

    # print("Current url:", driver.current_url)

print("Total books:", len(all_books))

data = pd.DataFrame({"Book Name":all_books, "Price": all_prices})

for item in range(len(all_books)):
    print("Book Name: ", all_books[item])
    print("Price: ", all_prices[item])

# # Using zip()
# for book, price in zip(books, prices):
#     print("Book Name:", book.get_attribute("title"))
#     print("Price:", price.text)

with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    data.to_excel(
        writer,
        sheet_name="All Books",
        index=False
    )

driver.quit()