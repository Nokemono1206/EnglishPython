import sqlite3

filepath = "task1.sqlite"
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS items")
cur.execute("""CREATE TABLE items(
    content TEXT,
    original_name TEXT,
    name TEXT UNIQUE)""")
conn.commit()