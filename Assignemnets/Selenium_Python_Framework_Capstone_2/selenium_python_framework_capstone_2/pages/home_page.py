from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    MY_ACCOUNT = (By.XPATH, "//span[contains(text(),'My Account')]")
    REGISTER = (By.LINK_TEXT, "Register")
    LOGIN = (By.LINK_TEXT, "Login")
    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MY_ACCOUNT)
        ).click()

    def click_register(self):
        self.click_my_account()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REGISTER)
        ).click()

    def click_login(self):
        self.click_my_account()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN)
        ).click()

    def search(self, text):
        box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        box.clear()
        box.send_keys(text)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
