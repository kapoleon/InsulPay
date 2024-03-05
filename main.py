from program_settings import *

# Run the script that performs necessary startup checks
check_and_run()
create_directories()


class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Scratch")
        self.geometry("1000x600")
        self.resizable(False, False)

        self.font = ctk.CTkFont(family="Roboto", size=18)

        # Create the menu bar
        self.menu_manager = MenuManager(self)
        self.menu_manager.create_main_menu()

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        self.create_pay_sheet_widgets()
        self.create_work_order_widgets()
        self.create_database_manager()

    def create_pay_sheet_widgets(self):
        create_pay_sheet_label = ctk.CTkLabel(self, text="Create Pay Sheet", font=self.font)
        create_pay_sheet_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        batt_pay_sheet_button = ctk.CTkButton(self,
                                              text="Batt Pay Sheet",
                                              font=self.font,
                                              width=200,
                                              height=30,
                                              command=self.open_batt_pay_sheet_toplevel)
        batt_pay_sheet_button.grid(row=1, column=0, padx=10, pady=10)

        attic_pay_sheet_button = ctk.CTkButton(self, text="Attic Pay Sheet",
                                               font=self.font,
                                               width=200,
                                               height=30,
                                               command=self.open_attic_pay_sheet_toplevel)
        attic_pay_sheet_button.grid(row=2, column=0, padx=10, pady=10)

        foam_pay_sheet_button = ctk.CTkButton(self, text="Foam Pay Sheet",
                                              font=self.font,
                                              width=200,
                                              height=30,
                                              command=self.open_foam_pay_sheet_toplevel)
        foam_pay_sheet_button.grid(row=3, column=0, padx=10, pady=10)

        vacation_request_button = ctk.CTkButton(self, text="Vacation Request",
                                                font=self.font,
                                                width=200,
                                                height=30,
                                                command=self.open_vacation_request_toplevel)
        vacation_request_button.grid(row=1, column=1, padx=10, pady=10)

        shop_pay_sheet_button = ctk.CTkButton(self, text="Shop Pay Sheet",
                                              font=self.font,
                                              width=200,
                                              height=30,
                                              command=self.open_shop_pay_sheet_toplevel)
        shop_pay_sheet_button.grid(row=2, column=1, padx=10, pady=10)

    def create_work_order_widgets(self):
        create_work_order_label = ctk.CTkLabel(self, text="Create Work Order", font=self.font)
        create_work_order_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

        new_construction_button = ctk.CTkButton(self, text="New Construction",
                                                font=self.font,
                                                width=200,
                                                height=30,
                                                command=self.open_new_construction_toplevel)
        new_construction_button.grid(row=1, column=2, padx=10, pady=10)

        existing_construction_button = ctk.CTkButton(self, text="Existing Construction",
                                                     font=self.font,
                                                     width=200,
                                                     height=30,
                                                     command=self.open_existing_construction_toplevel)
        existing_construction_button.grid(row=2, column=2, padx=10, pady=10)

        attic_work_order_button = ctk.CTkButton(self, text="Attic Work Order",
                                                font=self.font,
                                                width=200,
                                                height=30,
                                                command=self.open_attic_work_order_toplevel)
        attic_work_order_button.grid(row=3, column=2, padx=10, pady=10)

        foam_work_order_button = ctk.CTkButton(self, text="Foam Work Order",
                                               font=self.font,
                                               width=200,
                                               height=30,
                                               command=self.open_foam_work_order_toplevel)
        foam_work_order_button.grid(row=1, column=3, padx=10, pady=10)

        shop_work_order_button = ctk.CTkButton(self, text="Shop Work Order",
                                               font=self.font,
                                               width=200,
                                               height=30,
                                               command=self.open_shop_work_order_toplevel)
        shop_work_order_button.grid(row=2, column=3, padx=10, pady=10)

        cellulose_work_order_button = ctk.CTkButton(self, text="Cellulose Work Order",
                                                    font=self.font,
                                                    width=200,
                                                    height=30,
                                                    command=self.open_cellulose_work_order_toplevel)
        cellulose_work_order_button.grid(row=3, column=3, padx=10, pady=10)

    def create_database_manager(self):
        database_manager_label = ctk.CTkLabel(self, text="Database Manager", font=self.font)
        database_manager_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        employee_table_manager_button = ctk.CTkButton(self,
                                                      text="Employee Table",
                                                      font=self.font,
                                                      width=200,
                                                      height=30,
                                                      command=self.open_employee_table_manager_toplevel)
        employee_table_manager_button.grid(row=5, column=0, padx=10, pady=10)

        batt_pay_rate_table_manager_button = ctk.CTkButton(self,
                                                           text="Batt Pay Rate Table",
                                                           font=self.font,
                                                           width=200,
                                                           height=30,
                                                           command=self.open_batt_pay_rate_table_manager_toplevel)
        batt_pay_rate_table_manager_button.grid(row=6, column=0, padx=10, pady=10)

        attic_pay_rate_table_manager_button = ctk.CTkButton(self,
                                                            text="Attic Pay Rate Table",
                                                            font=self.font,
                                                            width=200,
                                                            height=30,
                                                            command=self.open_attic_pay_rate_table_manager_toplevel)
        attic_pay_rate_table_manager_button.grid(row=7, column=0, padx=10, pady=10)

        foam_pay_rate_table_manager_button = ctk.CTkButton(self,
                                                           text="Foam Pay Rate Table",
                                                           font=self.font,
                                                           width=200,
                                                           height=30,
                                                           command=self.open_foam_pay_rate_table_manager_toplevel)
        foam_pay_rate_table_manager_button.grid(row=8, column=0, padx=10, pady=10)

        vacation_rate_table_manager_button = ctk.CTkButton(self, text="Vacation Pay Rate Table",
                                                              font=self.font,
                                                              width=200,
                                                              height=30,
                                                              command=self.open_vacation_table_manager_toplevel)
        vacation_rate_table_manager_button.grid(row=9, column=0, padx=10, pady=10)

    def open_foam_pay_rate_table_manager_toplevel(self):
        window = FoamPayRateTableManager(self)
        window.grab_set()

    def open_attic_pay_rate_table_manager_toplevel(self):
        window = AtticPayRateTableManager(self)
        window.grab_set()

    def open_batt_pay_rate_table_manager_toplevel(self):
        window = BattPayRateTableManager(self)
        window.grab_set()

    def open_employee_table_manager_toplevel(self):
        window = EmployeeTableNotebook(self)
        window.grab_set()

    def open_vacation_table_manager_toplevel(self):
        window = VacationPayRateTableManager(self)
        window.grab_set()

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

    @staticmethod
    def open_new_construction_toplevel():
        window = NewConstructionWorkOrder()
        window.grab_set()

    @staticmethod
    def open_existing_construction_toplevel():
        window = ExistingConstructionWorkOrder()
        window.grab_set()

    @staticmethod
    def open_attic_work_order_toplevel():
        window = AtticWorkOrder()
        window.grab_set()

    @staticmethod
    def open_foam_work_order_toplevel():
        window = SprayFoamWorkOrder()
        window.grab_set()

    @staticmethod
    def open_shop_work_order_toplevel():
        window = ShopWorkOrder()
        window.grab_set()

    @staticmethod
    def open_cellulose_work_order_toplevel():
        window = CelluloseWorkOrder()
        window.grab_set()

    # Close the Application
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    app = MainApplication()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
