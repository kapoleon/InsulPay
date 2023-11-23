import customtkinter as ctk
from tkinter import messagebox
from scripts.database.tables.attic_pay_rate_table import AtticPayRateTable


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
        attic_pay_rate_table = AtticPayRateTable()
        attic_pay_rate_table.connect()
        attic_pay_rate_table.add_attic_pay_rate(attic_pay_rate_name, attic_pay_rate_amount, attic_pay_rate_description)

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
        attic_pay_rate_table = AtticPayRateTable()
        attic_pay_rate_table.connect()
        attic_pay_rate_table.edit_attic_pay_rate(attic_pay_rate_name, new_attic_pay_rate_name,
                                                 new_attic_pay_rate_amount,
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
        attic_pay_rate_table = AtticPayRateTable()
        attic_pay_rate_table.connect()
        attic_pay_rate_table.delete_attic_pay_rate(attic_pay_rate_name)

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
        attic_pay_rate_table = AtticPayRateTable()
        attic_pay_rate_table.connect()
        try:
            attic_pay_rate_data = attic_pay_rate_table.view_attic_pay_rate(attic_pay_rate_name)
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
