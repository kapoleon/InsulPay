# batt_pay_sheet_table.py
from scripts.database.tables.base_table import BaseTable


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
                                                                    
                                    UNIQUE(batt_pay_sheet_job_name)
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
