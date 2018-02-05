class Payment (object):

    _criteria = ()

    def __init__(self, date, item, cost):
        self._data = date
        self._item = item
        self._cost = cost

    @classmethod
    def is_type_of(cls, criteria):
        return criteria in cls._criteria

    @property
    def data(self):
        return self._data

    @property
    def item(self):
        return self._item

    @property
    def cost(self):
        return self._cost

    @property
    def criteria(self):
        return self._criteria


class PaymentCoffee(Payment):
    _criteria = (
        'IZ *Nkora                London       GBR',
        'CLIMPSON & SONS        LONDON  E8    GBR'
    )


class PaymentTravel(Payment):
    _criteria = (
        'TfL Travel Charge        TFL.gov.uk/CPGBR',
        'TFL.GOV.UK/CP          TFL TRAVEL CH GBR'
    )


class PaymentAmazon(Payment):
    _criteria = (
        'AMAZON.CO.UK             LUXEMBOURG, LLUX',
    )
