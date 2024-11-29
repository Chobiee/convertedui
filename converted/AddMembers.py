import tkinter as tk
from tkinter import messagebox

class AddMembers:
    def __init__(self, root, open_group_dashboard):
        self.root = root
        self.open_group_dashboard = open_group_dashboard
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Add Members", font=("Arial", 20)).pack(pady=20)

        tk.Label(self.root, text="Member Name:").pack(pady=10)
        self.member_name_entry = tk.Entry(self.root)
        self.member_name_entry.pack(pady=10)

        tk.Label(self.root, text="Member IP:").pack(pady=10)
        self.member_ip_entry = tk.Entry(self.root)
        self.member_ip_entry.pack(pady=10)

        tk.Button(self.root, text="Add Member", command=self.add_member).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.open_group_dashboard).pack(pady=10)

    def add_member(self):
        member_name = self.member_name_entry.get()
        member_ip = self.member_ip_entry.get()
        if member_name and member_ip:
            # You can add MongoDB insertion logic here
            messagebox.showinfo("Success", f"Member '{member_name}' added successfully!")
            self.open_group_dashboard()
        else:
            messagebox.showerror("Error", "Please fill out all fields.")
