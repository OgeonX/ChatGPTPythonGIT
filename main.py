

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

def generate_prompt_with_code(api_key