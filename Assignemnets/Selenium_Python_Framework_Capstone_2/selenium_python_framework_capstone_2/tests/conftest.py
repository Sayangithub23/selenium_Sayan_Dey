import pytest
from config.config_reader import ConfigReader
from utils.driver_factory import create_driver
from utils.screenshot import take_screenshot

@pytest.fixture
def driver():
    driver = create_driver()
    config = ConfigReader()
    driver.implicitly_wait(config.get_int("application", "implicit_wait"))
    driver.get(config.get("application", "base_url"))
    yield driver
    driver.quit()

def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, item.name)
