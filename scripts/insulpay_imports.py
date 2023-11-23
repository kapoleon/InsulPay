# This file is used to import all the necessary modules and classes for the InsulPay program.
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

from scripts.batt_pay_sheet_table import BattPaySheetTable
from scripts.attic_pay_sheet_table import AtticPaySheetTable
from scripts.foam_pay_sheet_table import FoamPaySheetTable
from scripts.vacation_request_table import VacationRequestTable
from scripts.shop_pay_sheet_table import ShopPaySheetTable

from scripts.employee_db_toplevel import AddEmployeeWindow, EditEmployeeWindow, DeleteEmployeeWindow, ViewEmployeeWindow
from scripts.batt_pay_rate_toplevel import AddBattPayRateWindow, EditBattPayRateWindow, DeleteBattPayRateWindow, \
    ViewBattPayRateWindow
from scripts.attic_pay_rate_toplevel import AddAtticPayRateWindow, EditAtticPayRateWindow, DeleteAtticPayRateWindow, \
    ViewAtticPayRateWindow
from scripts.foam_pay_rate_toplevel import AddFoamPayRateWindow, EditFoamPayRateWindow, DeleteFoamPayRateWindow, \
    ViewFoamPayRateWindow

from scripts.employee_class import Employee

from scripts.batt_pay_sheet_toplevel import BattPaySheetTopLevel
from scripts.attic_pay_sheet_toplevel import AtticPaySheetTopLevel
from scripts.foam_pay_sheet_toplevel import FoamPaySheetTopLevel
from scripts.vacation_request_toplevel import VacationRequestTopLevel
from scripts.shop_pay_sheet_toplevel import ShopPaySheetTopLevel

# Set the appearance mode and default color theme for CustomTkinter
ctk.set_appearance_mode("system")  # system, dark , light
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
