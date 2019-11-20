import argparse
import pandas as pd
from python_package import stock
from python_package import currency_handler


default_datafile = 'data/allowed_currencies.csv'

def read_currency_data(datafile = default_datafile):
    df = pd.read_csv(default_datafile, sep=";")
    df.columns = ['currency','curr/dollar','symbol']
    return df


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", 
                        help = "The symbol associated with a company")
    parser.add_argument("-c", default = 'dollar', required = True, 
                        help = "The currency related to the stock value",
                        choices = read_currency_data()['currency'].tolist())
    parser.add_argument("-v", help = "Be more verbose", action="store_true")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    currency = args.c
    price, name = stock.get_price(args.symbol, args.v)
    price, currency_symbol = currency_handler.get_adjusted_price(price, currency)
    print('Company "{}" (Symbol: {}) has a stock value of {} {}.'.format(name,
                                                               args.symbol,
                                                               price,
                                                               currency))
                                                            

