import sqlite3
conn = sqlite3.connect("projectDatabase.db")
cursor = conn.cursor()
cursor.execute("UPDATE users SET lastLoggedIn = ? WHERE username = ?", ("2025-03-20", "user5"))
conn.commit()
conn.close()