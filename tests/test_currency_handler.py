import unittest
import sys
sys.path.append('..')
from python_package.currency_handler import get_adjusted_price
import pandas as pd


class TestMain(unittest.TestCase):

    def setUp(self):
        self.path = 'data/allowed_currencies.csv'
        self.currency_dataframe = pd.DataFrame(columns = ['currency',
                                                          'curr_to_dollar',
                                                          'symbol'])

        self.currency_dataframe = self.currency_dataframe.append({
                'currency':'euro',
                'curr_to_dollar':'0.9',
                'symbol':'€'}, ignore_index = True)
    
        self.currency_dataframe.set_index('currency', inplace = True)
        
    def test_cannot_be_negative(self):
        price, symbol = get_adjusted_price(-5, 'euro', self.currency_dataframe)
        self.assertGreater(price, 0)

    def test_is_string(self):
        price, symbol = get_adjusted_price(30, 'euro', self.currency_dataframe)
        self.assertIsInstance(symbol, str)

    def tearDown(self):
        self.path = None
        self.currency_dataframe = None