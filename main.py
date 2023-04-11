

import os
import requests
from dotenv import load_dotenv
from testapikey import test_api_key
from github_uploader import upload_to_github

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
GITHUB_REPO_OWNER = os.getenv("GITHUB_REPO_OWNER")
GITHUB_REPO_NAME = os.getenv("GITHUB_REPO_NAME")

def generate_prompt_with_code(api_key, code, suggestions):
    endpoint_url = "https://api.openai.com/v1/engines/text-davinci-002/completions"

    headers =