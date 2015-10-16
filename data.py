import sqlite3

def make_table():
	con = sqlite3.connect("database.db")
	c = con.cursor()
	q = "create table if not exists users(uname integer, pword text, userid text)"
        c.execute(q)
        q = "create table if not exists post(words text, postid integer, authorid integer, date text)"
        c.execute(q)
        q = "create table if not exists comment(words text, postid integer, commid integer, authorid integer, date text)"
        c.execute(q)
        con.commit()

# ---------------------------USER TABLES---------------------------------
def add_user(uname, pword, userid):
    con = sqlite3.connect("database.db")
    c = con.cursor()
    q = " SELECT * FROM user "
    result = c.execute(q)
    for r in result:
        print r
        print "\n"
        q = "INSERT INTO POST VALUES('{}','{}','{}')".format(uname, pword, userid)
        c.execute(q)
        q = " SELECT * FROM user "
        result = c.execute(q)
        for r in result:
            print r
            print"\n"
        con.commit()


# def delete_user(userid):


#------------------------------COMMENT TABLES-----------------------------------
def add_comment(words, postid, commid, authorid, date):
	con = sqlite3.connect("database.db")
	c = con.cursor()
	q = "SELECT * FROM comment "
	result = c.execute(q)
	for r in result:
		print r
		print "\n"
	q = "INSER INTO comment VALUES ('{}','{}','{}','{}','{}')".format(words, postid, commid, authorid, date)
	c.execute(q)
	q = " SELECT * FROM comment"
	result = c.execute(q)
	for r in result:
		print r
		print "\n"
	con.commit()

# def delete_comment(commid):

            
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

con = sqlite3.connect("database.db")
c = con.cursor()
c.execute("delete from post")
con.commit()
make_table()
add_post("alsdfughlkasdbggfadgr","1","authorid","1/1/11")
delete_post(":)","authorid")
delete_post("1","dsagouhadfkg")
delete_post("1","authorid")
