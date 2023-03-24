import os
import subprocess
import multiprocessing

def run_chat_process():
    subprocess.call(["python", "chat.py"])

def run_git_process():
    subprocess.call(["python", "git.py"])

def main():
    # Set up message queue
    message_queue = multiprocessing.Queue()

    # Start chat process
    chat_process = multiprocessing.Process(target=run_chat_process, args=(message_queue,))
    chat_process.start()

    # Start git process
    git_process = multiprocessing.Process(target=run_git_process, args=(message_queue,))
    git_process.start()

    # Wait for processes to finish
    chat_process.join()
    git_process.join()

if __name__ == "__main__":
    main()
