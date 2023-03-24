import os

# Set up local path to the Git repository
local_repo_path = "C:\\Users\\admin\\source\\repos\\ChatGPTPythonGIT" # Change this to the path of your local repo

def read_file(file_name):
    file_path = os.path.join(local_repo_path, file_name)
    with open(file_path) as f:
        content = f.read()
    return content

def get_file_contents():
    # Read the contents of all Python files in the repository, excluding the .git and __pycache__ folders
    files = [f for f in os.listdir(local_repo_path) if f.endswith(".py") and f not in [".git", "__pycache__", ".vs"]]
    file_contents = ""
    for file_name in files:
        try:
            file_contents += read_file(file_name)
        except Exception as e:
            print(f"Error reading file {file_name}: {e}")
    return file_contents
