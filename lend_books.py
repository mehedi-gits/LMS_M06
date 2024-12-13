import json
from datetime import datetime, timedelta
from save_all_books import save_all_books

def lend_book(all_books):

    try:
        with open("lend_books.json", "r") as fp:
            lend_books = json.load(fp)
        if isinstance(lend_books, dict):
            lend_books = [lend_books]
    except FileNotFoundError:
        lend_books = []

    book_title = input("Enter the title of the book to lend: ").lower()

    for book in all_books:
        if book["title"].lower() == book_title:
            if book["quantity"] > 0:
                borrower_name = input("Enter Borrower's Name: ")
                borrower_phone = input("Enter Borrower's Phone Number: ")
                due_date = datetime.now() + timedelta(days=14)

                lend_info = {
                    "title": book["title"],
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "lend_date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "due_date": due_date.strftime("%d-%m-%Y %H:%M:%S")
                }

                lend_books.append(lend_info)

                with open("lend_books.json", "w") as fp:
                    json.dump(lend_books, fp, indent=4)

                book["quantity"] -= 1
                save_all_books(all_books)

                print("Book lent successfully.")
                return

            else:
                print("There are not enough books available to lend.")
                return

    print("Book not found.")

def return_book(all_books):
    book_title = input("Enter the title of the book to return: ").lower()
    borrower_name = input("Enter Borrower's Name: ")

    try:
        with open("lend_books.json", "r") as fp:
            lend_books = json.load(fp)

        book_found = False
        updated_lend_books = []

        for lend_info in lend_books:
            if lend_info["title"].lower() == book_title and lend_info["borrower_name"].lower() == borrower_name.lower():
                book_found = True
                for book in all_books:
                    if book["title"].lower() == book_title:
                        book["quantity"] += 1
                        save_all_books(all_books)
                        break
            else:
                updated_lend_books.append(lend_info)

        if not book_found:
            print("Lend record not found.")
            return

        with open("lend_books.json", "w") as fp:
            json.dump(updated_lend_books, fp, indent=4)

        print("Book returned successfully.")
    except FileNotFoundError:
        print("No lend records found.")
