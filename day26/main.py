from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 7)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

try:
    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "my-text-id")
        )
    )

    username.send_keys("dip")

    password = driver.find_element(By.NAME, "my-password")
    password.send_keys("123456")

    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.TAG_NAME, "button")
        )
    )

    submit_button.click()

    wait.until(
        EC.url_contains("submitted-form.html")
    )

    print("Submit Successful!")

except Exception as e:
    print("Problem with:", type(e).__name__)


finally:
    driver.quit()