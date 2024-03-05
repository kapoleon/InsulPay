# BaseTable.py

# This file contains the base class for all tables in the database.

import sqlite3


class BaseTable:
    def __init__(self, db_name="InsulPay.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Database connected successfully!")
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            raise MyDatabaseConnectionError("Error connecting to the database") from e
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise MyGeneralError("An unexpected error occurred") from e

    def disconnect(self):
        try:
            if self.conn:
                self.conn.close()
                print("Database disconnected successfully!")
        except Exception as e:
            print(f"Error disconnecting from the database: {e}")


# Add custom exception classes here if needed
class MyDatabaseConnectionError(Exception):
    pass


class MyGeneralError(Exception):
    pass
