from program_settings import *


class EmployeeTableNotebook:
    def __init__(self, parent):
        self.top_level = tk.Toplevel(parent)
        self.top_level.title("Employee Table Manager")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Employee")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="Edit Employee")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Delete Employee")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="View Employees")

    def pack(self):
        self.notebook.pack(expand=True, fill='both')

    def grab_set(self):
        self.top_level.grab_set()
        self.top_level.wait_window()

    def destroy(self):
        self.top_level.destroy()

    def mainloop(self):
        self.top_level.mainloop()


class TabOne:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Add Employee", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.first_name_label = ctk.CTkLabel(self.frame, text="First Name:")
        self.first_name_entry = ctk.CTkEntry(self.frame)
        self.last_name_label = ctk.CTkLabel(self.frame, text="Last Name:")
        self.last_name_entry = ctk.CTkEntry(self.frame)
        self.vacation_days_label = ctk.CTkLabel(self.frame, text="Vacation Days:")
        self.vacation_days_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.add_employee_button = ctk.CTkButton(self.frame, text="Add Employee", command=self.add_employee)

        # Place the widgets
        self.first_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.last_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.vacation_days_label.grid(row=3, column=0, padx=10, pady=10)
        self.vacation_days_entry.grid(row=3, column=1, padx=10, pady=10)
        self.add_employee_button.grid(row=4, column=0, padx=10, pady=10)

        # Set the focus to the first name entry box
        self.first_name_entry.focus_set()

    def add_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        vacation_days = self.vacation_days_entry.get()

        # Check if the user entered all the required information
        if first_name == "" or last_name == "" or vacation_days == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the vacation days is a number
        try:
            vacation_days = int(vacation_days)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for vacation days!")
            return

        # Check if the vacation days is a positive number
        if vacation_days < 0:
            messagebox.showerror("Error", "Please enter a positive number for vacation days!")
            return

        # Add the employee to the database
        employee_table = EmployeeTable()
        employee_table.connect()
        employee_table.create_table()
        employee_table.add_employee(first_name, last_name, vacation_days)

        messagebox.showinfo("Success", "Employee added successfully!")

        # Clear the entry boxes
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.vacation_days_entry.delete(0, 'end')


class TabTwo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Edit Employee", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.first_name_label = ctk.CTkLabel(self.frame, text="First Name:")
        self.first_name_entry = ctk.CTkEntry(self.frame)

        self.last_name_label = ctk.CTkLabel(self.frame, text="Last Name:")
        self.last_name_entry = ctk.CTkEntry(self.frame)

        self.new_first_name_label = ctk.CTkLabel(self.frame, text="New First Name:")
        self.new_first_name_entry = ctk.CTkEntry(self.frame)

        self.new_last_name_label = ctk.CTkLabel(self.frame, text="New Last Name:")
        self.new_last_name_entry = ctk.CTkEntry(self.frame)

        self.new_vacation_days_label = ctk.CTkLabel(self.frame, text="New Vacation Days:")
        self.new_vacation_days_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.edit_employee_button = ctk.CTkButton(self.frame, text="Edit Employee", command=self.edit_employee)

        # Place the widgets
        self.first_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.last_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_first_name_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_first_name_entry.grid(row=3, column=1, padx=10, pady=10)
        self.new_last_name_label.grid(row=4, column=0, padx=10, pady=10)
        self.new_last_name_entry.grid(row=4, column=1, padx=10, pady=10)
        self.new_vacation_days_label.grid(row=5, column=0, padx=10, pady=10)
        self.new_vacation_days_entry.grid(row=5, column=1, padx=10, pady=10)
        self.edit_employee_button.grid(row=6, column=0, padx=10, pady=10)

    def edit_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        new_first_name = self.new_first_name_entry.get()
        new_last_name = self.new_last_name_entry.get()
        new_vacation_days = self.new_vacation_days_entry.get()

        # Check if the user entered all the required information
        if (first_name == "" or last_name == "" or new_first_name == "" or new_last_name == "" or
                new_vacation_days == ""):
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the vacation days is a number
        try:
            new_vacation_days = int(new_vacation_days)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for vacation days!")
            return

        # Check if the vacation days is a positive number
        if new_vacation_days < 0:
            messagebox.showerror("Error", "Please enter a positive number for vacation days!")
            return

        # Edit the employee in the database
        employee_table = EmployeeTable()
        employee_table.connect()
        employee_table.create_table()
        employee_table.edit_employee(first_name, last_name, new_first_name, new_last_name, new_vacation_days)

        messagebox.showinfo("Success", "Employee edited successfully!")

        # Clear the entry boxes
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')
        self.new_first_name_entry.delete(0, 'end')
        self.new_last_name_entry.delete(0, 'end')
        self.new_vacation_days_entry.delete(0, 'end')


class TabThree:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Delete Employee", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.first_name_label = ctk.CTkLabel(self.frame, text="First Name:")
        self.first_name_entry = ctk.CTkEntry(self.frame)
        self.last_name_label = ctk.CTkLabel(self.frame, text="Last Name:")
        self.last_name_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.delete_employee_button = ctk.CTkButton(self.frame, text="Delete Employee", command=self.delete_employee)

        # Place the widgets
        self.first_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.last_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.delete_employee_button.grid(row=3, column=0, padx=10, pady=10)

        # Set the focus to the first name entry box
        self.first_name_entry.focus_set()

    def delete_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()

        # Check if the user entered all the required information
        if first_name == "" or last_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Delete the employee in the database
        employee_table = EmployeeTable()
        employee_table.connect()
        employee_table.create_table()
        employee_table.delete_employee(first_name, last_name)

        messagebox.showinfo("Success", "Employee deleted successfully!")

        # Clear the entry boxes
        self.first_name_entry.delete(0, 'end')
        self.last_name_entry.delete(0, 'end')


class TabFour:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="View Employees", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        self.first_label = ctk.CTkLabel(self.frame, text="First Name")
        self.first_entry = ctk.CTkEntry(self.frame)
        self.last_label = ctk.CTkLabel(self.frame, text="Last Name")
        self.last_entry = ctk.CTkEntry(self.frame)
        self.view_employee_button = ctk.CTkButton(self.frame, text="View Employee", command=self.view_employee)

        self.first_label.grid(row=1, column=0, padx=10, pady=10)
        self.first_entry.grid(row=1, column=1, padx=10, pady=10)
        self.last_label.grid(row=2, column=0, padx=10, pady=10)
        self.last_entry.grid(row=2, column=1, padx=10, pady=10)
        self.view_employee_button.grid(row=3, column=0, padx=10, pady=10)

        # Set the focus to the first name entry box
        self.first_entry.focus_set()

    def view_employee(self):
        first_name = self.first_entry.get()
        last_name = self.last_entry.get()

        # Check if the user entered all the required information
        if first_name == "" or last_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # View the employee in the database
        employee_table = EmployeeTable()
        employee_table.connect()
        employee_table.create_table()
        try:
            employee_data = employee_table.view_employee(first_name, last_name)
            if employee_data:
                # Create a string representation of the employee information
                employee_info = "\n".join([f"{key}: {value}" for key, value in
                                           zip(["ID", "First Name", "Last Name", "Vacation Days"], employee_data[0])])
                messagebox.showinfo("Employee Information", f"Employee Details:\n{employee_info}")
            else:
                messagebox.showinfo("Employee Not Found", "No employee found with the given details.")
        except Exception as e:
            messagebox.showerror("Error", f"Error viewing employee: {e}")

        # Clear the entry boxes
        self.first_entry.delete(0, 'end')
        self.last_entry.delete(0, 'end')
