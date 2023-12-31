import os
from scripts.database.tables.base_table import BaseTable
from scripts.database.tables.employee_table import EmployeeTable
from scripts.database.tables.batt_pay_rate_table import BattPayRateTable
from scripts.database.tables.attic_pay_rate_table import AtticPayRateTable
from scripts.database.tables.foam_pay_rate_table import FoamPayRateTable
from scripts.database.tables.batt_pay_sheet_table import BattPaySheetTable


def check_and_run():
    print("Checking for database file...")
    # Specify the path to your SQLite database file
    db_file_path = 'InsulPay.db'

    if not os.path.exists(db_file_path):
        print("Database file not found. Creating database file...")
        create_database()

    else:
        print("Database file found. Continuing...")


def create_database():
    # Create 10 employees to test the database
    print("Creating employee table...")
    employee_table = EmployeeTable()
    print("Connecting to database...")
    employee_table.connect()
    print("Creating table...")
    employee_table.create_table()

    print("Adding employees...")
    employee_table.add_employee("New", "Employee 1", 5)
    employee_table.add_employee("New", "Employee 2", 5)
    employee_table.add_employee("New", "Employee 3", 5)
    employee_table.add_employee("New", "Employee 4", 5)
    employee_table.add_employee("New", "Employee 5", 5)
    employee_table.add_employee("New", "Employee 6", 5)
    employee_table.add_employee("New", "Employee 7", 5)
    employee_table.add_employee("New", "Employee 8", 5)
    employee_table.add_employee("New", "Employee 9", 5)
    employee_table.add_employee("New", "Employee 10", 5)

    print("Disconnecting from database...")
    employee_table.disconnect()

    # Create 11 batt pay rates to test the database
    print("Creating batt pay rate table...")
    batt_pay_rate_table = BattPayRateTable()
    print("Connecting to database...")
    batt_pay_rate_table.connect()
    print("Creating table...")
    batt_pay_rate_table.create_table()

    print("Adding batt pay rates...")
    batt_pay_rate_table.add_batt_pay_rate("Batt 1", 0.09, "Pay Rate 1 Description")
    batt_pay_rate_table.add_batt_pay_rate("Batt 2", 0.10, "Pay Rate 2 Description")
    batt_pay_rate_table.add_batt_pay_rate("Soffit-New", 0.55, "Pay Rate 3 Description")
    batt_pay_rate_table.add_batt_pay_rate("Caulk & Foam", 1, "Pay Rate 4 Description")
    batt_pay_rate_table.add_batt_pay_rate("BIBS-Full Install", 0.20, "Pay Rate 5 Description")
    batt_pay_rate_table.add_batt_pay_rate("BIBS-Hang Netting", 0.06, "Pay Rate 6 Description")
    batt_pay_rate_table.add_batt_pay_rate("BIBS-Tack Netting", 0.06, "Pay Rate 7 Description")
    batt_pay_rate_table.add_batt_pay_rate("BIBS-Walls Blown", 0.08, "Pay Rate 8 Description")
    batt_pay_rate_table.add_batt_pay_rate("Cellulose", 1, "Pay Rate 9 Description")
    batt_pay_rate_table.add_batt_pay_rate("Bonus Pay", 1, "Pay Rate 10 Description")
    batt_pay_rate_table.add_batt_pay_rate("Other Amount", 1, "Pay Rate 11 Description")

    print("Disconnecting from database...")
    batt_pay_rate_table.disconnect()

    # Create 11 attic pay rates to test the database
    print("Creating attic pay rate table...")
    attic_pay_rate_table = AtticPayRateTable()
    print("Connecting to database...")
    attic_pay_rate_table.connect()
    print("Creating table...")
    attic_pay_rate_table.create_table()

    print("Adding attic pay rates...")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 1", 5, "Pay Rate 1 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 2", 5, "Pay Rate 2 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 3", 5, "Pay Rate 3 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 4", 5, "Pay Rate 4 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 5", 5, "Pay Rate 5 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 6", 5, "Pay Rate 6 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 7", 5, "Pay Rate 7 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 8", 5, "Pay Rate 8 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 9", 5, "Pay Rate 9 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 10", 5, "Pay Rate 10 Description")
    attic_pay_rate_table.add_attic_pay_rate("Pay Rate 11", 5, "Pay Rate 11 Description")

    print("Disconnecting from database...")
    attic_pay_rate_table.disconnect()

    # Create 11 foam pay rates to test the database
    print("Creating foam pay rate table...")
    foam_pay_rate_table = FoamPayRateTable()
    print("Connecting to database...")
    foam_pay_rate_table.connect()
    print("Creating table...")
    foam_pay_rate_table.create_table()

    print("Adding foam pay rates...")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 1", 5, "Pay Rate 1 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 2", 5, "Pay Rate 2 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 3", 5, "Pay Rate 3 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 4", 5, "Pay Rate 4 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 5", 5, "Pay Rate 5 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 6", 5, "Pay Rate 6 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 7", 5, "Pay Rate 7 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 8", 5, "Pay Rate 8 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 9", 5, "Pay Rate 9 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 10", 5, "Pay Rate 10 Description")
    foam_pay_rate_table.add_foam_pay_rate("Pay Rate 11", 5, "Pay Rate 11 Description")

    print("Disconnecting from database...")
    foam_pay_rate_table.disconnect()

    # create the batt pay sheet table
    print("Creating batt pay sheet table...")
    batt_pay_sheet_table = BattPaySheetTable()
    print("Connecting to database...")
    batt_pay_sheet_table.connect()
    print("Creating table...")
    batt_pay_sheet_table.create_table()
    print("Disconnecting from database...")
    batt_pay_sheet_table.disconnect()
