# batt_pay_sheet_table.py
from scripts.base_table import BaseTable


class BattPaySheetTable(BaseTable):
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS batt_pay_sheet (
                                    batt_pay_sheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    batt_pay_sheet_job_name TEXT NOT NULL,
                                    batt_pay_sheet_date TEXT NOT NULL,
                                    batt_pay_sheet_batt_1 TEXT NOT NULL,
                                    batt_pay_sheet_batt_2 REAL NOT NULL,
                                    batt_pay_sheet_soffit REAL NOT NULL,
                                    batt_pay_sheet_caulk_foam TEXT NOT NULL,
                                    batt_pay_sheet_cellulose REAL NOT NULL,
                                    batt_pay_sheet_bibs_full TEXT NOT NULL,
                                    batt_pay_sheet_bibs_hang INTEGER NOT NULL,
                                    batt_pay_sheet_bibs_staple INTEGER NOT NULL,
                                    batt_pay_sheet_bibs_blown INTEGER NOT NULL,
                                    batt_pay_sheet_bonus_amount REAL NOT NULL,
                                    batt_pay_sheet_other_amount REAL NOT NULL,
                                                                    
                                    UNIQUE(batt_pay_sheet_job_name)
                                );""")
            self.conn.commit()
            print("Batt Pay Sheet table created successfully!")
        except Exception as e:
            print(f"Error creating batt pay sheet table: {e}")
