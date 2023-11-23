import customtkinter as ctk

class VacationRequestTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Vacation Request")
        self.geometry("800x600")
        self.resizable(False, False)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        pass
