import configparser
import csv

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from cart import add_to_cart, make_payment, place_order, proceed_to_checkout, view_cart
from logger import logger
from login import login
from register import register
from screenshot import take_screenshot
from search import search_product


def load_products():
    
    try:
        with open("products.csv", newline="", encoding="utf-8") as file:
            products = list(csv.DictReader(file))
    except OSError as error:
        logger.error("Failed to read product data: %s", error)
        raise

    logger.info("Product data loaded from CSV: %d product(s)", len(products))
    return products


def get_application_url():
    
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["application"]["url"]


def create_driver():
    
    options = Options()
    options.page_load_strategy = "eager"
    options.set_preference("permissions.default.image", 2)
    return webdriver.Firefox(options=options)


def run_ecommerce_flow():
   
    url = get_application_url()
    products = load_products()
    driver = create_driver()

    try:
        logger.info("Starting browser")
        driver.maximize_window()
        driver.get(url)
        logger.info("Website opened: %s", url)
        take_screenshot(driver, "01_homepage")

        register(driver)
        login(driver)

        for item in products:
            product = item["product"]
            logger.info("Processing product: %s", product)
            search_product(driver, product)
            add_to_cart(driver, product)
            logger.info("Finished processing product: %s", product)

        view_cart(driver)
        proceed_to_checkout(driver)
        place_order(driver)
        make_payment(driver)
        logger.info("E-commerce flow completed successfully")

    except Exception as error:
        logger.error("E-commerce flow failed: %s", error)
        raise

    finally:
        logger.info("Closing browser")
        driver.quit()
        logger.info("Browser closed")


if __name__ == "__main__":
    run_ecommerce_flow()
