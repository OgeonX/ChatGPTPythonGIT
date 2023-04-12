
1. Create separate functions for making the GET and POST requests to the OpenAI API endpoint.
2. Move the logic for loading the API key from the config file into a separate function.
3. Extract the logic for iterating over the files in the given directory and reading their contents into a separate function.
4. Create a separate function for verifying the uploaded files using the OpenAI's Files API.
5. Move the test_api_key() function into a separate module and import it when needed.
6. Create a helper function to handle any exceptions that may occur while decoding a file.
7. Refactor the code to use the logging module instead of printing out messages.