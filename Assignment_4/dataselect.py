import sqlite3
conn=sqlite3.connect("dbnew.db")
data=conn.execute("Select * FROM users ")
for x in data:
    print(x)

data = conn.execute("Select * FROM users WHERE usid= 2 ")
for x in data:
        print(x)


data=conn.execute("Select * FROM new ")
for x in data:
    print(x)

data = conn.execute("Select * FROM new WHERE usid= 2 ")
for x in data:
        print(x)
