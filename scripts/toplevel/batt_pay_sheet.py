import customtkinter as ctk
from scripts.database.tables.employee_table import EmployeeTable
from scripts.database.tables.batt_pay_rate_table import BattPayRateTable


class BattPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Batt Pay Sheet")
        self.geometry("800x800")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create the font
        self.font = ctk.CTkFont("Roboto", 15)

        # Retrieve employee information
        self.employees = self.create_employee_db_instance()

        # Retrieve bay pay rate information
        self.rates = self.create_batt_pay_rate_database_instance()

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
    def create_batt_pay_rate_database_instance():
        batt_pay_rate_table = BattPayRateTable()
        batt_pay_rate_table.connect()

        batt_ids_to_retrieve = list(range(1, 12))
        rates = []

        for batt_pay_rate_id in batt_ids_to_retrieve:
            rate = batt_pay_rate_table.view_batt_pay_rate_by_id(batt_pay_rate_id)
            rates.append(rate)

            if rate:
                print("Batt pay rate found:")
                print(
                    f"Rate ID: {rate[0]}, Rate Name: {rate[1]}, Rate Amount: {rate[2]}, "
                    f"Rate Description: {rate[3]}")
            else:
                print("Batt pay rate not found.")

        batt_pay_rate_table.disconnect()
        return rates

    def create_widgets(self):
        self.create_employee_checkboxes()
        self.create_pay_rate_entries()

        # Create the calculate pay button
        calculate_pay_button = ctk.CTkButton(self, text="Calculate Pay", font=self.font, command=self.calculate_pay)
        calculate_pay_button.grid(row=11, column=0, padx=10, pady=10)


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
        # Create the label and entry for the bay pay rate widgets
        for i, rate in enumerate(self.rates):
            if rate:
                label = ctk.CTkLabel(self, text=f"{rate[1]}:", font=self.font)
                label.grid(row=i, column=1, padx=10, pady=10)

                entry = ctk.CTkEntry(self)
                entry.grid(row=i, column=2, padx=10, pady=10)

                # Store the entry widgets in a list
                self.entry_widgets.append(entry)

    def checkbox_clicked(self):
        for i, checkbox_var in enumerate(self.checkbox_vars):
            if checkbox_var.get() == 1:
                print(f"Checkbox {i + 1} is checked.")

    def get_entry_values(self, index):
        return self.entry_widgets[index].get()

# todo finish this method so all the pay rates are calculated
    def calculate_pay(self):
        total_pay = 0
        entry_value = float(self.get_entry_values(0))
        rate = float(self.rates[0][2])  # Assuming the rate is stored in the third column of the rates list
        total_pay += entry_value * rate
        print(total_pay)



    def on_closing(self):
        self.destroy()
