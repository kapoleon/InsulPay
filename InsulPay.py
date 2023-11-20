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

    # Create Employee Table in Database
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

    # Create Batt Pay Rate Table in Database
    def create_batt_pay_rate_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS batt_pay_rates (
                                    batt_pay_rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    batt_pay_rate_name TEXT NOT NULL,
                                    batt_pay_rate_amount REAL NOT NULL,
                                    batt_pay_rate_description TEXT NOT NULL,
                                    
                                    UNIQUE(batt_pay_rate_name)
                                );""")
            self.conn.commit()
            print("Batt Pay Rate table created successfully!")
        except Exception as e:
            print(f"Error creating batt pay rate table: {e}")

    def add_batt_pay_rate(self, batt_pay_rate_name, batt_pay_rate_amount, batt_pay_rate_description):
        try:
            self.cursor.execute("""INSERT INTO batt_pay_rates (batt_pay_rate_name, batt_pay_rate_amount, 
            batt_pay_rate_description) VALUES (?, ?, ?);""",
                                (batt_pay_rate_name, batt_pay_rate_amount, batt_pay_rate_description))
            self.conn.commit()
            print("Batt Pay Rate added successfully!")
        except Exception as e:
            print(f"Error adding batt pay rate: {e}")
        finally:
            self.disconnect()

    def edit_batt_pay_rate(self, batt_pay_rate_name, new_batt_pay_rate_name, new_batt_pay_rate_amount,
                           new_batt_pay_rate_description):
        try:
            self.cursor.execute(
                """UPDATE batt_pay_rates SET batt_pay_rate_name = ?, batt_pay_rate_amount = ?, 
                batt_pay_rate_description = ? WHERE batt_pay_rate_name = ?;""",
                (new_batt_pay_rate_name, new_batt_pay_rate_amount, new_batt_pay_rate_description, batt_pay_rate_name))
            self.conn.commit()
            print("Batt Pay Rate edited successfully!")
        except Exception as e:
            print(f"Error editing batt pay rate: {e}")
        finally:
            self.disconnect()

    def delete_batt_pay_rate(self, batt_pay_rate_name):
        try:
            self.cursor.execute("""DELETE FROM batt_pay_rates WHERE batt_pay_rate_name = ?;""",
                                (batt_pay_rate_name,))
            self.conn.commit()
            print("Batt Pay Rate deleted successfully!")
        except Exception as e:
            print(f"Error deleting batt pay rate: {e}")
        finally:
            self.disconnect()

    def view_batt_pay_rate(self, batt_pay_rate_name):
        try:
            self.cursor.execute("""SELECT * FROM batt_pay_rates WHERE batt_pay_rate_name = ?;""",
                                (batt_pay_rate_name,))
            batt_pay_rate_data = self.cursor.fetchall()
            return batt_pay_rate_data
        except Exception as e:
            print(f"Error viewing batt pay rate: {e}")
        finally:
            self.disconnect()

    def view_all_batt_pay_rates(self):
        try:
            self.cursor.execute("""SELECT * FROM batt_pay_rates;""")
            batt_pay_rate_data = self.cursor.fetchall()
            return batt_pay_rate_data
        except Exception as e:
            print(f"Error viewing all batt pay rates: {e}")
        finally:
            self.disconnect()

    # Create Attic Pay Rate Table in Database
    def create_attic_pay_rate_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS attic_pay_rates (
                                    attic_pay_rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    attic_pay_rate_name TEXT NOT NULL,
                                    attic_pay_rate_amount REAL NOT NULL,
                                    attic_pay_rate_description TEXT NOT NULL,
                                    
                                    UNIQUE(attic_pay_rate_name)
                                );""")
            self.conn.commit()
            print("Attic Pay Rate table created successfully!")
        except Exception as e:
            print(f"Error creating attic pay rate table: {e}")

    def add_attic_pay_rate(self, attic_pay_rate_name, attic_pay_rate_amount, attic_pay_rate_description):
        try:
            self.cursor.execute("""INSERT INTO attic_pay_rates (attic_pay_rate_name, attic_pay_rate_amount, 
            attic_pay_rate_description) VALUES (?, ?, ?);""",
                                (attic_pay_rate_name, attic_pay_rate_amount, attic_pay_rate_description))
            self.conn.commit()
            print("Attic Pay Rate added successfully!")
        except Exception as e:
            print(f"Error adding attic pay rate: {e}")
        finally:
            self.disconnect()

    def edit_attic_pay_rate(self, attic_pay_rate_name, new_attic_pay_rate_name, new_attic_pay_rate_amount,
                            new_attic_pay_rate_description):
        try:
            self.cursor.execute(
                """UPDATE attic_pay_rates SET attic_pay_rate_name = ?, attic_pay_rate_amount = ?, 
                 attic_pay_rate_description = ? WHERE attic_pay_rate_name = ?;""",
                (new_attic_pay_rate_name, new_attic_pay_rate_amount, new_attic_pay_rate_description,
                 attic_pay_rate_name))
            self.conn.commit()
            print("Attic Pay Rate edited successfully!")
        except Exception as e:
            print(f"Error editing attic pay rate: {e}")
        finally:
            self.disconnect()

    def delete_attic_pay_rate(self, attic_pay_rate_name):
        try:
            self.cursor.execute("""DELETE FROM attic_pay_rates WHERE attic_pay_rate_name = ?;""",
                                (attic_pay_rate_name,))
            self.conn.commit()
            print("Attic Pay Rate deleted successfully!")
        except Exception as e:
            print(f"Error deleting attic pay rate: {e}")
        finally:
            self.disconnect()

    def view_attic_pay_rate(self, attic_pay_rate_name):
        try:
            self.cursor.execute("""SELECT * FROM attic_pay_rates WHERE attic_pay_rate_name = ?;""",
                                (attic_pay_rate_name,))
            attic_pay_rate_data = self.cursor.fetchall()
            return attic_pay_rate_data
        except Exception as e:
            print(f"Error viewing attic pay rate: {e}")
        finally:
            self.disconnect()

    def view_all_attic_pay_rates(self):
        try:
            self.cursor.execute("""SELECT * FROM attic_pay_rates;""")
            attic_pay_rate_data = self.cursor.fetchall()
            return attic_pay_rate_data
        except Exception as e:
            print(f"Error viewing all attic pay rates: {e}")
        finally:
            self.disconnect()

    # Create Foam Pay Rate Table in Database
    def create_foam_pay_rate_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS foam_pay_rates (
                                    foam_pay_rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    foam_pay_rate_name TEXT NOT NULL,
                                    foam_pay_rate_amount REAL NOT NULL,
                                    foam_pay_rate_description TEXT NOT NULL,
                                    
                                    UNIQUE(foam_pay_rate_name)
                                );""")
            self.conn.commit()
            print("Foam Pay Rate table created successfully!")
        except Exception as e:
            print(f"Error creating foam pay rate table: {e}")

    def add_foam_pay_rate(self, foam_pay_rate_name, foam_pay_rate_amount, foam_pay_rate_description):
        try:
            self.cursor.execute("""INSERT INTO foam_pay_rates (foam_pay_rate_name, foam_pay_rate_amount, 
            foam_pay_rate_description) VALUES (?, ?, ?);""",
                                (foam_pay_rate_name, foam_pay_rate_amount, foam_pay_rate_description))
            self.conn.commit()
            print("Foam Pay Rate added successfully!")
        except Exception as e:
            print(f"Error adding foam pay rate: {e}")
        finally:
            self.disconnect()

    def edit_foam_pay_rate(self, foam_pay_rate_name, new_foam_pay_rate_name, new_foam_pay_rate_amount,
                           new_foam_pay_rate_description):
        try:
            self.cursor.execute(
                """UPDATE foam_pay_rates SET foam_pay_rate_name = ?, foam_pay_rate_amount = ?, 
                 foam_pay_rate_description = ? WHERE foam_pay_rate_name = ?;""",
                (new_foam_pay_rate_name, new_foam_pay_rate_amount, new_foam_pay_rate_description,
                 foam_pay_rate_name))
            self.conn.commit()
            print("Foam Pay Rate edited successfully!")
        except Exception as e:
            print(f"Error editing foam pay rate: {e}")
        finally:
            self.disconnect()

    def delete_foam_pay_rate(self, foam_pay_rate_name):
        try:
            self.cursor.execute("""DELETE FROM foam_pay_rates WHERE foam_pay_rate_name = ?;""",
                                (foam_pay_rate_name,))
            self.conn.commit()
            print("Foam Pay Rate deleted successfully!")
        except Exception as e:
            print(f"Error deleting foam pay rate: {e}")
        finally:
            self.disconnect()

    def view_foam_pay_rate(self, foam_pay_rate_name):
        try:
            self.cursor.execute("""SELECT * FROM foam_pay_rates WHERE foam_pay_rate_name = ?;""",
                                (foam_pay_rate_name,))
            foam_pay_rate_data = self.cursor.fetchall()
            return foam_pay_rate_data
        except Exception as e:
            print(f"Error viewing foam pay rate: {e}")
        finally:
            self.disconnect()

    def view_all_foam_pay_rates(self):
        try:
            self.cursor.execute("""SELECT * FROM foam_pay_rates;""")
            foam_pay_rate_data = self.cursor.fetchall()
            return foam_pay_rate_data
        except Exception as e:
            print(f"Error viewing all foam pay rates: {e}")
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


# Batt Pay Rate Management Windows
# Add Batt Pay Rate Window Class
class AddBattPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Add Batt Pay Rate")
        self.geometry("400x400")
        self.resizable(False, False)

        # Create the labels and entry boxes
        self.batt_pay_rate_name_label = ctk.CTkLabel(self, text="Batt Pay Rate Name:")
        self.batt_pay_rate_name_entry = ctk.CTkEntry(self)
        self.batt_pay_rate_amount_label = ctk.CTkLabel(self, text="Batt Pay Rate Amount:")
        self.batt_pay_rate_amount_entry = ctk.CTkEntry(self)
        self.batt_pay_rate_description_label = ctk.CTkLabel(self, text="Batt Pay Rate Description:")
        self.batt_pay_rate_description_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.add_batt_pay_rate_button = ctk.CTkButton(self, text="Add Batt Pay Rate", command=self.add_batt_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.batt_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.batt_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.batt_pay_rate_amount_label.grid(row=1, column=0, padx=10, pady=10)
        self.batt_pay_rate_amount_entry.grid(row=1, column=1, padx=10, pady=10)
        self.batt_pay_rate_description_label.grid(row=2, column=0, padx=10, pady=10)
        self.batt_pay_rate_description_entry.grid(row=2, column=1, padx=10, pady=10)
        self.add_batt_pay_rate_button.grid(row=3, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=3, column=1, padx=10, pady=10)

        # Set the focus to the batt pay rate name entry box
        self.batt_pay_rate_name_entry.focus_set()

    def add_batt_pay_rate(self):
        batt_pay_rate_name = self.batt_pay_rate_name_entry.get()
        batt_pay_rate_amount = self.batt_pay_rate_amount_entry.get()
        batt_pay_rate_description = self.batt_pay_rate_description_entry.get()

        # Check if the user entered all the required information
        if batt_pay_rate_name == "" or batt_pay_rate_amount == "" or batt_pay_rate_description == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the batt pay rate amount is a number
        try:
            batt_pay_rate_amount = float(batt_pay_rate_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for batt pay rate amount!")
            return

        # Check if the batt pay rate amount is a positive number
        if batt_pay_rate_amount < 0:
            messagebox.showerror("Error", "Please enter a positive number for batt pay rate amount!")
            return

        # Add the batt pay rate to the database
        database = ApplicationDatabase()
        database.connect()
        database.create_batt_pay_rate_table()
        database.add_batt_pay_rate(batt_pay_rate_name, batt_pay_rate_amount, batt_pay_rate_description)

        messagebox.showinfo("Success", "Batt Pay Rate added successfully!")

        # Destroy the window
        self.destroy()


# Edit Batt Pay Rate Window Class
class EditBattPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.batt_pay_rate_name_label = ctk.CTkLabel(self, text="Batt Pay Rate Name:")
        self.batt_pay_rate_name_entry = ctk.CTkEntry(self)
        self.new_batt_pay_rate_name_label = ctk.CTkLabel(self, text="New Batt Pay Rate Name:")
        self.new_batt_pay_rate_name_entry = ctk.CTkEntry(self)
        self.new_batt_pay_rate_amount_label = ctk.CTkLabel(self, text="New Batt Pay Rate Amount:")
        self.new_batt_pay_rate_amount_entry = ctk.CTkEntry(self)
        self.new_batt_pay_rate_description_label = ctk.CTkLabel(self, text="New Batt Pay Rate Description:")
        self.new_batt_pay_rate_description_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.edit_batt_pay_rate_button = ctk.CTkButton(self, text="Edit Batt Pay Rate", command=self.edit_batt_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.batt_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.batt_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.new_batt_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.new_batt_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_batt_pay_rate_amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_batt_pay_rate_amount_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_batt_pay_rate_description_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_batt_pay_rate_description_entry.grid(row=3, column=1, padx=10, pady=10)
        self.edit_batt_pay_rate_button.grid(row=4, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=4, column=1, padx=10, pady=10)

        # Set the focus to the batt pay rate name entry box
        self.batt_pay_rate_name_entry.focus_set()

    def edit_batt_pay_rate(self):
        batt_pay_rate_name = self.batt_pay_rate_name_entry.get()
        new_batt_pay_rate_name = self.new_batt_pay_rate_name_entry.get()
        new_batt_pay_rate_amount = self.new_batt_pay_rate_amount_entry.get()
        new_batt_pay_rate_description = self.new_batt_pay_rate_description_entry.get()

        # Check if the user entered all the required information
        if (batt_pay_rate_name == "" or new_batt_pay_rate_name == "" or new_batt_pay_rate_amount == "" or
                new_batt_pay_rate_description == ""):
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the batt pay rate amount is a number
        try:
            new_batt_pay_rate_amount = float(new_batt_pay_rate_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for batt pay rate amount!")
            return

        # Check if the batt pay rate amount is a positive number
        if new_batt_pay_rate_amount < 0:
            messagebox.showerror("Error", "Please enter a positive number for batt pay rate amount!")
            return

        # Edit the batt pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_batt_pay_rate_table()
        database.edit_batt_pay_rate(batt_pay_rate_name, new_batt_pay_rate_name, new_batt_pay_rate_amount,
                                    new_batt_pay_rate_description)

        messagebox.showinfo("Success", "Batt Pay Rate edited successfully!")

        # Destroy the window
        self.destroy()


# Delete Batt Pay Rate Window Class
class DeleteBattPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.batt_pay_rate_name_label = ctk.CTkLabel(self, text="Batt Pay Rate Name:")
        self.batt_pay_rate_name_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.delete_batt_pay_rate_button = ctk.CTkButton(self, text="Delete Batt Pay Rate",
                                                         command=self.delete_batt_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.batt_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.batt_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.delete_batt_pay_rate_button.grid(row=1, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10)

        # Set the focus to the batt pay rate name entry box
        self.batt_pay_rate_name_entry.focus_set()

    def delete_batt_pay_rate(self):
        batt_pay_rate_name = self.batt_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if batt_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Delete the batt pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_batt_pay_rate_table()
        database.delete_batt_pay_rate(batt_pay_rate_name)

        messagebox.showinfo("Success", "Batt Pay Rate deleted successfully!")

        # Destroy the window
        self.destroy()


# View Batt Pay Rate Window Class
class ViewBattPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("View Batt Pay Rate")
        self.geometry("400x400")
        self.resizable(False, False)

        self.batt_pay_rate_name_label = ctk.CTkLabel(self, text="Batt Pay Rate Name")
        self.batt_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.batt_pay_rate_name_entry = ctk.CTkEntry(self)
        self.batt_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.view_batt_pay_rate_button = ctk.CTkButton(self, text="View Batt Pay Rate",
                                                       command=self.view_batt_pay_rate)
        self.view_batt_pay_rate_button.grid(row=1, column=0, padx=10, pady=10)

        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10)

        # Set the focus to the batt pay rate name entry box
        self.batt_pay_rate_name_entry.focus_set()

    def view_batt_pay_rate(self):
        batt_pay_rate_name = self.batt_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if batt_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # View the batt pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_batt_pay_rate_table()
        try:
            batt_pay_rate_data = database.view_batt_pay_rate(batt_pay_rate_name)
            if batt_pay_rate_data:
                # Create a string representation of the batt pay rate information
                batt_pay_rate_info = "\n".join([f"{key}: {value}" for key, value in
                                                zip(["ID", "Batt Pay Rate Name", "Batt Pay Rate Amount",
                                                     "Batt Pay Rate Description"], batt_pay_rate_data[0])])
                messagebox.showinfo("Batt Pay Rate Information", f"Batt Pay Rate Details:\n{batt_pay_rate_info}")
            else:
                messagebox.showinfo("Batt Pay Rate Not Found", "No batt pay rate found with the given details.")
        except Exception as e:
            messagebox.showerror("Error", f"Error viewing batt pay rate: {e}")

        # Destroy the window
        self.destroy()


# Attic Pay Rate Management Windows
# Add Attic Pay Rate Window Class
class AddAtticPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Add Attic Pay Rate")
        self.geometry("400x400")
        self.resizable(False, False)

        # Create the labels and entry boxes
        self.attic_pay_rate_name_label = ctk.CTkLabel(self, text="Attic Pay Rate Name:")
        self.attic_pay_rate_name_entry = ctk.CTkEntry(self)
        self.attic_pay_rate_amount_label = ctk.CTkLabel(self, text="Attic Pay Rate Amount:")
        self.attic_pay_rate_amount_entry = ctk.CTkEntry(self)
        self.attic_pay_rate_description_label = ctk.CTkLabel(self, text="Attic Pay Rate Description:")
        self.attic_pay_rate_description_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.add_attic_pay_rate_button = ctk.CTkButton(self, text="Add Attic Pay Rate", command=self.add_attic_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.attic_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.attic_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.attic_pay_rate_amount_label.grid(row=1, column=0, padx=10, pady=10)
        self.attic_pay_rate_amount_entry.grid(row=1, column=1, padx=10, pady=10)
        self.attic_pay_rate_description_label.grid(row=2, column=0, padx=10, pady=10)
        self.attic_pay_rate_description_entry.grid(row=2, column=1, padx=10, pady=10)
        self.add_attic_pay_rate_button.grid(row=3, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=3, column=1, padx=10, pady=10)

        # Set the focus to the attic pay rate name entry box
        self.attic_pay_rate_name_entry.focus_set()

    def add_attic_pay_rate(self):
        attic_pay_rate_name = self.attic_pay_rate_name_entry.get()
        attic_pay_rate_amount = self.attic_pay_rate_amount_entry.get()
        attic_pay_rate_description = self.attic_pay_rate_description_entry.get()

        # Check if the user entered all the required information
        if attic_pay_rate_name == "" or attic_pay_rate_amount == "" or attic_pay_rate_description == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the attic pay rate amount is a number
        try:
            attic_pay_rate_amount = float(attic_pay_rate_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for attic pay rate amount!")
            return

        # Check if the attic pay rate amount is a positive number
        if attic_pay_rate_amount < 0:
            messagebox.showerror("Error", "Please enter a positive number for attic pay rate amount!")
            return

        # Add the attic pay rate to the database
        database = ApplicationDatabase()
        database.connect()
        database.create_attic_pay_rate_table()
        database.add_attic_pay_rate(attic_pay_rate_name, attic_pay_rate_amount, attic_pay_rate_description)

        messagebox.showinfo("Success", "Attic Pay Rate added successfully!")

        # Destroy the window
        self.destroy()


# Edit Attic Pay Rate Window Class
class EditAtticPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.attic_pay_rate_name_label = ctk.CTkLabel(self, text="Attic Pay Rate Name:")
        self.attic_pay_rate_name_entry = ctk.CTkEntry(self)
        self.new_attic_pay_rate_name_label = ctk.CTkLabel(self, text="New Attic Pay Rate Name:")
        self.new_attic_pay_rate_name_entry = ctk.CTkEntry(self)
        self.new_attic_pay_rate_amount_label = ctk.CTkLabel(self, text="New Attic Pay Rate Amount:")
        self.new_attic_pay_rate_amount_entry = ctk.CTkEntry(self)
        self.new_attic_pay_rate_description_label = ctk.CTkLabel(self, text="New Attic Pay Rate Description:")
        self.new_attic_pay_rate_description_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.edit_attic_pay_rate_button = ctk.CTkButton(self, text="Edit Attic Pay Rate",
                                                        command=self.edit_attic_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.attic_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.attic_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.new_attic_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.new_attic_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_attic_pay_rate_amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_attic_pay_rate_amount_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_attic_pay_rate_description_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_attic_pay_rate_description_entry.grid(row=3, column=1, padx=10, pady=10)
        self.edit_attic_pay_rate_button.grid(row=4, column=0, padx=10, pady=10)

        # Set the focus to the attic pay rate name entry box
        self.attic_pay_rate_name_entry.focus_set()

    def edit_attic_pay_rate(self):
        attic_pay_rate_name = self.attic_pay_rate_name_entry.get()
        new_attic_pay_rate_name = self.new_attic_pay_rate_name_entry.get()
        new_attic_pay_rate_amount = self.new_attic_pay_rate_amount_entry.get()
        new_attic_pay_rate_description = self.new_attic_pay_rate_description_entry.get()

        # Check if the user entered all the required information
        if (attic_pay_rate_name == "" or new_attic_pay_rate_name == "" or new_attic_pay_rate_amount == "" or
                new_attic_pay_rate_description == ""):
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the attic pay rate amount is a number
        try:
            new_attic_pay_rate_amount = float(new_attic_pay_rate_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for attic pay rate amount!")
            return

        # Check if the attic pay rate amount is a positive number
        if new_attic_pay_rate_amount < 0:
            messagebox.showerror("Error", "Please enter a positive number for attic pay rate amount!")
            return

        # Edit the attic pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_attic_pay_rate_table()
        database.edit_attic_pay_rate(attic_pay_rate_name, new_attic_pay_rate_name, new_attic_pay_rate_amount,
                                     new_attic_pay_rate_description)

        messagebox.showinfo("Success", "Attic Pay Rate edited successfully!")

        # Destroy the window
        self.destroy()


# Delete Attic Pay Rate Window Class
class DeleteAtticPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.attic_pay_rate_name_label = ctk.CTkLabel(self, text="Attic Pay Rate Name:")
        self.attic_pay_rate_name_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.delete_attic_pay_rate_button = ctk.CTkButton(self, text="Delete Attic Pay Rate",
                                                          command=self.delete_attic_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.attic_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.attic_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.delete_attic_pay_rate_button.grid(row=1, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10)

        # Set the focus to the attic pay rate name entry box
        self.attic_pay_rate_name_entry.focus_set()

    def delete_attic_pay_rate(self):
        attic_pay_rate_name = self.attic_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if attic_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Delete the attic pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_attic_pay_rate_table()
        database.delete_attic_pay_rate(attic_pay_rate_name)

        messagebox.showinfo("Success", "Attic Pay Rate deleted successfully!")

        # Destroy the window
        self.destroy()


# View Attic Pay Rate Window Class
class ViewAtticPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("View Attic Pay Rate")
        self.geometry("400x400")
        self.resizable(False, False)

        self.attic_pay_rate_name_label = ctk.CTkLabel(self, text="Attic Pay Rate Name")
        self.attic_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.attic_pay_rate_name_entry = ctk.CTkEntry(self)
        self.attic_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.view_attic_pay_rate_button = ctk.CTkButton(self, text="View Attic Pay Rate",
                                                        command=self.view_attic_pay_rate)
        self.view_attic_pay_rate_button.grid(row=1, column=0, padx=10, pady=10)

        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10)

        # Set the focus to the attic pay rate name entry box
        self.attic_pay_rate_name_entry.focus_set()

    def view_attic_pay_rate(self):
        attic_pay_rate_name = self.attic_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if attic_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # View the attic pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_attic_pay_rate_table()
        try:
            attic_pay_rate_data = database.view_attic_pay_rate(attic_pay_rate_name)
            if attic_pay_rate_data:
                # Create a string representation of the attic pay rate information
                attic_pay_rate_info = "\n".join([f"{key}: {value}" for key, value in
                                                 zip(["ID", "Attic Pay Rate Name", "Attic Pay Rate Amount",
                                                      "Attic Pay Rate Description"], attic_pay_rate_data[0])])
                messagebox.showinfo("Attic Pay Rate Information", f"Attic Pay Rate Details:\n{attic_pay_rate_info}")
            else:
                messagebox.showinfo("Attic Pay Rate Not Found", "No attic pay rate found with the given details.")
        except Exception as e:
            messagebox.showerror("Error", f"Error viewing attic pay rate: {e}")

        # Destroy the window
        self.destroy()


# Foam Pay Rate Management Windows
# Add Foam Pay Rate Window Class
class AddFoamPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Add Foam Pay Rate")
        self.geometry("400x400")
        self.resizable(False, False)

        # Create the labels and entry boxes
        self.foam_pay_rate_name_label = ctk.CTkLabel(self, text="Foam Pay Rate Name:")
        self.foam_pay_rate_name_entry = ctk.CTkEntry(self)
        self.foam_pay_rate_amount_label = ctk.CTkLabel(self, text="Foam Pay Rate Amount:")
        self.foam_pay_rate_amount_entry = ctk.CTkEntry(self)
        self.foam_pay_rate_description_label = ctk.CTkLabel(self, text="Foam Pay Rate Description:")
        self.foam_pay_rate_description_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.add_foam_pay_rate_button = ctk.CTkButton(self, text="Add Foam Pay Rate", command=self.add_foam_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.foam_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.foam_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.foam_pay_rate_amount_label.grid(row=1, column=0, padx=10, pady=10)
        self.foam_pay_rate_amount_entry.grid(row=1, column=1, padx=10, pady=10)
        self.foam_pay_rate_description_label.grid(row=2, column=0, padx=10, pady=10)
        self.foam_pay_rate_description_entry.grid(row=2, column=1, padx=10, pady=10)
        self.add_foam_pay_rate_button.grid(row=3, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=3, column=1, padx=10, pady=10)

        # Set the focus to the foam pay rate name entry box
        self.foam_pay_rate_name_entry.focus_set()

    def add_foam_pay_rate(self):
        foam_pay_rate_name = self.foam_pay_rate_name_entry.get()
        foam_pay_rate_amount = self.foam_pay_rate_amount_entry.get()
        foam_pay_rate_description = self.foam_pay_rate_description_entry.get()

        # Check if the user entered all the required information
        if foam_pay_rate_name == "" or foam_pay_rate_amount == "" or foam_pay_rate_description == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the foam pay rate amount is a number
        try:
            foam_pay_rate_amount = float(foam_pay_rate_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for foam pay rate amount!")
            return

        # Check if the foam pay rate amount is a positive number
        if foam_pay_rate_amount < 0:
            messagebox.showerror("Error", "Please enter a positive number for foam pay rate amount!")
            return

        # Add the foam pay rate to the database
        database = ApplicationDatabase()
        database.connect()
        database.create_foam_pay_rate_table()
        database.add_foam_pay_rate(foam_pay_rate_name, foam_pay_rate_amount, foam_pay_rate_description)

        messagebox.showinfo("Success", "Foam Pay Rate added successfully!")

        # Destroy the window
        self.destroy()


# Edit Foam Pay Rate Window Class
class EditFoamPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.foam_pay_rate_name_label = ctk.CTkLabel(self, text="Foam Pay Rate Name:")
        self.foam_pay_rate_name_entry = ctk.CTkEntry(self)
        self.new_foam_pay_rate_name_label = ctk.CTkLabel(self, text="New Foam Pay Rate Name:")
        self.new_foam_pay_rate_name_entry = ctk.CTkEntry(self)
        self.new_foam_pay_rate_amount_label = ctk.CTkLabel(self, text="New Foam Pay Rate Amount:")
        self.new_foam_pay_rate_amount_entry = ctk.CTkEntry(self)
        self.new_foam_pay_rate_description_label = ctk.CTkLabel(self, text="New Foam Pay Rate Description:")
        self.new_foam_pay_rate_description_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.edit_foam_pay_rate_button = ctk.CTkButton(self, text="Edit Foam Pay Rate", command=self.edit_foam_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.foam_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.foam_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.new_foam_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.new_foam_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_foam_pay_rate_amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_foam_pay_rate_amount_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_foam_pay_rate_description_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_foam_pay_rate_description_entry.grid(row=3, column=1, padx=10, pady=10)
        self.edit_foam_pay_rate_button.grid(row=4, column=0, padx=10, pady=10)

        # Set the focus to the foam pay rate name entry box
        self.foam_pay_rate_name_entry.focus_set()

    def edit_foam_pay_rate(self):
        foam_pay_rate_name = self.foam_pay_rate_name_entry.get()
        new_foam_pay_rate_name = self.new_foam_pay_rate_name_entry.get()
        new_foam_pay_rate_amount = self.new_foam_pay_rate_amount_entry.get()
        new_foam_pay_rate_description = self.new_foam_pay_rate_description_entry.get()

        # Check if the user entered all the required information
        if (foam_pay_rate_name == "" or new_foam_pay_rate_name == "" or new_foam_pay_rate_amount == "" or
                new_foam_pay_rate_description == ""):
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Check if the foam pay rate amount is a number
        try:
            new_foam_pay_rate_amount = float(new_foam_pay_rate_amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a number for foam pay rate amount!")
            return

        # Check if the foam pay rate amount is a positive number
        if new_foam_pay_rate_amount < 0:
            messagebox.showerror("Error", "Please enter a positive number for foam pay rate amount!")
            return

        # Edit the foam pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_foam_pay_rate_table()
        database.edit_foam_pay_rate(foam_pay_rate_name, new_foam_pay_rate_name, new_foam_pay_rate_amount,
                                    new_foam_pay_rate_description)

        messagebox.showinfo("Success", "Foam Pay Rate edited successfully!")

        # Destroy the window
        self.destroy()


# Delete Foam Pay Rate Window Class
class DeleteFoamPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create the labels and entry boxes
        self.foam_pay_rate_name_label = ctk.CTkLabel(self, text="Foam Pay Rate Name:")
        self.foam_pay_rate_name_entry = ctk.CTkEntry(self)

        # Create the buttons
        self.delete_foam_pay_rate_button = ctk.CTkButton(self, text="Delete Foam Pay Rate",
                                                         command=self.delete_foam_pay_rate)
        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)

        # Place the widgets
        self.foam_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)
        self.foam_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.delete_foam_pay_rate_button.grid(row=1, column=0, padx=10, pady=10)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10)

        # Set the focus to the foam pay rate name entry box
        self.foam_pay_rate_name_entry.focus_set()

    def delete_foam_pay_rate(self):
        foam_pay_rate_name = self.foam_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if foam_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # Delete the foam pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_foam_pay_rate_table()
        database.delete_foam_pay_rate(foam_pay_rate_name)

        messagebox.showinfo("Success", "Foam Pay Rate deleted successfully!")

        # Destroy the window
        self.destroy()


# View Foam Pay Rate Window Class
class ViewFoamPayRateWindow(ctk.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("View Foam Pay Rate")
        self.geometry("400x400")
        self.resizable(False, False)

        self.foam_pay_rate_name_label = ctk.CTkLabel(self, text="Foam Pay Rate Name")
        self.foam_pay_rate_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.foam_pay_rate_name_entry = ctk.CTkEntry(self)
        self.foam_pay_rate_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.view_foam_pay_rate_button = ctk.CTkButton(self, text="View Foam Pay Rate",
                                                       command=self.view_foam_pay_rate)
        self.view_foam_pay_rate_button.grid(row=1, column=0, padx=10, pady=10)

        self.cancel_button = ctk.CTkButton(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10)

        # Set the focus to the foam pay rate name entry box
        self.foam_pay_rate_name_entry.focus_set()

    def view_foam_pay_rate(self):
        foam_pay_rate_name = self.foam_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if foam_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information!")
            return

        # View the foam pay rate in the database
        database = ApplicationDatabase()
        database.connect()
        database.create_foam_pay_rate_table()
        try:
            foam_pay_rate_data = database.view_foam_pay_rate(foam_pay_rate_name)
            if foam_pay_rate_data:
                # Create a string representation of the foam pay rate information
                foam_pay_rate_info = "\n".join([f"{key}: {value}" for key, value in
                                                zip(["ID", "Foam Pay Rate Name", "Foam Pay Rate Amount",
                                                     "Foam Pay Rate Description"], foam_pay_rate_data[0])])
                messagebox.showinfo("Foam Pay Rate Information", f"Foam Pay Rate Details:\n{foam_pay_rate_info}")
            else:
                messagebox.showinfo("Foam Pay Rate Not Found", "No foam pay rate found with the given details.")
        except Exception as e:
            messagebox.showerror("Error", f"Error viewing foam pay rate: {e}")

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

        # Create Batt Pay Rate Management Submenu
        batt_pay_rate_management_menu = tk.Menu(database_menu, tearoff=False)

        # Add Batt Pay Rate Management Menu to Database Menu
        database_menu.add_cascade(label="Batt Pay Rate Manager", menu=batt_pay_rate_management_menu,
                                  font=self.menu_font)

        # Add Commands to Batt Pay Rate Management Menu
        batt_pay_rate_management_menu.add_command(label="Add Batt Pay Rate", command=self.add_batt_pay_rate,
                                                  font=self.menu_font)
        batt_pay_rate_management_menu.add_command(label="Edit Batt Pay Rate", command=self.edit_batt_pay_rate,
                                                  font=self.menu_font)
        batt_pay_rate_management_menu.add_command(label="Delete Batt Pay Rate", command=self.delete_batt_pay_rate,
                                                  font=self.menu_font)
        batt_pay_rate_management_menu.add_command(label="View Batt Pay Rate", command=self.view_batt_pay_rate,
                                                  font=self.menu_font)

        # Create Attic Pay Rate Management Submenu
        attic_pay_rate_management_menu = tk.Menu(database_menu, tearoff=False)

        # Add Attic Pay Rate Management Menu to Database Menu
        database_menu.add_cascade(label="Attic Pay Rate Manager", menu=attic_pay_rate_management_menu,
                                  font=self.menu_font)

        # Add Commands to Attic Pay Rate Management Menu
        attic_pay_rate_management_menu.add_command(label="Add Attic Pay Rate", command=self.add_attic_pay_rate,
                                                   font=self.menu_font)
        attic_pay_rate_management_menu.add_command(label="Edit Attic Pay Rate", command=self.edit_attic_pay_rate,
                                                   font=self.menu_font)
        attic_pay_rate_management_menu.add_command(label="Delete Attic Pay Rate", command=self.delete_attic_pay_rate,
                                                   font=self.menu_font)
        attic_pay_rate_management_menu.add_command(label="View Attic Pay Rate", command=self.view_attic_pay_rate,
                                                   font=self.menu_font)

        # Create Foam Pay Rate Management Submenu
        foam_pay_rate_management_menu = tk.Menu(database_menu, tearoff=False)

        # Add Foam Pay Rate Management Menu to Database Menu
        database_menu.add_cascade(label="Foam Pay Rate Manager", menu=foam_pay_rate_management_menu,
                                  font=self.menu_font)

        # Add Commands to Foam Pay Rate Management Menu
        foam_pay_rate_management_menu.add_command(label="Add Foam Pay Rate", command=self.add_foam_pay_rate,
                                                  font=self.menu_font)
        foam_pay_rate_management_menu.add_command(label="Edit Foam Pay Rate", command=self.edit_foam_pay_rate,
                                                  font=self.menu_font)
        foam_pay_rate_management_menu.add_command(label="Delete Foam Pay Rate", command=self.delete_foam_pay_rate,
                                                  font=self.menu_font)
        foam_pay_rate_management_menu.add_command(label="View Foam Pay Rate", command=self.view_foam_pay_rate,
                                                  font=self.menu_font)

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

    # Batt Pay Rate Management Submenu Commands
    def add_batt_pay_rate(self):
        add_batt_pay_rate_window = AddBattPayRateWindow(self)
        add_batt_pay_rate_window.grab_set()

    def edit_batt_pay_rate(self):
        edit_batt_pay_rate_window = EditBattPayRateWindow(self)
        edit_batt_pay_rate_window.grab_set()

    def delete_batt_pay_rate(self):
        delete_batt_pay_rate_window = DeleteBattPayRateWindow(self)
        delete_batt_pay_rate_window.grab_set()

    def view_batt_pay_rate(self):
        view_batt_pay_rate_window = ViewBattPayRateWindow(self)
        view_batt_pay_rate_window.grab_set()

    # Attic Pay Rate Management Submenu Commands
    def add_attic_pay_rate(self):
        add_attic_pay_rate_window = AddAtticPayRateWindow(self)
        add_attic_pay_rate_window.grab_set()

    def edit_attic_pay_rate(self):
        edit_attic_pay_rate_window = EditAtticPayRateWindow(self)
        edit_attic_pay_rate_window.grab_set()

    def delete_attic_pay_rate(self):
        delete_attic_pay_rate_window = DeleteAtticPayRateWindow(self)
        delete_attic_pay_rate_window.grab_set()

    def view_attic_pay_rate(self):
        view_attic_pay_rate_window = ViewAtticPayRateWindow(self)
        view_attic_pay_rate_window.grab_set()

    # Foam Pay Rate Management Submenu Commands
    def add_foam_pay_rate(self):
        add_foam_pay_rate_window = AddFoamPayRateWindow(self)
        add_foam_pay_rate_window.grab_set()

    def edit_foam_pay_rate(self):
        edit_foam_pay_rate_window = EditFoamPayRateWindow(self)
        edit_foam_pay_rate_window.grab_set()

    def delete_foam_pay_rate(self):
        delete_foam_pay_rate_window = DeleteFoamPayRateWindow(self)
        delete_foam_pay_rate_window.grab_set()

    def view_foam_pay_rate(self):
        view_foam_pay_rate_window = ViewFoamPayRateWindow(self)
        view_foam_pay_rate_window.grab_set()

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
