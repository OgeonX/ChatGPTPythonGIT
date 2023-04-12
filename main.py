import os
import requests
from dotenv import load_dotenv
from testapikey import test_api_key
from github_uploader import upload_to_github
import logging

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
GITHUB_REPO_OWNER = os.getenv("GITHUB_REPO_OWNER")
GITHUB_REPO_NAME = os.getenv("GITHUB_REPO_NAME")

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def generate_prompt_with_code(api_key, code, suggestions):
    endpoint_url = "https://api.openai.com/v1/engines/text-davinci-002/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "prompt": f"Here is a Python code snippet:\n```\n{code}\n```\nPlease apply the following suggestions to the code:\n{suggestions}\nModified code:",
        "max_tokens": 2048,
        "n": 1,
        "stop": None,
        "temperature": 0.8,
    }

    try:
        response = requests.post(endpoint_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Request failed with status code {response.status_code}: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed with error: {e}")
        return None


print(f"OPENAI_API_KEY from .env: {OPENAI_API_KEY}")
print(f"GITHUB_API_KEY from .env: {GITHUB_API_KEY}")
print(f"GITHUB_REPO_OWNER from .env: {GITHUB_REPO_OWNER}")
print(f"GITHUB_REPO_NAME from .env: {GITHUB_REPO_NAME}")

# Test OpenAI API key
if test_api_key(OPENAI_API_KEY, "OpenAI"):
    print("OpenAI API key is valid")
else:
    print("OpenAI API key is not valid")

# Test GitHub API key
if test_api_key(GITHUB_API_KEY, "GitHub"):
    print("GitHub API key is valid")
else:
    print("GitHub API key is not valid")

# List all .py files in the directory where the script is run
py_files = [file for file in os.listdir() if file.endswith('.py')]

# Read and process each .py file
for file_path in py_files:
    with open(file_path, 'r') as file:
        file_content = file.read()

    print(f"\nProcessing '{file_path}':")
    response = generate_prompt_with_code(OPENAI_API_KEY, file_content, "")
    if response:
        suggestions = response["choices"][0]["text"]
        print(f"Suggestions for '{file_path}':\n{suggestions}")

        response = generate_prompt_with_code(OPENAI_API_KEY, file_content, suggestions)
        if response:
            modified_code = response["choices"][0]["text"]
            print(f"Modified code for '{file_path}':\n{modified_code}")

            # Upload modified code to GitHub
            try:
                upload_to_github(GITHUB_API_KEY, GITHUB_REPO_OWNER, GITHUB_REPO_NAME, "dev", file_path, modified_code, "Commited from OpenAI API")
                logging.info(f"Modified code for '{file_path}' uploaded to GitHub")
            except Exception as e:
                logging.error(f"Failed to upload modified code for '{file_path}' to GitHub: {e}")
        else:
            logging.error(f"No modified code generated for '{file_path}'")
    else:
        logging.error(f"No suggestions generated for '{file_path}'")
