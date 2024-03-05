from program_settings import *


# todo finish this to go to database and spreadsheet
class VacationRequestTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Vacation Request")
        self.geometry("800x750")
        self.resizable(False, False)

        # Create the font
        self.font = ctk.CTkFont("Roboto", 15)

        # Retrieve employee information
        self.employees = self.create_employee_db_instance()

        # Retrieve the vacation pay rate information
        self.rates = self.create_vacation_pay_rate_db_instance()

        # Create the  list for variables for the checkboxes
        self.checkbox_vars = []

        # Create the list to store the pay rate entries
        self.entry_widgets = []

        # Create widgets using database information
        self.create_widgets()

    @staticmethod
    def create_employee_db_instance():
        employee_table = EmployeeTable()
        employee_table.connect()

        employee_ids_to_retrieve = list(range(1, 16))
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
    def create_vacation_pay_rate_db_instance():
        vacation_pay_rate_table = VacationPayRateTable()
        vacation_pay_rate_table.connect()

        rates = vacation_pay_rate_table.view_all_vacation_pay_rates()

        for rate in rates:
            print(f"Vacation pay rate found: {rate[0]} days = {rate[1]}%")

        vacation_pay_rate_table.disconnect()
        return rates

    def create_widgets(self):
        self.create_employee_checkboxes()
        self.create_pay_rate_entries()

    def create_employee_checkboxes(self):
        # Create checkboxes for each employee
        for i, employee in enumerate(self.employees):
            if employee:
                checkbox_var = ctk.IntVar(value=0)
                self.checkbox_vars.append(checkbox_var)

                # Create the checkbox
                checkbox = ctk.CTkCheckBox(self,
                                           text=f"{employee[1]} {employee[2]}",
                                           font=self.font,
                                           variable=checkbox_var,
                                           onvalue=1,
                                           offvalue=0,
                                           command=self.checkbox_clicked)
                checkbox.grid(row=i, column=0, padx=10, pady=10)

    def create_pay_rate_entries(self):
        # Create the label and entry for the attic pay rate widgets
        for i, rate in enumerate(self.rates):
            if rate:
                label = ctk.CTkLabel(self, text=f"{rate[1]}:", font=self.font)
                label.grid(row=i, column=1, padx=10, pady=10)

                entry = ctk.CTkEntry(self)
                entry.grid(row=i, column=2, padx=10, pady=10)

                entry.insert(0, 0)

                # Store the entry widgets in a list
                self.entry_widgets.append(entry)

    def checkbox_clicked(self):
        for i, checkbox_var in enumerate(self.checkbox_vars):
            if checkbox_var.get() == 1:
                print(f"Checkbox {i + 1} is checked.")

        print(f"Total checked checkboxes: {self.count_checked_checkboxes()}")

    def count_checked_checkboxes(self):
        count = 0

        for checkbox_var in self.checkbox_vars:
            if checkbox_var.get() == 1:
                count += 1

        return count
