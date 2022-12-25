Feature: Login
  In order to manage the patients records
  As a admin
  I would like to access the OpenEMR dashboard

#  @valid
#  Scenario: Valid Login
#    Given I have browser with openemr application
#    When I enter username as "admin"
#    And I enter password as "pass"
#    And I click on login
#    Then I should get access to dashboard with "OpenEMR"

  @invalid
  Scenario: Invalid Login
    Given I have browser with openemr application
    When I enter username as "admin"
    And I enter password as "pass123"
    And I click on login
    Then I should not get access to dashboard with "Invalid username or password"


  @valid
  Scenario Outline: Valid Login
    Given I have browser with openemr application
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I click on login
    Then I should get access to dashboard with "<expected_title>"
    Examples:
      | username   | password   | expected_title |
      | admin      | pass       | OpenEMR        |
      | accountant | accountant | OpenEMR        |