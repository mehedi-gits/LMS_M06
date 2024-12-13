import json

def view_lend_history():
    try:
        with open("lend_books.json", "r") as fp:
            lend_books = json.load(fp)

        if isinstance(lend_books, dict):
            lend_books = [lend_books]

        if isinstance(lend_books, list) and all(isinstance(record, dict) for record in lend_books):
            print("\nLend Book History:")
            for record in lend_books:
                print(f"Borrower Name: {record['borrower_name']} | Phone: {record['borrower_phone']} | Book Title: {record['title']} | Lend Date: {record['lend_date']} | Due Date: {record['due_date']}")
        else:
            print("\nInvalid lending record format.")
    except FileNotFoundError:
        print("\nNo lending records found. The file 'lend_books.json' does not exist.")