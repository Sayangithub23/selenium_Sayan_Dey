# Capstone Assignment 2 - Selenium Python Framework

## Requirements covered
- Selenium Python
- Unittest
- PyTest
- Page Object Model (POM)
- Utility classes
- Configuration management
- CSV test data
- Screenshots on failure
- HTML reporting

## Application
TutorialsNinja Demo: https://tutorialsninja.com/demo/

## Structure
```text
config/
  config.ini
  config_reader.py
data/
  login_data.csv
  search_data.csv
pages/
  home_page.py
  login_page.py
  search_page.py
tests/
  conftest.py
  test_login_unittest.py
  test_search_pytest.py
utils/
  csv_reader.py
  driver_factory.py
  screenshot.py
pytest.ini
requirements.txt
run_pytest.py
run_unittest.py
```

## Install
```bash
pip install -r requirements.txt
```

Selenium 4 uses Selenium Manager, so ChromeDriver normally does not need to be downloaded manually.

## Run PyTest
```bash
python run_pytest.py
```

HTML report:
```text
reports/pytest_report.html
```

## Run Unittest
```bash
python run_unittest.py
```

## Framework idea
Feature-specific Selenium locators and actions are placed in Page Object classes. Tests call page methods rather than scattering locators throughout test files.

Configuration is kept in `config/config.ini`.

CSV files provide external test data.

PyTest failures trigger screenshots through `pytest_runtest_makereport`; Unittest failures trigger screenshots in `tearDown()`.

The login data intentionally uses invalid credentials because this is a public demo site and no real credentials are required.
