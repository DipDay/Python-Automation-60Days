from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://books.toscrape.com/")

all_books = []

for page in range(3):

    books = driver.find_elements(
        By.CSS_SELECTOR,
        "article.product_pod h3 a"
    )

    for book in books:
        all_books.append(book.get_attribute("title"))

    print(f"Page {page + 1} completed!")

    if page < 2:
        old_url = driver.current_url

        next_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "li.next a")
            )
        )

        next_button.click()

        wait.until(
            EC.url_changes(old_url)
        )

print("Total books:", len(all_books))

for book in all_books:
    print(book)

driver.quit()