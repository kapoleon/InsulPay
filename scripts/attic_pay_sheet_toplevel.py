import customtkinter as ctk

class AtticPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Attic Pay Sheet")
        self.geometry("500x500")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()
