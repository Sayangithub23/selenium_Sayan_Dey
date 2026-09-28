Feature: Booking API

  Background:
    Given I have valid Booker credentials
    And I authenticate with the Booker API

  Scenario: Create a new booking
    When I create a booking
    Then the booking response status should be 200
    And the response should contain a booking ID
    And the booking details should contain "Sayan" as firstname

  Scenario: Get an existing booking
    Given I have created a booking
    When I request the created booking
    Then the booking response status should be 200
    And the response should contain booking details

  Scenario: Update an existing booking
    Given I have created a booking
    When I update the booking firstname to "UpdatedSayan"
    Then the booking response status should be 200
    And the booking firstname should be "UpdatedSayan"

  Scenario: Delete an existing booking
    Given I have created a booking
    When I delete the created booking
    Then the booking response status should be 201
