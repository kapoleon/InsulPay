# employee_class.py
from database_tables import EmployeeTable


class Employee:
    def __init__(self, employee_id, first_name, last_name, vacation_days):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.vacation_days = vacation_days

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Vacation Days: {self.vacation_days}"
