from pymongo import MongoClient

def authenticate(uname,pword):
    connection = MongoClient()
    db = connections['database']
    result = db.users.find({"username":uname});
    if uname == result.username and pword == result.password:
            return True
    return False
