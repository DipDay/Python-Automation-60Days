from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

driver.get("https://www.scrapingcourse.com/ecommerce/")

try:
    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "product-item")      
        )
    )

except TimeoutException as e:
    print("Time out error!", e)
    driver.save_screenshot("E:\\Code\\Python-Automation-60Days\\day31\\debug_timeout.png")
    print("Screenshot Saved!")
    
    print("Current URL:", driver.current_url)


finally:
    driver.quit()