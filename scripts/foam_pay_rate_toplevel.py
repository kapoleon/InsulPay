import customtkinter as ctk
from tkinter import messagebox
from scripts.database.tables.foam_pay_rate_table import FoamPayRateTable


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
        foam_pay_rate_table = FoamPayRateTable()
        foam_pay_rate_table.connect()
        foam_pay_rate_table.add_foam_pay_rate(foam_pay_rate_name, foam_pay_rate_amount, foam_pay_rate_description)

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
        foam_pay_rate_table = FoamPayRateTable()
        foam_pay_rate_table.connect()
        foam_pay_rate_table.edit_foam_pay_rate(foam_pay_rate_name, new_foam_pay_rate_name, new_foam_pay_rate_amount,
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
        foam_pay_rate_table = FoamPayRateTable()
        foam_pay_rate_table.connect()
        foam_pay_rate_table.delete_foam_pay_rate(foam_pay_rate_name)

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
        foam_pay_rate_table = FoamPayRateTable()
        foam_pay_rate_table.connect()
        try:
            foam_pay_rate_data = foam_pay_rate_table.view_foam_pay_rate(foam_pay_rate_name)
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
