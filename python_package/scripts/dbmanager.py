import sqlite3
import random

def create_users_table():
    # Create table
    global conn
    global cursor
    cursor.execute('''CREATE TABLE users
                   (username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    salt SMALLINT NOT NULL,
                    PRIMARY KEY (username))''')

def save_new_username(username, password):
    global conn
    global cursor
    salt = random,randint(1, 10000)
    password = str(salt) + password
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()
    

def check_for_username(username, password):
    global conn
    global cursor
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    rows = cursor.execute("SELECT * FROM users WHERE username=? and password=?",
                          (username, digest))
    conn.commit()
    results = rows.fetchall()