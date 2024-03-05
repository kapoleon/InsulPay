from program_settings import *


class VacationPayRateTableManager:
    def __init__(self, parent):
        self.top_level = tk.Toplevel(parent)
        self.top_level.title("Vacation Pay Rate Table Manager")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Vacation Pay Rate")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="Edit Vacation Pay Rate")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Delete Vacation Pay Rate")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="View Vacation Pay Rate")

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

        label = ttk.Label(self.frame, text="Add Vacation Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.vacation_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Vacation Pay Rate Name")
        self.vacation_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.vacation_pay_rate_label = ctk.CTkLabel(self.frame, text="Vacation Pay Rate")
        self.vacation_pay_rate_entry = ctk.CTkEntry(self.frame)
        self.vacation_pay_description_label = ctk.CTkLabel(self.frame, text="Vacation Pay Description")
        self.vacation_pay_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.add_button = ctk.CTkButton(self.frame, text="Add", command=self.add_vacation_pay_rate)

        # Grid the widgets
        self.vacation_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.vacation_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.vacation_pay_rate_label.grid(row=2, column=0, padx=10, pady=10)
        self.vacation_pay_rate_entry.grid(row=2, column=1, padx=10, pady=10)
        self.vacation_pay_description_label.grid(row=3, column=0, padx=10, pady=10)
        self.vacation_pay_description_entry.grid(row=3, column=1, padx=10, pady=10)

        # Grid the buttons
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

    def add_vacation_pay_rate(self):
        vacation_pay_rate_name = self.vacation_pay_rate_name_entry.get()
        vacation_pay_rate = self.vacation_pay_rate_entry.get()
        vacation_pay_description = self.vacation_pay_description_entry.get()

        # Check if the user entered all the required information
        if vacation_pay_rate_name == "" or vacation_pay_rate == "" or vacation_pay_description == "":
            messagebox.showerror("Error", "Please enter all the required information.")
            return

        # Check if the vacation pay rate is a number
        try:
            vacation_pay_rate = float(vacation_pay_rate)
        except ValueError:
            messagebox.showerror("Error", "Vacation pay rate must be a number.")
            return

        # Check if the vacation pay rate is greater than 0
        if vacation_pay_rate <= 0:
            messagebox.showerror("Error", "Vacation pay rate must be greater than 0.")
            return

        # Add the vacation pay rate to the database
        vacation_pay_rate_table = VacationPayRateTable()
        vacation_pay_rate_table.connect()
        vacation_pay_rate_table.add_vacation_pay_rate(vacation_pay_rate_name, vacation_pay_rate,
                                                      vacation_pay_description)
        vacation_pay_rate_table.disconnect()

        # Clear the entry boxes
        self.vacation_pay_rate_name_entry.delete(0, 'end')
        self.vacation_pay_rate_entry.delete(0, 'end')
        self.vacation_pay_description_entry.delete(0, 'end')


class TabTwo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Edit Vacation Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.vacation_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Vacation Pay Rate Name")
        self.vacation_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_vacation_pay_rate_name_label = ctk.CTkLabel(self.frame, text="New Vacation Pay Rate Name")
        self.new_vacation_pay_rate_name_entry = ctk.CTkEntry(self.frame)
        self.new_vacation_pay_rate_label = ctk.CTkLabel(self.frame, text="New Vacation Pay Rate")
        self.new_vacation_pay_rate_entry = ctk.CTkEntry(self.frame)
        self.new_vacation_pay_description_label = ctk.CTkLabel(self.frame, text="New Vacation Pay Description")
        self.new_vacation_pay_description_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.edit_button = ctk.CTkButton(self.frame, text="Edit", command=self.edit_vacation_pay_rate)

        # Grid the widgets
        self.vacation_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.vacation_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)
        self.new_vacation_pay_rate_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.new_vacation_pay_rate_name_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_vacation_pay_rate_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_vacation_pay_rate_entry.grid(row=3, column=1, padx=10, pady=10)
        self.new_vacation_pay_description_label.grid(row=4, column=0, padx=10, pady=10)
        self.new_vacation_pay_description_entry.grid(row=4, column=1, padx=10, pady=10)

        # Grid the buttons
        self.edit_button.grid(row=5, column=0, padx=10, pady=10)

    def edit_vacation_pay_rate(self):
        vacation_pay_rate_name = self.vacation_pay_rate_name_entry.get()
        new_vacation_pay_rate_name = self.new_vacation_pay_rate_name_entry.get()
        new_vacation_pay_rate = self.new_vacation_pay_rate_entry.get()
        new_vacation_pay_description = self.new_vacation_pay_description_entry.get()

        # Check if the user entered all the required information
        if vacation_pay_rate_name == "" or new_vacation_pay_rate_name == "" or new_vacation_pay_rate == "" or new_vacation_pay_description == "":
            messagebox.showerror("Error", "Please enter all the required information.")
            return

        # Check if the new vacation pay rate is a number
        try:
            new_vacation_pay_rate = float(new_vacation_pay_rate)
        except ValueError:
            messagebox.showerror("Error", "New vacation pay rate must be a number.")
            return

        # Check if the new vacation pay rate is greater than 0
        if new_vacation_pay_rate <= 0:
            messagebox.showerror("Error", "New vacation pay rate must be greater than 0.")
            return

        # Edit the vacation pay rate in the database
        vacation_pay_rate_table = VacationPayRateTable()
        vacation_pay_rate_table.connect()
        vacation_pay_rate_table.edit_vacation_pay_rate(vacation_pay_rate_name, new_vacation_pay_rate_name,
                                                       new_vacation_pay_rate, new_vacation_pay_description)
        vacation_pay_rate_table.disconnect()

        # Clear the entry boxes
        self.vacation_pay_rate_name_entry.delete(0, 'end')
        self.new_vacation_pay_rate_name_entry.delete(0, 'end')
        self.new_vacation_pay_rate_entry.delete(0, 'end')
        self.new_vacation_pay_description_entry.delete(0, 'end')


