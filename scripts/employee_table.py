# employee_table.py

from scripts.base_table import BaseTable


class EmployeeTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                                                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                first_name TEXT NOT NULL,
                                                last_name TEXT NOT NULL,
                                                vacation_days INTEGER NOT NULL,
                                                UNIQUE(first_name, last_name)
                                            );""")
            self.conn.commit()
            print("Employee table created successfully!")
        except Exception as e:
            print(f"Error creating employee table: {e}")

    def add_employee(self, first_name, last_name, vacation_days):
        try:
            self.cursor.execute("""INSERT INTO employees (first_name, last_name, vacation_days) VALUES (?, ?, ?);""",
                                (first_name, last_name, vacation_days))
            self.conn.commit()
            print("Employee added successfully!")
        except Exception as e:
            print(f"Error adding employee: {e}")
        finally:
            self.disconnect()

    def edit_employee(self, first_name, last_name, new_first_name, new_last_name, new_vacation_days):
        try:
            self.cursor.execute(
                """UPDATE employees SET first_name = ?, last_name = ?, vacation_days = ? WHERE first_name = ? AND 
                last_name = ?;""",
                (new_first_name, new_last_name, new_vacation_days, first_name, last_name))
            self.conn.commit()
            print("Employee edited successfully!")
        except Exception as e:
            print(f"Error editing employee: {e}")
        finally:
            self.disconnect()

    def delete_employee(self, first_name, last_name):
        try:
            self.cursor.execute("""DELETE FROM employees WHERE first_name = ? AND last_name = ?;""",
                                (first_name, last_name))
            self.conn.commit()
            print("Employee deleted successfully!")
        except Exception as e:
            print(f"Error deleting employee: {e}")
        finally:
            self.disconnect()

    def view_employee(self, first_name, last_name):
        try:
            self.cursor.execute("""SELECT * FROM employees WHERE first_name = ? AND last_name = ?;""",
                                (first_name, last_name))
            employee_data = self.cursor.fetchall()
            return employee_data
        except Exception as e:
            print(f"Error viewing employee: {e}")
        finally:
            self.disconnect()

    def view_all_employees(self):
        try:
            self.cursor.execute("""SELECT * FROM employees;""")
            employee_data = self.cursor.fetchall()
            return employee_data
        except Exception as e:
            print(f"Error viewing all employees: {e}")
        finally:
            self.disconnect()
