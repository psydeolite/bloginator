import sqlite3

def testing():
     conn = sqlite.connect("database.db")
     c = conn.cursor()

     q = " SELECT * FROM users "
     result = c.execute(q)
     for r in result:
         print r
     
