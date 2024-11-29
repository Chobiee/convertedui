import tkinter as tk
from tkinter import messagebox

class AddGroup:
    def __init__(self, root, open_main_dashboard):
        self.root = root
        self.open_main_dashboard = open_main_dashboard
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Add Group", font=("Arial", 20)).pack(pady=20)

        tk.Label(self.root, text="Group Name:").pack(pady=10)
        self.group_name_entry = tk.Entry(self.root)
        self.group_name_entry.pack(pady=10)

        tk.Button(self.root, text="Add Group", command=self.add_group).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.open_main_dashboard).pack(pady=10)

    def add_group(self):
        group_name = self.group_name_entry.get()
        if group_name:
            # You can add MongoDB insertion logic here
            messagebox.showinfo("Success", f"Group '{group_name}' added successfully!")
            self.open_main_dashboard()
        else:
            messagebox.showerror("Error", "Please enter a group name.")
