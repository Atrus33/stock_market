import requests
import json

 # url of the API
fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'

def get_price(company, verbose = False):
    """Return price and name of company the label is referring to.
    
    Given the label of a company in the stock market, the function makes a 
    request to the financialmodelingprep service trying to get the price and 
    the name of the company.
    
    Parameters:
    company (str): The company label
    
    Returns:
    price (float): The price of the company stock
    name (str): The name of the company
    """ 
    if verbose:
        print("Trying to fetch the data from the API")    
    r = requests.get(fmp_URL % company)
    data = json.loads(r.text)
    if verbose:
        print("Successfully fetched data")
    price = data['profile']['price']
    name = data['profile']['companyName']
    return price, name

