
Feature: Tests for Target sign-in

  Scenario: A logged out user can sign-in
    Given Open target main page
    When Click on sign account
    And Click on Sign in
    And Verify Sign in form opened
    And Enter username
    And Click continue
    And Enter password
    And Click continue
    And Click on sign account
    Then Verify user is signed in



