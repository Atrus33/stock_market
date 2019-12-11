import sqlite3
import random
import hashlib
import argparse

def create_users_table(conn, cursor):
    """Create the users' table if it does not exist
    
    :param conn: the connection handler
    :type conn: Connection Object
    :param cursor: the cursor
    :type cursor: Cursor Handler
    :return: no value
    :rtype: none
    """
    # Create table
    cursor.execute('''CREATE TABLE users
                   (username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    salt SMALLINT NOT NULL,
                    PRIMARY KEY (username))''')


def save_new_username(conn, cursor, username, password):
    """Save a new user in the database
    
    :param conn: the connection handler
    :type conn: Connection Object
    :param cursor: the cursor
    :type cursor: Cursor Handler
    :param username: the username
    :type username: string
    :param password: the password
    :type password: string
    :return: no value
    :rtype: none
    """
    salt = random.randint(1, 10000)
    password = str(salt) + password
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()
    
    
def check_for_username(conn, cursor, username, password):
    """Check the credentials of a user
        
    The user provided his credentials for authentication. If the user exists
    in the db, the SHA256(salt+password) is computed. If the digest of the 
    password provided by the user is the same as the digest computed as above,
    the user is authenticated and the action is allowed.
    
    :param conn: the connection handler
    :type conn: Connection Object
    :param cursor: the cursor
    :type cursor: Cursor Handler
    :param username: the username provided by the user for the authentication
    :param password: the password provided by the user for the authentication
    :return: True if the user can be authenticated, False otherwise.
    :rtype: Boolean
    """
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
    
def parse_arguments():
    parser = argparse.ArgumentParser(
            description = "Manage possible database actions (add/remove user)",
            prog = "stock_info",
            usage = "%(prog)s [options]",
            epilog = "Using SQLite3")
    
    parser.add_argument("-add", required = False,
                        help = "Add username '-u' with password '-p' (Bool)",
                        action = "store_true") 
    parser.add_argument("-rm", required = False, 
                        help= "Remove username '-u' with password '-p' (Bool)",
                        action = "store_true")
    
    parser.add_argument('-u', help="add a username name (requires -p)",
                        required = True)
    parser.add_argument('-p', help = "the username password",
                        required = False)
    
    parser.add_argument("--version",
                        action = "version",
                        version = "%(prog)s 1.0")
    args = parser.parse_args()
    return args

    
if __name__ == "__main__":
    args = parse_arguments()
    print(args)