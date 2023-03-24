import tkinter as tk
from tkinter import simpledialog

def get_user_input():
    # Display a prompt for the user to enter a message
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring(title="Enter your message", prompt="Type your message here:")
    return user_input

