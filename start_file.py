from program_settings import *


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
    # Create 15 employees to test the database
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
    employee_table.add_employee("New", "Employee 11", 5)
    employee_table.add_employee("New", "Employee 12", 5)
    employee_table.add_employee("New", "Employee 13", 5)
    employee_table.add_employee("New", "Employee 14", 5)
    employee_table.add_employee("New", "Employee 15", 5)

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

    # Create attic pay rates to test the database
    print("Creating attic pay rate table...")
    attic_pay_rate_table = AtticPayRateTable()
    print("Connecting to database...")
    attic_pay_rate_table.connect()
    print("Creating table...")
    attic_pay_rate_table.create_table()

    print("Adding attic pay rates...")
    attic_pay_rate_table.add_attic_pay_rate("R19", .08, "Pay Rate 1 Description")
    attic_pay_rate_table.add_attic_pay_rate("R30", .09, "Pay Rate 2 Description")
    attic_pay_rate_table.add_attic_pay_rate("R38", .10, "Pay Rate 3 Description")
    attic_pay_rate_table.add_attic_pay_rate("R49", .11, "Pay Rate 4 Description")
    attic_pay_rate_table.add_attic_pay_rate("Cellulose", .10, "Pay Rate 5 Description")
    attic_pay_rate_table.add_attic_pay_rate("Soffits", 2.50, "Pay Rate 6 Description")
    attic_pay_rate_table.add_attic_pay_rate("Bonus Amount", 1, "Pay Rate 7 Description")
    attic_pay_rate_table.add_attic_pay_rate("Other Amount", 1, "Pay Rate 8 Description")
    attic_pay_rate_table.add_attic_pay_rate("Air Seal", 1, "Pay Rate 9 Description")
    print("Disconnecting from database...")
    attic_pay_rate_table.disconnect()

    # Create foam pay rates to test the database
    print("Creating foam pay rate table...")
    foam_pay_rate_table = FoamPayRateTable()
    print("Connecting to database...")
    foam_pay_rate_table.connect()
    print("Creating table...")
    foam_pay_rate_table.create_table()

    print("Adding foam pay rates...")
    foam_pay_rate_table.add_foam_pay_rate("Closed Cell 3/4", .15, "Pay Rate 1 Description")
    foam_pay_rate_table.add_foam_pay_rate("Closed Cell 1", .22, "Pay Rate 2 Description")
    foam_pay_rate_table.add_foam_pay_rate("Closed Cell 2", .22, "Pay Rate 3 Description")
    foam_pay_rate_table.add_foam_pay_rate("Closed Cell 3", .33, "Pay Rate 4 Description")
    foam_pay_rate_table.add_foam_pay_rate("Open Cell 4", .15, "Pay Rate 5 Description")
    foam_pay_rate_table.add_foam_pay_rate("Open Cell 6", .20, "Pay Rate 6 Description")
    foam_pay_rate_table.add_foam_pay_rate("Open Cell 8", .22, "Pay Rate 7 Description")
    foam_pay_rate_table.add_foam_pay_rate("Bonus Pay", 1, "Pay Rate 8 Description")
    foam_pay_rate_table.add_foam_pay_rate("Other Amount", 1, "Pay Rate 9 Description")

    print("Disconnecting from database...")
    foam_pay_rate_table.disconnect()

    # Create vacation pay rates to test the database
    print("Creating vacation pay rate table...")
    vacation_pay_rate_table = VacationPayRateTable()
    print("Connecting to database...")
    vacation_pay_rate_table.connect()
    print("Creating table...")
    vacation_pay_rate_table.create_table()

    print("Adding vacation pay rates...")
    vacation_pay_rate_table.add_vacation_pay_rate("Vacation", 130, "Vacation Pay")

    print("Disconnecting from database...")
    vacation_pay_rate_table.disconnect()


