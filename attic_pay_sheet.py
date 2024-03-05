from program_settings import *


# noinspection PyTypeChecker
class AtticPaySheetTopLevel(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Attic Pay Sheet")
        self.geometry("800x750")
        self.resizable(True, True)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Create the font
        self.font = ctk.CTkFont("Roboto", 15)

        # Retrieve employee information
        self.employees = self.create_employee_db_instance()

        # Retrieve attic pay rate information
        self.rates = self.create_attic_pay_rate_database_instance()

        # Create the  list for variables for the checkboxes
        self.checkbox_vars = []

        # Create the list to store the pay rate entries
        self.entry_widgets = []

        # Create widgets using database information
        self.create_widgets()

        # Create instance variables for total pay and average pay entry widgets
        self.total_pay_label = ctk.CTkLabel(self, text="Total Pay:", font=self.font)
        self.total_pay_label.grid(row=1, column=3, padx=10, pady=10)

        self.total_pay_entry = ctk.CTkEntry(self)
        self.total_pay_entry.grid(row=1, column=4, padx=10, pady=10)
        self.total_pay_entry.insert(0, 0)

        self.average_pay_label = ctk.CTkLabel(self, text="Average Pay:", font=self.font)
        self.average_pay_label.grid(row=2, column=3, padx=10, pady=10)

        self.average_pay_entry = ctk.CTkEntry(self)
        self.average_pay_entry.grid(row=2, column=4, padx=10, pady=10)
        self.average_pay_entry.insert(0, 0)

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
    def create_attic_pay_rate_database_instance():
        attic_pay_rate_table = AtticPayRateTable()
        attic_pay_rate_table.connect()

        attic_ids_to_retrieve = list(range(1, 10))
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
        self.create_employee_checkboxes()
        self.create_pay_rate_entries()

        # Create the calculate pay button
        calculate_pay_button = ctk.CTkButton(self, text="Calculate Pay", font=self.font,
                                             command=self.calculate_total_pay)
        calculate_pay_button.grid(row=4, column=3, columnspan=2, padx=10, pady=10)

        # Create the save file button
        save_file_button = ctk.CTkButton(self, text="Save File", font=self.font,
                                         command=self.save_file)
        save_file_button.grid(row=5, column=3, columnspan=2, padx=10, pady=10)

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

    def get_entry_values(self, index):
        return self.entry_widgets[index].get()

    def calculate_total_pay(self):
        total_pays = [0] * 9  # Initialize a list to store total pay for each entry

        # Iterate through each entry
        for i in range(9):
            # Retrieve the value of the entry and convert it to a float
            entry_value = float(self.get_entry_values(i))
            # Assuming the rate is stored in the third column of the rates list
            rate = float(self.rates[i][2])
            # Calculate and store the total pay for the current entry
            total_pays[i] = entry_value * rate

        # Print individual total pays for each entry
        for index, total_pay in enumerate(total_pays, start=1):
            print(f"Total pay for entry {index}: {total_pay}")

        # Calculate and print the total pay for the entire job
        job_total_pay = sum(total_pays)
        print(f"Total pay for the job: {job_total_pay}")

        # Set the value of the total pay entry widget
        self.total_pay_entry.delete(0, 'end')  # Clear the entry
        self.total_pay_entry.insert(0, str(job_total_pay))  # Insert the new value

        # Calculate the average pay and print it
        self.calculate_average_pay(job_total_pay, count=self.count_checked_checkboxes())

    def calculate_average_pay(self, job_total_pay, count):
        # avoid division by zero
        if count == 0:
            print("Cannot calculate average pay with zero entries.")
            return

        average_pay = job_total_pay / count

        # Set the value of the average pay entry widget
        self.average_pay_entry.delete(0, 'end')  # Clear the entry
        self.average_pay_entry.insert(0, str(average_pay))

        print(f"Average pay: {average_pay}")

    def save_file(self):
        print("Saving file...")
        job_name = self.get_job_name_dialog().get_input()

        if job_name:
            print(f"Saving file for Job: {job_name}")
            self.add_pay_sheet_to_database(job_name)
            self.copy_pay_sheet_template()
            self.create_pay_spreadsheet(job_name)
            self.append_pay_spreadsheet(job_name)
            self.clear_entries()

            # message box to confirm file was saved
            messagebox.showinfo("File Saved", f"File for Job: {job_name} saved.")

            self.on_closing()

        else:
            print("Job name not provided. File not saved.")

    @staticmethod
    def get_job_name_dialog():
        job_name = ctk.CTkInputDialog(text="Enter the job name:", title="Job Name")
        return job_name

    def add_pay_sheet_to_database(self, job_name):
        attic_pay_sheet_table = AtticPaySheetTable()
        attic_pay_sheet_table.connect()
        attic_pay_sheet_table.create_table()

        # initialize list to store values for each entry
        values = [0] * 9

        # iterate through each entry
        for i in range(9):
            # retrieve the value of the entry and convert it to a float
            entry_value = float(self.get_entry_values(i))
            # store the value in the values list
            # noinspection PyTypeChecker
            values[i] = entry_value

        # add the values to the database
        attic_pay_sheet_table.add_attic_record(job_name=job_name,
                                               r19=values[0],
                                               r30=values[1],
                                               r38=values[2],
                                               r49=values[3],
                                               cellulose=values[4],
                                               soffits=values[5],
                                               bonus_amount=values[6],
                                               other_amount=values[7],
                                               air_seal=values[8])

        attic_pay_sheet_table.disconnect()

    def clear_entries(self):
        for entry in self.entry_widgets:
            entry.delete(0, 'end')

            entry.insert(0, 0)

        self.total_pay_entry.delete(0, 'end')
        self.total_pay_entry.insert(0, 0)

        self.average_pay_entry.delete(0, 'end')
        self.average_pay_entry.insert(0, 0)

    @staticmethod
    def copy_pay_sheet_template():
        print("Copying template file...")
        # Get the path of the template file
        template_path = os.path.join(os.getcwd(), "templates", "Attic Pay Sheet.xlsx")
        print(f"Template path: {template_path}")

        # Get the path of the destination file
        destination_path = os.path.join(os.getcwd(), "temp", "pay sheets", "attic pay sheets", "Attic Pay Sheet.xlsx")
        print(f"Destination path: {destination_path}")

        # Copy the template file to the destination file
        shutil.copyfile(template_path, destination_path)
        print("Template file copied.")

    @staticmethod
    def create_pay_spreadsheet(job_name):
        file_name = f"{job_name}.xlsx"

        print("Creating pay spreadsheet...")
        os.rename(os.path.join(os.getcwd(), "temp", "pay sheets", "attic pay sheets", "Attic Pay Sheet.xlsx"),
                  os.path.join(os.getcwd(), "temp", "pay sheets", "attic pay sheets", file_name))

        workbook = openpyxl.load_workbook(
            os.path.join(os.getcwd(), "temp", "pay sheets", "attic pay sheets", file_name))
        sheet = workbook.active

        # add the job name to the spreadsheet
        sheet['A2'] = job_name

        workbook.save(os.path.join(os.getcwd(), "temp", "pay sheets", "attic pay sheets", file_name))

        workbook.close()

    def append_pay_spreadsheet(self, job_name):

        file_name = f"{job_name}.xlsx"

        # Load the existing workbook
        workbook = openpyxl.load_workbook(
            os.path.join(os.getcwd(), "temp", "pay sheets", "attic pay sheets", file_name))
        sheet = workbook.active

        # Append the employee names and calculated values for checked checkboxes
        for i, (employee, checkbox_var) in enumerate(zip(self.employees, self.checkbox_vars)):
            if employee and checkbox_var.get() == 1:
                # Append employee name to the spreadsheet
                sheet.cell(row=i + 5, column=1).value = f"{employee[1]} {employee[2]}"
                print(f"Employee {i + 1} name added to spreadsheet.")

                # append the calculated value to the spreadsheet
                for j in range(9):
                    # retrieve the value of the entry and convert it to a float
                    entry_value = float(self.get_entry_values(j))
                    # Assuming the rate is stored in the third column of the rates list
                    rate = float(self.rates[j][2])
                    # Calculate and store the total pay for the current entry
                    total_pay = entry_value * rate / self.count_checked_checkboxes()

                    # append the total pay to the spreadsheet
                    sheet.cell(row=i + 5, column=j + 2).value = total_pay
                    print(f"Total pay for employee {i + 1} added to spreadsheet.")

        # Save the workbook
        workbook.save(os.path.join(os.getcwd(), "temp", "pay sheets", "attic pay sheets", file_name))

        # Close the workbook
        workbook.close()

    def on_closing(self):
        self.destroy()
