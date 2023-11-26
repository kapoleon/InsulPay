# attic_pay_rate_table.py

from scripts.database.tables.base_table import BaseTable


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
