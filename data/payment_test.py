import unittest
from payment import *


class TestPayment(unittest.TestCase):
    def setUp(self):
        pass

    def test_payment(self):
        self.assertNotEqual(Payment.is_type_of('11111'), True)

    def test_paymentCoffee(self):
        a = PaymentCoffee(1, 2, 3, 4)
        print a.criteria
        self.assertTrue(PaymentCoffee.is_type_of('IZ *Nkora                London       GBR'))


if __name__ == '__main__':
    unittest.main()

