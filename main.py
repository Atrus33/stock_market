import argparse
from python_package import stock


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", 
                        help = "The symbol associated with a company") 
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    price, name = stock.get_price(args.symbol)
    print('Company "{}" (Symbol: {}) has a stock value of {}$.'.format(name,
                                                               args.symbol,
                                                               price))