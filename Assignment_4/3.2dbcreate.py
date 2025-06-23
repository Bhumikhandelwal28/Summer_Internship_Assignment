import sqlite3
conn=sqlite3.connect("dbnew.db")
conn.execute('''
Create table users(
usid INTEGER PRIMARY KEY AUTOINCREMENT,
usnm VARCHAR(100),
pass VARCHAR(50)
)
''')

conn.close()