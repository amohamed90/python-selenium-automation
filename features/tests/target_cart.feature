Feature: Target cart test cases


  Scenario: Verify that a cart is empty
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown
