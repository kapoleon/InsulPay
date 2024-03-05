from program_settings import *


class AtticPayRateTableManager:
    def __init__(self, parent):
        self.top_level = tk.Toplevel(parent)
        self.top_level.title("Attic Pay Rate Table Manager")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Attic Pay Rate")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="Edit Attic Pay Rate")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Delete Attic Pay Rate")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="View Attic Pay Rate")

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

        label = ttk.Label(self.frame, text="Add Attic Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.attic_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Attic Pay Rate Name:")
        self.attic_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.attic_pay_rate_amount_label = ctk.CTkLabel(self.frame, text="Attic Pay Rate Amount:")
        self.attic_pay_rate_amount_entry = ctk.CTkEntry(self.frame)
        self.attic_pay_rate_description_label = ctk.CTkLabel(self.frame, text="Attic Pay Rate Description:")
        self.attic_pay_rate_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.add_attic_pay_rate_button = ctk.CTkButton(self.frame, text="Add Attic Pay Rate",
                                                       command=self.add_attic_pay_rate)

        # Grid the labels and entry boxes
        self.attic_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.attic_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.attic_pay_rate_amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.attic_pay_rate_amount_entry.grid(row=2, column=1, padx=10, pady=10)
        self.attic_pay_rate_description_label.grid(row=3, column=0, padx=10, pady=10)
        self.attic_pay_rate_description_entry.grid(row=3, column=1, padx=10, pady=10)

        # Grid the buttons
        self.add_attic_pay_rate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

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
        attic_pay_rate_table.create_table()
        attic_pay_rate_table.add_attic_pay_rate(attic_pay_rate_name, attic_pay_rate_amount, attic_pay_rate_description)

        messagebox.showinfo("Success", "Attic Pay Rate added successfully!")

        # Clear the entry boxes
        self.attic_pay_rate_name_entry.delete(0, 'end')
        self.attic_pay_rate_amount_entry.delete(0, 'end')
        self.attic_pay_rate_description_entry.delete(0, 'end')


class TabTwo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Edit Attic Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.attic_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Attic Pay Rate Name:")
        self.attic_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_attic_pay_rate_name_label = ctk.CTkLabel(self.frame, text="New Attic Pay Rate Name:")
        self.new_attic_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_attic_pay_rate_amount_label = ctk.CTkLabel(self.frame, text="New Attic Pay Rate Amount:")
        self.new_attic_pay_rate_amount_entry = ctk.CTkEntry(self.frame)
        self.new_attic_pay_rate_description_label = ctk.CTkLabel(self.frame, text="New Attic Pay Rate Description:")
        self.new_attic_pay_rate_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.edit_attic_pay_rate_button = ctk.CTkButton(self.frame, text="Edit Attic Pay Rate",
                                                        command=self.edit_attic_pay_rate)

        # Grid the labels and entry boxes
        self.attic_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.attic_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_attic_pay_rate_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_attic_pay_rate_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_attic_pay_rate_amount_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_attic_pay_rate_amount_entry.grid(row=3, column=1, padx=10, pady=10)
        self.new_attic_pay_rate_description_label.grid(row=4, column=0, padx=10, pady=10)
        self.new_attic_pay_rate_description_entry.grid(row=4, column=1, padx=10, pady=10)

        # Grid the buttons
        self.edit_attic_pay_rate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

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

        # Clear the entry boxes
        self.attic_pay_rate_name_entry.delete(0, 'end')
        self.new_attic_pay_rate_name_entry.delete(0, 'end')
        self.new_attic_pay_rate_amount_entry.delete(0, 'end')
        self.new_attic_pay_rate_description_entry.delete(0, 'end')


class TabThree:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Delete Attic Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.attic_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Attic Pay Rate Name:")
        self.attic_pay_rate_name_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.delete_attic_pay_rate_button = ctk.CTkButton(self.frame, text="Delete Attic Pay Rate",
                                                          command=self.delete_attic_pay_rate)

        # Grid the labels and entry boxes
        self.attic_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.attic_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Grid the buttons
        self.delete_attic_pay_rate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

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

        # Clear the entry boxes
        self.attic_pay_rate_name_entry.delete(0, 'end')


class TabFour:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="View Attic Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.attic_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Attic Pay Rate Name")
        self.attic_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)

        self.attic_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.attic_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.view_attic_pay_rate_button = ctk.CTkButton(self.frame, text="View Attic Pay Rate",
                                                        command=self.view_attic_pay_rate)
        self.view_attic_pay_rate_button.grid(row=2, column=0, padx=10, pady=10)

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

        # Clear the entry boxes
        self.attic_pay_rate_name_entry.delete(0, 'end')
