import tkinter as tk

class GroupDashboard:
    def __init__(self, root, open_main_dashboard, open_add_members):
        self.root = root
        self.open_main_dashboard = open_main_dashboard
        self.open_add_members = open_add_members
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Group Dashboard", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="Add Members", command=self.open_add_members).pack(pady=10)
        tk.Button(self.root, text="Back to Main Dashboard", command=self.open_main_dashboard).pack(pady=10)
