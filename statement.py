import csv
from data.payment import *


class Statement(object):
    payments = []

    def __init__(self, filename):
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            for r in reader:
                if PaymentCoffee.is_type_of(r[1]):
                    self.payments.append(PaymentCoffee(r[0], r[1], 0))
                elif PaymentTravel.is_type_of(r[1]):
                    self.payments.append(PaymentTravel(r[0], r[1], 0))
                elif PaymentAmazon.is_type_of(r[1]):
                    self.payments.append(PaymentAmazon(r[0], r[1], 0))
                else:
                    self.payments.append(Payment(r[0], r[1], 0))
            for p in self.payments:
                print p.item


