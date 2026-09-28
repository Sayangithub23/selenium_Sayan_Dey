from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger import logger



def search_product(driver, product):

    try:
        logger.info("Starting product search: %s", product)

        
        # Click Products
        products_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.PARTIAL_LINK_TEXT, "Products")
            )
        )

        
        products_button.click()

        logger.info("Products button clicked")

        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "search_product")
            )
        )

        search_box.clear()
        search_box.send_keys(product)

        logger.info("Product entered in search box: %s", product)

        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "submit_search")
            )
        )

        # Click Search
        search_button.click()

        logger.info("Search button clicked")

        # Verify product
        product_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,f"//div[contains(@class, 'productinfo')]//p[normalize-space()='{product}']"
                    
                )
            )
        )

        logger.info(
            "Product found in search results: %s",
            product_result.text
        )

    except Exception as e:

        logger.error(
            "Product search failed for %s: %s",
            product,
            e
        )

        raise