def create_directories():
    print("Checking for directories...")
    directory_path = os.path.join(os.getcwd(), 'temp')
    directory_path_1 = os.path.join(os.getcwd(), 'temp', 'work orders')
    directory_path_2 = os.path.join(os.getcwd(), 'temp', 'pay sheets')
    directory_path_3 = os.path.join(os.getcwd(), 'temp', 'vacation')
    directory_path_4 = os.path.join(os.getcwd(), 'temp', 'work orders', 'new construction')
    directory_path_5 = os.path.join(os.getcwd(), 'temp', 'work orders', 'existing homes')
    directory_path_6 = os.path.join(os.getcwd(), 'temp', 'work orders', 'spray foam')
    directory_path_7 = os.path.join(os.getcwd(), 'temp', 'work orders', 'attic')
    directory_path_8 = os.path.join(os.getcwd(), 'temp', 'work orders', 'cellulose')
    directory_path_9 = os.path.join(os.getcwd(), 'temp', 'work orders', 'shop work')
    directory_path_10 = os.path.join(os.getcwd(), 'temp', 'pay sheets', 'batt pay sheets')
    directory_path_11 = os.path.join(os.getcwd(), 'temp', 'pay sheets', 'attic pay sheets')
    directory_path_12 = os.path.join(os.getcwd(), 'temp', 'pay sheets', 'foam pay sheets')
    directory_path_13 = os.path.join(os.getcwd(), 'temp', 'pay sheets', 'shop pay sheets')
    directory_path_14 = os.path.join(os.getcwd(), 'temp', 'weekly payroll')
    directory_path_15 = os.path.join(os.getcwd(), 'payroll records')

    if not os.path.exists(directory_path):
        print("Creating temp directory...")
        os.mkdir(directory_path)
    else:
        print("Temp directory found. Continuing...")

    if not os.path.exists(directory_path_1):
        print("Creating work orders directory...")
        os.mkdir(directory_path_1)
    else:
        print("Work orders directory found. Continuing...")

    if not os.path.exists(directory_path_2):
        print("Creating pay sheets directory...")
        os.mkdir(directory_path_2)
    else:
        print("Pay sheets directory found. Continuing...")

    if not os.path.exists(directory_path_3):
        print("Creating vacation directory...")
        os.mkdir(directory_path_3)

    if not os.path.exists(directory_path_4):
        print("Creating new construction directory...")
        os.mkdir(directory_path_4)
    else:
        print("New construction directory found. Continuing...")

    if not os.path.exists(directory_path_5):
        print("Creating existing homes directory...")
        os.mkdir(directory_path_5)
    else:
        print("Existing homes directory found. Continuing...")

    if not os.path.exists(directory_path_6):
        print("Creating spray foam directory...")
        os.mkdir(directory_path_6)
    else:
        print("Spray foam directory found. Continuing...")

    if not os.path.exists(directory_path_7):
        print("Creating attic directory...")
        os.mkdir(directory_path_7)
    else:
        print("Attic directory found. Continuing...")

    if not os.path.exists(directory_path_8):
        print("Creating cellulose directory...")
        os.mkdir(directory_path_8)
    else:
        print("Cellulose directory found. Continuing...")

    if not os.path.exists(directory_path_9):
        print("Creating shop work directory...")
        os.mkdir(directory_path_9)
    else:
        print("Shop work directory found. Continuing...")

    if not os.path.exists(directory_path_10):
        print("Creating batt pay sheets directory...")
        os.mkdir(directory_path_10)
    else:
        print("Batt pay sheets directory found. Continuing...")

    if not os.path.exists(directory_path_11):
        print("Creating attic pay sheets directory...")
        os.mkdir(directory_path_11)
    else:
        print("Attic pay sheets directory found. Continuing...")

    if not os.path.exists(directory_path_12):
        print("Creating foam pay sheets directory...")
        os.mkdir(directory_path_12)
    else:
        print("Foam pay sheets directory found. Continuing...")

    if not os.path.exists(directory_path_13):
        print("Creating shop pay sheets directory...")
        os.mkdir(directory_path_13)
    else:
        print("Shop pay sheets directory found. Continuing...")

    if not os.path.exists(directory_path_14):
        print("Creating weekly payroll directory...")
        os.mkdir(directory_path_14)
    else:
        print("Weekly payroll directory found. Continuing...")

    if not os.path.exists(directory_path_15):
        print("Creating payroll records directory...")
        os.mkdir(directory_path_15)
    else:
        print("Payroll records directory found. Continuing...")

    print("Directories created. Continuing...")
