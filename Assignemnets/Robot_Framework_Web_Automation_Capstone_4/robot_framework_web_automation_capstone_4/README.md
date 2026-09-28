# Capstone Assignment 4 - Robot Framework Web Automation

## Objective

Complete Robot Framework web automation solution covering:

- Robot Framework basics
- SeleniumLibrary
- RIDE IDE
- Keyword-driven testing
- Data-driven testing
- Resource files
- User-defined keywords
- Setup and teardown
- Page Object Model concept
- Jenkins execution
- Command-line execution
- Reporting

## Application

TutorialsNinja Demo:

https://tutorialsninja.com/demo/

## Project Structure

```text
robot_framework_web_automation_capstone_4/
├── resources/
│   ├── common.resource
│   ├── login.resource
│   └── search_data.resource
├── tests/
│   ├── search_tests.robot
│   ├── login_tests.robot
│   └── data_driven_tests.robot
├── Jenkinsfile
├── requirements.txt
├── run_robot.py
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Command Line Execution

Run the complete suite:

```bash
robot --outputdir results tests
```

Or:

```bash
python run_robot.py
```

Run only smoke tests:

```bash
robot --include smoke --outputdir results tests
```

Run only search tests:

```bash
robot --include search --outputdir results tests
```

Run a specific file:

```bash
robot --outputdir results tests/search_tests.robot
```

## Reporting

After execution, Robot Framework generates:

```text
results/
├── log.html
├── report.html
└── output.xml
```

`report.html` provides the high-level execution report.

`log.html` provides detailed test and keyword execution information.

`output.xml` contains machine-readable execution results.

## Keyword-Driven Testing

Robot Framework tests are written using keywords:

```robot
Search Product    MacBook
Verify Search Results Exist
```

The actual Selenium implementation is hidden inside reusable user-defined keywords.

## Resource Files

Reusable functionality is stored in:

```text
resources/
```

For example:

```robot
Resource    ../resources/common.resource
```

This prevents the same Selenium logic from being repeated in every test.

## User-Defined Keywords

Examples include:

```robot
Open Application
Close Application
Click My Account
Search Product
Verify Search Results Exist
Open Login Page
Login With Credentials
Verify Login Error
```

## Setup and Teardown

Example:

```robot
Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To    ${BASE_URL}
```

Setup runs before execution and teardown runs after execution.

## Data-Driven Testing

`data_driven_tests.robot` uses Robot Framework's Test Template:

```robot
Test Template     Search Product And Verify
```

Multiple products can then reuse the same test keyword:

```robot
Search MacBook    MacBook
Search iPhone     iPhone
Search Canon      Canon
```

## Page Object Model Concept

Robot Framework does not require Python-style page classes for POM.

This project follows the POM concept by separating page/application operations into resource files.

For example:

```text
resources/common.resource
resources/login.resource
```

These files contain locators and reusable page-level operations, while `.robot` files contain test scenarios.

This gives a separation similar to:

```text
Test Cases
    ↓
Resource / Page Keywords
    ↓
SeleniumLibrary
    ↓
Browser
```

## SeleniumLibrary

SeleniumLibrary provides browser automation keywords such as:

```robot
Open Browser
Click Element
Input Text
Wait Until Element Is Visible
Page Should Contain Element
Capture Page Screenshot
Close All Browsers
```

## RIDE IDE

RIDE is an optional IDE for Robot Framework.

After installing RIDE, a project can be opened from the project directory. The `.robot` and `.resource` files remain normal Robot Framework files, so they can also be edited in VS Code or another text editor.

## Jenkins

The included `Jenkinsfile` demonstrates CI execution.

The Jenkins job should have:

- Python installed
- Robot Framework installed
- Selenium/browser environment available
- HTML Publisher Plugin installed

The pipeline runs:

```text
Install dependencies
        ↓
Run Robot tests
        ↓
Archive results
        ↓
Publish report
```

The Jenkinsfile uses Windows `bat` commands. For a Linux Jenkins agent, replace `bat` with `sh`.

## Important Note

The project uses a public demo website. No real account credentials are required. The login test deliberately uses invalid credentials and verifies that the application displays a login error.
