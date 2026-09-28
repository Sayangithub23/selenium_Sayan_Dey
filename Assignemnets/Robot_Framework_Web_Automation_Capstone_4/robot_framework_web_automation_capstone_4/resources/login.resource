*** Settings ***
Resource    common.resource

*** Variables ***
${EMAIL}       invalid@example.com
${PASSWORD}    WrongPassword123

*** Keywords ***
Open Login Page
    Click My Account
    Click Link    Login
    Wait Until Element Is Visible    id=input-email

Login With Credentials
    [Arguments]    ${email}    ${password}
    Input Text    id=input-email       ${email}
    Input Text    id=input-password     ${password}
    Click Element    css=input[type='submit']

Verify Login Error
    Wait Until Page Contains Element    css=.alert-danger
    Page Should Contain Element    css=.alert-danger
