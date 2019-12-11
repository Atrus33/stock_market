import unittest
import sys
import os
sys.path.append('../scripts')
from csv_reader import read_currency_data


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = '/tmp/temporary_file'
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
        df = read_currency_data(path="/tmp/nonexistentfile-wewefwwe")
        self.assertFalse(df)

    def test_empty_datafie(self):
        df = read_currency_data(path=self.temporary_file)
        self.assertFalse(df)

    def test_file_is_not_csv(self):
        df = read_currency_data(path=self.temporary_file)
        self.assertFalse(df)

    def tearDown(self):
        os.remove(self.temporary_file)