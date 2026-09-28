from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import logger
import csv


def login(driver):

    try:
        # Check if user is already logged in
        logout_button = driver.find_elements(
            By.PARTIAL_LINK_TEXT,
            "Logout"
        )

        if logout_button:
            logger.info("User is already logged in. Login skipped.")
            return

        logger.info("User is not logged in. Starting login process")

        # Read login data
        with open("testdata.csv", "r") as file:
            data = csv.DictReader(file)
            test_data = next(data)

        email = test_data["email"]
        password = test_data["password"]

        logger.info("Login data loaded from CSV")

        # Open Signup / Login page
        signup_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, "Signup / Login")
            )
        )

        signup_login.click()

        logger.info("Signup / Login clicked")

        # Enter Email
        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[data-qa='login-email']")
            )
        )

        email_field.send_keys(email)

        # Enter Password
        password_field = driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='login-password']"
        )

        password_field.send_keys(password)

        logger.info("Login credentials entered")

        # Click Login
        login_button = driver.find_element(
            By.CSS_SELECTOR,
            "button[data-qa='login-button']"
        )

        login_button.click()

        logger.info("Login button clicked")

        # Verify login
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(), 'Logged in as')]"
                )
            )
        )

        logger.info("Login successful")

    except Exception as e:
        logger.error("Login failed: %s", e)
        raise