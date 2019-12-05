import argparse
import pandas as pd
import sqlite3
from python_package import stock
from python_package import currency_handler as ch
from python_package.scripts import dbmanager

default_datafile = 'data/allowed_currencies.csv'
default_database = 'data/database.db'

conn = None
cursor = None

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect(default_database)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")  
    except sqlite3.OperationalError:
        dbmanager.create_users_table(conn, cursor)
   
        
    
def read_currency_data(path):
    df = pd.read_csv(path, sep=";")
    df.columns = ['currency','curr_to_dollar','symbol']
    df.set_index('currency', inplace = True)
    return df


def parse_arguments(c):
    parser = argparse.ArgumentParser(description = "Process ticker symbol and currency",
                                     prog = "stock_info",
                                     usage = "%(prog)s [options]",
                                     epilog = "Using financialmodelingprep API")
    parser.add_argument("-v", help = "Be more verbose", action="store_true")
    parser.add_argument("symbol", 
                        help = "The ticker (or stock) symbol associated with stocks of a company")
    parser.add_argument("-c", default = 'dollar', required = False, 
                        help = "The currency in which the value is expressed",
                        choices = c)
    
    # check username and password
    parser.add_argument('-a', help="add a usernamename (requires -p)",
                        required = True)
    parser.add_argument('-p', help="the username password",
                        required = True)
    
    parser.add_argument("--version", action = "version", version = "%(prog)s 1.0")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    open_and_create()
    currency_data = read_currency_data(path = default_datafile)
    currencies_allowed = currency_data.index.tolist()
    curr_chosen = args.c
    args = parse_arguments(currencies_allowed)
    if dbmanager.check_for_username(conn, cursor, args.a, args.p):
        price, name = stock.get_price(args.symbol, args.v)
        price, c_symbol = ch.get_adjusted_price(price, curr_chosen, currency_data)
        print('Company "{}" (Symbol: {}) has a stock value of {} {}.'.format(name,
                                                               args.symbol,
                                                               price,
                                                               c_symbol))
    else:
        print("Username does not exist or password is incorrect!")
                                                            

