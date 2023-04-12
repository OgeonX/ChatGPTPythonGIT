
To refactor this code following microservices best practices, it could be broken down into the following components and functions:

1. Authentication: This component would be responsible for authenticating the API key and setting the appropriate headers for requests.
2. File Retrieval: This component would be responsible for retrieving the file's current state from the API. It would return the SHA value if the file exists.
3. File Update/Creation: This component would be responsible for encoding the content, creating or updating the file, and committing the changes with a message.
4. Notification: This component would be responsible for returning success or failure messages depending on the status code of the requests.

Each of these components could then be further broken down into smaller, more focused functions that each handle a specific task. This would help to make the code more modular and easier to maintain. For example, the Authentication component could be broken down into functions for setting the authorization header and for validating the API key, and the File Update/Creation component could be broken down into functions for encoding the content, creating the file, and committing the changes.