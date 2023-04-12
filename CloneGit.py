
```
import os
import shutil

def clone_git_repository(git_repo_url, tmp_dir):
    # Remove temporary directory if it exists
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    # Clone the GitHub repository to a temporary directory
    os.system(f"git clone --depth 1 --branch HEAD {git_repo_url} {tmp_dir}")

    # Raise an exception if the repository was not successfully cloned
    if not os.path.exists(tmp_dir):
        raise Exception(f"Repository {git_repo_url} was not successfully cloned.")

```