# Created by Anil at 2/14/2021
Feature: # Amazon Cart Add
  # Enter feature description here

  Scenario: # User can add item to cart
    Given Open Amazon page
    When Search for tea cup
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 item
