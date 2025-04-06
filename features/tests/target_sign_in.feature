Feature: Target sign-in test cases


  Scenario: Logged out user can navigate to the Sign-in page
    Given Open Target main page
    When Main click sign in
    And Navigation click Sign In
    Then Verify Sign In form opened