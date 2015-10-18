import sqlite3
import create

def testing():
     conn = sqlite3.connect("database.db")
     c = conn.cursor()

     q = " SELECT * FROM users "
     result = c.execute(q)
     for r in result:
        print r

     q = " SELECT * FROM post "
     result = c.execute(q)
     for r in result:
	print r


testing()
