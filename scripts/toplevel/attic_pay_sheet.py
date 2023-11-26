import customtkinter as ctk
from scripts.database.tables.employee_table import EmployeeTable
from scripts.database.tables.attic_pay_rate_table import AtticPayRateTable


class AtticPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Attic Pay Sheet")
        self.geometry("800x600")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create the font
        self.font = ctk.CTkFont("Roboto", 15)

        # Retrieve employee information
        self.employees = self.create_employee_db_instance()

        # Retrieve attic pay rate information
        self.rates = self.create_attic_pay_rate_database_instance()

        # Create widgets using database information
        self.create_widgets()

    @staticmethod
    def create_employee_db_instance():
        employee_table = EmployeeTable()
        employee_table.connect()

        employee_ids_to_retrieve = list(range(1, 11))
        employees = []

        for emp_id in employee_ids_to_retrieve:
            employee = employee_table.view_employee_by_id(emp_id)
            employees.append(employee)

            if employee:
                print("Employee found:")
                print(
                    f"Employee ID: {employee[0]}, First Name: {employee[1]}, Last Name: {employee[2]}, "
                    f"Vacation Days: {employee[3]}")
            else:
                print("Employee not found.")

        employee_table.disconnect()
        return employees

    @staticmethod
    def create_attic_pay_rate_database_instance():
        attic_pay_rate_table = AtticPayRateTable()
        attic_pay_rate_table.connect()

        attic_ids_to_retrieve = list(range(1, 12))
        rates = []

        for attic_pay_rate_id in attic_ids_to_retrieve:
            rate = attic_pay_rate_table.view_attic_pay_rate_by_id(attic_pay_rate_id)
            rates.append(rate)

            if rate:
                print("Attic Pay Rate found:")
                print(
                    f"Rate ID: {rate[0]}, Rate Name: {rate[1]}, "
                    f"Rate Amount: {rate[2]}, Attic Pay Rate Description: {rate[3]}")
            else:
                print("Attic Pay Rate not found.")

        attic_pay_rate_table.disconnect()
        return rates

    def create_widgets(self):
        # Create checkboxes for each employee
        for i, employee in enumerate(self.employees):
            if employee:
                checkbox = ctk.CTkCheckBox(self, text=f"{employee[1]} {employee[2]}", font=self.font)
                checkbox.grid(row=i, column=0, padx=10, pady=10)

        # Create the labels and entry boxes for each rate
        for i, rate in enumerate(self.rates):
            if rate:
                label = ctk.CTkLabel(self, text=f"{rate[1]}", font=self.font)
                label.grid(row=i, column=1, padx=10, pady=10)

                entry = ctk.CTkEntry(self, font=self.font)
                entry.grid(row=i, column=2, padx=10, pady=10)

    def on_closing(self):
        self.destroy()
