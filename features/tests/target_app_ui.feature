# Created by alaamohamed at 7/1/25
Feature: Tests for Target App page
  # Ensure Privacy Policy opens in a new tab

  Scenario: User us able to open Privacy Policy tab
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy Page opened
    And Close current page
    And Return to original window