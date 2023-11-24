import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from scripts.tabs.employee_table_tabs import TabOne, TabTwo, TabThree, TabFour


class EmployeeTableManager:
    def __init__(self, parent):
        self.top_level = tk.Toplevel(parent)
        self.top_level.title("Employee Table Manager")

        self.notebook = ttk.Notebook(self.top_level)
        self.create_tabs()
        self.pack()

    def create_tabs(self):
        tab_one = TabOne(self.notebook)
        self.notebook.add(tab_one.frame, text="Add Employee")

        tab_two = TabTwo(self.notebook)
        self.notebook.add(tab_two.frame, text="Edit Employee")

        tab_three = TabThree(self.notebook)
        self.notebook.add(tab_three.frame, text="Delete Employee")

        tab_four = TabFour(self.notebook)
        self.notebook.add(tab_four.frame, text="View Employees")


    def pack(self):
        self.notebook.pack(expand=True, fill='both')

    def grab_set(self):
        self.top_level.grab_set()
        self.top_level.wait_window()

    def destroy(self):
        self.top_level.destroy()

    def mainloop(self):
        self.top_level.mainloop()
