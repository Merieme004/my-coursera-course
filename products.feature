# features/products.feature

Feature: Product management

  Scenario: Add a new product
    Given the following products exist
      | name          | description | price | category   | availability |
      | Test Product  | Test        | 20.99 | Electronics| True         |
    When I add a new product
    Then the product should be added successfully

  Scenario: Update a product's price
    Given the following products exist
      | name          | description | price | category   | availability |
      | Test Product  | Test        | 20.99 | Electronics| True         |
    When I update the price of the product
    Then the product price should be updated to 25.99

  Scenario: Delete a product
    Given the following products exist
      | name          | description | price | category   | availability |
      | Test Product  | Test        | 20.99 | Electronics| True         |
    When I delete the product
    Then the product should be removed

  Scenario: List all products
    Given the following products exist
      | name          | description | price | category   | availability |
      | Test Product  | Test        | 20.99 | Electronics| True         |
    When I list all products
    Then I should see all products
