from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent
output_path = BASE_DIR / "products.csv"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

all_products = []

driver.get("https://www.scrapingcourse.com/ecommerce/")

while True:

    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li.product")
        )
    )

    for product in products:

        title = product.find_element(
            By.CSS_SELECTOR,
            ".product-name"
        ).text

        price = product.find_element(
            By.CSS_SELECTOR,
            ".price"
        ).text

        product_data = {
            "title": title,
            "price": price
        }

        all_products.append(product_data)

    print("Scraped:", driver.current_url)

    next_links = driver.find_elements(
        By.CSS_SELECTOR,
        "a.next"
    )

    if not next_links:
        print("No more pages!")
        break

    current_url = driver.current_url

    next_links[0].click()

    wait.until(EC.url_changes(current_url))


print("Total Products:", len(all_products))

with open(output_path, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["title", "price"]
    )

    writer.writeheader()
    writer.writerows(all_products)

print("CSV file created successfully!")

driver.quit()
