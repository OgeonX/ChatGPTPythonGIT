

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
    response = requests.get(endpoint_url, headers=headers)

    # Check if request was successful
    if response.status_code == 200:
        return True
    else:
        return False

def upload_to_openai():
    # Set working directory to the folder containing the script and the config file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Load API