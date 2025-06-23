import sqlite3
conn=sqlite3.connect("dbnew.db")
conn.execute("UPDATE users set usnm='BHUMI' WHERE usid='2'")
conn.commit()
data=conn.execute("Select * FROM users ")
for x in data:
    print(x)


conn.execute("UPDATE new set name='BHUMI' WHERE usid='2'")
conn.commit()
data=conn.execute("Select * FROM new")
for x in data:
    print(x)
conn.close()
