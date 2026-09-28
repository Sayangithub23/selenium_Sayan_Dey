from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    ACCOUNT_HEADING = (By.XPATH, "//h2[contains(text(),'My Account')]")
    WARNING = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.ACCOUNT_HEADING)
            )
            return True
        except Exception:
            return False

    def is_login_error_displayed(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.WARNING)
            ).is_displayed()
        except Exception:
            return False
