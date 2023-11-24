import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

from scripts.attic_pay_rate_toplevel import AddAtticPayRateWindow, EditAtticPayRateWindow, DeleteAtticPayRateWindow, \
    ViewAtticPayRateWindow
from scripts.foam_pay_rate_toplevel import AddFoamPayRateWindow, EditFoamPayRateWindow, DeleteFoamPayRateWindow, \
    ViewFoamPayRateWindow


class MenuManager:
    def __init__(self, master):
        self.master = master
        self.menu_font = ("Roboto", 15, "bold")

    def create_main_menu(self):
        main_menu = tk.Menu(self.master)
        self.master.config(menu=main_menu)
        self.create_file_menu(main_menu)
        self.create_database_menu(main_menu)

    def create_file_menu(self, main_menu):
        file_menu = tk.Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File", command=self.open_file, font=self.menu_font)
        file_menu.add_command(label="Close Window", command=self.on_closing, font=self.menu_font)

    def create_database_menu(self, main_menu):
        database_menu = tk.Menu(main_menu, tearoff=False)
        main_menu.add_cascade(label="Database", menu=database_menu)
        self.create_attic_pay_rate_management_menu(database_menu)
        self.create_foam_pay_rate_management_menu(database_menu)

    def create_attic_pay_rate_management_menu(self, database_menu):
        attic_pay_rate_management_menu = tk.Menu(database_menu, tearoff=False)
        database_menu.add_cascade(label="Attic Pay Rate Manager", menu=attic_pay_rate_management_menu,
                                  font=self.menu_font)
        attic_pay_rate_management_menu.add_command(label="Add Attic Pay Rate", command=self.add_attic_pay_rate,
                                                   font=self.menu_font)
        attic_pay_rate_management_menu.add_command(label="Edit Attic Pay Rate", command=self.edit_attic_pay_rate,
                                                   font=self.menu_font)
        attic_pay_rate_management_menu.add_command(label="Delete Attic Pay Rate", command=self.delete_attic_pay_rate,
                                                   font=self.menu_font)
        attic_pay_rate_management_menu.add_command(label="View Attic Pay Rate", command=self.view_attic_pay_rate,
                                                   font=self.menu_font)

    def create_foam_pay_rate_management_menu(self, database_menu):
        foam_pay_rate_management_menu = tk.Menu(database_menu, tearoff=False)
        database_menu.add_cascade(label="Foam Pay Rate Manager", menu=foam_pay_rate_management_menu,
                                  font=self.menu_font)
        foam_pay_rate_management_menu.add_command(label="Add Foam Pay Rate", command=self.add_foam_pay_rate,
                                                  font=self.menu_font)
        foam_pay_rate_management_menu.add_command(label="Edit Foam Pay Rate", command=self.edit_foam_pay_rate,
                                                  font=self.menu_font)
        foam_pay_rate_management_menu.add_command(label="Delete Foam Pay Rate", command=self.delete_foam_pay_rate,
                                                  font=self.menu_font)
        foam_pay_rate_management_menu.add_command(label="View Foam Pay Rate", command=self.view_foam_pay_rate,
                                                  font=self.menu_font)

    # Placeholder methods for the commands
    @staticmethod
    def open_file():
        file_path = tk.filedialog.askopenfilename(initialdir="/",
                                                  title="Select A File",
                                                  filetypes=(("excel files", "*.xlsx"), ("All Files", "*.*")))
        subprocess.Popen([file_path], shell=True)

    # Close the Application
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

    # Attic Pay Rate Management Submenu Commands
    def add_attic_pay_rate(self):
        add_attic_pay_rate_window = AddAtticPayRateWindow(self.master)
        add_attic_pay_rate_window.grab_set()

    def edit_attic_pay_rate(self):
        edit_attic_pay_rate_window = EditAtticPayRateWindow(self.master)
        edit_attic_pay_rate_window.grab_set()

    def delete_attic_pay_rate(self):
        delete_attic_pay_rate_window = DeleteAtticPayRateWindow(self.master)
        delete_attic_pay_rate_window.grab_set()

    def view_attic_pay_rate(self):
        view_attic_pay_rate_window = ViewAtticPayRateWindow(self.master)
        view_attic_pay_rate_window.grab_set()

    # Foam Pay Rate Management Submenu Commands
    def add_foam_pay_rate(self):
        add_foam_pay_rate_window = AddFoamPayRateWindow(self.master)
        add_foam_pay_rate_window.grab_set()

    def edit_foam_pay_rate(self):
        edit_foam_pay_rate_window = EditFoamPayRateWindow(self.master)
        edit_foam_pay_rate_window.grab_set()

    def delete_foam_pay_rate(self):
        delete_foam_pay_rate_window = DeleteFoamPayRateWindow(self.master)
        delete_foam_pay_rate_window.grab_set()

    def view_foam_pay_rate(self):
        view_foam_pay_rate_window = ViewFoamPayRateWindow(self.master)
        view_foam_pay_rate_window.grab_set()
