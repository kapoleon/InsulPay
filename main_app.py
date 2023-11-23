from scripts.insulpay_imports import *


class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Scratch")
        self.geometry("800x600")
        self.resizable(False, False)

        # Create the menu bar
        self.menu_manager = MenuManager(self)
        self.menu_manager.create_main_menu()

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        create_pay_sheet_label = ctk.CTkLabel(self, text="Create Pay Sheet")
        create_pay_sheet_label.grid(row=0, column=0, padx=10, pady=10)

        batt_pay_sheet_button = ctk.CTkButton(self, text="Batt Pay Sheet", command=self.open_batt_pay_sheet_toplevel)
        batt_pay_sheet_button.grid(row=1, column=0, padx=10, pady=10)

        attic_pay_sheet_button = ctk.CTkButton(self, text="Attic Pay Sheet", command=self.open_attic_pay_sheet_toplevel)
        attic_pay_sheet_button.grid(row=2, column=0, padx=10, pady=10)

        foam_pay_sheet_button = ctk.CTkButton(self, text="Foam Pay Sheet", command=self.open_foam_pay_sheet_toplevel)
        foam_pay_sheet_button.grid(row=3, column=0, padx=10, pady=10)

        vacation_request_button = ctk.CTkButton(self, text="Vacation Request",
                                                command=self.open_vacation_request_toplevel)
        vacation_request_button.grid(row=4, column=0, padx=10, pady=10)

        shop_pay_sheet_button = ctk.CTkButton(self, text="Shop Pay Sheet",
                                              command=self.open_shop_pay_sheet_toplevel)
        shop_pay_sheet_button.grid(row=5, column=0, padx=10, pady=10)

    @staticmethod
    def open_batt_pay_sheet_toplevel():
        window = BattPaySheetTopLevel()
        window.grab_set()

    @staticmethod
    def open_attic_pay_sheet_toplevel():
        window = AtticPaySheetTopLevel()
        window.grab_set()

    @staticmethod
    def open_foam_pay_sheet_toplevel():
        window = FoamPaySheetTopLevel()
        window.grab_set()

    @staticmethod
    def open_vacation_request_toplevel():
        window = VacationRequestTopLevel()
        window.grab_set()

    @staticmethod
    def open_shop_pay_sheet_toplevel():
        window = ShopPaySheetTopLevel()
        window.grab_set()

    # Close the Application
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    app = MainApplication()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
