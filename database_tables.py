from base_table import BaseTable


class EmployeeTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                                                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                first_name TEXT NOT NULL,
                                                last_name TEXT NOT NULL,
                                                vacation_days INTEGER NOT NULL,
                                                UNIQUE(employee_id)
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

    def delete_employee(self, first_name, last_name):
        try:
            self.cursor.execute("""DELETE FROM employees WHERE first_name = ? AND last_name = ?;""",
                                (first_name, last_name))
            self.conn.commit()
            print("Employee deleted successfully!")
        except Exception as e:
            print(f"Error deleting employee: {e}")

    def view_employee(self, first_name, last_name):
        try:
            self.cursor.execute("""SELECT * FROM employees WHERE first_name = ? AND last_name = ?;""",
                                (first_name, last_name))
            employee_data = self.cursor.fetchall()
            return employee_data
        except Exception as e:
            print(f"Error viewing employee: {e}")

    def view_all_employees(self):
        try:
            self.cursor.execute("""SELECT * FROM employees;""")
            employee_data = self.cursor.fetchall()
            return employee_data
        except Exception as e:
            print(f"Error viewing all employees: {e}")

    def view_employee_by_id(self, employee_id):
        try:
            self.cursor.execute("""SELECT * FROM employees WHERE employee_id = ?;""", (employee_id,))
            employee_data = self.cursor.fetchone()
            return employee_data
        except Exception as e:
            print(f"Error viewing employee by ID: {e}")


class BattPayRateTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS batt_pay_rates (
                                    batt_pay_rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    batt_pay_rate_name TEXT NOT NULL,
                                    batt_pay_rate_amount REAL NOT NULL,
                                    batt_pay_rate_description TEXT NOT NULL,
                                    UNIQUE(batt_pay_rate_id)
                                );""")
            self.conn.commit()
            print("Batt Pay Rate table created successfully!")
        except Exception as e:
            print(f"Error creating batt pay rate table: {e}")

    def add_batt_pay_rate(self, batt_pay_rate_name, batt_pay_rate_amount, batt_pay_rate_description):
        try:
            self.cursor.execute("""INSERT INTO batt_pay_rates (batt_pay_rate_name, batt_pay_rate_amount, 
            batt_pay_rate_description) VALUES (?, ?, ?);""",
                                (batt_pay_rate_name, batt_pay_rate_amount, batt_pay_rate_description))
            self.conn.commit()
            print("Batt Pay Rate added successfully!")
        except Exception as e:
            print(f"Error adding batt pay rate: {e}")

    def edit_batt_pay_rate(self, batt_pay_rate_name, new_batt_pay_rate_name, new_batt_pay_rate_amount,
                           new_batt_pay_rate_description):
        try:
            self.cursor.execute(
                """UPDATE batt_pay_rates SET batt_pay_rate_name = ?, batt_pay_rate_amount = ?, 
                batt_pay_rate_description = ? WHERE batt_pay_rate_name = ?;""",
                (new_batt_pay_rate_name, new_batt_pay_rate_amount, new_batt_pay_rate_description, batt_pay_rate_name))
            self.conn.commit()
            print("Batt Pay Rate edited successfully!")
        except Exception as e:
            print(f"Error editing batt pay rate: {e}")

    def delete_batt_pay_rate(self, batt_pay_rate_name):
        try:
            self.cursor.execute("""DELETE FROM batt_pay_rates WHERE batt_pay_rate_name = ?;""",
                                (batt_pay_rate_name,))
            self.conn.commit()
            print("Batt Pay Rate deleted successfully!")
        except Exception as e:
            print(f"Error deleting batt pay rate: {e}")

    def view_batt_pay_rate(self, batt_pay_rate_name):
        try:
            self.cursor.execute("""SELECT * FROM batt_pay_rates WHERE batt_pay_rate_name = ?;""",
                                (batt_pay_rate_name,))
            batt_pay_rate_data = self.cursor.fetchall()
            return batt_pay_rate_data
        except Exception as e:
            print(f"Error viewing batt pay rate: {e}")

    def view_all_batt_pay_rates(self):
        try:
            self.cursor.execute("""SELECT * FROM batt_pay_rates;""")
            batt_pay_rate_data = self.cursor.fetchall()
            return batt_pay_rate_data
        except Exception as e:
            print(f"Error viewing all batt pay rates: {e}")

    def view_batt_pay_rate_by_id(self, batt_pay_rate_id):
        try:
            self.cursor.execute("""SELECT * FROM batt_pay_rates WHERE batt_pay_rate_id = ?;""", (batt_pay_rate_id,))
            batt_pay_rate_data = self.cursor.fetchone()
            return batt_pay_rate_data
        except Exception as e:
            print(f"Error viewing batt pay rate by id: {e}")


class AtticPayRateTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS attic_pay_rates (
                                    attic_pay_rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    attic_pay_rate_name TEXT NOT NULL,
                                    attic_pay_rate_amount REAL NOT NULL,
                                    attic_pay_rate_description TEXT NOT NULL,
                                    UNIQUE(attic_pay_rate_id)
                                );""")
            self.conn.commit()
            print("Attic Pay Rate table created successfully!")
        except Exception as e:
            print(f"Error creating attic pay rate table: {e}")

    def add_attic_pay_rate(self, attic_pay_rate_name, attic_pay_rate_amount, attic_pay_rate_description):
        try:
            self.cursor.execute("""INSERT INTO attic_pay_rates (attic_pay_rate_name, attic_pay_rate_amount, 
            attic_pay_rate_description) VALUES (?, ?, ?);""",
                                (attic_pay_rate_name, attic_pay_rate_amount, attic_pay_rate_description))
            self.conn.commit()
            print("Attic Pay Rate added successfully!")
        except Exception as e:
            print(f"Error adding attic pay rate: {e}")

    def edit_attic_pay_rate(self, attic_pay_rate_name, new_attic_pay_rate_name, new_attic_pay_rate_amount,
                            new_attic_pay_rate_description):
        try:
            self.cursor.execute(
                """UPDATE attic_pay_rates SET attic_pay_rate_name = ?, attic_pay_rate_amount = ?, 
                 attic_pay_rate_description = ? WHERE attic_pay_rate_name = ?;""",
                (new_attic_pay_rate_name, new_attic_pay_rate_amount, new_attic_pay_rate_description,
                 attic_pay_rate_name))
            self.conn.commit()
            print("Attic Pay Rate edited successfully!")
        except Exception as e:
            print(f"Error editing attic pay rate: {e}")

    def delete_attic_pay_rate(self, attic_pay_rate_name):
        try:
            self.cursor.execute("""DELETE FROM attic_pay_rates WHERE attic_pay_rate_name = ?;""",
                                (attic_pay_rate_name,))
            self.conn.commit()
            print("Attic Pay Rate deleted successfully!")
        except Exception as e:
            print(f"Error deleting attic pay rate: {e}")

    def view_attic_pay_rate(self, attic_pay_rate_name):
        try:
            self.cursor.execute("""SELECT * FROM attic_pay_rates WHERE attic_pay_rate_name = ?;""",
                                (attic_pay_rate_name,))
            attic_pay_rate_data = self.cursor.fetchall()
            return attic_pay_rate_data
        except Exception as e:
            print(f"Error viewing attic pay rate: {e}")

    def view_all_attic_pay_rates(self):
        try:
            self.cursor.execute("""SELECT * FROM attic_pay_rates;""")
            attic_pay_rate_data = self.cursor.fetchall()
            return attic_pay_rate_data
        except Exception as e:
            print(f"Error viewing all attic pay rates: {e}")

    def view_attic_pay_rate_by_id(self, attic_pay_rate_id):
        try:
            self.cursor.execute("""SELECT * FROM attic_pay_rates WHERE attic_pay_rate_id = ?;""",
                                (attic_pay_rate_id,))
            attic_pay_rate_data = self.cursor.fetchone()
            return attic_pay_rate_data
        except Exception as e:
            print(f"Error viewing attic pay rate by id: {e}")


class FoamPayRateTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS foam_pay_rates (
                                    foam_pay_rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    foam_pay_rate_name TEXT NOT NULL,
                                    foam_pay_rate_amount REAL NOT NULL,
                                    foam_pay_rate_description TEXT NOT NULL,
                                    UNIQUE(foam_pay_rate_id)
                                );""")
            self.conn.commit()
            print("Foam Pay Rate table created successfully!")
        except Exception as e:
            print(f"Error creating foam pay rate table: {e}")

    def add_foam_pay_rate(self, foam_pay_rate_name, foam_pay_rate_amount, foam_pay_rate_description):
        try:
            self.cursor.execute("""INSERT INTO foam_pay_rates (foam_pay_rate_name, foam_pay_rate_amount, 
            foam_pay_rate_description) VALUES (?, ?, ?);""",
                                (foam_pay_rate_name, foam_pay_rate_amount, foam_pay_rate_description))
            self.conn.commit()
            print("Foam Pay Rate added successfully!")
        except Exception as e:
            print(f"Error adding foam pay rate: {e}")

    def edit_foam_pay_rate(self, foam_pay_rate_name, new_foam_pay_rate_name, new_foam_pay_rate_amount,
                           new_foam_pay_rate_description):
        try:
            self.cursor.execute(
                """UPDATE foam_pay_rates SET foam_pay_rate_name = ?, foam_pay_rate_amount = ?, 
                 foam_pay_rate_description = ? WHERE foam_pay_rate_name = ?;""",
                (new_foam_pay_rate_name, new_foam_pay_rate_amount, new_foam_pay_rate_description,
                 foam_pay_rate_name))
            self.conn.commit()
            print("Foam Pay Rate edited successfully!")
        except Exception as e:
            print(f"Error editing foam pay rate: {e}")

    def delete_foam_pay_rate(self, foam_pay_rate_name):
        try:
            self.cursor.execute("""DELETE FROM foam_pay_rates WHERE foam_pay_rate_name = ?;""",
                                (foam_pay_rate_name,))
            self.conn.commit()
            print("Foam Pay Rate deleted successfully!")
        except Exception as e:
            print(f"Error deleting foam pay rate: {e}")

    def view_foam_pay_rate(self, foam_pay_rate_name):
        try:
            self.cursor.execute("""SELECT * FROM foam_pay_rates WHERE foam_pay_rate_name = ?;""",
                                (foam_pay_rate_name,))
            foam_pay_rate_data = self.cursor.fetchall()
            return foam_pay_rate_data
        except Exception as e:
            print(f"Error viewing foam pay rate: {e}")

    def view_all_foam_pay_rates(self):
        try:
            self.cursor.execute("""SELECT * FROM foam_pay_rates;""")
            foam_pay_rate_data = self.cursor.fetchall()
            return foam_pay_rate_data
        except Exception as e:
            print(f"Error viewing all foam pay rates: {e}")

    def view_foam_pay_rate_by_id(self, foam_pay_rate_id):
        try:
            self.cursor.execute("""SELECT * FROM foam_pay_rates WHERE foam_pay_rate_id = ?;""",
                                (foam_pay_rate_id,))
            foam_pay_rate_data = self.cursor.fetchone()
            return foam_pay_rate_data
        except Exception as e:
            print(f"Error viewing all foam pay rates by id: {e}")


class VacationPayRateTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS vacation_pay_rates (
                                    vacation_pay_rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    vacation_pay_rate_name TEXT NOT NULL,
                                    vacation_pay_rate_amount REAL NOT NULL,
                                    vacation_pay_rate_description TEXT NOT NULL,
                                    UNIQUE(vacation_pay_rate_id)
                                );""")
            self.conn.commit()
            print("Vacation Pay Rate table created successfully!")
        except Exception as e:
            print(f"Error creating vacation pay rate table: {e}")

    def add_vacation_pay_rate(self, vacation_pay_rate_name, vacation_pay_rate_amount, vacation_pay_rate_description):
        try:
            self.cursor.execute("""INSERT INTO vacation_pay_rates (vacation_pay_rate_name, vacation_pay_rate_amount, 
            vacation_pay_rate_description) VALUES (?, ?, ?);""",
                                (vacation_pay_rate_name, vacation_pay_rate_amount, vacation_pay_rate_description))
            self.conn.commit()
            print("Vacation Pay Rate added successfully!")
        except Exception as e:
            print(f"Error adding vacation pay rate: {e}")

    def edit_vacation_pay_rate(self, vacation_pay_rate_name, new_vacation_pay_rate_name, new_vacation_pay_rate_amount,
                               new_vacation_pay_rate_description):
        try:
            self.cursor.execute(
                """UPDATE vacation_pay_rates SET vacation_pay_rate_name = ?, vacation_pay_rate_amount = ?, 
                  vacation_pay_rate_description = ? WHERE vacation_pay_rate_name = ?;""",
                (new_vacation_pay_rate_name, new_vacation_pay_rate_amount, new_vacation_pay_rate_description,
                 vacation_pay_rate_name))
            self.conn.commit()
            print("Vacation Pay Rate edited successfully!")
        except Exception as e:
            print(f"Error editing vacation pay rate: {e}")

    def delete_vacation_pay_rate(self, vacation_pay_rate_name):
        try:
            self.cursor.execute("""DELETE FROM vacation_pay_rates WHERE vacation_pay_rate_name = ?;""",
                                (vacation_pay_rate_name,))
            self.conn.commit()
            print("Vacation Pay Rate deleted successfully!")
        except Exception as e:
            print(f"Error deleting vacation pay rate: {e}")

    def view_vacation_pay_rate(self, vacation_pay_rate_name):
        try:
            self.cursor.execute("""SELECT * FROM vacation_pay_rates WHERE vacation_pay_rate_name = ?;""",
                                (vacation_pay_rate_name,))
            vacation_pay_rate_data = self.cursor.fetchall()
            return vacation_pay_rate_data
        except Exception as e:
            print(f"Error viewing vacation pay rate: {e}")

    def view_all_vacation_pay_rates(self):
        try:
            self.cursor.execute("""SELECT * FROM vacation_pay_rates;""")
            vacation_pay_rate_data = self.cursor.fetchall()
            return vacation_pay_rate_data
        except Exception as e:
            print(f"Error viewing all vacation pay rates: {e}")

    def view_vacation_pay_rate_by_id(self, vacation_pay_rate_id):
        try:
            self.cursor.execute("""SELECT * FROM vacation_pay_rates WHERE vacation_pay_rate_id = ?;""",
                                (vacation_pay_rate_id,))
            vacation_pay_rate_data = self.cursor.fetchone()
            return vacation_pay_rate_data
        except Exception as e:
            print(f"Error viewing vacation pay rate by id: {e}")


class BattPaySheetTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS batt_pay_sheet (
                                    batt_pay_sheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    batt_pay_sheet_job_name TEXT NOT NULL,
                                    batt_pay_sheet_batt_1 REAL NOT NULL,
                                    batt_pay_sheet_batt_2 REAL NOT NULL,
                                    batt_pay_sheet_soffit REAL NOT NULL,
                                    batt_pay_sheet_caulk_foam REAL NOT NULL,
                                    batt_pay_sheet_cellulose REAL NOT NULL,
                                    batt_pay_sheet_bibs_full REAL NOT NULL,
                                    batt_pay_sheet_bibs_hang REAL NOT NULL,
                                    batt_pay_sheet_bibs_staple REAL NOT NULL,
                                    batt_pay_sheet_bibs_blown REAL NOT NULL,
                                    batt_pay_sheet_bonus_amount REAL NOT NULL,
                                    batt_pay_sheet_other_amount REAL NOT NULL,

                                    UNIQUE(batt_pay_sheet_id)
                                );""")
            self.conn.commit()
            print("Batt Pay Sheet table created successfully!")
        except Exception as e:
            print(f"Error creating batt pay sheet table: {e}")

    def add_batt_record(self, job_name, batt_1, batt_2, soffit, caulk_foam, cellulose, bibs_full, bibs_hang,
                        bibs_staple, bibs_blown, bonus_amount, other_amount):
        try:
            self.cursor.execute("""INSERT INTO batt_pay_sheet (batt_pay_sheet_job_name, batt_pay_sheet_batt_1, 
            batt_pay_sheet_batt_2, batt_pay_sheet_soffit, batt_pay_sheet_caulk_foam, batt_pay_sheet_cellulose, 
            batt_pay_sheet_bibs_full, batt_pay_sheet_bibs_hang, batt_pay_sheet_bibs_staple, 
            batt_pay_sheet_bibs_blown, batt_pay_sheet_bonus_amount, batt_pay_sheet_other_amount) VALUES (?, ?, ?, ?, 
            ?, ?, ?, ?, ?, ?, ?, ?);""", (
                job_name, batt_1, batt_2, soffit, caulk_foam, cellulose, bibs_full, bibs_hang, bibs_staple, bibs_blown,
                bonus_amount, other_amount))
            self.conn.commit()
            print("Batt record added successfully!")
        except Exception as e:
            print(f"Error adding batt record: {e}")

    def update_batt_record(self, job_name, batt_1, batt_2, soffit, caulk_foam, cellulose, bibs_full, bibs_hang,
                           bibs_staple, bibs_blown, bonus_amount, other_amount):
        try:
            self.cursor.execute("""UPDATE batt_pay_sheet SET batt_pay_sheet_batt_1 = ?, batt_pay_sheet_batt_2 = ?, 
            batt_pay_sheet_soffit = ?, batt_pay_sheet_caulk_foam = ?, batt_pay_sheet_cellulose = ?, 
            batt_pay_sheet_bibs_full = ?, batt_pay_sheet_bibs_hang = ?, batt_pay_sheet_bibs_staple = ?, 
            batt_pay_sheet_bibs_blown = ?, batt_pay_sheet_bonus_amount = ?, batt_pay_sheet_other_amount = ? WHERE 
            batt_pay_sheet_job_name = ?;""", (
                batt_1, batt_2, soffit, caulk_foam, cellulose, bibs_full, bibs_hang, bibs_staple, bibs_blown,
                bonus_amount,
                other_amount, job_name))
            self.conn.commit()
            print("Batt record updated successfully!")
        except Exception as e:
            print(f"Error updating batt record: {e}")

    def delete_batt_record(self, job_name):
        try:
            self.cursor.execute("""DELETE FROM batt_pay_sheet WHERE batt_pay_sheet_job_name = ?;""", (job_name,))
            self.conn.commit()
            print("Batt record deleted successfully!")
        except Exception as e:
            print(f"Error deleting batt record: {e}")

    def get_batt_record(self, job_name):
        try:
            self.cursor.execute("""SELECT * FROM batt_pay_sheet WHERE batt_pay_sheet_job_name = ?;""", (job_name,))
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(f"Error getting batt record: {e}")

    def get_all_batt_records(self):
        try:
            self.cursor.execute("""SELECT * FROM batt_pay_sheet;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting all batt records: {e}")

    def get_batt_job_names(self):
        try:
            self.cursor.execute("""SELECT batt_pay_sheet_job_name FROM batt_pay_sheet;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting batt job names: {e}")


class AtticPaySheetTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS attic_pay_sheet (
                                    attic_pay_sheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    attic_pay_sheet_job_name TEXT NOT NULL,
                                    attic_pay_sheet_r19 REAL NOT NULL,
                                    attic_pay_sheet_r30 REAL NOT NULL,
                                    attic_pay_sheet_r38 REAL NOT NULL,
                                    attic_pay_sheet_r49 REAL NOT NULL,
                                    attic_pay_sheet_cellulose REAL NOT NULL,
                                    attic_pay_sheet_soffits REAL NOT NULL,
                                    attic_pay_sheet_bonus_amount REAL NOT NULL,
                                    attic_pay_sheet_other_amount REAL NOT NULL,
                                    attic_pay_sheet_air_seal REAL NOT NULL,

                                    UNIQUE(attic_pay_sheet_id)
                                );""")
            self.conn.commit()
            print("Attic Pay Sheet table created successfully!")
        except Exception as e:
            print(f"Error creating attic pay sheet table: {e}")

    def add_attic_record(self, job_name, r19, r30, r38, r49, cellulose, soffits, bonus_amount, other_amount, air_seal):
        try:
            self.cursor.execute("""INSERT INTO attic_pay_sheet (attic_pay_sheet_job_name, attic_pay_sheet_r19, 
            attic_pay_sheet_r30, attic_pay_sheet_r38, attic_pay_sheet_r49, attic_pay_sheet_cellulose, 
            attic_pay_sheet_soffits, attic_pay_sheet_bonus_amount, attic_pay_sheet_other_amount, attic_pay_sheet_air_seal) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (
                job_name, r19, r30, r38, r49, cellulose, soffits, bonus_amount, other_amount, air_seal))
            self.conn.commit()
            print("Attic record added successfully!")
        except Exception as e:
            print(f"Error adding attic record: {e}")

    def update_attic_record(self, job_name, r19, r30, r38, r49, cellulose, soffits, bonus_amount, other_amount,
                            air_seal):
        try:
            self.cursor.execute("""UPDATE attic_pay_sheet SET attic_pay_sheet_r19 = ?, attic_pay_sheet_r30 = ?, 
            attic_pay_sheet_r38 = ?, attic_pay_sheet_r49 = ?, attic_pay_sheet_cellulose = ?, attic_pay_sheet_soffits = ?, 
            attic_pay_sheet_bonus_amount = ?, attic_pay_sheet_other_amount = ?, attic_pay_sheet_air_seal = ? WHERE 
            attic_pay_sheet_job_name = ?;""", (
                r19, r30, r38, r49, cellulose, soffits, bonus_amount, other_amount, air_seal, job_name))
            self.conn.commit()
            print("Attic record updated successfully!")
        except Exception as e:
            print(f"Error updating attic record: {e}")

    def delete_attic_record(self, job_name):
        try:
            self.cursor.execute("""DELETE FROM attic_pay_sheet WHERE attic_pay_sheet_job_name = ?;""", (job_name,))
            self.conn.commit()
            print("Attic record deleted successfully!")
        except Exception as e:
            print(f"Error deleting attic record: {e}")

    def get_attic_record(self, job_name):
        try:
            self.cursor.execute("""SELECT * FROM attic_pay_sheet WHERE attic_pay_sheet_job_name = ?;""", (job_name,))
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(f"Error getting attic record: {e}")

    def get_all_attic_records(self):
        try:
            self.cursor.execute("""SELECT * FROM attic_pay_sheet;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting all attic records: {e}")

    def get_attic_job_names(self):
        try:
            self.cursor.execute("""SELECT attic_pay_sheet_job_name FROM attic_pay_sheet;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting attic job names: {e}")


class FoamPaySheetTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS foam_pay_sheet (
                                    foam_pay_sheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    foam_pay_sheet_job_name TEXT NOT NULL,
                                    foam_pay_sheet_closed34 REAL NOT NULL,
                                    foam_pay_sheet_closed1 REAL NOT NULL,
                                    foam_pay_sheet_closed2 REAL NOT NULL,
                                    foam_pay_sheet_closed3 REAL NOT NULL,
                                    foam_pay_sheet_open4 REAL NOT NULL,
                                    foam_pay_sheet_open6 REAL NOT NULL,
                                    foam_pay_sheet_open8 REAL NOT NULL,
                                    foam_pay_sheet_bonus_amount REAL NOT NULL,
                                    foam_pay_sheet_other_amount REAL NOT NULL,

                                    UNIQUE(foam_pay_sheet_id)
                                );""")
            self.conn.commit()
            print("Foam Pay Sheet table created successfully!")
        except Exception as e:
            print(f"Error creating foam pay sheet table: {e}")

    def add_foam_record(self, job_name, closed34, closed1, closed2, closed3, open4, open6, open8, bonus_amount,
                        other_amount):
        try:
            self.cursor.execute("""INSERT INTO foam_pay_sheet (foam_pay_sheet_job_name, foam_pay_sheet_closed34, 
            foam_pay_sheet_closed1, foam_pay_sheet_closed2, foam_pay_sheet_closed3, foam_pay_sheet_open4, 
            foam_pay_sheet_open6, foam_pay_sheet_open8, foam_pay_sheet_bonus_amount, foam_pay_sheet_other_amount) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (
                job_name, closed34, closed1, closed2, closed3, open4, open6, open8, bonus_amount, other_amount))
            self.conn.commit()
            print("Foam record added successfully!")
        except Exception as e:
            print(f"Error adding foam record: {e}")

    def update_foam_record(self, job_name, closed34, closed1, closed2, closed3, open4, open6, open8, bonus_amount,
                           other_amount):
        try:
            self.cursor.execute("""UPDATE foam_pay_sheet SET foam_pay_sheet_closed34 = ?, foam_pay_sheet_closed1 = ?, 
                foam_pay_sheet_closed2 = ?, foam_pay_sheet_closed3 = ?, foam_pay_sheet_open4 = ?, foam_pay_sheet_open6 = ?, 
                foam_pay_sheet_open8 = ?, foam_pay_sheet_bonus_amount = ?, foam_pay_sheet_other_amount = ? WHERE 
                foam_pay_sheet_job_name = ?;""", (
                closed34, closed1, closed2, closed3, open4, open6, open8, bonus_amount, other_amount, job_name))
            self.conn.commit()
            print("Foam record updated successfully!")
        except Exception as e:
            print(f"Error updating foam record: {e}")

    def delete_foam_record(self, job_name):
        try:
            self.cursor.execute("""DELETE FROM foam_pay_sheet WHERE foam_pay_sheet_job_name = ?;""", (job_name,))
            self.conn.commit()
            print("Foam record deleted successfully!")
        except Exception as e:
            print(f"Error deleting foam record: {e}")

    def get_foam_record(self, job_name):
        try:
            self.cursor.execute("""SELECT * FROM foam_pay_sheet WHERE foam_pay_sheet_job_name = ?;""", (job_name,))
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(f"Error getting foam record: {e}")

    def get_all_foam_records(self):
        try:
            self.cursor.execute("""SELECT * FROM foam_pay_sheet;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting all foam records: {e}")

    def get_foam_job_names(self):
        try:
            self.cursor.execute("""SELECT foam_pay_sheet_job_name FROM foam_pay_sheet;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting foam job names: {e}")


# todo create the shop pay sheet table
class ShopPaySheetTable(BaseTable):
    def create_table(self):
        pass


class VacationRequestTable(BaseTable):

    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS vacation_requests (
                                    vacation_request_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    employee_name TEXT NOT NULL,
                                    requested_days INTEGER NOT NULL,
                                    total_pay_amount INTEGER NOT NULL,
                                    UNIQUE(vacation_request_id)
                                );""")
            self.conn.commit()
            print("Vacation Request table created successfully!")
        except Exception as e:
            print(f"Error creating vacation request table: {e}")

    def add_vacation_request(self, employee_name, requested_days, total_pay_amount):
        try:
            self.cursor.execute("""INSERT INTO vacation_requests (employee_name, requested_days, total_pay_amount) 
            VALUES (?, ?, ?);""", (employee_name, requested_days, total_pay_amount))
            self.conn.commit()
            print("Vacation request added successfully!")
        except Exception as e:
            print(f"Error adding vacation request: {e}")

    def update_vacation_request(self, employee_name, requested_days, total_pay_amount):
        try:
            self.cursor.execute("""UPDATE vacation_requests SET requested_days = ?, total_pay_amount = ? WHERE 
            employee_name = ?;""", (requested_days, total_pay_amount, employee_name))
            self.conn.commit()
            print("Vacation request updated successfully!")
        except Exception as e:
            print(f"Error updating vacation request: {e}")

    def delete_vacation_request(self, vacation_request_id):
        try:
            self.cursor.execute("""DELETE FROM vacation_requests WHERE vacation_request_id = ?;""",
                                (vacation_request_id,))
            self.conn.commit()
            print("Vacation request deleted successfully!")
        except Exception as e:
            print(f"Error deleting vacation request: {e}")

    def get_vacation_request(self, employee_name):
        try:
            self.cursor.execute("""SELECT * FROM vacation_requests WHERE employee_name = ?;""", (employee_name,))
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(f"Error getting vacation request: {e}")

    def get_all_vacation_requests(self):
        try:
            self.cursor.execute("""SELECT * FROM vacation_requests;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting all vacation requests: {e}")

    def get_vacation_request_names(self):
        try:
            self.cursor.execute("""SELECT employee_name FROM vacation_requests;""")
            records = self.cursor.fetchall()
            return records
        except Exception as e:
            print(f"Error getting vacation request names: {e}")

    def get_vacation_request_by_id(self, vacation_request_id):
        try:
            self.cursor.execute("""SELECT * FROM vacation_requests WHERE vacation_request_id = ?;""",
                                (vacation_request_id,))
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(f"Error getting vacation request by id: {e}")
