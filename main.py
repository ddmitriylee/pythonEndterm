from Book import Book
from Database import Database

db = Database()
book = Book()

while True:
    print("""Hello, Librarian! You have following functions to execute:
    1. Create book
    2. Update book
    3. Delete book
    4. Show all books
    """.strip())
    temp_choice = int(input())
    match temp_choice:
        case 1:
            temp_name = input("Input the name of book: ")
            temp_category = input("Input the category of book: ")
            temp_availability = bool(input("Input the availability of book (True or False): "))
            book.insert(temp_name, temp_category, temp_availability)
            db.my_db.commit()

        case 2:
            for i in book.all_books():
                print(f"{i[0]}) Name = {i[1]}; Category = {i[2]}; Availability = {i[3]}")
            temp_id = int(input("Input the id of book to change: "))
            temp_newname = input("Input the new name of book: ")
            book.update(temp_id, temp_newname)
            db.my_db.commit()
        case 3:
            for i in book.all_books():
                print(f"{i[0]}) Name = {i[1]}; Category = {i[2]}; Availability = {i[3]}")
            temp_id = int(input("Input the id of book to delete: "))
            book.delete(temp_id)
            db.my_db.commit()
        case 4:
            for i in book.all_books():
                print(f"{i[0]}) Name = {i[1]}; Category = {i[2]}; Availability = {i[3]}")
