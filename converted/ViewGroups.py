import tkinter as tk

class ViewGroups:
    def __init__(self, root, open_main_dashboard):
        self.root = root
        self.open_main_dashboard = open_main_dashboard
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="View Groups", font=("Arial", 20)).pack(pady=20)

        # You can list groups here
        tk.Label(self.root, text="(List of Groups)").pack(pady=20)

        tk.Button(self.root, text="Back", command=self.open_main_dashboard).pack(pady=10)
