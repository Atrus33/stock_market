
def get_adjusted_price(price_value, currency_name, currency_data):
    price_value = price_value * currency_data.at[currency_name,'curr_to_dollar'] 
    symbol = currency_data.at[currency_name, 'symbol']
    return price_value, symbol