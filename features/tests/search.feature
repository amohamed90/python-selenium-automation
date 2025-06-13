# Created by alaamohamed at 6/9/25
Feature: User can search for a product

  Scenario: Search for a tea
    Given Open target main page
    When Search for tea
    Then Verify tea results show


  Scenario: Search for a coffee
    Given Open target main page
    When Search for coffee
    Then Verify coffee results show


  Scenario: Search for a chips
    Given Open target main page
    When Search for chips
    Then Verify chips results show