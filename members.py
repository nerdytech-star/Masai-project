from auth import register, find_user_by_email

def register_member():
    print("\n👤 Register New Member")
    name = input("Full Name: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    success = register(name, email, password, role="Member")
    if success:
        # Retrieve and show the new Member ID
        new_user = find_user_by_email(email)
        if new_user:
            print(f"🆔 Member registered with ID: {new_user[0]}")
        print("✅ Member registered successfully.")

