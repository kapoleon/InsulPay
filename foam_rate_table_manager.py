from program_settings import *


class FoamPayRateTableManager:
    def __init__(self, parent):
        self.top_level = tk.Toplevel(parent)
        self.top_level.title("Foam Pay Rate Table Manager")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Foam Pay Rate")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="Edit Foam Pay Rate")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Delete Foam Pay Rate")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="View Foam Pay Rate")

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

        label = ttk.Label(self.frame, text="Add Foam Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.foam_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Foam Pay Rate Name:")
        self.foam_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.foam_pay_rate_amount_label = ctk.CTkLabel(self.frame, text="Foam Pay Rate Amount:")
        self.foam_pay_rate_amount_entry = ctk.CTkEntry(self.frame)
        self.foam_pay_rate_description_label = ctk.CTkLabel(self.frame, text="Foam Pay Rate Description:")
        self.foam_pay_rate_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.add_foam_pay_rate_button = ctk.CTkButton(self.frame, text="Add Foam Pay Rate",
                                                      command=self.add_foam_pay_rate)

        # Grid the labels and entry boxes
        self.foam_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.foam_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.foam_pay_rate_amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.foam_pay_rate_amount_entry.grid(row=2, column=1, padx=10, pady=10)
        self.foam_pay_rate_description_label.grid(row=3, column=0, padx=10, pady=10)
        self.foam_pay_rate_description_entry.grid(row=3, column=1, padx=10, pady=10)

        # Grid the buttons
        self.add_foam_pay_rate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

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
        foam_pay_rate_table.create_table()
        foam_pay_rate_table.add_foam_pay_rate(foam_pay_rate_name, foam_pay_rate_amount, foam_pay_rate_description)

        messagebox.showinfo("Success", "Foam Pay Rate added successfully!")

        # Clear the entry boxes
        self.foam_pay_rate_name_entry.delete(0, 'end')
        self.foam_pay_rate_amount_entry.delete(0, 'end')
        self.foam_pay_rate_description_entry.delete(0, 'end')


class TabTwo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Edit Foam Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.foam_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Foam Pay Rate Name:")
        self.foam_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_foam_pay_rate_name_label = ctk.CTkLabel(self.frame, text="New Foam Pay Rate Name:")
        self.new_foam_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_foam_pay_rate_amount_label = ctk.CTkLabel(self.frame, text="New Foam Pay Rate Amount:")
        self.new_foam_pay_rate_amount_entry = ctk.CTkEntry(self.frame)
        self.new_foam_pay_rate_description_label = ctk.CTkLabel(self.frame, text="New Foam Pay Rate Description:")
        self.new_foam_pay_rate_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.edit_foam_pay_rate_button = ctk.CTkButton(self.frame, text="Edit Foam Pay Rate",
                                                       command=self.edit_foam_pay_rate)

        # Grid the labels and entry boxes
        self.foam_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.foam_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_foam_pay_rate_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_foam_pay_rate_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_foam_pay_rate_amount_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_foam_pay_rate_amount_entry.grid(row=3, column=1, padx=10, pady=10)
        self.new_foam_pay_rate_description_label.grid(row=4, column=0, padx=10, pady=10)
        self.new_foam_pay_rate_description_entry.grid(row=4, column=1, padx=10, pady=10)

        # Grid the buttons
        self.edit_foam_pay_rate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

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

        # Clear the entry boxes
        self.foam_pay_rate_name_entry.delete(0, 'end')
        self.new_foam_pay_rate_name_entry.delete(0, 'end')
        self.new_foam_pay_rate_amount_entry.delete(0, 'end')
        self.new_foam_pay_rate_description_entry.delete(0, 'end')


class TabThree:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Delete Foam Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.foam_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Foam Pay Rate Name:")
        self.foam_pay_rate_name_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.delete_foam_pay_rate_button = ctk.CTkButton(self.frame, text="Delete Foam Pay Rate",
                                                         command=self.delete_foam_pay_rate)

        # Grid the labels and entry boxes
        self.foam_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.foam_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Grid the buttons
        self.delete_foam_pay_rate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

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

        # Clear the entry boxes
        self.foam_pay_rate_name_entry.delete(0, 'end')


class TabFour:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="View Foam Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.foam_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Foam Pay Rate Name")
        self.foam_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)

        self.foam_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.foam_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.view_foam_pay_rate_button = ctk.CTkButton(self.frame, text="View Foam Pay Rate",
                                                       command=self.view_foam_pay_rate)
        self.view_foam_pay_rate_button.grid(row=2, column=0, padx=10, pady=10)

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

        # Clear the entry boxes
        self.foam_pay_rate_name_entry.delete(0, 'end')
