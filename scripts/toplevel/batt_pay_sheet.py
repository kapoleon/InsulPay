import customtkinter as ctk
from scripts.database.tables.employee_table import EmployeeTable


class BattPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Batt Pay Sheet")
        self.geometry("500x500")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create the font
        self.font = ctk.CTkFont("Roboto", 12)

        # Retrieve employee information
        self.employees = self.create_employee_db_instance()

        # Create widgets using employee information
        self.create_widgets()

    @staticmethod
    def create_employee_db_instance():
        employee_table = EmployeeTable()
        employee_table.connect()

        employee_ids_to_retrieve = list(range(1, 12))
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

    def create_widgets(self):
        # Create checkboxes for each employee
        for i, employee in enumerate(self.employees):
            if employee:
                checkbox = ctk.CTkCheckBox(self, text=f"{employee[1]} {employee[2]}")
                checkbox.grid(row=i, column=0, padx=10, pady=10)

    def on_closing(self):
        self.destroy()
