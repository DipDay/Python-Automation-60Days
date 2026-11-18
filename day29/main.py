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

driver.get("https://www.scrapingcourse.com/ecommerce/")

products = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "li.product")
        # (By.CSS_SELECTOR, "li.type-product")
    )
)

all_products = []

for product in products:

    title = product.find_element(
        By.CSS_SELECTOR,
        # ".woocommerce-loop-product__title"
        ".product-name"
    ).text

    price = product.find_element(
        By.CSS_SELECTOR,
        ".price"
    ).text

    # print("Product:", title)
    # print("Price:", price)
    # print("-" * 30)

    product_data = {
        "title": title,
        "price": price
    }
    all_products.append(product_data)

print(all_products)

# Save CSV
with open(output_path, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["title", "price"]
    )

    writer.writeheader()
    writer.writerows(all_products)

print("CSV file created successfully!")


driver.quit()
