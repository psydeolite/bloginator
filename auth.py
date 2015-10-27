from pymongo import MongoClient

def authenticate(uname,pword):
    connection = MongoClient()
    db = connections['database']
    result = db.users.find({'username':uname});
    for r in result:
        if uname == r.username and pword == r.password:
            return True
    return False
