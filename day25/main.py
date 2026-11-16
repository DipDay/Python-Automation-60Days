from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

element = driver.find_element(By.ID, "my-text-id")
time.sleep(1)

# send_keys()
element.send_keys("Dip Day")
time.sleep(2)

# clear()
element.clear()
element.send_keys("Python Automation")
time.sleep(2)

# click() - Button
button = driver.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(2)

driver.back()
time.sleep(2)

# get_attribute() - Input
element = driver.find_element(By.NAME, "my-readonly")
print(element.get_attribute("value"))
time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button")
print(button.text)
time.sleep(2)

# Explicit Wait
wait = WebDriverWait(driver, 10)

# element = wait.until(
#     EC.visibility_of_element_located(
#         (By.ID, "my-text-id")
#     )
# )
button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button")
    )
)
button.click()

driver.quit()