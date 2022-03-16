
from typing import Any, NamedTuple


class Data(NamedTuple):
    current: float
    high: float
    low: float
    change: float

stocks = {
    "A": Data(1, 1, 1, 1),
    "B": Data(1, 2, 3, 4),
}


for k, v in stocks.items():
    print(f"{k} last value is {v.low}")

"""
The key of the dictionary can be anything as long as it is immutable
This includes strings, tuples and even objects
"""

random_keys = {}
random_keys["key"] = "value"
random_keys[5] = "integer value"
random_keys[(12, "tuple")] = "tuples"

class DummyObject:

    def __init__(self, val: Any) -> None:
        self.val = val

obj = DummyObject(42)
random_keys[obj] = "object"

print(f"{random_keys}")