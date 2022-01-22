import datetime
from typing import NamedTuple


def middle(stock, date):
    """
    >>> middle(("AAPL",123.52, 53.15, 137.98),datetime.date(2020,12,4))
    """
    symbol, current, high, low = stock
    return (high + low) / 2, date


def high(stock):
    """
    >>> s = ('AAPL', 123.52, 53.15, 137.98)
    >>> high(s)
    """
    symbol, current, high, low = stock
    return high


class Stock(NamedTuple):
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
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        return (self.high + self.low) / 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
