
"""
This example shows how we can use sort objects in lists
See page 280 for the problem statement
"""

from dataclasses import dataclass
import datetime
from functools import total_ordering
from typing import Any, Optional, cast


@dataclass(frozen=True) # This 
class MultiItem:
    
    data_source: str
    timestamp: Optional[float]
    creation_date: Optional[str]
    name: str
    owner_etc: str

    """
    To make any object sortable, we need to implement __lt__() method
   
    In the current example, we use values from two columns since they have missing values
    """
    def __lt__(self, other: Any) -> bool:
        if self.data_source == "Local":
            self_datetime = datetime.datetime.fromtimestamp(
                cast(float, self.timestamp)    
            )
        else:
            self_datetime = datetime.datetime.fromisoformat(
                cast(str, self.creation_date)
            )

        if other.data_source == "Local":
            other_datetime = datetime.datetime.fromtimestamp(
                cast(float, other.timestamp)
            )

        else:
            other_datetime = datetime.datetime.fromisoformat(
                cast(str, other.creation_date)
            )

        return self_datetime < other_datetime

@total_ordering     # Since we implemented lt and eq, this decorator can implement all the rest operators
@dataclass(frozen=True)
class Simple:

    """


    >>> obj_list = [Simple(10), Simple(5), Simple(100), Simple(1)]
    >>> obj_list.sort()
    >>> obj_list
    [Simple(value=1), Simple(value=5), Simple(value=10), Simple(value=100)]    

    """
    value: int

    def __lt__(self, other: "Simple"):
        return self.value < other.value

    def __eq__(self, other: "Simple") -> bool:
        return self.value == other.value


@dataclass(frozen=True)
class ObjectsSortByDifferentValues:
    value_a: int
    value_b: int

    """
    In this example, we can pass the function to the sort argument
    Whatever attribute we return, the sorting will be based on that
    Here, we have two functions for sorting on two values
    """
def by_value_a(item: "ObjectsSortByDifferentValues") -> int:
    return item.value_a

def by_value_b(item: "ObjectsSortByDifferentValues") -> int:
    return item.value_b

"""
Usage
>>> vals = [ObjectsSortByDifferentValues(2,7), ObjectsSortByDifferentValues(4,2), 
ObjectsSortByDifferentValues(3, 10), ObjectsSortByDifferentValues(1, 1)]

>>> vals
[ObjectsSortByDifferentValues(value_a=2, value_b=7), ObjectsSortByDifferentValues(value_a=4, value_b=2), 
ObjectsSortByDifferentValues(value_a=3, value_b=10), ObjectsSortByDifferentValues(value_a=1, value_b=1)]

>>> vals.sort(key=by_value_b)
[ObjectsSortByDifferentValues(value_a=1, value_b=1), ObjectsSortByDifferentValues(value_a=4, value_b=2), 
ObjectsSortByDifferentValues(value_a=2, value_b=7), ObjectsSortByDifferentValues(value_a=3, value_b=10)]
"""