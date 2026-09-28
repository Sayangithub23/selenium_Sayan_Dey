from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.config_reader import ConfigReader

def create_driver():
    config = ConfigReader()
    browser = config.get("application", "browser").lower()
    headless = config.get_bool("application", "headless")

    if browser == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        return driver

    raise ValueError(f"Unsupported browser: {browser}")
