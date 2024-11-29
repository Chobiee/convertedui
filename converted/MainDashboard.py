import tkinter as tk

class MainDashboard:
    def __init__(self, root, open_group_dashboard, open_add_group, open_view_groups):
        self.root = root
        self.open_group_dashboard = open_group_dashboard
        self.open_add_group = open_add_group
        self.open_view_groups = open_view_groups
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Main Dashboard", font=("Arial", 20)).pack(pady=20)

        tk.Button(self.root, text="View Groups", command=self.open_view_groups).pack(pady=10)
        tk.Button(self.root, text="Add Group", command=self.open_add_group).pack(pady=10)
        tk.Button(self.root, text="Manage Groups", command=self.open_group_dashboard).pack(pady=10)
