import argparse
import pandas as pd
import sqlite3
from python_package import stock
from python_package import currency_handler as ch
from python_package.scripts import dbmanager

default_datafile = 'data/allowed_currencies.csv'
default_database_path = 'data/database.db'

conn = None
cursor = None

def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect(default_database_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")  
    except sqlite3.OperationalError:
        dbmanager.create_users_table(conn, cursor)
   
        
    
def read_currency_data(csv_path):
    df_valid_currencies = pd.read_csv(csv_path, sep = ";")
    df_valid_currencies.columns = ['currency','curr_to_dollar','symbol']
    df_valid_currencies.set_index('currency', inplace = True)
    return df_valid_currencies


def parse_arguments(currency_name_list):
    parser = argparse.ArgumentParser(
             description = "Process ticker symbol and currency",
             prog = "stock_info",
             usage = "%(prog)s [options]",
             epilog = "Using financialmodelingprep API")
    parser.add_argument("-v", help = "Be more verbose", action = "store_true")
    parser.add_argument("symbol", 
                        help = "Ticker symbol related to company's stocks")
    parser.add_argument("-c", default = 'dollar', required = False, 
                        help = "The currency in which the value is expressed",
                        choices = currency_name_list)
    
    # check username and password
    parser.add_argument('-a', help = "add a usernamename (requires -p)",
                        required = True)
    parser.add_argument('-p', help="the username password",
                        required = True)
    
    parser.add_argument("--vers", action = "version", version = "%(prog)s 1.0")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    open_and_create()
    curr_data = read_currency_data(path = default_datafile)
    currencies_allowed = curr_data.index.tolist()
    curr_chosen = args.c
    args = parse_arguments(currencies_allowed)
    if dbmanager.check_for_username(conn, cursor, args.a, args.p):
        price, name = stock.get_price(args.symbol, args.v)
        price, c_symbol = ch.get_adjusted_price(price, curr_chosen, curr_data)
        print('{} (Symbol: {}) has a stock value of {} {}.'.format(name,
                                                                   args.symbol,
                                                                   price,
                                                                   c_symbol))
    else:
        print("Username does not exist or password is incorrect!")
                                                            

