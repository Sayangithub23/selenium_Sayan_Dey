import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import configparser
import csv
import time

from logger import logger
from screenshot import take_screenshot

from register import register
from login import login
from search import search_product

from cart import (
    add_to_cart,
    view_cart,
    proceed_to_checkout,
    place_order,
    make_payment
)


@pytest.fixture
def driver():

    # Read configuration
    config = configparser.ConfigParser()
    config.read("config.ini")

    url = config["application"]["url"]

    # Firefox options
    options = Options()

    # Don't wait for every page resource to finish loading
    options.page_load_strategy = "eager"

    # Disable images to reduce page loading time
    options.set_preference(
        "permissions.default.image",
        2
    )

    # Start browser
    logger.info("Starting browser")

    driver = webdriver.Firefox(
        options=options
    )

    driver.maximize_window()

    logger.info("Browser maximized")

    # Open website
    driver.get(url)

    logger.info(
        "Website opened: %s",
        url
    )

    # Screenshot
    take_screenshot(
        driver,
        "01_homepage"
    )

    yield driver

    # Close browser
    logger.info("Closing browser")

    driver.quit()

    logger.info("Browser closed")


def test_ecommerce_flow(driver):

    logger.info("Starting e-commerce test")

    # Registration
    register(driver)

    # Login
    login(driver)

    # Read products from CSV
    with open("products.csv", "r") as file:

        data = csv.DictReader(file)
        products = list(data)

    # Search and add products to cart
    for item in products:

        product = item["product"]

        logger.info(
            "Processing product: %s",
            product
        )

        # Search product
        search_product(
            driver,
            product
        )

        # Add product to cart
        add_to_cart(
            driver,
            product
        )

    # View cart
    view_cart(driver)

    # Proceed to checkout
    proceed_to_checkout(driver)

    # Place order
    place_order(driver)

    # Enter payment details and confirm order
    make_payment(driver)

    # Keep browser open temporarily
    time.sleep(20)

    logger.info("E-commerce test completed")