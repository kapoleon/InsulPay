# foam_pay_rate_table.py

from scripts.database.tables.base_table import BaseTable


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
