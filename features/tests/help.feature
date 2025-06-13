# Created by alaamohamed at 6/10/25
Feature: UI elements on the help page


  Scenario: Target Help Text show on the page
    Given Open Target Help Page
    Then Verify Target Help UI text
#    And Verify Search Help Input
#    And Verify Search Click

  Scenario: Target Help grids show
    Given Open Target Help Page
    Then Verify Target Help grids


  Scenario: Manage My Text show on the page
    Given Open Target Help Page
    Then Verify Manage My Text


  Scenario: Links Under Manage My shows on the page
    Given Open Target Help Page
    Then Verify Manage My Links

  Scenario: Contact us information exist
    Given Open Target Help Page
    Then Verify Contact Us Card
    Then Verify See Contact Options Link

  Scenario: Product Recalls Information exist
    Given Open Target Help Page
    Then Verify Product Recalls Card
    Then Verify All Product recalls Link

  Scenario: Browse help pages text exist
    Given Open Target Help Page
    Then Verify Browse All Help Pages Text exist

  Scenario: Browse All links show
    Given Open Target Help Page
    Then Verify Browse All Help Links