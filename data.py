import sqlite3
import csv

def get(amount):
	con = sqlite3.connect("data.db")
	c = con.cursor()
	return c.execute("SELECT * LIMIT %(amount)s")