from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    driver.get(
        "https://www.selenium.dev/selenium/web/web-form.html"
    )

    wait = WebDriverWait(driver, 10)

    # Find text input
    text_box = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "my-text-id")
        )
    )

    # Enter text
    text_box.send_keys("Dip Day")

    # Read input value
    print("Entered Text:", text_box.get_attribute("value"))

    # Clear input
    text_box.clear()

    print("After Clear:", text_box.get_attribute("value"))

    # Enter new text
    text_box.send_keys("Python Automation")

    print("New Text:", text_box.get_attribute("value"))

    # Find textarea
    textarea = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "my-textarea")
        )
    )

    textarea.send_keys("Learning Selenium Day 25")

    print("Textarea:", textarea.get_attribute("value"))

    # Find submit button
    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button")
        )
    )

    print("Button:", submit_button.text)

    # Click submit
    submit_button.click()

    # Wait for submission result
    wait.until(
        EC.url_contains("submitted-form.html")
    )

    print("Form Submitted Successfully!")
    print("Current URL:", driver.current_url)

finally:
    driver.quit()
