Feature: Get a fact about cat
  As a user
  I want to get a cat fact
  So test that the service is working correctly


  Scenario: Get a fact about a cat
    Given the endpoint "https://catfact.ninja/fact"
    Then obtain status code "200"
