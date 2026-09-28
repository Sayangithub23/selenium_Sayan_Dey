from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from logger import logger
import csv


def register(driver):

    # Read registration data
    try:
        with open("testdata.csv", "r") as file:

            data = csv.DictReader(file)
            test_data = next(data)

        name = test_data["name"]
        email = test_data["email"]
        password = test_data["password"]
        title = test_data["title"]

        birth_day = test_data["birth_day"]
        birth_month = test_data["birth_month"]
        birth_year = test_data["birth_year"]

        firstname = test_data["firstname"]
        lastname = test_data["lastname"]
        company = test_data["company"]

        address1 = test_data["address1"]
        address2 = test_data["address2"]

        country = test_data["country"]
        state = test_data["state"]
        city = test_data["city"]
        zipcode = test_data["zipcode"]
        mobile = test_data["mobile"]

        logger.info("Registration data loaded from CSV")

    except Exception as e:

        logger.error(
            "Failed to read registration data: %s",
            e
        )

        raise

    try:

        logger.info("Starting registration process")

       
        signup_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, "Signup / Login")
            )
        )

        # remove_ads(driver)

        signup_login.click()

        logger.info("Signup / Login clicked")

        # Enter Name
        name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "input[data-qa='signup-name']"
                )
            )
        )

        name_field.send_keys(name)

        # Enter Email
        email_field = driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='signup-email']"
        )

        email_field.send_keys(email)

        logger.info("Signup details entered")

        # Click Signup
        signup_button = driver.find_element(
            By.CSS_SELECTOR,
            "button[data-qa='signup-button']"
        )

        signup_button.click()

        logger.info("Signup button clicked")

        # Check Account Information page
        try:

            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "//b[contains(text(), 'Enter Account Information')]"
                    )
                )
            )

            logger.info("Account Information page opened")

        except Exception:

            logger.info(
                "Email already exists. Registration skipped."
            )

            return

        # Select Title
        

        if title == "Mr":

            driver.find_element(
                By.ID,
                "id_gender1"
            ).click()

        else:

            driver.find_element(
                By.ID,
                "id_gender2"
            ).click()

        logger.info(
            "Title selected: %s",
            title
        )

        # Password
        password_field = driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='password']"
        )

        password_field.send_keys(password)

        logger.info("Password entered")

        # Date of Birth
        Select(
            driver.find_element(
                By.CSS_SELECTOR,
                "select[data-qa='days']"
            )
        ).select_by_value(birth_day)

        Select(
            driver.find_element(
                By.CSS_SELECTOR,
                "select[data-qa='months']"
            )
        ).select_by_value(birth_month)

        Select(
            driver.find_element(
                By.CSS_SELECTOR,
                "select[data-qa='years']"
            )
        ).select_by_value(birth_year)

        logger.info("Date of birth selected")

        # Newsletter
        newsletter = driver.find_element(
            By.ID,
            "newsletter"
        )

        if not newsletter.is_selected():
            newsletter.click()

        logger.info("Newsletter option selected")

        # First Name
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='first_name']"
        ).send_keys(firstname)

        # Last Name
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='last_name']"
        ).send_keys(lastname)

        # Company
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='company']"
        ).send_keys(company)

        # Address 1
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='address']"
        ).send_keys(address1)

        # Address 2
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='address2']"
        ).send_keys(address2)

        # Country
        Select(
            driver.find_element(
                By.CSS_SELECTOR,
                "select[data-qa='country']"
            )
        ).select_by_visible_text(country)

        # State
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='state']"
        ).send_keys(state)

        # City
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='city']"
        ).send_keys(city)

        # Zipcode
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='zipcode']"
        ).send_keys(zipcode)

        # Mobile Number
        driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='mobile_number']"
        ).send_keys(mobile)

        logger.info("Address information entered")

        # Create Account
        create_account = driver.find_element(
            By.CSS_SELECTOR,
            "button[data-qa='create-account']"
        )

        # remove_ads(driver)

        create_account.click()

        logger.info("Create Account button clicked")

        # Verify Account Created
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//b[contains(text(), 'Account Created')]"
                )
            )
        )

        logger.info("Account created successfully")

        # Click Continue
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "a[data-qa='continue-button']"
                )
            )
        )

        # remove_ads(driver)

        continue_button.click()

        logger.info("Continue button clicked")

    except Exception as e:

        logger.error(
            "Registration failed: %s",
            e
        )

        raise