from utils import hash_password, check_password, read_csv, append_csv
from datetime import date

MEMBERS_FILE = 'members.csv'

# === Helper to find user by email ===
def find_user_by_email(email: str):
    members = read_csv(MEMBERS_FILE)
    for row in members:
        if row[3] == email:  # Email is 4th column
            return row
    return None

# === Register New User ===
def register(name: str, email: str, password: str, role: str = "Member") -> bool:
    if find_user_by_email(email):
        print("❌ Email already registered.")
        return False

    member_id = generate_member_id()
    hashed = hash_password(password)
    join_date = date.today().isoformat()

    # Store role in name temporarily like: "Ananya Singh|Librarian"
    full_name = f"{name}|{role}"
    append_csv(MEMBERS_FILE, [member_id, full_name, hashed.decode(), email, join_date])
    print("✅ Registration successful.")
    return True

# === Login ===
def login(email: str, password: str):
    user = find_user_by_email(email)
    if not user:
        print("❌ User not found.")
        return None

    if check_password(password, user[2].encode()):
        name, role = user[1].split("|")
        return {
            "id": user[0],
            "name": name,
            "email": user[3],
            "role": role
        }
    else:
        print("❌ Incorrect password.")
        return None

# === Generate Member ID ===
def generate_member_id():
    members = read_csv(MEMBERS_FILE)
    if len(members) == 0:
        return "1001"
    else:
        last_id = int(members[-1][0])
        return str(last_id + 1)
