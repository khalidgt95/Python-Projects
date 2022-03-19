from typing import Any, Callable

"""
This example demonstrates how we can pass multiple
functions as arguments.

We have to be careful about how we call them with different
values
"""

def fizz(x: int) -> bool:
    return x % 3 == 0

def buzz(x: int) -> bool:
    return x % 5 == 0

def cash(x: str) -> str:
    return "str"

def name_or_number(
        number: int, 
        *tests: Callable[[int], bool]   # Variable list of functions
    ) -> Any:

    for func in tests:
        if func(number):
            return func.__name__
    
    return str(number)

for i in range(1, 11):
    print(name_or_number(i, fizz, buzz))  # Order of function matters

    """
    
    The following call will print only 'cash' since it
    is always true in the if statement
    """
    # print(name_or_number(i, cash, fizz, buzz))
