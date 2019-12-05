import sqlite3
import random
import hashlib
def create_users_table(conn, cursor):
    # Create table
    cursor.execute('''CREATE TABLE users
                   (username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    salt SMALLINT NOT NULL,
                    PRIMARY KEY (username))''')

def save_new_username(username, password):
    salt = random,randint(1, 10000)
    password = str(salt) + password
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()
    

def check_for_username(conn, cursor, username, password):
    rows = cursor.execute("SELECT * FROM users WHERE username=?",
                          (username,))
    conn.commit()
    results = rows.fetchall()
    password = str(results[0][2]) + password
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if digest == results[0][1].lower():
        return True
    else:
        return False