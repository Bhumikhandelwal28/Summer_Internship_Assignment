import sqlite3

conn=sqlite3.connect("dbnew.db")
id=input("iD to delete from users:")
conn.execute("DELETE FROM users WHERE usid="+id)
conn.commit()
data=conn.execute("Select * FROM users ")
for x in data:
    print(x)

conn=sqlite3.connect("dbnew.db")
id=input("iD to delete from new:")
conn.execute("DELETE FROM new WHERE usid="+id)
conn.commit()
data=conn.execute("Select * FROM new ")
for x in data:
    print(x)

conn.close()