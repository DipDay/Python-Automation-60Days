from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()

driver.get("https://www.scrapingcourse.com/ecommerce/")

try:
    product = driver.find_element(
        By.CSS_SELECTOR,
        "h2.product-name"
    )

    name = product.text

    driver.refresh()

    print(product.text)

except StaleElementReferenceException:
    print("Element is stale!")

    product = driver.find_element(
        By.CSS_SELECTOR,
        "h2.product-name"
    )

    print("New Product:", product.text)

finally:
    driver.quit()