from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
output_path = BASE_DIR / "Products_Report.xlsx"

num = int(input("How many pages: "))
keyword = input("Enter product keyword: ").strip().lower()

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

all_products = []

try:
    driver.get("https://www.scrapingcourse.com/ecommerce/")
    for i in range(num):
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

            # Filter
            if keyword not in title.lower():
                continue

            raw_price = product.find_element(
                By.CSS_SELECTOR,
                ".price"
            ).text

            price = float(raw_price.replace("$", "").strip())

            product_url = product.find_element(
                By.CSS_SELECTOR,
                # "a"
                "a.woocommerce-loop-product__link"
            )

            product_data = {
                "Title": title,
                "Price": price,
                "Url": product_url.get_attribute("href")
            }
            all_products.append(product_data)

        # Next button
        next_links = driver.find_elements(
            By.CSS_SELECTOR,
            "a.next"
        )
        if not next_links or i==(num-1):
            print("No more pages!")
            break

        current_url = driver.current_url

        next_links[0].click()

        wait.until(EC.url_changes(current_url))

    print("Total Products:", len(all_products))


    # Save Excel
    if not all_products:
        df = pd.DataFrame({"Title": ["No Product Found!"], "Price": [""], "Url": [""]})
    else:
        df = pd.DataFrame(all_products, columns=["Title", "Price", "Url"])

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            sheet_name="All Products",
            index=False
        )

    print("Excel file created successfully!")

except Exception as e:
    print(f"Something went wrong: {e}")

finally:
    driver.quit()
