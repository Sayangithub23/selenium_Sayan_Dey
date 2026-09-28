import os
from datetime import datetime

def take_screenshot(driver, test_name):
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(c if c.isalnum() or c in "_-" else "_" for c in test_name)
    path = os.path.join("screenshots", f"{safe_name}_{timestamp}.png")
    driver.save_screenshot(path)
    return path
