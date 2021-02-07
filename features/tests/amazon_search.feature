# Created by Anil at 1/30/2021
Feature: Amazon Search Test
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Watches into Amazon search field
    And Click on Amazon search icon
    Then Product results for "Watches" are shown on Amazon
    And Page URL has Watches in it

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Dress into Amazon search field
    And Click on Amazon search icon
    Then Product results for "Dress" are shown on Amazon
    And Page URL has Dress in it
