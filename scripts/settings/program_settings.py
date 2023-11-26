# This file is used to import all the necessary modules and classes for the InsulPay program.
import customtkinter as ctk
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog

# Import the custom menu
from scripts.menu.menu_manager import MenuManager

# Import the Employee class
from scripts.otherclass.employee_class import Employee

# Import the database tables
from scripts.database.tables.employee_table import EmployeeTable
from scripts.database.tables.batt_pay_rate_table import BattPayRateTable

# Import paysheet toplevels
from scripts.toplevel.batt_pay_sheet import BattPaySheetTopLevel
from scripts.toplevel.attic_pay_sheet import AtticPaySheetTopLevel
from scripts.toplevel.foam_pay_sheet import FoamPaySheetTopLevel
from scripts.toplevel.shop_pay_sheet import ShopPaySheetTopLevel
from scripts.toplevel.vacation_request import VacationRequestTopLevel

# Import work order toplevels
from scripts.toplevel.new_construction_work_order import NewConstructionWorkOrder
from scripts.toplevel.existing_construction_work_order import ExistingConstructionWorkOrder
from scripts.toplevel.attic_work_order import AtticWorkOrder
from scripts.toplevel.shop_work_order import ShopWorkOrder
from scripts.toplevel.cellulose_work_order import CelluloseWorkOrder
from scripts.toplevel.spray_foam_work_order import SprayFoamWorkOrder

# Import Database notebooks
from scripts.toplevel.employee_table_manager import EmployeeTableManager
from scripts.toplevel.batt_rate_table_manager import BattPayRateTableManager
from scripts.toplevel.attic_rate_table_manager import AtticPayRateTableManager
from scripts.toplevel.foam_rate_table_manager import FoamPayRateTableManager

# Import Database notebook tabs
from scripts.tabs.employee_table_tabs import TabOne, TabTwo, TabThree, TabFour
from scripts.tabs.batt_pay_rate_table_tabs import TabOne, TabTwo, TabThree, TabFour
from scripts.tabs.attic_pay_rate_table_tabs import TabOne, TabTwo, TabThree, TabFour
from scripts.tabs.foam_pay_rate_table_tabs import TabOne, TabTwo, TabThree, TabFour

# Set the appearance mode and default color theme for CustomTkinter
ctk.set_appearance_mode("system")  # system, dark , light
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
