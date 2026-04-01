import os
import sqlite3

os.makedirs("db", exist_ok=True)

conn = sqlite3.connect("db/real_estate.db")

with open("create_db.sql", "r") as f:
    conn.executescript(f.read())

conn.close()
