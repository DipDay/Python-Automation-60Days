from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

time.sleep(2)

# ID Locator
element1 = driver.find_element(By.ID, "my-text-id")
print("ID:", element1.get_attribute("id"))

# NAME Locator
element2 = driver.find_element(By.NAME, "my-text")
print("NAME:", element2.get_attribute("name"))

# CLASS_NAME Locator
element3 = driver.find_element(By.CLASS_NAME, "form-control")
print("CLASS:", element3.get_attribute("class"))

# TAG_NAME Locator
element4 = driver.find_element(By.TAG_NAME, "input")
print("TAG:", element4.tag_name)

# CSS_SELECTOR Locator
element5 = driver.find_element(
    By.CSS_SELECTOR, "input#my-text-id"
)
print("CSS:", element5.get_attribute("id"))

# XPATH Locator
element6 = driver.find_element(
    By.XPATH, "//input[@id='my-text-id']"
)
print("XPATH:", element6.get_attribute("id"))

# Find multiple elements
elements = driver.find_elements(By.TAG_NAME, "input")
print("Total Input Elements:", len(elements))

time.sleep(5)

driver.quit()