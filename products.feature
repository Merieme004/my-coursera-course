Feature: Product Management

  # Scenario to test creating a product
  Scenario: Create a new product
    Given I am an authenticated user
    When I create a product with name "Sample Product" and category "Electronics"
    Then the product should be successfully created

  # Scenario to test reading a product by its ID
  Scenario: Read a product by ID
    Given a product with name "Sample Product" exists
    When I view the product details
    Then I should see the product's name and category

  # Scenario to test updating a product
  Scenario: Update a product
    Given a product with name "Sample Product" exists
    When I update the product's name to "Updated Product"
    Then the product's name should be updated successfully

  # Scenario to test deleting a product
  Scenario: Delete a product
    Given a product with name "Sample Product" exists
    When I delete the product
    Then the product should no longer exist

  # Scenario to test listing all products
  Scenario: List all products
    Given multiple products exist
    When I view the list of products
    Then I should see all the product names

  # Scenario to search products by name
  Scenario: Search products by name
    Given products with names "Sample Product" and "Another Product" exist
    When I search for products by name "Sample Product"
    Then I should see the product "Sample Product"

  # Scenario to search products by category
  Scenario: Search products by category
    Given products in categories "Electronics" and "Furniture" exist
    When I search for products in the "Electronics" category
    Then I should see all products in the "Electronics" category

  # Scenario to filter products by availability
  Scenario: Filter products by availability
    Given products with different availability statuses exist
    When I filter products by "In Stock"
    Then I should only see products that are "In Stock"
