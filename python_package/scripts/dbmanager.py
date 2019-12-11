import sqlite3
import random
import hashlib
import argparse
import os
db_path = os.path.abspath(os.path.join(os.getcwd(), '../../data/database.db'))

conn = None
cursor = None

def open_and_create():
    """Connect to the database
    
    :return: no value
    :rtype: none
    """
    global conn
    global cursor
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")  
    except sqlite3.OperationalError:
        create_users_table(conn, cursor)
   
def create_users_table():
    """Create the users' table if it does not exist
    
    :return: no value
    :rtype: none
    """
       
    global conn
    global cursor
    # Create table
    cursor.execute('''CREATE TABLE users
                   (username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    salt SMALLINT NOT NULL,
                    PRIMARY KEY (username))''')


def save_new_username(username, password):
    """Save a new user in the database
    
    :param username: the username
    :type username: string
    :param password: the password
    :type password: string
    :return: no value
    :rtype: none
    """
    
    global conn
    global cursor
    salt = random.randint(1, 10000)
    password = str(salt) + password
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()
    
    
def check_for_username(username, password):
    """Check the credentials of a user
        
    The user provided his credentials for authentication. If the user exists
    in the db, the SHA256(salt+password) is computed. If the digest of the 
    password provided by the user is the same as the digest computed as above,
    the user is authenticated and the action is allowed.
    
    :param username: the username provided by the user for the authentication
    :param password: the password provided by the user for the authentication
    :return: True if the user can be authenticated, False otherwise.
    :rtype: Boolean
    """
    
    global conn
    global cursor
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
    
    parser.add_argument("-add", required = False, default = False,
                        help = "Add username '-u' with password '-p' (Bool)",
                        action = "store_true") 
    parser.add_argument("-rm", required = False, default = False,
                        help= "Remove username '-u' with password '-p' (Bool)",
                        action = "store_true")
    
    parser.add_argument('-u', help="add a username name (requires -p)",
                        required = True, default = None)
    parser.add_argument('-p', help = "the username password",
                        required = False, default = None)
    
    parser.add_argument("--version",
                        action = "version",
                        version = "%(prog)s 1.0")
    args = parser.parse_args()
    return args

    
if __name__ == "__main__":
    open_and_create()
    args = parse_arguments()
    if args.add and args.rm:
        print("You cannot add and remove a user at the same time!")
    elif args.add:
        if args.u is None or args.p is None:
            print("Please provide a proper username and password combination!")
        else:
            save_new_username(args.u, args.p)
            print("Successfully inserted user {}".format(args.u))
            
    #print(args)