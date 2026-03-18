import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS collections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    bonus REAL,
    penalty REAL
)
""")

conn.commit()


def insert_data(amount, bonus, penalty):
    cursor.execute(
        "INSERT INTO collections (amount, bonus, penalty) VALUES (?, ?, ?)",
        (amount, bonus, penalty)
    )
    conn.commit()


def fetch_data():
    cursor.execute("SELECT * FROM collections")
    return cursor.fetchall()