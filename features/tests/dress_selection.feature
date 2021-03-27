# Created by Anil at 2/20/2021
Feature: Test for dress selection
  # Enter feature description here

  Scenario: User can select dress colors
    Given Open Amazon Dress B07RRS7N5R page
    Then Verify user can click through colors

  Scenario: Size tooltip is shown upon hovering over Add To Cart button
    #Given Open Amazon product B07RRS7N5R page
    Given Open Amazon Dress B074TBCSC8 page
    When Hover over Add to Cart button
    Then Verify size selection tooltip is shown

  Scenario: Deals are shown upon hovering over New Arrivals link
    Given Open Amazon Dress B074TBCSC8 page
    When Hover over New Arrivals link
    Then Verify the deals are shown
