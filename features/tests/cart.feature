# Created by alaamohamed at 6/7/25
Feature: Tests for Target cart


  Scenario: Cart is empty
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Add to cart
    And Store product name
    And Add to cart button from side-nav
    And Open cart page
    Then Verify cart has items
    And Verify cart has correct product