class TabThree:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="Delete Vacation Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.vacation_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Vacation Pay Rate Name")
        self.vacation_pay_rate_name_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.delete_button = ctk.CTkButton(self.frame, text="Delete", command=self.delete_vacation_pay_rate)

        # Grid the widgets
        self.vacation_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.vacation_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Grid the buttons
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

    def delete_vacation_pay_rate(self):
        vacation_pay_rate_name = self.vacation_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if vacation_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information.")
            return

        # Delete the vacation pay rate from the database
        vacation_pay_rate_table = VacationPayRateTable()
        vacation_pay_rate_table.connect()
        vacation_pay_rate_table.delete_vacation_pay_rate(vacation_pay_rate_name)
        vacation_pay_rate_table.disconnect()

        # Clear the entry boxes
        self.vacation_pay_rate_name_entry.delete(0, 'end')


class TabFour:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.widget_font = ("Roboto", 15, "bold")

        label = ttk.Label(self.frame, text="View Vacation Pay Rate", font=self.widget_font)
        label.grid(row=0, column=0, padx=10, pady=10)

        # Create the labels and entry boxes
        self.vacation_pay_rate_name_label = ctk.CTkLabel(self.frame, text="Vacation Pay Rate Name")
        self.vacation_pay_rate_name_entry = ctk.CTkEntry(self.frame)

        # Create the buttons
        self.view_button = ctk.CTkButton(self.frame, text="View", command=self.view_vacation_pay_rate)

        # Grid the widgets
        self.vacation_pay_rate_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.vacation_pay_rate_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Grid the buttons
        self.view_button.grid(row=2, column=0, padx=10, pady=10)

    def view_vacation_pay_rate(self):
        vacation_pay_rate_name = self.vacation_pay_rate_name_entry.get()

        # Check if the user entered all the required information
        if vacation_pay_rate_name == "":
            messagebox.showerror("Error", "Please enter all the required information.")
            return

        # View the vacation pay rate in the database
        vacation_pay_rate_table = VacationPayRateTable()
        vacation_pay_rate_table.connect()
        try:
            vacation_pay_rate_data = vacation_pay_rate_table.view_vacation_pay_rate(vacation_pay_rate_name)
            if vacation_pay_rate_data:
                # Create a string representation of the attic pay rate information
                vacation_pay_rate_info = "\n".join([f"{key}: {value}" for key, value in
                                                    zip(["ID", "Vacation Pay Rate Name", "Vacation Pay Rate Amount",
                                                         "Vacation Pay Rate Description"], vacation_pay_rate_data[0])])
                messagebox.showinfo("Vacation Pay Rate Information",
                                    f"Vacation Pay Rate Details:\n{vacation_pay_rate_info}")
            else:
                messagebox.showinfo("Vacation Pay Rate Not Found", "No vacation pay rate found with the given details.")
        except Exception as e:
            messagebox.showerror("Error", f"Error viewing vacation pay rate: {e}")

        # Clear the entry boxes
        self.vacation_pay_rate_name_entry.delete(0, 'end')
