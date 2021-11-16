Feature: Login in Store
  As a user
  I want to access the Store page
  So Login correctly

  Background:
    Given the Login Store webPage


  Scenario: Login in store webPage using excel data
    When complete user and pass from excel
    Then my account page is displayed