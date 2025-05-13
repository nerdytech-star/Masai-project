import csv
import bcrypt

# Path helper (use for reading/writing data)
DATA_DIR = 'data/'

# === Password Hashing ===

def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)

# === CSV Helpers ===

def read_csv(filename: str) -> list:
    with open(DATA_DIR + filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        return list(reader)

def write_csv(filename: str, data: list) -> None:
    with open(DATA_DIR + filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def append_csv(filename: str, row: list) -> None:
    with open(DATA_DIR + filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(row)
