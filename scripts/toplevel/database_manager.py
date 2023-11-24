import customtkinter as ctk

class DatabaseManagerTopLevel(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Database Manager")
        self.resizable(False, False)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
