# Created by alaamohamed at 6/7/25
Feature: Tests for Target cart


  Scenario: Cart is empty
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty


  Scenario: Cart has 1 item
    Given Open target main page
    When Search for tea
    And Add to cart
    Then Verify cart has items