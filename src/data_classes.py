from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    current: float
    high: float
    low: float


# Example 1
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


class StockOrdinary:
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


# Example 2
"""
>>> s_ord = StockOrdinary("AAPL", 123.52, 137.98, 53.15)
>>> s_ord
<src.dataclasses.StockOrdinary object at 0x7f526a0bc1f0>
"""