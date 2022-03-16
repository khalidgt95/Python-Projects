from collections import defaultdict
import collections
from dataclasses import dataclass
from pprint import pprint
from typing import DefaultDict, List


def count_letter_frequency(sentence: str) -> DefaultDict[str, int]:

    """
    >>> count_letter_frequency("khalid")
    defaultdict(<class 'int'>, {'k': 1, 'h': 1, 'a': 1, 'l': 1, 'i': 1, 'd': 1})

    """
    frequencies: defaultdict[str, int] = defaultdict(int)   # The float() method is called

    for letter in sentence:
        frequencies[letter] += 1
    
    return frequencies

def assigning_list(sentence: str) -> DefaultDict[str, list]:

    """
    Creates a new list if the key does not exist

    >>> assigning_list("sentence") 
    defaultdict(<class 'list'>, {'s': [1], 'e': [1, 1, 1], 'n': [1, 1], 't': [1], 'c': [1]})
    """
    list_frequencies: defaultdict[str, list] = defaultdict(list)

    for letter in sentence:
        list_frequencies[letter].append(1)
    
    return list_frequencies


@dataclass
class Prices:
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0

def assigning_custom_dataclass() -> None:

    """
    >>> assigning_custom_dataclass()
    defaultdict(<class '__main__.Prices'>,
                {'AAPL': Prices(current=100.0, high=150.0, low=90.0),
                'GOOG': Prices(current=0.0, high=0.0, low=0.0)})
    """
    portfolio = collections.defaultdict(Prices)

    portfolio["GOOG"]
    portfolio["AAPL"] = Prices(100.0, 150.0, 90.0)

    pprint(portfolio)


