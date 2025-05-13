from utils import append_csv, read_csv
from utils import read_csv

def search_books():
    print("\n🔍 Search Catalogue")
    keyword = input("Enter title or author: ").strip().lower()

    books = read_csv('books.csv')
    found = False
    for book in books:
        if keyword in book[1].lower() or keyword in book[2].lower():
            print(f"📘 {book[1]} by {book[2]} | ISBN: {book[0]} | Available: {book[4]}")
            found = True
    if not found:
        print("❌ No books found with that keyword.")


BOOKS_FILE = 'books.csv'

def add_book():
    print("\n📘 Add New Book")
    isbn = input("ISBN: ").strip()
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    copies = input("Number of Copies: ").strip()

    if not isbn or not title or not author or not copies.isdigit():
        print("❌ Invalid input. All fields are required.")
        return

    book = [isbn, title, author, copies, copies]  # CopiesTotal, CopiesAvailable
    append_csv(BOOKS_FILE, book)
    print("✅ Book added successfully.")
