from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    RESULTS = (By.CSS_SELECTOR, ".product-layout")
    NO_RESULTS = (By.XPATH, "//*[contains(text(),'There is no product')]")

    def __init__(self, driver):
        self.driver = driver

    def has_results(self):
        return len(self.driver.find_elements(*self.RESULTS)) > 0

    def has_no_results_message(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.NO_RESULTS)
            ).is_displayed()
        except Exception:
            return False
