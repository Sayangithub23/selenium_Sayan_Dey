*** Settings ***
Resource    ../resources/common.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Template     Search Product And Verify

*** Test Cases ***    Product
Search MacBook         MacBook
Search iPhone          iPhone
Search Canon           Canon

*** Keywords ***
Search Product And Verify
    [Arguments]    ${product}
    Go To    ${BASE_URL}
    Search Product    ${product}
    Verify Search Results Exist
