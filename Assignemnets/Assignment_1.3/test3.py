
# Identify and locate child/nested web elements using CSS child selectors and interact with
# the required elements.
# Example: Locate a button inside a specific div using a CSS child selector.



from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("https://testautomationpractice.blogspot.com/")
    button = driver.find_element(By.CSS_SELECTOR,
                                 "div.dropdown > button"
    )
    print("Button : ", button.text)
   

finally:
    driver.quit()