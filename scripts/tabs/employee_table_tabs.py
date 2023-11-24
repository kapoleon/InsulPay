import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from scripts.database.tables.employee_table import EmployeeTable


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


class TabTwo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        label = ttk.Label(self.frame, text="Edit Employee")
        label.pack(padx=10, pady=10)


class TabThree:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        label = ttk.Label(self.frame, text="Delete Employee")
        label.pack(padx=10, pady=10)


class TabFour:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        label = ttk.Label(self.frame, text="View Employees")
        label.pack(padx=10, pady=10)
