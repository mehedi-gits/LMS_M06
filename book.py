import add_books
import lend_books
import view_all_books
import restore_books_file
from datetime import datetime
import update_book_file, delete_book_file
import view_lend_history

all_books = []


while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Book Update")
    print("4. Book Remove/Delete")
    print("5. Lend Book")
    print("6. View Lend History")
    print("7. Return Book")

    all_books = restore_books_file.restore_all_books(all_books)
    
    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book_file.update_books(all_books)
    elif menu == "4":
        delete_book_file.delete_books(all_books)
    elif menu == "5":
        lend_books.lend_book(all_books)
    elif menu == "6":
        view_lend_history.view_lend_history()
    elif menu == "7":
        lend_books.return_book(all_books)
    else:
        print("Choose a valid number")