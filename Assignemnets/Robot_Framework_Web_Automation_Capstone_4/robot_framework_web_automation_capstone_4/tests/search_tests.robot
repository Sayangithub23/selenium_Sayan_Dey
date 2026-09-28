*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/search_data.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Setup        Go To    ${BASE_URL}
Test Teardown     Capture Page Screenshot    ${TEST NAME}.png

*** Test Cases ***
Search For MacBook
    [Tags]    smoke    search
    Search Product    MacBook
    Verify Search Results Exist

Search For iPhone
    [Tags]    regression    search
    Search Product    iPhone
    Verify Search Results Exist

Search For Canon
    [Tags]    regression    search
    Search Product    Canon
    Verify Search Results Exist
