
1. Create a function to set the API endpoint URL based on the API key type. This will allow the code to be more modular and easily maintainable as new API key types can be added.

2. Create a function to make the GET request to the API endpoint. This will allow the code to be more modular and easily maintainable as different types of requests can be made to the API.

3. Create a function to check the response status code and print an error message if the request was unsuccessful. This will allow the code to be more modular and easily maintainable.

4. Move the API key and API key type arguments from the test_api_key() function to the functions that make the API request and check the response. This will make the code more organized and readable.

5. Extract constants such as the API URL endpoints and authorization header into variables. This will make the code more organized and readable.