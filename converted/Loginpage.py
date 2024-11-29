# Loginpage.py
import tkinter as tk
from tkinter import messagebox

class LoginPage:
    def __init__(self, root, show_main_dashboard):
        self.root = root
        self.show_main_dashboard = show_main_dashboard
        self.build_login_page()

    def build_login_page(self):
        self.root.title("Login Page")

        # Username label and text entry box
        username_label = tk.Label(self.root, text="Username")
        username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=10)

        # Password label and password entry box
        password_label = tk.Label(self.root, text="Password")
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack(pady=10)

        # Login button
        login_button = tk.Button(self.root, text="Login", command=self.validate_login)
        login_button.pack(pady=10)

    def validate_login(self):
        # Placeholder login validation logic
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Example validation (Replace with actual validation logic)
        if username == "admin" and password == "password":
            self.show_main_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# Note: The above username and password check is for demonstration purposes only.
# Replace it with your actual authentication mechanism.
