import unittest
from statement import *


class TestPayment(unittest.TestCase):
    def setUp(self):
        pass

    def test_load(self):
        file_statemant = Statement('transactions.csv')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
