import sqlite3

conn=sqlite3.connect("dbnew.db")
conn.execute(
    '''
    CREATE table new(usid INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(20),
    address varchar(20),
    mobile varchar(10)
    )
    '''
)
conn.close()