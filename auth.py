import sqlite3

def authenticate(uname,pword):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    q = " SELECT * FROM users "
    result = c.execute(q)
    for r in result:
        if uname == r[0] and pword == r[1]:
            return True
    return False
