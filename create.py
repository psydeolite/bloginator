import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

q = "create table User(User_ID integer, Name text) if does not exist"
c.execute(q)

