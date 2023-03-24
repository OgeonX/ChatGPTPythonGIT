import os
import subprocess
import time
from multiprocessing import Process, Queue


def git_process(message_queue):
    # Set up Git repository URL and local path
    git_repo_url = "https://github.com/OgeonX/ChatGPTPythonGIT.git"
    local_repo_path = "C:\\Users\\admin\\source\\repos\\ChatGPTPythonGIT"  # Change this to the path of your local repo

    # Clone the Git repository if it doesn't exist locally, otherwise use the existing one
    if not os.path.exists(local_repo_path):
        # Read Git credentials from environment variables
        git_creds = os.environ.get("GIT_CREDENTIALS")
        if git_creds:
            # Clone the repository using Git credentials
            git_password = git_creds.split(":")[1]
            p = subprocess.Popen(
                ["git", "clone", git_repo_url, local_repo_path],
                env={"GIT_ASKPASS": "git-gui--askpass", "GIT_USERNAME": "oauth2"},
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            p.stdin.write(f"{git_creds}\n".encode())
            p.stdin.flush()
            p.wait()
        else:
            # Clone the repository without Git credentials
            subprocess.call(["git", "clone", git_repo_url, local_repo_path])

    while True:
        try:
            # Check the message queue for new messages
            if not message_queue.empty():
                message = message_queue.get()

                # Determine the tag to use based on the message type
                if message["type"] == "chat":
                    tag = "Chat:"
                elif message["type"] == "generated":
                    tag = "AI:"

                # Add the message to a new file in the repository
                file_name = "{}.txt".format(len(os.listdir(local_repo_path)) + 1)
                file_path = os.path.join(local_repo_path, file_name)
                with open(file_path, "w") as f:
                    f.write("{} {}\n".format(tag, message["text"]))

                # Commit the changes to the repository
                p = subprocess.Popen(["git", "add", "."], cwd=local_repo_path)
                p.wait()
                p = subprocess.Popen(
                    ["git", "commit", "-m", "{} {}".format(tag, file_name)], cwd=local_repo_path
                )
                p.wait()

                # Push the changes to the remote repository
                p = subprocess.Popen(["git", "push"], cwd=local_repo_path)
                p.wait()

        except Exception as e:
            print("There was an error: {}".format(e))

        time.sleep(1)
