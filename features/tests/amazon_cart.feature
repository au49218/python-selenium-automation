# Created by Anil at 2/6/2021
Feature: # Amazon Cart Empty
  # Enter feature description here

  Scenario: # User can verify Cart is Empty
    Given Open Amazon main page
    When Click on Amazon cart icon
    Then Cart results for Your Amazon Cart is empty are shown on cart page
