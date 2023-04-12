

```
import os
import shutil

def clone_git_repository(git_repo_url, tmp_dir):
    # Create temporary directory if it doesn't exist
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    # Remove any existing files in the temporary directory 
    for file in os.listdir(tmp_dir):
        file_path = os.path.join(tmp_dir, file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    # Clone the GitHub repository to a temporary directory
    os.system(f"git clone --depth 1 --branch HEAD {git_repo_url} {tmp_dir}")

    # Return the temporary directory path
    return tmp_dir

```