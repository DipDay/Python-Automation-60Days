from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 1.ID Locator
element = driver.find_element(By.ID, "my-text-id")
# 2.NAME Locator
element = driver.find_element(By.NAME, "my-text")
# 3.CLASS_NAME Locator
element = driver.find_element(By.CLASS_NAME, "form-control")


# 4.TAG_NAME Locator
elements = driver.find_elements(By.TAG_NAME, "input")
print(len(elements))
# print(elements)     # element's list


# 5.CSS_SELECTOR Locator
element = driver.find_element(By.CSS_SELECTOR, "#my-text-id")                   # ID
element = driver.find_element(By.CSS_SELECTOR, ".form-control")                 # Class
element = driver.find_element(By.CSS_SELECTOR, "input#my-text-id")              # Tag & ID
element = driver.find_element(By.CSS_SELECTOR, "input[name='my-text']")         # Attribute


# 6.XPATH Locator
element = driver.find_element(By.XPATH, "//input[@id='my-text-id']")            # ID
element = driver.find_element(By.XPATH, "//input[@name='my-text']")             # Name (Attribute)
element = driver.find_element(By.XPATH, "//input")                              # Tag
element = driver.find_element(By.XPATH, "//button[text()='Submit']")            # Using text


print(element)

driver.quit()