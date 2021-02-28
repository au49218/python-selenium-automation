# Created by Anil at 2/13/2021
Feature: Amazon Best Sellers
  # Enter feature description here

  Scenario: User can see 5 links on best sellers page
    Given Open Amazon Best Sellers page
    Then Verify 5 links are displayed

  Scenario: User can click 5 links on best sellers page
    Given Open Amazon Best Sellers page
    Then User can click through top links and verify correct page opens
