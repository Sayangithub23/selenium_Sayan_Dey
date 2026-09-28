# Python API Automation Framework

## Technologies

- Python
- Requests
- REST API
- Behave BDD
- Allure Reporting
- Reusable API client
- Authentication
- Pytest is not required because this assignment specifically uses Behave.

## API Used

This project uses the public Restful Booker demo API:

`https://restful-booker.herokuapp.com`

The framework demonstrates:

1. Authentication
2. Create booking
3. Get booking
4. Update booking
5. Delete booking
6. Reusable Requests session
7. BDD feature files
8. Assertions
9. Allure result generation
10. Configuration through environment variables

## Project Structure

```text
api_automation_framework/
├── config/
│   └── config.py
├── utils/
│   ├── api_client.py
│   └── assertions.py
├── features/
│   ├── authentication.feature
│   ├── booking.feature
│   ├── environment.py
│   └── steps/
│       ├── auth_steps.py
│       └── booking_steps.py
├── behave.ini
├── requirements.txt
├── run_tests.py
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
python run_tests.py
```

Or:

```bash
behave
```

The Allure results are generated inside:

```text
allure-results/
```

## View Allure Report

If Allure CLI is installed:

```bash
allure serve allure-results
```

Or generate a report:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Configuration

Default credentials are stored in `config/config.py` for the demo API.

For a real project, credentials should be supplied through environment variables:

```bash
set BOOKER_USERNAME=admin
set BOOKER_PASSWORD=password123
set BASE_URL=https://restful-booker.herokuapp.com
```

Linux/macOS:

```bash
export BOOKER_USERNAME=admin
export BOOKER_PASSWORD=password123
export BASE_URL=https://restful-booker.herokuapp.com
```

## Framework Design

`APIClient` contains reusable HTTP methods so individual test steps do not directly repeat Requests code.

`assertions.py` contains reusable validation functions.

Behave `.feature` files contain business-readable scenarios, while Python step definitions contain implementation logic.

`environment.py` handles scenario setup and attaches API responses to Allure.

## Important Note

Restful Booker is a demo API, so its data can occasionally reset or behave differently from a production service. The framework is intentionally designed as a college capstone/demo project rather than a production API test suite.
