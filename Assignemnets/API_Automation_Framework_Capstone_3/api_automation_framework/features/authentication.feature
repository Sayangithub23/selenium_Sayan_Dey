Feature: API Authentication

  Scenario: Generate an authentication token with valid credentials
    Given I have valid Booker credentials
    When I request an authentication token
    Then the authentication response status should be 200
    And an authentication token should be generated
