*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${BASE_URL}       https://tutorialsninja.com/demo/
${BROWSER}        chrome
${TIMEOUT}        10s

*** Keywords ***
Open Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    ${TIMEOUT}

Close Application
    Close All Browsers

Click My Account
    Click Element    xpath=//span[contains(text(),'My Account')]

Search Product
    [Arguments]    ${product}
    Wait Until Element Is Visible    name=search
    Input Text    name=search    ${product}
    Click Button    css=button.btn.btn-default.btn-lg

Verify Search Results Exist
    Page Should Contain Element    css=.product-layout

Take Failure Screenshot
    [Arguments]    ${name}
    Capture Page Screenshot    ${name}.png
