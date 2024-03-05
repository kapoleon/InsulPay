from program_settings import *


class ShopPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Shop Pay Sheet")
        self.geometry("800x600")
        self.resizable(False, False)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        label = ctk.CTkLabel(self, text="Coming Soon", font=("Arial", 24))
        label.pack()
