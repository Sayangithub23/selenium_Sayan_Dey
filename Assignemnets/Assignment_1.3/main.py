from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("https://testautomationpractice.blogspot.com/")
    #BY ID
    phone  = driver.find_element(By.ID, "phone")
    print("By ID: ", phone.get_attribute("placeholder"))
    # BY NAME
    gender = driver.find_element(By.NAME, "gender")
    print("By Name: ", gender.get_attribute("value"))
    # By TAG
    links = driver.find_elements(By.TAG_NAME, "a")
    print("By TAG_NAME: Number of Links -> ", len(links))

    for link in links:
        print('Link: ', link.text)
    #BY LINK_TEXT
    apple = driver.find_element(By.LINK_TEXT, "Apple")
    print("By LINK_TEXT: ", apple.text)
    #BY CLASS_NAME
    visitor = driver.find_element(By.CLASS_NAME, "counter-wrapper")
    print("By.CLASS_NAME: ", visitor.get_attribute('textContent'))

finally:
    driver.quit()