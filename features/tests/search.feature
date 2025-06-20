Feature: User can search for a product

  Scenario: Search for a tea
    Given Open target main page
    When Search for candy
    Then Verify candy results show


  Scenario: Search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify coffee results show


  Scenario: Search for chips
    Given Open target main page
    When Search for chips
    Then Verify chips results show


  Scenario: Search for tea
    Given Open target main page
    When Search for tea
    Then Verify tea name
    And Verify tea image


