from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pages = int(input("How many pages: "))

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

all_books = []
all_prices = []

try:
    driver.get("https://books.toscrape.com/index.html")

    for page in range(pages):
        wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "article.product_pod")
            )
        )

        book_items = driver.find_elements(
            By.CSS_SELECTOR,
            "article.product_pod",
        )

        for item in book_items:
            name = item.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            price = item.find_element(By.CSS_SELECTOR, "p.price_color").text

            all_books.append(name)
            all_prices.append(price)

        if page < pages - 1:
            old_url = driver.current_url
            next_buttons = driver.find_elements(By.CSS_SELECTOR, "li.next a")

            if not next_buttons:
                break

            next_buttons[0].click()
            wait.until(EC.url_changes(old_url))

    for book, price in zip(all_books, all_prices):
        print("Book Name:", book)
        print("Price:", price)
        print("-" * 30)

    print("Total books:", len(all_books))
finally:
    driver.quit()