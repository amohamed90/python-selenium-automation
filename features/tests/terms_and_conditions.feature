# Created by alaamohamed at 7/3/25
Feature: Tests for Terms and Conditions opening in a new tab

  Scenario: User can open and close Terms and Conditions from sign in page
     Given Open target main page
     When Click on sign account
     And Click on Sign in
     And Store original window
     And Click on Target terms and conditions link
     And Switch to the newly opened window
     Then Verify Terms and Conditions page is opened
     And User can close new window
     And switch back to original