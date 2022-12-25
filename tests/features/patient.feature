@patient
Feature: Patient
  In order to manage the patients records
  As a admin
  I would like to access the OpenEMR dashboard


  Scenario Outline: Add Patient
    Given I have browser with openemr application
    When I enter username as "admin"
    And I enter password as "pass"
    And I click on login
    And I click on Patient menu
    And I click on New search menu
    And I fill the form
      | firstname   | lastname   | dob   | gender   | licencenumber   |
      | <firstname> | <lastname> | <dob> | <gender> | <licencenumber> |
    And I click on create new patient
    And I click on Confirm Create New Patient
    And I handle the alert
    And I handle the happybirthday pop if available
    Then alert message should contains "<expectedalert>"
    And I should see the added patient details as "<expectedpatientname>"

    Examples:
      | firstname | lastname | gender | dob        | licencenumber | expectedalert | expectedpatientname                  |
      | John      | Wick     | Male   | 2022-05-20 | E120          | Toba          | Medical Record Dashboard - John Wick |
#      | Peter     | Paul     | Male   | 2022-05-20 | R3030         | Toba          | Medical Record Dashboard - Peter Paul |