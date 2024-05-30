# CRUD Operations with Python Flask Server

I recently completed a lab where I created a product list using a Flask server. The application supports CRUD operations through REST API endpoints.

## Objectives
- Create API endpoints for CRUD operations.
- Test endpoints using cURL and POSTMAN.

## Project Overview

### Prerequisites
- Python 3.x
- Flask

### Setup
1. **Install Flask**:
    ```sh
    pip install Flask
    ```
2. **Create Flask Server**:
    - Implement API endpoints for adding, retrieving, updating, and deleting products.
    - Ensure data is transient and handled in memory.

### Testing
- **Use cURL**:
    - To add a product:
        ```sh
        curl -X POST -H "Content-Type: application/json" -d '{"name":"Product1","price":100}' http://localhost:5000/products
        ```
    - To retrieve all products:
        ```sh
        curl http://localhost:5000/products
        ```
    - To retrieve a specific product by ID:
        ```sh
        curl http://localhost:5000/products/<id>
        ```
    - To update a product by ID:
        ```sh
        curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Product","price":150}' http://localhost:5000/products/<id>
        ```
    - To delete a product by ID:
        ```sh
        curl -X DELETE http://localhost:5000/products/<id>
        ```

- **Use POSTMAN**:
    - Create and send requests to test the endpoints similarly to cURL.

## Conclusion
Completing this lab helped me understand how to create and test REST API endpoints using Flask. I utilized both cURL and POSTMAN for thorough testing of the implemented functionalities.
