import os
from git import Repo, InvalidGitRepositoryError

# Set up Git repository URL and local path
git_repo_url = "https://github.com/OgeonX/ChatGPTPythonGIT.git"
local_repo_path = "C:\\Users\\admin\\source\\repos\\ChatGPTPythonGIT" # Change this to the path of your local repo

try:
    repo = Repo(local_repo_path)
except InvalidGitRepositoryError:
    # Clone the repository if it doesn't exist locally
    repo = Repo.clone_from(git_repo_url, local_repo_path)

def add_file_to_repo(file_name, file_contents):
    # Add the generated response to a new file in the repository
    file_path = os.path.join(local_repo_path, file_name)
    with open(file_path, "w") as f:
        f.write(file_contents)

    # Commit the changes to the repository
    repo.git.add(".")
    repo.index.commit(file_name)

    # Push the changes to the remote repository
    repo.git.push()
