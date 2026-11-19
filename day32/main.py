from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from selenium.common.exceptions import WebDriverException

BASE_DIR = Path(__file__).resolve().parent
output_path = BASE_DIR / "products.xlsx"


def input_keyword():
    # Keep asking until the user provides a non-empty search keyword.
    while True:
        keyword = input("Enter keyword: ").strip().lower()

        if not keyword:
            print("Give a valid input!")
            continue
        return keyword


def input_page_num():
    # Accept zero for all pages, or a positive number to limit the scrape.
    while True:
        try:
            page_num = int(input("Enter number of pages (0 for all): "))

            if page_num < 0:
                print("Give a positive number!")
                continue

            return page_num

        except ValueError:
            print("Invalid input! Give a number.")


# Collect the user's filters before opening the browser.
keyword = input_keyword()
page_num = input_page_num()
driver = None



all_products = []
seen_urls = set()

try:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.scrapingcourse.com/ecommerce/")

    # Track progress and prevent the same product from being saved twice.
    pages_scraped = 0
    repeated_products = 0

    while True:
        products = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "li.product")
            )
        )

        # Inspect each product on the current page and keep matching items.
        for product in products:
            title = product.find_element(
                By.CSS_SELECTOR, ".product-name"
            ).text

            if keyword not in title.lower():
                continue

            raw_price = product.find_element(
                By.CSS_SELECTOR, ".price"
            ).text

            price = float(raw_price.replace("$", "").strip())

            product_url = product.find_element(
                By.CSS_SELECTOR,
                "a.woocommerce-loop-product__link",
            ).get_attribute("href")

            if product_url in seen_urls:
                repeated_products += 1
                continue

            seen_urls.add(product_url)

            # Store a consistent record so it can be written to Excel later.
            product_data = {
                "Product": title,
                "Price": price,
                "URL": product_url,
                "Keyword": keyword
            }

            all_products.append(product_data)

        pages_scraped += 1

        next_links = driver.find_elements(By.CSS_SELECTOR, "a.next")

        if not next_links:
            print("No more pages!")
            break

        if page_num != 0 and pages_scraped >= page_num:
            break

        current_url = driver.current_url
        next_links[0].click()

        wait.until(EC.url_changes(current_url))

    print("Total Products:", len(all_products))

    # Create a compact summary sheet for the scraping run.
    summary = pd.DataFrame({
        "Metric": [
            "Page Visited",
            "Repeat Products Removed",
            "Total product"
        ],
        "Value": [
            pages_scraped,
            repeated_products,
            len(all_products)
        ]
    })

    # Use a placeholder row when no products matched the keyword.
    if not all_products:
        df = pd.DataFrame({
            "Product": ["No Product Found!"],
            "Price": [""],
            "URL": [""],
            "Keyword": [keyword],
        })
    else:
        df = pd.DataFrame(all_products, columns=["Product", "Price", "URL", "Keyword"])

    # Write both the detailed product list and the run summary to one workbook.
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(
            writer,
            sheet_name="All Products",
            index=False
        )
        summary.to_excel(
            writer,
            sheet_name="Summary",
            index=False,
        )

        # Freeze the header and size each column to fit its longest value.
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            worksheet.freeze_panes = "A2"
            for col in worksheet.columns:
                max_length = 0
                col_letter = get_column_letter(col[0].column)

                for cell in col:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))

                worksheet.column_dimensions[col_letter].width = max_length + 2

    # Reopen the workbook so openpyxl can apply Excel-specific formatting.
    wb = load_workbook(output_path)
    ws = wb["All Products"]

    # Display numeric prices with a dollar sign and two decimal places.
    for cell in ws["B"][1:]:
        if isinstance(cell.value, (int, float)):
            cell.number_format = '$#,##0.00'

    ws.auto_filter.ref = ws.dimensions

    # Apply the same readable header style to every worksheet.
    for sheet in wb.worksheets:
        for cell in sheet[1]:
            cell.font = Font(
                bold=True,
                color="FFFFFF",
            )

            cell.fill = PatternFill(
                fill_type="solid",
                fgColor="1565C0",
            )

            cell.alignment = Alignment(
                horizontal="center",
            )

    # Save the completed workbook to the configured output path.
    wb.save(output_path)

    print("Excel file created successfully!")

except WebDriverException as e:
    if "ERR_INTERNET_DISCONNECTED" in str(e):
        print("No Internet Connection!")
    else:
        print(f"Something went wrong: {e}")

except Exception as e:
    print(f"Something went wrong: {e}")

finally:
    if driver is not None:
        driver.quit()
