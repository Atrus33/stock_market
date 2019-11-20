import os

def get_adjusted_price(price, currency):
    default_datafile = '../data/allowed_currencies.csv'
    
    if currency == "euro":
        return price * 0.9, '€'
    else:
        return price * 0.77, '£'
