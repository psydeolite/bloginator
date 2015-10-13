import sqlite3

def make_table():
	con = sqlite3.connect("database.db")
	c = con.cursor()
	q = "create table if not exists users(uname text, pword text, userid text)"
        c.execute(q)
        q = "create table if not exists blog(blogid text, authorid text, bname text, date text)"
        c.execute(q)
        q = "create table if not exists post(words text, postid text, authorid text, date text)"
        c.execute(q)
        q = "create table if not exists comment(words text, postid text, commid text, authorid text, date text)"
        c.execute(q)
        con.commit()

def add_post(words, postid, authorid):
        con = sqlite3.connect("database.db")
        c = con.cursor()
        q = "INSERT INTO post VALUES('{}','{}','{}')".format(words,postid,authorid)
        c.execute(q)
        con.commit()

def delete_post(postid,authorid):
        con = sqlite3.connect("database.db")
        c = con.cursor()
        q = "SELECT userid FROM post WHERE username ='{}' AND postid = '{}'".format(authorid,postid)
        c.execute(q)
        p = c.fetchone()
        if p is None:
                return False
        else:
                q = "UPDATE post SET words = '{}' WHERE authorid = '{}' AND postid = '{}'".format("This post is no longer viewable",authorid,postid)
                c.execute(q)
                con.commit()
