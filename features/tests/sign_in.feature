# Created by Anil at 2/13/2021
Feature: Amazon Sign In Test
  # Enter feature description here

  Scenario: Sign In page can be opened from Sign In popup
    Given Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page opens
