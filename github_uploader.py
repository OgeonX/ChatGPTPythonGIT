
```
import requests
import base64

def upload_to_github(github_api_key, repo_owner, repo_name, branch, path, content, commit_message):
    headers = {
        "Authorization": f"token {github_api_key}",
        "Content-Type": "application/json",
    }

    # Get the file's current state
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{path}"
    response = requests.get(api_url, headers=headers, params={"ref": branch})

    if response.status_code in [200, 404]:
        sha = None
        if response.status_code == 200:
            sha = response.json()["sha"]

        # Update or create the file
        content_base64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        data = {
            "message": commit_message,
            "content": content_base64,
            "branch": branch,
        }
        if sha:
            data["sha"] = sha

        response = requests.put(api_url, headers=headers, json=data)

        if response.status_code in [200, 201]:
            print(f"File successfully uploaded to GitHub: {path}")
            return True
        else:
            print(f"File upload to GitHub failed with status code {response.status_code}: {response.text}")
            return False
    else:
        print(f"File retrieval from GitHub failed with status code {response.status_code}: {response.text}")
        return False

```