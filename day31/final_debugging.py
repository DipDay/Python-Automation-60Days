from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
    InvalidSelectorException
)

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get("https://www.scrapingcourse.com/ecommerce/")

# TASK 01: NoSuchElementException
try:
    products = driver.find_element(By.CLASS_NAME, "form-control")

except NoSuchElementException:
    print("[ERROR] Element not found!")


# TASK 02: TimeoutException + Screenshot
try:
    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-item")
        )
    )
except TimeoutException:
    print("[ERROR] Timeout occurred!")
    driver.save_screenshot("E:\\Code\\Python-Automation-60Days\\day31\\debug_timeout01.png")
    print("Screenshot Saved!")


# TASK 03: StaleElementReferenceException
try:
    product = driver.find_element(
        By.CSS_SELECTOR,
        "h2.product-name"
    )

    driver.refresh()

    print(product.text)

except StaleElementReferenceException:
    print("[ERROR] Element is stale!")
    products = driver.find_elements(
        By.CSS_SELECTOR,
        "h2.product-name"
    )

    print("New element located!")

    for product in products:
        print(product.text)


# TASK 04: InvalidSelectorException
try:
    product = driver.find_element(
        By.CSS_SELECTOR,
        "h2.product-name["
    )

except InvalidSelectorException:
    print("[ERROR] Invalid CSS Selector!")


# TASK 05: Collect all products
products = driver.find_elements(
    By.CSS_SELECTOR,
    "h2.product-name"
)

for product in products:
    print(product.text)

print("Total Products:", len(products))

driver.quit()
