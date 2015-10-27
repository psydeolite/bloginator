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
    #q = " SELECT * FROM users "
    #result = c.execute(q)
    #for r in result:
        #print r
        #print "\n"
    #q = """INSERT INTO users VALUES('{}','{}','{}')""".format(uname, pword, rname)
    #c.execute(q)
    #q = " SELECT * FROM users "
    #result = c.execute(q)
    #for r in result:
        #print r
        #print"\n"
    #con.commit()


def delete_user(uname, pword):
    connection = MongoClient()
    db = connection.database
    users = db.users
    users.remove({"username":uname,"password":pword})
    #con = sqlite3.connect("database.db")
    #c = con.cursor()
    #q = " SELECT * FROM users "
    #result = c.execute(q)
    #for r in result:
        #print r
        #print "\n"
    #q = """" DELETE FROM users where username = '{}' and password = '{}'""".format(uname,pword)
    #c.execute(q)
    #q = """ DELETE FROM post where aname = '{}'""".format(uname)
    #c.execute(q)
    #q = " SELECT * FROM users "
    #result = c.execute(q)
    #for r in result:
        #print r
        #print "\n"
    #con.commit()

def all_user():
    connection = MongoClient()
    db = connection.database
    users = db.users
    result = users.find()
        #q = " SELECT * FROM users"
        #result = c.execute(q)
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
    #con = sqlite3.connect("database.db")
	#c = con.cursor()
	#q = "SELECT * FROM comment "
	#result = c.execute(q)
	#for r in result:
		#print r
		#print "\n"
	#q = """INSERT INTO comment VALUES ('{}','{}','{}')""".format(words, ptitle, aname)
	#c.execute(q)
	#q = " SELECT * FROM comment"
	#result = c.execute(q)
	#for r in result:
		#print r
		#print "\n"
	#con.commit()

def delete_comment(aname,ptitle):
    connection = MongoClient()
    db = connection.database
    comment = db.comment
    words = db.find({"aname":aname,"ptitle":ptitle})
    comment.remove({"words":words,"aname":aname,"ptitle":ptitle})
    #con = sqlite3.connect("database.db")
    #c = con.cursor()
    #q = " SELECT * FROM comment"
    #result = c.execute(q)
    #for r in result:
        #print r
        #print "\n"
    #q = """DELETE FROM comment WHERE aname = '{}' and ptitle = '{}'""".format(aname,ptitle)
    #c.execute(q)
    #q = " SELECT * FROM comment"
    #result = c.execute(q)
    #for r in result:
        #print r
        #print "\n"
    #con.commit()

def all_comment():
    connection = MongoClient()
    db = connection.database
    comment = db.comment
    result = comment.find()
    #q = " SELECT * FROM comment"
    #result = c.execute(q)
    for r in result:
        print r
        print"\n"
        
            
#-------------------------------POST TABLES--------------------------------------
def add_post(words,aname,title):
        connection = MongoClient()
        db = connection.database
        post = db.post
        post.insert({"words":words,"title":title,"aname":aname})
        
        #con = sqlite3.connect("database.db")
        #c = con.cursor()
        #q = " SELECT * FROM post "
        #result = c.execute(q)
        #for r in result:
                #print r
                #print"\n"
        #q = """INSERT INTO post VALUES('{}','{}','{}')""".format(words,aname,title)
        #c.execute(q)
        #q = " SELECT * FROM post"
        #result = c.execute(q)
        #for r in result:
                #print r
                #print"\n"
        #con.commit()

def delete_post(title,aname):
        connection = MongoClient()
        db = connection.database
        post = db.post
        post.remove({"aname":aname,"ptitle":ptitle})
        
        #con = sqlite3.connect("database.db")
        #c = con.cursor()
        #q = " SELECT * FROM post"
        #result = c.execute(q)
        #for r in result:
                #print r
                #print"\n"
        #q = """SELECT * FROM post WHERE aname='{}' AND title = '{}'""".format(aname,title)
        #c.execute(q)
        #p = c.fetchone()
        #if p is None:
                #return False
        #else:
                #q = """UPDATE post SET words = '{}' WHERE aname = '{}' AND title = '{}'""".format("This post is no longer viewable",aname,title)
                #c.execute(q)
                #con.commit()
        #q = " SELECT * FROM post"
        #result = c.execute(q)
        #for r in result:
                #print r
                #print"\n"

def all_post():
        connection = MongoClient()
        db = connection.database
        post = db.post
        result = post.find()
        #q = " SELECT * FROM post"
        #result = c.execute(q)
        for r in result:
                print r
                print"\n"
#---------------------------------------------------------------------------------------------

con = sqlite3.connect("database.db")
c = con.cursor()
make_table()
#c.execute("DELETE FROM post")
#c.execute("DELETE FROM users")
#c.execute("DELETE FROM comment")
con.commit()
#add_post("Hello there","1","authorid","1/1/11")
#add_post("Oh hi", "2", "authorid", "1/2/12")
#add_post("Testing testing", "3", "authorid", "1/3/13")
#add_comment("HIYA GUYS", 123, 456, 789)
#add_user("greg","gerg",2271, "Gregory Redozubov")
#add_user("drothblatt", "cronut123", 2589, "David Rothblatt")
#add_user("nspektor", "bootstrap", 2222, "Nellie Spektor") 


#print("Official Results: \n--------------------------------")

#add_comment("alsdfughlkasdbggfadgr",1,258,786)
#delete_comment(786,324)
#delete_comment(1,258)
#delete_comment(786,258)
#add_comment("HIYA GUYS", 123, 456, 789)
#add_user("greg","gerg",2271, "Gregory Redozubov")
#delete_user("greg","erg")
#delete_user("erg","gerg")
#delete_user("greg","gerg")
#add_post("HI",1,2,"BYE")
#delete_post(1,3)
#delete_post(2,2)
#delete_post(1,2)
#print("--------------------------------")

#all_user()
#print("-----------------------------------")
#all_post()
#print("-----------------------------------")
#all_comment()
