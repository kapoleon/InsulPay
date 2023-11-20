# Import Statements
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import customtkinter as ctk

'''Appearance Settings for CustomTkinter'''

# Set the appearance mode and default color theme for CustomTkinter
ctk.set_appearance_mode("system")  # system, dark , light
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

'''End of Appearance Settings for CustomTkinter'''

'''Application Database'''


class ApplicationDatabase:
    def __init__(self, db_name="InsulPay.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Database connected successfully!")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        try:
            self.conn.close()
            print("Database disconnected successfully!")
        except Exception as e:
            print(f"Error disconnecting to the database: {e}")

    def create_employee_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                                    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    first_name TEXT NOT NULL,
                                    last_name TEXT NOT NULL,
                                    vacation_days INTEGER NOT NULL,

                                    UNIQUE(first_name, last_name)
                                );""")
            self.conn.commit()
            print("Employee table created successfully!")
        except Exception as e:
            print(f"Error creating employee table: {e}")

    def add_employee(self, first_name, last_name, vacation_days):
        try:
            self.cursor.execute("""INSERT INTO employees (first_name, last_name, vacation_days) VALUES (?, ?, ?);""",
                                (first_name, last_name, vacation_days))
            self.conn.commit()
            print("Employee added successfully!")
        except Exception as e:
            print(f"Error adding employee: {e}")
        finally:
            self.disconnect()

    def edit_employee(self, first_name, last_name, new_first_name, new_last_name, new_vacation_days):
        try:
            self.cursor.execute(
                """UPDATE employees SET first_name = ?, last_name = ?, vacation_days = ? WHERE first_name = ? AND 
                last_name = ?;""",
                (new_first_name, new_last_name, new_vacation_days, first_name, last_name))
            self.conn.commit()
            print("Employee edited successfully!")
        except Exception as e:
            print(f"Error editing employee: {e}")
        finally:
            self.disconnect()

    def delete_employee(self, first_name, last_name):
        try:
            self.cursor.execute("""DELETE FROM employees WHERE first_name = ? AND last_name = ?;""",
                                (first_name, last_name))
            self.conn.commit()
            print("Employee deleted successfully!")
        except Exception as e:
            print(f"Error deleting employee: {e}")
        finally:
            self.disconnect()

    def view_employee(self, first_name, last_name):
        try:
            self.cursor.execute("""SELECT * FROM employees WHERE first_name = ? AND last_name = ?;""",
                                (first_name, last_name))
            employee_data = self.cursor.fetchall()
            return employee_data
        except Exception as e:
            print(f"Error viewing employee: {e}")
        finally:
            self.disconnect()

    def view_all_employees(self):
        try:
            self.cursor.execute("""SELECT * FROM employees;""")
            employee_data = self.cursor.fetchall()
            return employee_data
        except Exception as e:
            print(f"Error viewing all employees: {e}")
        finally:
            self.disconnect()


'''End of Application Database'''

'''Main Application Main Menu Windows'''


# Employee Management Windows

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
        database = ApplicationDatabase()
        database.connect()
        database.create_employee_table()
        database.add_employee(first_name, last_name, vacation_days)

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
        database = ApplicationDatabase()
        database.connect()
        database.create_employee_table()
        database.edit_employee(first_name, last_name, new_first_name, new_last_name, new_vacation_days)

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
        database = ApplicationDatabase()
        database.connect()
        database.create_employee_table()
        database.delete_employee(first_name, last_name)

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
        database = ApplicationDatabase()
        database.connect()
        database.create_employee_table()
        try:
            employee_data = database.view_employee(first_name, last_name)
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


'''End of Main Application Main Menu Windows'''

'''Main Application'''


class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Scratch")
        self.geometry("800x600")
        self.resizable(False, False)
        self.menu_font = ctk.CTkFont(family="Roboto", size=20, weight="bold")
        self.create_main_menu()
        self.create_widgets()

        self.database = ApplicationDatabase()

    # Create Main Menu
    def create_main_menu(self):
        # Create Main Menu
        main_menu = tk.Menu(self)
        self.config(menu=main_menu)

        self.create_file_menu(main_menu)
        self.create_database_menu(main_menu)

    # Create Main Menu Sub Menus
    def create_file_menu(self, main_menu):
        # Create File Menu
        file_menu = tk.Menu(main_menu, tearoff=False)

        # Add File Menu to Main Menu
        main_menu.add_cascade(label="File", menu=file_menu)

        # Add Commands to File Menu
        file_menu.add_command(label="Open File", command=self.open_file, font=self.menu_font)
        file_menu.add_command(label="Close Window", command=self.on_closing, font=self.menu_font)

    def create_database_menu(self, main_menu):
        # Create Database Menu
        database_menu = tk.Menu(main_menu, tearoff=False)

        # Add Database Menu to Main Menu
        main_menu.add_cascade(label="Database", menu=database_menu)

        # Create Employee Management Submenu
        employee_management_menu = tk.Menu(database_menu, tearoff=False)

        # Add Employee Management Menu to Database Menu
        database_menu.add_cascade(label="Employee Manager", menu=employee_management_menu, font=self.menu_font)

        # Add Commands to Employee Management Menu
        employee_management_menu.add_command(label="Add Employee", command=self.add_employee, font=self.menu_font)
        employee_management_menu.add_command(label="Edit Employee", command=self.edit_employee, font=self.menu_font)
        employee_management_menu.add_command(label="Delete Employee", command=self.delete_employee, font=self.menu_font)
        employee_management_menu.add_command(label="View Employee", command=self.view_employee, font=self.menu_font)

    # File Menu Commands
    @staticmethod
    def open_file():
        file_path = tk.filedialog.askopenfilename(initialdir="/",
                                                  title="Select A File",
                                                  filetypes=(("excel files", "*.xlsx"), ("All Files", "*.*")))
        subprocess.Popen([file_path], shell=True)

    # Database Menu Commands

    # Employee Management Submenu Commands
    def add_employee(self):
        add_employee_window = AddEmployeeWindow(self)
        add_employee_window.grab_set()

    def edit_employee(self):
        edit_employee_window = EditEmployeeWindow(self)
        edit_employee_window.grab_set()

    def delete_employee(self):
        delete_employee_window = DeleteEmployeeWindow(self)
        delete_employee_window.grab_set()

    def view_employee(self):
        view_employee_window = ViewEmployeeWindow(self)
        view_employee_window.grab_set()

    # Create Widgets for Main Application
    def create_widgets(self):
        pass

    # Close the Application
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


'''End of Main Application'''

# Run Program
if __name__ == "__main__":
    app = MainApplication()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
