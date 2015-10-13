import sqlite3

def create(): 
	conn = sqlite3.connect("database.db")

	c = conn.cursor()

	q = "create table users(username text, password text, u_id integer, name text) if does not exist"
	c.execute(q)

	q = "insert into users values("drothblatt", "cronut123", 2589, "David Rothblatt");"
	c.execute(q)

	q = "create table posts(body text, title text, username text, post_id integer) if does not exist"
	c.execute(q)

	q = "insert into posts values ("Hi there", "First Post", "drothblatt", 1);" 
	c.execute(q)

	q = "create table comments(post_id integer, u_id integer, comment text) if does not exist"
	c.execute(q)

	conn.commit()


