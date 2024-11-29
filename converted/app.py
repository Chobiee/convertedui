import tkinter as tk
from .Loginpage import LoginPage
from .MainDashboard import MainDashboard
from .GroupDashboard import GroupDashboard
from .AddGroup import AddGroup
from .ViewGroups import ViewGroups
from .AddMembers import AddMembers

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Application")
        self.show_login_page()

    def show_login_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        LoginPage(self.root, self.show_main_dashboard)

    def show_main_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        MainDashboard(
            self.root,
            open_group_dashboard=self.show_group_dashboard,
            open_add_group=self.show_add_group,
            open_view_groups=self.show_view_groups,
        )

    def show_group_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        GroupDashboard(
            self.root,
            open_main_dashboard=self.show_main_dashboard,
            open_add_members=self.show_add_members,
        )

    def show_add_group(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        AddGroup(self.root, open_main_dashboard=self.show_main_dashboard)

    def show_view_groups(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        ViewGroups(self.root, open_main_dashboard=self.show_main_dashboard)

    def show_add_members(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        AddMembers(self.root, open_group_dashboard=self.show_group_dashboard)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
