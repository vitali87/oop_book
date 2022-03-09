from dataclasses import dataclass


@dataclass
class Stock:
    """
    >>> s = Stock("AAPL", 123.52, 137.98, 53.15)
    >>> s
    Stock(symbol='AAPL', current=123.52, high=137.98, low=53.15)
    >>> s.current
    123.52
    >>> s.current = 122.15
    >>> s.current
    122.15
    >>> s.unexpected_attribute = "allowed"
    >>> s.unexpected_attribute
    'allowed'
    """
    symbol: str
    current: float
    high: float
    low: float


class StockOrdinary:
    """
    >>> s_ord = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
    >>> s_ord
    <src.data_classes.StockOrdinary object at 0x7fe1ae55b580>
    >>> s_ord_2 = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
    >>> s_ord == s_ord_2
    False
    >>> stock2 = Stock("AAPL", current=122.15, high=137.98, low=53.15)
    >>> s = Stock("AAPL", 123.52, 137.98, 53.15)
    >>> s
    Stock(symbol='AAPL', current=123.52, high=137.98, low=53.15)
    >>> s.current
    123.52
    >>> s.current = 122.15
    >>> s == stock2
    True
    """

    def __init__(
            self,
            name: str,
            current: float,
            high: float,
            low: float
    ) -> None:
        self.name = name
        self.current = current
        self.high = high
        self.low = low


@dataclass
class StockDefault:
    """
    >>> StockDefault("GOOG")
    StockDefault(name='GOOG', current=0.0, high=0.0, low=0.0)
    >>> StockDefault("GOOG", 1826.77, 1847.20, 1013.54)
    StockDefault(name='GOOG', current=1826.77, high=1847.2, low=1013.54)
    """
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


@dataclass(order=True)
class StockOrdered:
    """
    >>> stock_ordered1 = StockOrdered("GOOG", 1826.77, 1847.20, 1013.54)
    >>> stock_ordered2 = StockOrdered("GOOG")
    >>> stock_ordered3 = StockOrdered("GOOG", 1728.28, high=1733.18, low=1666.33)
    >>> stock_ordered1 < stock_ordered2
    False
    >>> stock_ordered1 > stock_ordered2
    True
    >>> from pprint import pprint
    >>> pprint(sorted([stock_ordered1,stock_ordered2,stock_ordered3]))
    [StockOrdered(name='GOOG', current=0.0, high=0.0, low=0.0),
     StockOrdered(name='GOOG', current=1728.28, high=1733.18, low=1666.33),
     StockOrdered(name='GOOG', current=1826.77, high=1847.2, low=1013.54)]
    """
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
