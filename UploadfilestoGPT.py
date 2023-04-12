


```
import os
import requests
import config
import chardet

def test_api_key(api_key):
    # Set OpenAI API endpoint URL
    endpoint_url = "https://api.openai.com/v1/engines"

    # Set GET request parameters
    headers = {"Authorization": f"Bearer {api_key}"}

    # Make GET request to OpenAI API endpoint
    try:
        response = requests.get(endpoint_url, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            return True
        else:
            print(f"API key test failed with status code {response.status_code}: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"API key test failed with error: {e}")
        return False

def upload_to_openai():
    # Set working directory to the folder containing the script and the config file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Load API key from config file
    api_key = config.OPENAI_API_KEY

    # Test if API key is valid
    if not test_api_key(api_key):
        print("Invalid API key provided.")
        return

    # Set OpenAI API endpoint URL
    endpoint_url = "https://api.openai.com/v1/files"

    # Set the directory containing the Python files to upload
    python_dir = os.getcwd()

    # Read file contents
    file_contents = ""
    for dirpath, dirnames, filenames in os.walk(python_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "rb") as file:
                    file_content = file.read()
                    try:
                        encoding = chardet.detect(file_content)['encoding']
                        file_contents += file_content.decode(encoding)
                    except UnicodeDecodeError as e:
                        print(f"Error decoding {filename} with error: {e}")
    print(file_contents)

    # Set POST request parameters
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"purpose": "fine-tune", "file": file_contents}

    # Make POST request to OpenAI API endpoint
    try:
        response = requests.post(endpoint_url, headers=headers, data=data)

        # Check if request was successful
        if response.status_code == 200:
            print("Files uploaded successfully!")
        else:
            print("Files upload failed.")
            print(response.text)

        # Verify uploaded file using OpenAI's Files API
        uploaded_file_id = response.json().get('id')
        if uploaded_file_id is not None:
            verify_endpoint_url = f"https://api.openai.com/v1/files/{uploaded_file_id}/verify"
            verify_headers = {"Authorization": f"Bearer {api_key}"}
            verify_response = requests.get(verify_endpoint_url, headers=verify_headers)

            # Check if verification was successful
            if verify_response.status_code == 200:
                print("Verification successful!")
            else:
                print("Verification failed.")
                print(verify_response.text)
        else:
            print("No uploaded file ID found")
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")

if __name__ == "__main__":
    upload_to_openai()

```