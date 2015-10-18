import sqlite3

def make_table():
	con = sqlite3.connect("database.db")
	c = con.cursor()
	q = "create table if not exists users(uname text, pword text, userid integer, rname text)"
        c.execute(q)
        q = "create table if not exists post(words text, postid integer, authorid integer, date text)"
        c.execute(q)
        q = "create table if not exists comment(words text, postid integer, commid integer, authorid integer, date text)"
        c.execute(q)
        con.commit()

# ---------------------------USERS TABLES---------------------------------
def add_user(uname, pword, userid, rname):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    q = " SELECT * FROM users "
    result = c.execute(q)
    for r in result:
        print r
        print "\n"
    q = "INSERT INTO users VALUES('{}','{}','{}','{}')".format(uname, pword, userid, rname)
    c.execute(q)
    q = " SELECT * FROM users "
    result = c.execute(q)
    for r in result:
        print r
        print"\n"
    con.commit()


def delete_user(uname, pword):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    q = "SELECT user.userid FROM user WHERE uname = '{}' and pword = '{}'".format(uname,pword)
    result = c.execute(q)
    q = " DELETE * FROM user where uname = '{}' and pword = '{}'".format(uname,pword)
    c.execute(q)
    q = " DELETE * FROM post where authorid = '{}'".format(result)
    c.exeucte(q)
    con.commit()

def all_user():
        q = " SELECT * FROM users"
        result = c.execute(q)
        for r in result:
                print r
                print"\n"
#------------------------------COMMENT TABLES-----------------------------------
def add_comment(words, postid, commid, authorid, date):
	con = sqlite3.connect("database.db")
	c = con.cursor()
	q = "SELECT * FROM comment "
	result = c.execute(q)
	for r in result:
		print r
		print "\n"
	q = "INSERT INTO comment VALUES ('{}','{}','{}','{}','{}')".format(words, postid, commid, authorid, date)
	c.execute(q)
	q = " SELECT * FROM comment"
	result = c.execute(q)
	for r in result:
		print r
		print "\n"
	con.commit()

def delete_comment(authorid,commid):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    q = "SELECT * FROM comment WHERE authorid='{}' AND commid = '{}'".format(authorid,commid)
    c.execute(q)
    p = c.fetchone()
    if p is None:
        return False
    else:
        q = "UPDATE comment SET words = '{}' WHERE authorid = '{}' AND postid = '{}'".format("This comment is no longer viewable",authorid,commid)
        c.execute(q)
    con.commit()

def all_comment():
        q = " SELECT * FROM comment"
        result = c.execute(q)
        for r in result:
                print r
                print"\n"
            
#-------------------------------POST TABLES--------------------------------------
def add_post(words, postid, authorid,date):
        con = sqlite3.connect("database.db")
        c = con.cursor()
        q = " SELECT * FROM post "
        result = c.execute(q)
        for r in result:
                print r
                print"\n"
        q = "INSERT INTO post VALUES('{}','{}','{}','{}')".format(words,postid,authorid,date)
        c.execute(q)
        q = " SELECT * FROM post"
        result = c.execute(q)
        for r in result:
                print r
                print"\n"
        con.commit()

def delete_post(postid,authorid):
        con = sqlite3.connect("database.db")
        c = con.cursor()
        q = " SELECT * FROM post"
        result = c.execute(q)
        for r in result:
                print r
                print"\n"
        q = "SELECT * FROM post WHERE authorid='{}' AND postid = '{}'".format(authorid,postid)
        c.execute(q)
        p = c.fetchone()
        if p is None:
                return False
        else:
                q = "UPDATE post SET words = '{}' WHERE authorid = '{}' AND postid = '{}'".format("This post is no longer viewable",authorid,postid)
                c.execute(q)
                con.commit()
        q = " SELECT * FROM post"
        result = c.execute(q)
        for r in result:
                print r
                print"\n"

def all_post():
        q = " SELECT * FROM post"
        result = c.execute(q)
        for r in result:
                print r
                print"\n"
#---------------------------------------------------------------------------------------------

con = sqlite3.connect("database.db")
c = con.cursor()
c.execute("DELETE FROM post")
c.execute("DELETE FROM users")
c.execute("DELETE FROM comment")
con.commit()
make_table()
add_post("alsdfughlkasdbggfadgr","1","authorid","1/1/11")
delete_post(":)","authorid")
delete_post("1","dsagouhadfkg")
delete_post("1","authorid")
add_comment("HIYA GUYS", 123, 456, 789, "10/16/15")
add_user("greg","gerg",2271, "Gregory Redozubov")
print("--------------------------------")
all_user()
print("-----------------------------------")
all_post()
print("-----------------------------------")
all_comment()
