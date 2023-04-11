

# file_uploader.py
import requests
import os

def upload_file_to_openai(api_key, file_path):
    endpoint_url = "https://api.openai.com/v1/files"

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    try:
        with open(file_path, 'rb') as file:
            # Prepare the file as a multipart/form-data
            file_data = {
                'file': (os.path.basename(file_path), file, 'application/octet-stream'),
                'purpose': (None, 'fine-tune')
            }

            response = requests.post(endpoint_url, headers=headers, files=file_data)
            if response.status_code == 201:
                print