import sqlite3

conn = sqlite3.connect("transforaiq.db")

cursor = conn.cursor()

with open("database/schema.sql", "r") as f:
    schema = f.read()

cursor.executescript(schema)

conn.commit()
conn.close()

print("Database initialized successfully.")