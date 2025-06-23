import sqlite3
conn=sqlite3.connect("dbnew.db")
conn.execute('''
INSERT INTO users(usnm,pass) VALUES("ABY","abc"),("BHUMI","bh237"),("ANUSHRI","anubhu2")
''')
conn.commit()
conn.close()
