# This file is used to import all the necessary modules and classes for the InsulPay program.
import customtkinter as ctk
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
import os
import shutil
import openpyxl
import subprocess

# Import the custom menu
from custom_menu import MenuManager

# Import the Employee class
from employee_class import Employee

# Import the database tables
from database_tables import *

# Import paysheet toplevels
from batt_pay_sheet import BattPaySheetTopLevel
from attic_pay_sheet import AtticPaySheetTopLevel
from foam_pay_sheet import FoamPaySheetTopLevel
from shop_pay_sheet import ShopPaySheetTopLevel
from vacation_request import VacationRequestTopLevel

# Import work order toplevels
from new_construction_work_order import NewConstructionWorkOrder
from existing_construction_work_order import ExistingConstructionWorkOrder
from attic_work_order import AtticWorkOrder
from shop_work_order import ShopWorkOrder
from cellulose_work_order import CelluloseWorkOrder
from spray_foam_work_order import SprayFoamWorkOrder

# Import Database Managers
from employee_table_manager import *
from batt_rate_table_manager import *
from attic_rate_table_manager import *
from foam_rate_table_manager import *
from vacation_rate_table_manager import *

# run the script that perform necessary files for start up
from start_file import *


# Set the appearance mode and default color theme for CustomTkinter
ctk.set_appearance_mode("system")  # system, dark , light
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
