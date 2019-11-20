import os

def get_adjusted_price(price, currency, currency_data):
    price = price * currency_data.at[currency,'curr_to_dollar'] 
    symbol = currency_data.at[currency, 'symbol']
    return price, symbol