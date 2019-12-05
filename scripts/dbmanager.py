import sqlite3

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('example-pwd.db')
    cursor = conn.cursor()
