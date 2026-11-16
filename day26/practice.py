from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

try:
    # start_button = wait.until(                # find the first "button" (not suitable)
    #     EC.element_to_be_clickable(
    #         (By.TAG_NAME, "button")
    #     )
    # )
    start_button = wait.until(                  # to target the specific start button
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#start button")
        )
    )
    start_button.click()



    finish = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "finish")
        )
    )

    print(finish.text)

except Exception as e:
    print("Problem with:", type(e).__name__)


finally:
    driver.quit()