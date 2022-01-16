import datetime
from typing import NamedTuple


def middle(stock,date):
    symbol, current, high, low = stock
    return (high + low)/2, date


# Example 1
""" 
>>> middle(("AAPL",123.52, 53.15, 137.98),datetime.date(2020,12,4)) 
"""


def high(stock):
    symbol, current, high, low = stock
    return high


# Example 2
"""
>>> s = ('AAPL', 123.52, 53.15, 137.98)
>>> high(s)
"""


class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        return (self.high + self.low)/2


# Example 3
"""
>>> Stock("AAPL", 123.52, 53.15, 137.98)
>>> s2 = Stock("AAPL", 123.52, high=53.15, low=137.98)
>>> t = ("Relayer",["Gates of Delirium", "Sound Chaser"])
>>> t[1]
['Gates of Delirium', 'Sound Chaser']
>>> t[1].append("To Be Over")
>>> t[1]
['Gates of Delirium', 'Sound Chaser', 'To Be Over']
>>> s = Stock("AAPL", 123.52, 53.15, 137.98)
>>> s.middle
"""
