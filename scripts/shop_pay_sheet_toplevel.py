import customtkinter as ctk


class ShopPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Shop Pay Sheet")
        self.geometry("800x600")
        self.resizable(False, False)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        pass
