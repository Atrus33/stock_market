import requests
import json


# url of the API
fmp_URL = 'https://financialmodelingprep.com/api/v3/company/profile/%s'


def get_price(company, verbose=False):

    """Return price and name of company the label is referring to.

    Given the label of a company in the stock market, the function makes a
    request to the financialmodelingprep service trying to get the price and
    the name of the company.

    :param company: The company label
    :type company: string
    :param verbose: Verbosity activated
    :type verbose: Boolean
    :return: price and name of the company
    :rtype: string, string
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
