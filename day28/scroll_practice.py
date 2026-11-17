from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/infinite_scroll")
time.sleep(2)

# croll Down 500 pixels
driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)

# croll Up 500 pixels
driver.execute_script("window.scrollBy(0, -500);")
time.sleep(2)

# Scroll to Bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Scroll to Top
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)


driver.quit()