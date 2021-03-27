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





  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for coffee mug
    And Click on the first product
    And Click on Add to cart button
    Then Verify cart has 1 item

 Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for shoes
    And Click on the first product
    And Select shoes size
    And Click on Add to cart button
    Then Verify cart has 1 item

   Scenario: User can select and search in a department
     Given Open Amazon page
     When Select department by alias stripbooks
     And Search for Faust
     Then Verify books department is selected

   Scenario: User can select and search in a department
     Given Open Amazon page
     When Select department by alias software
     And Search for Windows
     Then Verify software department is selected
