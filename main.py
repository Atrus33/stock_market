import argparse
from stock_package.scripts import stock
from stock_package.scripts import currency_handler as ch
from stock_package.scripts import dbmanager as db
from stock_package.scripts import csv_reader as reader

default_datafile = 'stock_package/data/allowed_currencies.csv'
companies_file = 'stock_package/data/allowed_companies.csv'
db_path = 'stock_package/data/database.db'

def parse_arguments(currencies, companies):
    parser = argparse.ArgumentParser(
            description = "Process ticker symbol and currency",
            prog = "stock_info",
            usage = "%(prog)s [options]",
            epilog = "Using financialmodelingprep API")
    parser.add_argument("-v", help = "Be more verbose", action="store_true")
    parser.add_argument("symbol", choices = companies,
                        help ='''The ticker (or stock) symbol
                        associated with stocks of a company''')
    parser.add_argument("-c", default = 'dollar', required = False, 
                        help = "The currency in which the value is expressed",
                        choices = currencies)
    
    # check username and password
    parser.add_argument('-u', help="add a username name (requires -p)",
                        required = True)
    parser.add_argument('-p', help="the username password",
                        required = True)
    
    parser.add_argument("--version",
                        action = "version",
                        version = "%(prog)s 1.0")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    db.open_and_create(db_path)
    currency_data = reader.read_currency_data(path = default_datafile)
    currencies_allowed = currency_data.index.tolist()
    companies_allowed = reader.read_available_companies(companies_file)
    args = parse_arguments(currencies_allowed, companies_allowed)
    curr_chosen = args.c
    if db.check_for_username(args.u, args.p):
        price, name = stock.get_price(args.symbol, args.v)
        price, c_symbol = ch.get_adjusted_price(price,
                                                curr_chosen,
                                                currency_data)
        print('{} (Symbol: {}) has a stock value of {} {}.'.format(name,
                                                               args.symbol,
                                                               price,
                                                               c_symbol))
    else:
        print("Username does not exist or password is incorrect!")
                                                            

