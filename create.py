import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

q = "create table users(username text, password text, u_id integer, name text) if does not exist"
c.execute(q)

q = "create table posts(body text, title text, username text, post_id integer, post_time date) if does not exist"
c.execute(q)

q = "create table comments(post_id integer, u_id integer, comment text, comment_time date) if does not exist"
c.execute(q)

conn.commit()
