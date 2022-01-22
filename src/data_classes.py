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


if __name__ == "__main__":
    import doctest

    doctest.testmod()