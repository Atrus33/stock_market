import pandas as pd
def read_currency_data(path):
    """Read the file containing data about currencies, store it in a DataFrame
    
    :param path: The path to the .csv file containing currencies info
    :type path: string
    :return: the Dataframe containing infos about the currencies
    :rtype: Pandas.Dataframe
    """
    if path.split('.')[-1] != 'csv':
        return False
    df = pd.DataFrame()
    try:
        df = pd.read_csv(path, sep=";")
        df.columns = ['currency','curr_to_dollar','symbol']
        df.set_index('currency', inplace = True)
    except :
        return False
    return df

def read_available_companies(path):
    """Read the file containing data about companies, store it in a DataFrame
    
    :param path: The path to the .csv file containing companies info
    :type path: string
    :return: the Dataframe containing infos about the companies
    :rtype: Pandas.Dataframe
    """
    if path.split('.')[-1] != 'csv':
        return False
    df = pd.DataFrame
    try:
        df = pd.read_csv(path, sep=";")
    except:
        return False
    return set(list(df['ticker']))