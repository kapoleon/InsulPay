import customtkinter as ctk

class FoamPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Foam Pay Sheet")
        self.geometry("800x600")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        pass