
import os
import shutil

def clone_git_repository(git_repo_url, tmp_dir):
    # Remove temporary directory if it exists
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    # Clone the GitHub repository to a temporary directory
    os.system(f"git clone --depth 1 {git_repo_url} {tmp_dir}")

    # Return the temporary directory path
    return tmp_dir