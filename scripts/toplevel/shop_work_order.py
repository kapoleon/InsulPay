import customtkinter as ctk


class ShopWorkOrder(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Shop Work Order")
        self.geometry("800x600")
        self.resizable(False, False)
        self.config(bg="white")

        self._create_widgets()

    def _create_widgets(self):
        pass
