from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger import logger
from screenshot import take_screenshot


def add_to_cart(driver, product):

    try:
        logger.info("Adding product to cart: %s", product)

        # Find the product
        product_card = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@class, 'productinfo')]"
                    f"//p[normalize-space()='{product}']"
                )
            )
        )

        # Get the product card
        product_container = product_card.find_element(
            By.XPATH,
            "./ancestor::div[contains(@class, 'product-image-wrapper')]"
        )

        # Find Add to Cart button
        add_button = product_container.find_element(
            By.XPATH,
            ".//a[contains(@class, 'add-to-cart')]"
        )

        # Scroll to product
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_button
        )

        take_screenshot(
            driver,
            f"add_to_cart_{product.replace(' ', '_')}"
        )

        # Click Add to Cart
        add_button.click()

        logger.info(
            "Add to Cart clicked for: %s",
            product
        )

        # Wait for Added modal
        view_cart = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(normalize-space(), 'View Cart')]"
                )
            )
        )

        logger.info(
            "Product added to cart: %s",
            product
        )

        take_screenshot(
            driver,
            f"cart_added_{product.replace(' ', '_')}"
        )

        # Continue Shopping
        continue_shopping = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(normalize-space(), 'Continue Shopping')]"
                )
            )
        )

        continue_shopping.click()

        logger.info(
            "Continue Shopping clicked"
        )

    except Exception as e:

        logger.error(
            "Failed to add product to cart %s: %s",
            product,
            e
        )

        raise


def view_cart(driver):

    try:
        logger.info("Opening shopping cart")

        # Click Cart
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, "Cart")
            )
        )

        cart_button.click()

        logger.info("Cart button clicked")

        # Wait for cart page
        WebDriverWait(driver, 10).until(
            EC.url_contains("/view_cart")
        )

        logger.info("Shopping cart opened")

        take_screenshot(
            driver,
            "cart_view"
        )

    except Exception as e:

        logger.error(
            "Failed to open shopping cart: %s",
            e
        )

        raise


def proceed_to_checkout(driver):

    try:
        logger.info("Proceeding to checkout")

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.check_out")
            )
        )

        checkout_button.click()

        logger.info("Proceed To Checkout clicked")

        take_screenshot(
            driver,
            "checkout_page"
        )

    except Exception as e:

        logger.error(
            "Failed to proceed to checkout: %s",
            e
        )

        raise



def place_order(driver):

    try:
        logger.info("Placing order")

        place_order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.check_out[href='/payment']")
            )
        )

        place_order_button.click()

        logger.info("Place Order clicked")

        take_screenshot(
            driver,
            "payment_page"
        )

    except Exception as e:

        logger.error(
            "Failed to place order: %s",
            e
        )

        raise




def make_payment(driver):

    try:
        logger.info("Entering payment details")

        # Name on Card
        name_on_card = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[data-qa='name-on-card']")
            )
        )
        name_on_card.send_keys("Test User")

        # Card Number
        card_number = driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='card-number']"
        )
        card_number.send_keys("4111111111111111")

        # CVC
        cvc = driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='cvc']"
        )
        cvc.send_keys("311")

        # Expiry Month
        expiry_month = driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='expiry-month']"
        )
        expiry_month.send_keys("12")

        # Expiry Year
        expiry_year = driver.find_element(
            By.CSS_SELECTOR,
            "input[data-qa='expiry-year']"
        )
        expiry_year.send_keys("2030")

        logger.info("Payment details entered")

        take_screenshot(
            driver,
            "payment_details"
        )

        # Pay and Confirm Order
        pay_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-qa='pay-button']")
            )
        )

        pay_button.click()

        logger.info("Pay and Confirm Order clicked")

        # Wait for page navigation
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != "https://automationexercise.com/payment"
        )

        logger.info(
            "Order completed. Current URL: %s",
            driver.current_url
        )

        take_screenshot(
            driver,
            "order_success"
        )

    except Exception as e:

        logger.error(
            "Payment failed: %s",
            e
        )

        raise