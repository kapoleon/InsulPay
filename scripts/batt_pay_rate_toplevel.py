import customtkinter as ctk
from tkinter import messagebox
from scripts.database.tables.batt_pay_rate_table import BattPayRateTable


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
        batt_pay_rate_table = BattPayRateTable()
        batt_pay_rate_table.connect()
        batt_pay_rate_table.add_batt_pay_rate(batt_pay_rate_name, batt_pay_rate_amount, batt_pay_rate_description)

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
        batt_pay_rate_table = BattPayRateTable()
        batt_pay_rate_table.connect()
        batt_pay_rate_table.edit_batt_pay_rate(batt_pay_rate_name, new_batt_pay_rate_name, new_batt_pay_rate_amount,
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
        batt_pay_rate_table = BattPayRateTable()
        batt_pay_rate_table.connect()
        batt_pay_rate_table.delete_batt_pay_rate(batt_pay_rate_name)

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
        batt_pay_rate_table = BattPayRateTable()
        batt_pay_rate_table.connect()
        try:
            batt_pay_rate_data = batt_pay_rate_table.view_batt_pay_rate(batt_pay_rate_name)
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
