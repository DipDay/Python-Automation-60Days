from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.scrapingcourse.com/ecommerce/")

try:
    products = wait.until(
        EC.presence_of_all_elements_located(
            # (By.CLASS_NAME, "product-item")       # wrong
            (By.CSS_SELECTOR, ".product")
            # (By.CSS_SELECTOR, "li.product")
        )
    )
    
    # driver.save_screenshot("E:\\Code\\Python-Automation-60Days\\day31\\debug.png")         # Take Screenshot

    print("Total Products:", len(products))

except Exception as e:
    print("Something wrong:", e)

finally:
    driver.quit()