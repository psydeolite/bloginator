from pymongo import MongoClient
# import sqlite3

def make_table():
    connection = MongoClient()
    db = connection.database
    users = db.users
    post = db.post
    comment = db.comment

    userinfo = {"username":"bloginator","password":"softdev","name":"blogger"}
    postinfo = {"words":"hello world","aname":"hello","title":"text"}
    commentinfo = {"words":"Testing!","ptitle":"test","aname":"hello"}

    users.insert(userinfo)
    post.insert(postinfo)
    comment.insert(commentinfo)

# ---------------------------USERS TABLES---------------------------------
def add_user(uname, pword, rname):
    connection = MongoClient()
    db = connection.database
    users = db.users
    userinfo = {"username":uname,"password":pword,"name":rname}
    users.insert(userinfo)


def delete_user(uname, pword):
    connection = MongoClient()
    db = connection.database
    users = db.users
    users.remove({"username":uname,"password":pword})

def all_user():
    connection = MongoClient()
    db = connection.database
    users = db.users
    result = users.find()
    for r in result:
        print r
        print"\n"
#------------------------------COMMENT TABLES-----------------------------------
def add_comment(words,ptitle,aname):
    connection = MongoClient()
    db = connection.database
    comment = db.comment
    c = {"words":words,"ptitle":ptitle,"aname":aname}
    comment.insert(c)

def delete_comment(aname,ptitle):
    connection = MongoClient()
    db = connection.database
    comment = db.comment
    words = db.find({"aname":aname,"ptitle":ptitle})
    comment.remove({"words":words,"aname":aname,"ptitle":ptitle})

def all_comment():
    connection = MongoClient()
    db = connection.database
    comment = db.comment
    result = comment.find()
    for r in result:
        print r
        print"\n"
        
            
#-------------------------------POST TABLES--------------------------------------
def add_post(words,aname,title):
<<<<<<< HEAD
    con=MongoClient()
    db=connection.database
    post=db.post
    postinfo={'words':words,'aname':aname,'title':title}
    post.insert(postinfo)
   
def delete_post(title,aname):
    con=MongoClient()
   
def delete_post(title,aname):
        connection = MongoClient()
        db = connection.database
        post = db.post
        post.remove({"aname":aname,"ptitle":ptitle})
        
   
def all_post():
    '''con=MongoClient()
    db=con.database
    posts=db.post.find()
    return posts'''
    connection = MongoClient()
    db = connection.database
    post = db.post
    result = post.find()
    return result
    
#---------------------------------------------------------------------------------------------


'''add_post("Hello there","1","authorid")
add_post("Oh hi", "2", "authorid")
add_post("Testing testing", "3", "authorid")
all_post()
add_comment("HIYA GUYS", "123", "456")
all_comment()
add_user("greg","gerg", "Gregory Redozubov")
add_user("drothblatt", "cronut123", "David Rothblatt")
add_user("nspektor", "bootstrap", "Nellie Spektor")
all_user()'''


