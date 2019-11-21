import argparse
import pandas as pd
from python_package import stock
from python_package import currency_handler as ch


default_datafile = 'data/allowed_currencies.csv'

def read_currency_data(path):
    df = pd.read_csv(path, sep=";")
    df.columns = ['currency','curr_to_dollar','symbol']
    df.set_index('currency', inplace = True)
    return df


def parse_arguments(c):
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", 
                        help = "The ticker (or stock) symbol associated with stocks of a company")
    parser.add_argument("-c", default = 'dollar', required = True, 
                        help = "The currency in which the value is expressed",
                        choices = c)
    parser.add_argument("-v", help = "Be more verbose", action="store_true")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    currency_data = read_currency_data(path = default_datafile)
    currencies_allowed = currency_data.index.tolist()
    args = parse_arguments(currencies_allowed)
    curr_chosen = args.c
    price, name = stock.get_price(args.symbol, args.v)
    price, c_symbol = ch.get_adjusted_price(price, curr_chosen, currency_data)
    print('Company "{}" (Symbol: {}) has a stock value of {} {}.'.format(name,
                                                               args.symbol,
                                                               price,
                                                               c_symbol))
                                                            

