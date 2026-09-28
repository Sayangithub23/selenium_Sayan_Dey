import os


def take_screenshot(driver, name):

    # Create screenshots folder if it doesn't exist
    os.makedirs("screenshots", exist_ok=True)

    # Save screenshot
    path = f"screenshots/{name}.png"

    driver.save_screenshot(path)

    return path

