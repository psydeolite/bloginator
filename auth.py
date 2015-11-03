from pymongo import MongoClient

def authenticate(uname,pword):
    connection = MongoClient()
    db = connection['database']
    result = db.users.find({"username":uname});
    print result
    #if uname == result.username and pword == result.password:
    #        return True
    for r in result:
        if uname==r['username']:
            if pword==r['password']:
                return True
    return False
