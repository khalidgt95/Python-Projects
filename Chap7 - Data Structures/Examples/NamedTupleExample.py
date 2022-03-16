
from typing import NamedTuple

"""
This class behaves like a tuple, and values cannot be modified
"""

class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def average(self) -> float:

        """
        Normal methods can be added
        """
        return (self.high / self.low) / 2

    def setSymbol(self, sa: str) -> None:

        """
        This method does not work because the object behaves like a tuple
        """
        # self.symbol = sa
