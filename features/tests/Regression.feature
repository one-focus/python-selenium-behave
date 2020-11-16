# Created by Alex Kardash at 14/11/2020
@regression
Feature: Login
  Check user can login with valid username and password

  Background:
    Given I open home page

  @search
  Scenario: Validate search
    When I type "Test automation" in search field
    When I click on search button
    Then I see "test automation is the use of" on the page

  Scenario Outline: Validate left menu
    When I click on <menu item>
    Then I see "<text>" on the page

    Examples:
      | menu item       | text                  |
      | Contents        | Wikipedia:Contents    |
      | Current events  | Portal:Current events |
      | About Wikipedia | Wikipedia:About       |
      | Contact us      | Wikipedia:Contact us  |
      | Donate          | Donation amount       |
      | Donate          | Donation w amount       |
