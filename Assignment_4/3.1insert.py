import sqlite3

conn=sqlite3.connect("dbnew.db")
conn.execute('''
INSERT INTO new(name,address,mobile) VALUES("Bhumi","Jagatpura","8746756757"),
("Chetan","Jaipur","9862981874"),("Mahak","Jaipur","7689765789")

''')
conn.commit()
print("Data has been inserted")
conn.close()