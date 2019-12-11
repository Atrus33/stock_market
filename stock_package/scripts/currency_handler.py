import os

def get_adjusted_price(price, currency, currency_data):
    """Return adjusted price and name of company the label is referring to.
    
    If a user wants the price value in a currency different from the dollar
    this function computes the stock value in such currency.
    
    :param price: The price of the stock of the chosen company
    :type price: float
    :param currency: The currency name chosen by the user 
    :type currency: string
    :param currency_data: The dataframe containing information on currencies
    :type currency_data: Pandas.Dataframe object 
    :return: price and name of the company
    :rtype: string, string
    """
    price = price * float(currency_data.at[currency,'curr_to_dollar'])
    price = abs(price)
    symbol = currency_data.at[currency, 'symbol']
    symbol = str(symbol)
    return price, symbol