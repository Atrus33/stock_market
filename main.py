import argparse
from python_package import stock
from python_package import currency_handler

valid_currencies = ['dollar', 'euro', 'gbp']

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", 
                        help = "The symbol associated with a company")
    parser.add_argument("-c", default = 'dollar', required = True, 
                        help = "The currency related to the stock value",
                        choices = valid_currencies)
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