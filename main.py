import os
import subprocess
import multiprocessing

def run_chat_process(message_queue):
    subprocess.call(["python", "chat.py", str(message_queue._address)])

def run_git_process(message_queue):
    subprocess.call(["python", "git_utils.py", str(message_queue._address)])

def main():
    # Set up shared message queue
    manager = multiprocessing.Manager()
    message_queue = manager.Queue()

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
