import customtkinter as ctk
from scripts.database.tables.employee_table import EmployeeTable
from scripts.database.tables.foam_pay_rate_table import FoamPayRateTable


class FoamPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Foam Pay Sheet")
        self.geometry("800x600")
        self.resizable(False, False)

        # Create the font
        self.font = ctk.CTkFont("Roboto", 15)

        # Retrieve employee information
        self.employees = self.create_employee_db_instance()

        # Retrieve foam pay rate information
        self.rates = self.create_foam_pay_rate_database_instance()

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
    def create_foam_pay_rate_database_instance():
        foam_pay_rate_table = FoamPayRateTable()
        foam_pay_rate_table.connect()

        foam_ids_to_retrieve = list(range(1, 12))
        rates = []

        for foam_pay_rate_id in foam_ids_to_retrieve:
            rate = foam_pay_rate_table.view_foam_pay_rate_by_id(foam_pay_rate_id)
            rates.append(rate)

            if rate:
                print("Foam pay rate found:")
                print(
                    f"Rate ID: {rate[0]}, Rate Name: {rate[1]}, Rate Amount: {rate[2]}, "
                    f"Rate Description: {rate[3]}")
            else:
                print("Foam pay rate not found.")

        foam_pay_rate_table.disconnect()
        return rates

    def create_widgets(self):
        # Create checkboxes for each employee
        for i, employee in enumerate(self.employees):
            if employee:
                checkbox = ctk.CTkCheckBox(self, text=f"{employee[1]} {employee[2]}", font=self.font)
                checkbox.grid(row=i, column=0, padx=10, pady=10)

        # Create the label and entry for the bay pay rate widgets
        for i, rate in enumerate(self.rates):
            if rate:
                label = ctk.CTkLabel(self, text=f"{rate[1]}:", font=self.font)
                label.grid(row=i, column=1, padx=10, pady=10)

                entry = ctk.CTkEntry(self)
                entry.grid(row=i, column=2, padx=10, pady=10)

    def on_closing(self):
        self.destroy()
