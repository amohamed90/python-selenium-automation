# Created by alaamohamed at 6/7/25
Feature: Tests for Target cart


  Scenario: Cart is empty
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty