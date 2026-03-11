Feature: Product A inventory forecast
  Scenario: Request forecast for a product and get valid response
    Given a forecast request event
    When the forecast service processes the request
    Then the response includes a prediction key
