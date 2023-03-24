import openai
import os
from git import Git, Repo, InvalidGitRepositoryError
import shutil
import tkinter as tk
from tkinter import simpledialog

# Set up OpenAI API key and Git repository
openai.api_key = "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"
git_repo_url = "https://github.com/OgeonX/ChatGPTPythonGIT.git"
local_repo_path = "C:\\Users\\admin\\source\\repos\\ChatGPTPythonGIT" # Change this to the path of your local repo
repo = None

# Clone the Git repository if it doesn't exist locally, otherwise use the existing one
if not os.path.exists(local_repo_path):
    repo = Repo.clone_from(git_repo_url, local_repo_path)
else:
    try:
        repo = Repo(local_repo_path)
    except InvalidGitRepositoryError:
        print("The path specified is not a valid Git repository.")
        exit()

# Function to read a file's content from the repository
def read_file(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

# Display a prompt for the user to enter a message
root = tk.Tk()
root.withdraw()
user_input = simpledialog.askstring(title="Chat with OpenAI", prompt="Enter your message:")

try:
    # Call OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    # Print the response
    print(response.choices[0].text.strip())

    # Add the generated response to a new file in the repository
    file_name = "{}.txt".format(len(os.listdir(local_repo_path)) + 1)
    file_path = os.path.join(local_repo_path, file_name)
    with open(file_path, "w") as f:
        f.write(response.choices[0].text.strip())

    # Commit the changes to the repository
    repo.git.add(".")
    repo.index.commit("Added new response from chatbot")

    # Push the changes to the remote repository
    repo.git.push()

except openai.error.APIError as e:
    print("There was an error with the OpenAI API: {}".format(e))
    
except Exception as e:
    print("There was an error: {}".format(e))
