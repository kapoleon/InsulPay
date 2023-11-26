from scripts.database.tables.employee_table import EmployeeTable
from scripts.database.tables.batt_pay_rate_table import BattPayRateTable

# Create 10 employees to test the database
employee_table = EmployeeTable()
employee_table.connect()
employee_table.create_table()

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

employee_table.disconnect()

# Create 11 batt pay rates to test the database
batt_pay_rate_table = BattPayRateTable()
batt_pay_rate_table.connect()
batt_pay_rate_table.create_table()

batt_pay_rate_table.add_batt_pay_rate("Pay Rate 1", 5, "Pay Rate 1 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 2", 5, "Pay Rate 2 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 3", 5, "Pay Rate 3 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 4", 5, "Pay Rate 4 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 5", 5, "Pay Rate 5 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 6", 5, "Pay Rate 6 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 7", 5, "Pay Rate 7 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 8", 5, "Pay Rate 8 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 9", 5, "Pay Rate 9 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 10", 5, "Pay Rate 10 Description")
batt_pay_rate_table.add_batt_pay_rate("Pay Rate 11", 5, "Pay Rate 11 Description")

batt_pay_rate_table.disconnect()
