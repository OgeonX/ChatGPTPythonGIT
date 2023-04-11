

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
        print(f"API key test failed with error: {