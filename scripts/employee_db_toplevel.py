from scripts.employee_table import EmployeeTable
import customtkinter as ctk
from tkinter import messagebox

'''Employee Management Windows'''


# Add Employee Window Class
class AddEmployeeWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Add Employee")
        self.geometry("400x300")
        self.resizable(False, False)

        # Create the labels and entry boxes
        self.first_name_label = ctk.CTkLabel(self, text="First Name:")
        self.first_name_entry = ctk.CTkEntry(self)
        self.last_name_label = ctk.CTkLabel(self, text="Last Name:")
        self.last_name_entry = ctk.CTkEntry(self)
        self.vacation_days_label = ctk.CTkLabel(self, text="Vacation Days:")
        self.vacation_days_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.add_employee_button = ctk.CTkButton(self, text="Add Employee", command=self.add_employee)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.first_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.last_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.vacation_days_label.grid(row=2, column=0, padx=10, pady=10)
        self.vacation_days_entry.grid(row=2, column=1, padx=10, pady=10)
        self.add_employee_button.grid(row=3, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=3, column=1, padx=10, pady=10)

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

        # Destroy the window
        self.destroy()


# Edit Employee Window Class
class EditEmployeeWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.first_name_label = ctk.CTkLabel(self, text="First Name:")
        self.first_name_entry = ctk.CTkEntry(self)

        self.last_name_label = ctk.CTkLabel(self, text="Last Name:")
        self.last_name_entry = ctk.CTkEntry(self)

        self.new_first_name_label = ctk.CTkLabel(self, text="New First Name:")
        self.new_first_name_entry = ctk.CTkEntry(self)

        self.new_last_name_label = ctk.CTkLabel(self, text="New Last Name:")
        self.new_last_name_entry = ctk.CTkEntry(self)

        self.new_vacation_days_label = ctk.CTkLabel(self, text="New Vacation Days:")
        self.new_vacation_days_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.edit_employee_button = ctk.CTkButton(self, text="Edit Employee", command=self.edit_employee)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.first_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.last_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_first_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_first_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_last_name_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_last_name_entry.grid(row=3, column=1, padx=10, pady=10)
        self.new_vacation_days_label.grid(row=4, column=0, padx=10, pady=10)
        self.new_vacation_days_entry.grid(row=4, column=1, padx=10, pady=10)
        self.edit_employee_button.grid(row=5, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=5, column=1, padx=10, pady=10)

        # Set the focus to the first name entry box
        self.first_name_entry.focus_set()

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

        # Destroy the window
        self.destroy()


# Delete Employee Window Class
class DeleteEmployeeWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.first_name_label = ctk.CTkLabel(self, text="First Name:")
        self.first_name_entry = ctk.CTkEntry(self)
        self.last_name_label = ctk.CTkLabel(self, text="Last Name:")
        self.last_name_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.delete_employee_button = ctk.CTkButton(self, text="Delete Employee", command=self.delete_employee)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.first_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.last_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.delete_employee_button.grid(row=2, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10)

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

        # Destroy the window
        self.destroy()


# View Employee Window Class
class ViewEmployeeWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("View Employee")
        self.geometry("400x400")
        self.resizable(False, False)

        self.first_label = ctk.CTkLabel(self, text="First Name")
        self.first_label.grid(row=0, column=0, padx=10, pady=10)

        self.first_entry = ctk.CTkEntry(self)
        self.first_entry.grid(row=0, column=1, padx=10, pady=10)

        self.last_label = ctk.CTkLabel(self, text="Last Name")
        self.last_label.grid(row=1, column=0, padx=10, pady=10)

        self.last_entry = ctk.CTkEntry(self)
        self.last_entry.grid(row=1, column=1, padx=10, pady=10)

        self.view_employee_button = ctk.CTkButton(self, text="View Employee", command=self.view_employee)
        self.view_employee_button.grid(row=2, column=0, padx=10, pady=10)

        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10)

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

        # Destroy the window
        self.destroy()
