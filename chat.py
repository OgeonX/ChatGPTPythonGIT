import os
import openai
import tkinter as tk
from tkinter import simpledialog
import subprocess
from git import Repo
from git.exc import InvalidGitRepositoryError
import sys

# Load OpenAI API key from config file
import config
openai.api_key = config.OPENAI_API_KEY

def read_file(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def generate_response(file_contents, user_input):
    # Call OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt="Context: {}\n\nUser Input: {}".format(file_contents, user_input),
        max_tokens=2000,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1,
    )
    generated_text = response.choices[0].text.strip()

    return generated_text

def write_to_file(local_repo_path, file_name, generated_text):
    # Add the generated response to a new file in the repository
    file_path = os.path.join(local_repo_path, file_name)
    with open(file_path, "w") as f:
        f.write(generated_text)

def commit_to_git(local_repo_path, repo, file_name, message_queue):
    # Determine the tag to use based on the file's status in the repository
    if repo.is_dirty(untracked_files=True):
        tag = "+"
    elif repo.untracked_files:
        tag = "-"
    else:
        tag = "*"

    # Commit the changes to the repository with the appropriate tag
    repo.git.add(".")
    repo.index.commit("{} {}".format(tag, file_name))

    # Push the changes to the remote repository
    p = subprocess.Popen(["git", "push"], cwd=local_repo_path)
    p.wait()

    # Send a message to the message queue
    message_queue.put("Changes committed to Git repository")

if __name__ == "__main__":
    # Set up Git repository URL and local path
    git_repo_url = "https://github.com/username/repo.git"
    local_repo_path = "C:\\Users\\admin\\source\\repos\\ChatGPTPythonGIT"
