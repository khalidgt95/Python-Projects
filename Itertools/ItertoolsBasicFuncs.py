
"""
This is a very basic implementation of the zip() builtin function in python

Returns a generator which is exhausted when all of the elements are looped over
"""

from typing import Callable


def zip_1(*iterables):

    max = len(iterables[0])

    lists = len(iterables)

    for item in range(0, max):

        val = []

        for j in range(0, lists):
            val.append(iterables[j][item])

        yield tuple(val)

def len_of_strings(val: str) -> int:
    return len(val)

def multiplier_10(num: int) -> float:
    return num * 10

def sum_of_numbers(*nums) -> int:
    
    val: int = 0

    for num in nums:
        val += num 

def map_one_list(function: Callable, iterables):

    for item in iterables:
        yield function(item)

    

