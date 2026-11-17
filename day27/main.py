from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

# Dropdown Automation
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = wait.until(
    EC.presence_of_element_located(
        (By.ID, "dropdown")
    )
)
select = Select(dropdown)
select.select_by_visible_text("Option 2")
print(select.first_selected_option.text)


# # Checkbox Automation
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "input[type='checkbox']")
    )
)

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
    print(checkbox.is_selected())


# Button Automation
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# add_button = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[text()='Add Element']")
#     )
# )

add_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[onclick='addElement()']")
    )
)

add_button.click()

delete_button = wait.until(
    EC.element_to_be_clickable(
        (By.CLASS_NAME, "added-manually")
    )
)
delete_button.click()

print("Button automation successful!")

driver.quit()