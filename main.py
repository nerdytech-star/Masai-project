from auth import register, login
from books import add_book
from loans import issue_book
from members import register_member
from loans import return_book
from datetime import date, timedelta
import csv
import os
import json
from loans import view_overdue_loans
from books import search_books
from loans import view_my_loans


# Constants




# Simple in-memory session to store logged-in user
session = {}

def welcome():
    print("\n📚 Welcome to the Library Management System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def main_menu():
    while True:
        welcome()
        choice = input("> ").strip()

        if choice == '1':
            name = input("Full Name: ").strip()
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            role = input("Role (Librarian/Member): ").strip().capitalize()
            if role not in ['Librarian', 'Member']:
                print("❌ Invalid role.")
                continue
            register(name, email, password, role)

        elif choice == '2':
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            user = login(email, password)
            if user:
                session.update(user)
                print(f"\n✅ Logged in as {user['name']} ({user['role']})")
                if user['role'] == "Librarian":
                    librarian_menu()
                else:
                    member_menu()

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Try again.")

# === Placeholder Menus ===

# def librarian_menu():
#     print("\n=== Librarian Dashboard ===")
#     print("1. Add Book\n2. Register Member\n3. Issue Book\n4. Return Book\n5. Overdue List\n6. Logout")
#     input("Press Enter to logout and return to main menu...")
#     session.clear()


def librarian_menu():
    while True:
        print("\n=== Librarian Dashboard ===")
        print("1. Add Book\n2. Register Member\n3. Issue Book\n4. Return Book\n5. Overdue List\n6. Logout")
        choice = input("> ").strip()

        if choice == '1':
            add_book()
        elif choice == '6':
            print("👋 Logged out.")
            session.clear()
            break
        elif choice == '3':
            issue_book()
        elif choice == '2':
            register_member()
        elif choice == '4':
            return_book()
        elif choice == '5':
            view_overdue_loans()

        else:
            print("⚠️ Feature not implemented yet.")


# def member_menu():
#     print("\n=== Member Dashboard ===")
#     print("1. Search Catalogue\n2. Borrow Book\n3. My Loans\n4. Logout")
#     input("Press Enter to logout and return to main menu...")
#     session.clear()

def member_menu():
    while True:
        print("\n=== Member Dashboard ===")
        print("1. Search Catalogue\n2. My Loans\n3. Logout")
        choice = input("> ").strip()

        if choice == '1':
            search_books()
        elif choice == '2':
            view_my_loans(session['id'])
        elif choice == '3':
            print("👋 Logged out.")
            session.clear()
            break
        else:
            print("❌ Invalid choice.")


# Run the app
if __name__ == "__main__":
    main_menu()
