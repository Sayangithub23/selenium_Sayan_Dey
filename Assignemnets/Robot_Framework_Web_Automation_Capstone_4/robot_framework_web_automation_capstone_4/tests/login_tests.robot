*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/login.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To    ${BASE_URL}

*** Test Cases ***
Invalid Login Test
    [Tags]    smoke    login
    Open Login Page
    Login With Credentials    ${EMAIL}    ${PASSWORD}
    Verify Login Error
