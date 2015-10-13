import sqlite3

def create(): 
	conn = sqlite3.connect("database.db")

	c = conn.cursor()

	q = "create table if not exists users(username text, password text, u_id integer, name text)"
	c.execute(q)

	q = """insert into users values("drothblatt", "cronut123", 2589, "David Rothblatt");"""
	c.execute(q)

	q = "create table if not exists posts(body text, title text, username text, post_id integer)"
	c.execute(q)

	q = """insert into posts values ("Hi there", "First Post", "drothblatt", 1);""" 
	c.execute(q)

	q = "create table if not exists comments(post_id integer, u_id integer, comment text)"
	c.execute(q)

	conn.commit()


