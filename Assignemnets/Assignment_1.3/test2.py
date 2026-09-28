from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("https://testautomationpractice.blogspot.com/")

    # CSS selector using ID
    name = driver.find_element(By.CSS_SELECTOR, "#name")
    print("ID selector:", name.get_attribute("placeholder"))

    #  CSS selector using class
    counter = driver.find_element(By.CSS_SELECTOR, ".counter-wrapper")
    print("Class selector:", counter.get_attribute("textContent"))

    #CSS attribute selector
    phone = driver.find_element(
        By.CSS_SELECTOR,
        'input[placeholder="Enter Phone"]'
    )
    print("Attribute selector:", phone.get_attribute("id"))

    stats = driver.find_element(
        By.CSS_SELECTOR, '[id^="Stats1_"]'
    )
    print("Starts with (^=):", stats.get_attribute("id"))
    stats_contains = driver.find_element(By.CSS_SELECTOR,'[id*="Stats1"]'
    )
    print("Contains (*=):", stats_contains.get_attribute("id"))

    total = driver.find_element(
        By.CSS_SELECTOR, '[id$="totalCount"]'
    )
    print("Ends with ($=):", total.get_attribute("id"))

finally:
    driver.quit()