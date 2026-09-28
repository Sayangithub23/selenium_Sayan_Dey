import csv
import os
import unittest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.driver_factory import create_driver
from utils.screenshot import take_screenshot

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://tutorialsninja.com/demo/")

    def tearDown(self):
        result = getattr(self._outcome, "result", None)
        if result and (getattr(result, "errors", []) or getattr(result, "failures", [])):
            take_screenshot(self.driver, self.id().split(".")[-1])

    def test_invalid_login(self):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "login_data.csv")
        with open(path, newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))

        home = HomePage(self.driver)
        login = LoginPage(self.driver)

        for row in rows:
            home.click_login()
            login.login(row["email"], row["password"])
            self.assertTrue(login.is_login_error_displayed())
            self.driver.get("https://tutorialsninja.com/demo/")
