import sqlite3

con = sqlite3.connect('accounts.db')
cur = con.cursor()

cur.execute('create table account (password text, username text, backup text)')