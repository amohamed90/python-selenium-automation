# Created by alaamohamed at 6/7/25
Feature: Tests for Target sign-in


  Scenario: A logged out user can sign-in
    Given Open target main page
    When Click on sign account
    When Click on Sign in
    Then Verify Sign in form opened