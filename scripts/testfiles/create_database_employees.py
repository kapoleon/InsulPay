from scripts.database.tables.employee_table import EmployeeTable

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

