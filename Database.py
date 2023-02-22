import sqlite3
class Database:
    my_db = sqlite3.connect("database.db")
    my_cursor = my_db.cursor()
    def __init__(self):
        self.my_cursor.execute("CREATE TABLE IF NOT EXISTS books(name TEXT, category TEXT, availability BOOLEAN)")

    def commit(self):
        try:
            self.my_db.commit()
        except Exception as e:
            return e

    def __del__(self):
        self.my_db.commit()