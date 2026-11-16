from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 20)

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    print("Website opened!")

    start_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#start button")
        )
    )

    start_button.click()
    print("Start button clicked!")

    finish = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "finish")
        )
    )

    print("Text found:", finish.text)

except TimeoutException as e:
    print("Timeout occurred!")
    print("Current URL:", driver.current_url)
    print("Error:", e)

except Exception as e:
    print("Other error:", type(e).__name__, e)

finally:
    driver.quit()