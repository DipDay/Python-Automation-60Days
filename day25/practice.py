import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)

try:
    wait = WebDriverWait(driver, 10)

    element = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "my-text-id")
        )
    )
    element.send_keys("Python Automation Tutorial")
    element.send_keys(Keys.ENTER)
    # time.sleep(5)

    # Wait for submission
    wait.until(
        EC.url_contains("submitted-form.html")
    )

    print("Form Submitted Successfully!")
    print("Current URL:", driver.current_url)


finally:
    driver.quit()
