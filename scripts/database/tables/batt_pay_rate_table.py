# batt_pay_rate_table.py

from scripts.database.tables.base_table import BaseTable


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
