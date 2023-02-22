from Database import Database as db
class Book(db):

    def all_books(self):
        try:
            db.my_cursor.execute("SELECT rowid, * FROM books")
            result = db.my_cursor.fetchall()
        except Exception as e:
            return e

        return result

    def insert(self, name, category, availability):
        try:
            db.my_cursor.execute("INSERT INTO books (name, category, availability) VALUES (?, ?, ?)", (name, category, availability))
        except Exception as e:
            return e

        return db.my_cursor.lastrowid

    def delete(self, id):
        try:
            db.my_cursor.execute(f"DELETE FROM books WHERE rowid = {id}")
        except Exception as e:
            return e

    def update(self, id, name):
        try:
            db.my_cursor.execute("UPDATE books SET name = ? WHERE rowid = ?", (name, id))
        except Exception as e:
            return e
