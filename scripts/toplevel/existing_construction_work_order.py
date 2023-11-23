import customtkinter as ctk


class ExistingConstructionWorkOrder(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Existing Construction Work Order")
        self.geometry("800x600")
        self.resizable(False, False)
        self.config(bg="white")

        self._create_widgets()

    def _create_widgets(self):
        pass
