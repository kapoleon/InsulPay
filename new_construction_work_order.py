from program_settings import *


class NewConstructionWorkOrder(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("New Construction Work Order")
        self.geometry("800x600")
        self.resizable(False, False)
        self.config(bg="white")

        self._create_widgets()

    def _create_widgets(self):
        label = ctk.CTkLabel(self, text="Coming Soon", font=("Arial", 24))
        label.pack()
