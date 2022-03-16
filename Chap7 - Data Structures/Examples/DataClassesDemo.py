
from dataclasses import dataclass


"""
Dataclass can be used to hold a set of attributes
Different arguments in the decorator can be used 
Similar to struct in C

"""
@dataclass(frozen=True) # frozen means that attributes cannot be changed once initialized (like NamedTuple)
class Stock:

    """
    
    >>> s = Stock("AAPL", 100.0, 150.5, 90.5)
    >>> s.current
    100.0

    >>> s.current = 10
    dataclasses.FrozenInstanceError: cannot assign to field 'current'
    
    """
    symbol: str
    current: float
    high: float = 0.0   # Assign default if no value is provided
    low: float = 0.0