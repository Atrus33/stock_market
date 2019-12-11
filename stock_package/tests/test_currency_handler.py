import unittest
import sys
sys.path.append('../scripts')
from currency_handler import get_adjusted_price
import pandas as pd


class TestMain(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame(columns=['currency','curr_to_dollar','symbol'])

        self.df = self.df.append({
                'currency':'euro',
                'curr_to_dollar':'0.9',
                'symbol':'€'}, ignore_index = True)
    
        self.df.set_index('currency', inplace = True)
        
    def test_cannot_be_negative(self):
        price, symbol = get_adjusted_price(-5, 'euro', self.df)
        self.assertGreater(price, 0)

    def test_is_string(self):
        price, symbol = get_adjusted_price(30, 'euro', self.df)
        self.assertIsInstance(symbol, str)

    def tearDown(self):
        pass