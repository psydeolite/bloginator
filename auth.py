from pymongo import Connection

def authenticate(uname,pword):
    connection = Connection('localhost',5000)
    db = connections.database
    q = " SELECT * FROM users "
    result = c.execute(q)
    for r in result:
        if uname == r[0] and pword == r[1]:
            return True
    return False
