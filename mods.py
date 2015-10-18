import sqlite3

def make_table():
	con = sqlite3.connect("database.db")
	c = con.cursor()
	q = "create table if not exists users(username text, password text, u_id integer, name text)"
        c.execute(q)
        q = "create table if not exists post(words text, postid integer, authorid integer, title text)"
        c.execute(q)
        q = "create table if not exists comment(words text, postid integer, commid integer, authorid integer)"
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
    q = " SELECT * FROM users "
    result = c.execute(q)
    for r in result:
        print r
        print "\n"
    q = "SELECT users.u_id FROM users WHERE username = '{}' and password = '{}'".format(uname,pword)
    result = c.execute(q)
    q = " DELETE FROM users where username = '{}' and password = '{}'".format(uname,pword)
    c.execute(q)
    q = " DELETE FROM post where authorid = '{}'".format(result)
    c.execute(q)
    q = " SELECT * FROM users "
    result = c.execute(q)
    for r in result:
        print r
        print "\n"
    con.commit()

def all_user():
        q = " SELECT * FROM users"
        result = c.execute(q)
        for r in result:
                print r
                print"\n"
#------------------------------COMMENT TABLES-----------------------------------
def add_comment(words, postid, commid, authorid):
	con = sqlite3.connect("database.db")
	c = con.cursor()
	q = "SELECT * FROM comment "
	result = c.execute(q)
	for r in result:
		print r
		print "\n"
	q = "INSERT INTO comment VALUES ('{}','{}','{}','{}')".format(words, postid, commid, authorid)
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
    q = " SELECT * FROM comment"
    result = c.execute(q)
    for r in result:
        print r
        print "\n"
    q = "DELETE FROM comment WHERE authorid = '{}' and commid = '{}'".format(authorid,commid)
    c.execute(q)
    q = " SELECT * FROM comment"
    result = c.execute(q)
    for r in result:
        print r
        print "\n"
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
