import customtkinter as ctk


class AtticWorkOrder(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Attic Work Order")
        self.geometry("800x600")
        self.resizable(False, False)
        self.config(bg="white")

        self._create_widgets()

    def _create_widgets(self):
        pass
