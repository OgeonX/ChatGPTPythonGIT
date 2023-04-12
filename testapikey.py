

import requests

def test_api_key(api_key, api_key_type="OpenAI"):
    # Set OpenAI API endpoint URL
    if api_key_type == "OpenAI":
        endpoint_url = "https://api.openai.com/v1/engines"
    elif api_key_type == "GitHub":
        endpoint_url = "https://api.github.com"
    else:
        print(f"Invalid API key type: {api_key_type}")
        return False

    # Set GET request parameters
    headers = {"Authorization": f"Bearer {api_key}"}

    # Make GET request to API endpoint
    try:
        response = requests.get(endpoint_url, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            return True
        else:
            print(f"{api_key_type} API key test failed with status code {response.status_code}: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"{api_key_type} API key test failed with error: {e}")
        return False