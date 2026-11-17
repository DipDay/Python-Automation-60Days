from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pages = int(input("How many pages: "))

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/index.html")
wait = WebDriverWait(driver, 10)

for page in range(pages):

    # Multiple Pages and Data Extraction

    # Method 1
    books = driver.find_elements(
        By.CSS_SELECTOR,
        "article.product_pod h3 a",
    )

    # Method 2
    # books = driver.find_elements(
    #     By.XPATH,
    #     "//article[@class='product_pod']//h3/a"
    # )

    for book in books:
        print(book.get_attribute("title"))  # Full name in the title
        # print(book.text)


    # Next Button
    old_url = driver.current_url

    next_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.next a"))
    )

    if page < (pages - 1):
        next_button.click()

        wait.until(EC.url_changes(old_url))

    # print("Current url:", driver.current_url)

driver.quit()