from program_settings import *


class BattPayRateTableManager:
    def __init__(self, parent):
        self.top_level = tk.Toplevel(parent)
        self.top_level.title("Batt Pay Rate Table Manager")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Batt Pay Rate")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="Edit Batt Pay Rate")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Delete Batt Pay Rate")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="View Batt Pay Rate")

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

        label = ttk.Label(self.frame, text="Add Batt Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.batt_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Batt Pay Rate Name:")
        self.batt_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.batt_pay_rate_amount_label = ctk.CTkLabel(self.frame, text="Batt Pay Rate Amount:")
        self.batt_pay_rate_amount_entry = ctk.CTkEntry(self.frame)
        self.batt_pay_rate_description_label = ctk.CTkLabel(self.frame, text="Batt Pay Rate Description:")
        self.batt_pay_rate_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.add_batt_pay_rate_button = ctk.CTkButton(self.frame, text="Add Batt Pay Rate",
                                                      command=self.add_batt_pay_rate)

        # Grid the labels and entry boxes
        self.batt_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.batt_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.batt_pay_rate_amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.batt_pay_rate_amount_entry.grid(row=2, column=1, padx=10, pady=10)
        self.batt_pay_rate_description_label.grid(row=3, column=0, padx=10, pady=10)
        self.batt_pay_rate_description_entry.grid(row=3, column=1, padx=10, pady=10)

        # Grid the buttons
        self.add_batt_pay_rate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

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
        batt_pay_rate_table.create_table()
        batt_pay_rate_table.add_batt_pay_rate(batt_pay_rate_name, batt_pay_rate_amount, batt_pay_rate_description)

        messagebox.showinfo("Success", "Batt Pay Rate added successfully!")

        # Clear the entry boxes
        self.batt_pay_rate_name_entry.delete(0, 'end')
        self.batt_pay_rate_amount_entry.delete(0, 'end')
        self.batt_pay_rate_description_entry.delete(0, 'end')


class TabTwo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Edit Batt Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.batt_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Batt Pay Rate Name:")
        self.batt_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_batt_pay_rate_name_label = ctk.CTkLabel(self.frame, text="New Batt Pay Rate Name:")
        self.new_batt_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_batt_pay_rate_amount_label = ctk.CTkLabel(self.frame, text="New Batt Pay Rate Amount:")
        self.new_batt_pay_rate_amount_entry = ctk.CTkEntry(self.frame)
        self.new_batt_pay_rate_description_label = ctk.CTkLabel(self.frame, text="New Batt Pay Rate Description:")
        self.new_batt_pay_rate_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.edit_batt_pay_rate_button = ctk.CTkButton(self.frame, text="Edit Batt Pay Rate",
                                                       command=self.edit_batt_pay_rate)

        # Grid the labels and entry boxes
        self.batt_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.batt_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_batt_pay_rate_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_batt_pay_rate_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_batt_pay_rate_amount_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_batt_pay_rate_amount_entry.grid(row=3, column=1, padx=10, pady=10)
        self.new_batt_pay_rate_description_label.grid(row=4, column=0, padx=10, pady=10)
        self.new_batt_pay_rate_description_entry.grid(row=4, column=1, padx=10, pady=10)

        # Grid the buttons
        self.edit_batt_pay_rate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

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

        # Clear the entry boxes
        self.batt_pay_rate_name_entry.delete(0, 'end')
        self.new_batt_pay_rate_name_entry.delete(0, 'end')
        self.new_batt_pay_rate_amount_entry.delete(0, 'end')
        self.new_batt_pay_rate_description_entry.delete(0, 'end')


class TabThree:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Delete Batt Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.batt_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Batt Pay Rate Name:")
        self.batt_pay_rate_name_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.delete_batt_pay_rate_button = ctk.CTkButton(self.frame, text="Delete Batt Pay Rate",
                                                         command=self.delete_batt_pay_rate)

        # Grid the labels and entry boxes
        self.batt_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.batt_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Grid the buttons
        self.delete_batt_pay_rate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

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

        # Clear the entry boxes
        self.batt_pay_rate_name_entry.delete(0, 'end')


class TabFour:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="View Batt Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.batt_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Batt Pay Rate Name")
        self.batt_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)

        self.batt_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.batt_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.view_batt_pay_rate_button = ctk.CTkButton(self.frame, text="View Batt Pay Rate",
                                                       command=self.view_batt_pay_rate)
        self.view_batt_pay_rate_button.grid(row=2, column=0, padx=10, pady=10)

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

        # Clear the entry boxes
        self.batt_pay_rate_name_entry.delete(0, 'end')
