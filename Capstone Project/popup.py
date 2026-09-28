from logger import logger


def remove_ads(driver):

    try:
        driver.execute_script("""
            document.querySelectorAll(
                "iframe[id^='aswift'], " +
                "iframe[name^='aswift'], " +
                "iframe[src*='googleads'], " +
                "iframe[src*='doubleclick']"
            ).forEach(function(iframe) {
                iframe.remove();
            });
        """)

        logger.info("Advertising iframes removed")

    except Exception as e:

        logger.warning(
            "Failed to remove advertising iframes: %s",
            e
        )