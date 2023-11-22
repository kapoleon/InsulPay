import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sqlite3

from scripts.main_menu import MenuManager

from scripts.base_table import BaseTable
from scripts.employee_table import EmployeeTable
from scripts.batt_pay_rate_table import BattPayRateTable
from scripts.attic_pay_rate_table import AtticPayRateTable
from scripts.foam_pay_rate_table import FoamPayRateTable


from scripts.employee_db_toplevel import AddEmployeeWindow, EditEmployeeWindow, DeleteEmployeeWindow, ViewEmployeeWindow
from scripts.batt_pay_rate_toplevel import AddBattPayRateWindow, EditBattPayRateWindow, DeleteBattPayRateWindow, \
    ViewBattPayRateWindow
from scripts.attic_pay_rate_toplevel import AddAtticPayRateWindow, EditAtticPayRateWindow, DeleteAtticPayRateWindow, \
    ViewAtticPayRateWindow
from scripts.foam_pay_rate_toplevel import AddFoamPayRateWindow, EditFoamPayRateWindow, DeleteFoamPayRateWindow, \
    ViewFoamPayRateWindow

from scripts.employee_class import Employee


# Set the appearance mode and default color theme for CustomTkinter
ctk.set_appearance_mode("system")  # system, dark , light
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
