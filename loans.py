from utils import read_csv, write_csv, append_csv
from datetime import date, timedelta

BOOKS_FILE = 'books.csv'
LOANS_FILE = 'loans.csv'
MEMBERS_FILE = 'members.csv'

def issue_book():
    print("\n📕 Issue Book to Member")

    isbn = input("ISBN to issue: ").strip()
    member_id = input("Member ID: ").strip()

    # 🔍 Validate member ID
    members = read_csv(MEMBERS_FILE)
    valid_member = any(row[0] == member_id for row in members)
    if not valid_member:
        print("❌ Member ID not found.")
        return

    # Load books
    books = read_csv(BOOKS_FILE)
    book_found = False
    for i, book in enumerate(books):
        if book[0] == isbn:
            book_found = True
            available = int(book[4])
            if available < 1:
                print("❌ Book is not available.")
                return
            books[i][4] = str(available - 1)
            break

    if not book_found:
        print("❌ ISBN not found.")
        return

    # Generate Loan ID
    loans = read_csv(LOANS_FILE)
    loan_id = str(int(loans[-1][0]) + 1) if loans else "1"

    issue_date = date.today()
    due_date = issue_date + timedelta(days=14)

    new_loan = [
        loan_id,
        member_id,
        isbn,
        issue_date.isoformat(),
        due_date.isoformat(),
        ""
    ]

    write_csv(BOOKS_FILE, books)
    append_csv(LOANS_FILE, new_loan)

    print(f"✅ Book issued. Due on {due_date.strftime('%d-%b-%Y')}.")

def return_book():
    print("\n📗 Return Book")

    loan_id = input("Loan ID: ").strip()

    loans = read_csv(LOANS_FILE)
    updated = False

    for i, loan in enumerate(loans):
        if loan[0] == loan_id:
            if loan[5]:  # ReturnDate already filled
                print("⚠️ This book is already returned.")
                return
            loans[i][5] = date.today().isoformat()  # Fill ReturnDate
            isbn = loan[2]
            updated = True
            break

    if not updated:
        print("❌ Loan ID not found.")
        return

    # Update CopiesAvailable in books.csv
    books = read_csv(BOOKS_FILE)
    for i, book in enumerate(books):
        if book[0] == isbn:
            books[i][4] = str(int(book[4]) + 1)
            break

    write_csv(LOANS_FILE, loans)
    write_csv(BOOKS_FILE, books)

    print("✅ Book returned and inventory updated.")

def view_overdue_loans():
    print("\n📙 Overdue Loans Report")

    today = date.today()
    loans = read_csv(LOANS_FILE)
    overdue_found = False

    for loan in loans:
        loan_id, member_id, isbn, issue, due, returned = loan
        if returned.strip() == "" and due < today.isoformat():
            overdue_found = True
            print(f"🔴 Loan ID: {loan_id} | Member: {member_id} | Book: {isbn} | Due: {due}")
    
    if not overdue_found:
        print("✅ No overdue books.")

def view_my_loans(member_id):
    print("\n📄 Your Loans")

    loans = read_csv('loans.csv')
    found = False
    for loan in loans:
        if loan[1] == member_id:
            print(f"📚 ISBN: {loan[2]} | Issued: {loan[3]} | Due: {loan[4]} | Returned: {loan[5] or 'No'}")
            found = True
    if not found:
        print("📭 You have no loans.")



